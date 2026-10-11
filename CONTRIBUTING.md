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

After editing the data, regenerate both README tables:

```bash
python3 scripts/generate_catalog.py
python3 scripts/generate_catalog.py --check
```

Do not edit content between the `GENERATED CATALOG` markers directly. The generator overwrites those sections.

## Scope checks

Core ES/ZO sections require persistent LLM parameters, adapters, structured parameter subspaces, or quantized weights, with function evaluations, a zeroth-order estimator, evolutionary selection, or a population ES update.

Boundary work on prompts, chain-of-thought, candidate answers, skills, workflows, harnesses, scripts, memory, reward modules, model composition, and inference-time search belongs in a labeled related section when the official abstract establishes a concrete LLM/VLM optimization connection. Do not include papers that merely use “evolving” as rhetoric without a concrete method connection. Do not infer frozen weights, absence of backpropagation, or absence of persistent model updates from an external search object; record each model, proposer, scorer/verifier, surrogate, and external artifact separately, and mark missing facts as unverified.

## Classification

Scope extensions include persistent action-side ZO adaptation in VLA models. Hybrid methods that retain backpropagation and inference-time calibration without parameter updates belong only in the explicitly labeled related-research categories.

Choose exactly one primary section:

- `es_pretraining` — ES pretraining
- `es_single_turn` — ES single-turn reasoning/alignment
- `es_multi_turn` — ES multi-turn/agentic reasoning
- `es_understanding` — ES understanding/analysis
- `zo_pretraining` — forward-only ZO pretraining
- `zo_baselines` — ZO baselines, sparse updates, and subspaces
- `zo_directions` — ZO direction design and variance reduction
- `zo_systems` — ZO memory systems, preconditioning, and quantization
- `zo_alignment` — ZO comparison-based preference alignment
- `zo_multi_turn` — ZO multi-turn agent adaptation
- `zo_understanding` — ZO understanding/systems
- `related_hybrid` — related hybrid first-/zeroth-order methods
- `related_inference` — related inference-time calibration without parameter updates
- `related_prompt_agent` — gradient-free search over prompts, agent skills/workflows/harnesses, memory, scripts, rewards, model composition, or other external artifacts; separately record model-weight updates, external-artifact persistence, and unknown component training

Use the exact category keys from `data/papers.json`; the labels above describe where each key appears in the README.

## Style

Use the existing JSON records as the format reference. Keep both descriptions factual and to one sentence, and preserve Markdown links in the two `resources_*` fields.

If an implementation cannot be verified, write `code not located`. Do not copy abstracts verbatim.
