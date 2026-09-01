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

Add new papers to [`data/papers.json`](data/papers.json) in reverse chronological order within the most specific category. Prefer arXiv, ACL Anthology, OpenReview, PMLR, or the publisher page over secondary summaries. Each record contains the shared title and date, its category key, bilingual descriptions, and bilingual resource links.

After editing the data, regenerate both README tables and all distribution charts:

```bash
python3 scripts/generate_catalog.py
python3 scripts/generate_catalog.py --check
```

Do not edit content between the `GENERATED CATALOG` markers directly. The generator overwrites those sections.

## Scope checks

The optimized object must be persistent LLM parameters, adapters, structured parameter subspaces, or quantized weights. The optimization loop must explicitly use function evaluations, a zeroth-order estimator, evolutionary selection, or a population ES update.

Prompt evolution, chain-of-thought search, candidate-answer evolution, skill/memory evolution, and other object-level methods are out of scope. General reinforcement learning and generic agent self-improvement are not sufficient.

## Classification

Choose exactly one primary section:

- `es_pretraining` — ES pretraining
- `es_single_turn` — ES single-turn reasoning/alignment
- `es_multi_turn` — ES multi-turn/agentic reasoning
- `es_understanding` — ES understanding/analysis
- `zo_baselines` — ZO baselines, sparse updates, and subspaces
- `zo_directions` — ZO direction design and variance reduction
- `zo_systems` — ZO memory systems, preconditioning, and quantization
- `zo_multi_turn` — ZO multi-turn agent adaptation
- `zo_understanding` — ZO understanding/systems

Use the exact category keys from `data/papers.json`; the labels above describe where each key appears in the README.

## Style

Use the existing JSON records as the format reference. Keep both descriptions factual and to one sentence, and preserve Markdown links in the two `resources_*` fields.

If an implementation cannot be verified, write `code not located`. Do not copy abstracts verbatim.
