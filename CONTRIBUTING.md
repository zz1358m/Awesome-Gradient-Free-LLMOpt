# Contributing

Thank you for helping keep this list accurate and focused.

## Add a paper

Open an issue or pull request with:

- the exact paper title and author list;
- a primary paper or proceedings URL;
- the official implementation URL, if available, or `code not located`;
- publication or first-posted year and month;
- one sentence explaining how model parameters are optimized with ES or ZO;
- the task regime: single-turn, multi-turn/agentic, or understanding/analysis;
- representative experimental datasets.

Add new papers in reverse chronological order within the most specific section. Prefer arXiv, ACL Anthology, OpenReview, PMLR, or the publisher page over secondary summaries.

## Scope checks

The optimized object must be persistent LLM parameters, adapters, structured parameter subspaces, or quantized weights. The optimization loop must explicitly use function evaluations, a zeroth-order estimator, evolutionary selection, or a population ES update.

Prompt evolution, chain-of-thought search, candidate-answer evolution, skill/memory evolution, and other object-level methods are out of scope. General reinforcement learning and generic agent self-improvement are not sufficient.

## Classification

Choose exactly one primary section:

- ES — single-turn reasoning/alignment
- ES — multi-turn/agentic reasoning
- ES — understanding/analysis
- ZO — single-turn SFT/adaptation
- ZO — multi-turn agent adaptation
- ZO — understanding/systems

## Style

Use this format, keeping the implementation entry on the paper's own line:

```markdown
- **Paper title** — One-sentence contribution and representative datasets. [paper](PRIMARY_URL) · [code](OFFICIAL_URL) · YYYY-MM
```

If an implementation cannot be verified, write `code not located`. Do not copy abstracts verbatim.
