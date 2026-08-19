# Knowledge base generation prompt

You are writing the internal knowledge base for TaskFlow, a fictional project-management
SaaS. Plans: Free, Pro at $12 per user per month, Enterprise at $29 per user per month.

Write document {n} of 42: "{title}" (type: {doc_type}, tier: {product_tier}).

Requirements:
- 300-700 words of markdown, with 2-4 "##" sections.
- Include at least one concrete number, limit, or timeframe that a support agent would
  have to quote exactly ("within 30 days", "up to $500", "14-day trial", "5 GB per seat").
- Include one edge case or exception to the main rule.
- Vary the structure across documents: some should contain a table, some a numbered
  procedure, some a short FAQ list.
- Neutral internal-documentation voice. Not marketing copy.
- Never mention a real company. Never invent URLs or email addresses other than
  support@taskflow.example and billing@taskflow.example.

Output only the markdown body. No frontmatter, no commentary, no code fences.
