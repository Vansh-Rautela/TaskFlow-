#!/usr/bin/env python3
"""Comprehensive System & AI Verification Script for TaskFlow.

Tests and verifies:
1. Vector DB & FastEmbed Hybrid Search (dense bge-small-en + sparse bm25)
2. OpenRouter Cloud LLM Provider
3. Local Ollama LLM Provider
4. End-to-End Orchestrator Pipeline
"""

import asyncio
import sys
import time

sys.path.insert(0, ".")

from datetime import UTC, datetime

from taskflow.adapters.db.engine import build_engine, build_session_factory
from taskflow.adapters.db.orm import Base
from taskflow.adapters.db.repositories import SQLiteTraceRepository
from taskflow.adapters.llm.ollama import OllamaProvider
from taskflow.adapters.llm.openrouter import OpenRouterProvider
from taskflow.adapters.llm.router import ProviderRouter
from taskflow.adapters.vector.qdrant_store import QdrantVectorStore
from taskflow.config.settings import settings
from taskflow.domain.enums import Channel
from taskflow.domain.models import ClassificationOutput, InboundMessage
from taskflow.pipeline.orchestrator import Deps, run_pipeline


async def verify_all():
    print("==================================================")
    print("   TASKFLOW SYSTEM & SUBSYSTEM VERIFICATION")
    print("==================================================\n")

    # 1. Test Vector DB & FastEmbed
    print("--- 1. Testing Vector DB & FastEmbed Embeddings ---")
    start_v = time.perf_counter()
    qdrant = QdrantVectorStore()
    try:
        test_query = "What is your refund policy for unused seat licenses?"
        res = qdrant.search(query=test_query, tenant_id="taskflow-demo", limit=3)
        v_ms = (time.perf_counter() - start_v) * 1000
        print(f"✅ Vector DB Query Succeeded ({v_ms:.1f} ms)")
        print(f"   Query: '{test_query}'")
        print(f"   Chunks Retrieved: {len(res.chunks)}")
        for idx, sc in enumerate(res.chunks, start=1):
            print(
                f"   [{idx}] Score: {sc.rrf_score:.4f} | Title: '{sc.chunk.title}' | Chunk ID: {sc.chunk.chunk_id}"
            )
    except Exception as err:
        print(f"❌ Vector DB Verification Failed: {err}")

    # 2. Test OpenRouter LLM Provider
    print("\n--- 2. Testing OpenRouter LLM Provider ---")
    openrouter_key = settings().openrouter_api_key
    print(f"   OPENROUTER_API_KEY Configured: {bool(openrouter_key)}")
    if openrouter_key:
        try:
            op = OpenRouterProvider()
            router = ProviderRouter(
                providers={"openrouter": op, "claude": op, "ollama": OllamaProvider()}
            )
            healthy = await op.health()
            print(f"   Health Check: {healthy}")
            print("   Sending test completion to OpenRouter...")
            start_or = time.perf_counter()
            parsed, call_record = await router.complete_structured(
                purpose="classification",
                system="You are a classifier.",
                user="My card was charged twice for order #9921",
                schema=ClassificationOutput,
            )
            or_ms = (time.perf_counter() - start_or) * 1000
            print(f"✅ OpenRouter Structured Completion Succeeded ({or_ms:.1f} ms)")
            print(f"   Parsed Output: Intent={parsed.intent.value}, Confidence={parsed.confidence}")
            print(f"   Call Cost: ${call_record.cost_usd:.6f}")
        except Exception as err:
            print(f"❌ OpenRouter Test Failed: {err}")
    else:
        print("   Notice: OPENROUTER_API_KEY is empty in .env. Skipping live API completion test.")

    # 3. Test Local Ollama Provider
    print("\n--- 3. Testing Local Ollama LLM Provider ---")
    try:
        ollama_p = OllamaProvider()
        ol_health = await ollama_p.health()
        print(f"   Local Ollama Base URL: {settings().ollama_base_url}")
        print(f"   Ollama Service Reachable: {ol_health}")
        if ol_health:
            print("✅ Ollama is running and healthy!")
        else:
            print(
                "   Notice: Local Ollama daemon is offline (Router fallback logic will automatically handle offline mode)."
            )
    except Exception as err:
        print(f"   Notice: Ollama check: {err}")

    # 4. Test End-to-End Orchestrator Pipeline
    print("\n--- 4. Testing End-to-End Pipeline Orchestrator ---")
    try:
        engine = build_engine("sqlite+aiosqlite:///:memory:")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        sf = build_session_factory(engine)
        trace_repo = SQLiteTraceRepository(sf)

        op = OpenRouterProvider()
        router = ProviderRouter(
            providers={"openrouter": op, "claude": op, "ollama": OllamaProvider()}
        )
        deps = Deps(trace_repo=trace_repo, llm_router=router, vector_store=qdrant)

        now = datetime.now(UTC)
        msg = InboundMessage(
            message_id="verification-msg-1",
            dedupe_key="verification:1",
            tenant_id="taskflow-demo",
            channel=Channel.EMAIL,
            sender="customer@example.com",
            subject="Billing issue",
            body_text="Webhook endpoint keeps timing out with 504 gateway timeout",
            body_redacted="Webhook endpoint keeps timing out with 504 gateway timeout",
            provider_message_id="v-1",
            received_at=now,
        )

        start_p = time.perf_counter()
        decision = await run_pipeline(msg, deps)
        p_ms = (time.perf_counter() - start_p) * 1000

        print(f"✅ Pipeline Execution Succeeded ({p_ms:.1f} ms)")
        print(f"   Action Taken:   {decision.action.value}")
        print(f"   Reason:         {decision.reason}")
        print(f"   Quality Score:  {decision.confidence.score if decision.confidence else 'N/A'}")

        await engine.dispose()
    except Exception as err:
        print(f"❌ Pipeline Verification Failed: {err}")

    print("\n==================================================")
    print("   ALL SUBSYSTEM VERIFICATION COMPLETED")
    print("==================================================")


if __name__ == "__main__":
    asyncio.run(verify_all())
