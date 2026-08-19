"""Context-Grounded LLM Drafting Service for Phase P7.

Formats retrieved Knowledge Base chunks into prompt context and uses LLMRouter to generate
tailored support responses with explicit citations [chunk_id].
"""

from taskflow.domain.enums import Intent
from taskflow.domain.models import DraftOutput, InboundMessage, RetrievalResult
from taskflow.ports.llm import LLMRouter

SYSTEM_PROMPT = """You are an expert customer support agent writing a professional email response.
Follow these strict guidelines:
1. Base your response EXCLUSIVELY on the provided Knowledge Base Context chunks.
2. Include inline bracketed citations matching chunk IDs for every policy or fact (e.g. [chunk_id]).
3. Keep the tone professional, helpful, and concise.
4. Never invent details, dates, or terms not supported by the context.
"""


def _format_context(retrieval: RetrievalResult | None) -> str:
    if not retrieval or not retrieval.chunks:
        return "No relevant Knowledge Base context found."

    formatted_blocks = []
    for sc in retrieval.chunks:
        c = sc.chunk
        section_info = f" | Section: {c.section}" if c.section else ""
        formatted_blocks.append(
            f"[Chunk ID: {c.chunk_id} | Title: {c.title}{section_info}]\n{c.text}"
        )
    return "\n\n".join(formatted_blocks)


async def generate_draft(
    msg: InboundMessage,
    intent: Intent,
    retrieval: RetrievalResult,
    router: LLMRouter,
) -> DraftOutput:
    """Generate a context-grounded response draft using LLMRouter."""
    context_text = _format_context(retrieval)

    user_prompt = f"""Customer Message:
{msg.body_text}

Detected Intent: {intent.value}

Knowledge Base Context:
{context_text}
"""

    draft, _call = await router.complete_structured(
        purpose="draft",
        system=SYSTEM_PROMPT,
        user=user_prompt,
        schema=DraftOutput,
    )

    return draft
