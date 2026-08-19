# Python style

Python 3.12. Full type annotations on public functions. `X | None` not `Optional[X]`.
Pydantic v2 for boundary objects; dataclasses only for internal value objects.
Async for all I/O. `structlog` not `print`. No bare `except:`.
Never hardcode a model name, threshold, policy rule, or prompt — they live in `config/`.
Keep functions under ~40 lines; if a function needs a section comment, split it.
