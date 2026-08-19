"""Query builder service for Phase P5.

Applies deterministic normalization and alias expansion configured in config/settings.yaml
to improve dense and sparse keyword retrieval recall.
"""

import re

from taskflow.config.settings import app_config


def build_query(text: str) -> str:
    """Build an expanded query string using configured alias mappings."""
    if not text or not text.strip():
        return ""

    normalized = text.strip().lower()
    expansions = app_config().get("retrieval", {}).get("alias_expansions", {})

    expanded_terms = []
    for alias, expansion in expansions.items():
        pattern = re.compile(rf"\b{re.escape(alias)}\b", re.IGNORECASE)
        if pattern.search(normalized):
            expanded_terms.append(str(expansion))

    if expanded_terms:
        return f"{normalized} ({' '.join(expanded_terms)})"

    return normalized
