# Contributing

Thank you for helping keep this list accurate and focused.

## Add a paper

Open an issue or pull request with:

- the exact paper title and author list;
- a primary paper/proceedings URL;
- an official implementation URL, if available;
- publication or first-posted year and month;
- one sentence explaining why the paper is ES × LLM or ZO × LLM;
- one or more scope tags used in the README.

Add new papers in reverse chronological order within the most specific section. Prefer arXiv, ACL Anthology, OpenReview, PMLR, or the publisher page over secondary summaries.

## Scope checks

The optimized object must be an LLM parameterization or an LLM-side prompt/reasoning object, and the optimization loop must explicitly use function evaluations, zeroth-order estimation, or evolutionary population operations. General reinforcement learning and generic agent self-improvement are not sufficient.

## Style

Use this format:

```markdown
- **Paper title** — One-sentence contribution. [paper](PRIMARY_URL) · [code](OFFICIAL_URL) · YYYY-MM · `tag`
```

Keep descriptions factual and short. Do not copy abstracts verbatim.

