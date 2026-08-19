"""SQLite async engine with WAL mode, busy timeout, and FK enforcement.

Call `create_engine()` exactly once at startup (inside FastAPI lifespan or
the worker bootstrap). Never import SQLAlchemy from domain/ or services/.
"""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from sqlalchemy import event, text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


def build_engine(database_url: str) -> AsyncEngine:
    """Return a configured async engine.

    The pragma listener fires synchronously on every new connection to the
    pool before any async code runs, which is why we use the sync @event.listens_for
    pattern instead of an async startup query.
    """
    engine = create_async_engine(
        database_url,
        echo=False,
        pool_pre_ping=True,
    )

    @event.listens_for(engine.sync_engine, "connect")
    def _set_pragmas(dbapi_conn: Any, _connection_record: Any) -> None:
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("PRAGMA busy_timeout=5000")
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    return engine


def build_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@asynccontextmanager
async def session_scope(
    factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    """Provide a transactional scope around a series of operations."""
    async with factory() as session, session.begin():
        yield session


async def verify_engine(engine: AsyncEngine) -> None:
    """Smoke-test: round-trip a query to confirm the pragmas were applied.
    Called once at startup; raises if the DB is unreachable."""
    async with engine.connect() as conn:
        result = await conn.execute(text("PRAGMA journal_mode"))
        mode = result.scalar()
        if mode != "wal":
            raise RuntimeError(f"Expected WAL journal_mode, got {mode!r}")
