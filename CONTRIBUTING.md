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

Temporary scope exception (effective 2026-10-12): do not add papers whose primary research object or core mechanism is skill generation, skill libraries, skill retrieval, skill optimization/self-evolution, skill–policy co-evolution, or skill composition/basis adaptation, including robotics skills. This is a user-requested deferral rather than a scientific rejection. Do not apply a keyword blacklist: papers that merely use “skill” to mean capability, cite skills as background, or expose a system as a deployment skill remain eligible after paper-specific review. Deferred records are recoverable from [`data/deferred_papers/2026-10-12-skills.json`](data/deferred_papers/2026-10-12-skills.json) only after the user explicitly lifts this exception.

## Literature-search scope

For conference updates, discover candidates with explicit gradient-free method names or exact phrases, such as `zeroth-order`, `zero-order`, `gradient-free`, `derivative-free`, `backpropagation-free`, `forward-only`, `without backpropagation`, `without gradients`, `MeZO`, `SPSA`, `CMA-ES`, `evolution strategies`, `evolutionary optimization`, `neuroevolution`, parameter/weight perturbation, finite differences, and forward gradients. Prefer conference-scoped OpenReview queries with `type=exact`, `content=all`, the conference `group`, and `source=forum`; retain query URLs, counts, pages, timestamps, and deduplicated IDs.

Do not discover candidates by enumerating the full conference or by searching bare terms such as `language model`, `large language`, `LLM`, `vision-language`, `evolving`, or `training-free`. A broad corpus may be retained as historical evidence or used to correct metadata for papers already in the catalog, but it must not supply new catalog candidates. Every candidate must retain the exact method query that found it, and every inclusion or exclusion must be based on the paper-specific official abstract or another primary source rather than substring matching. Baselines and related-work components must not be attributed to the proposed method.

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
- `related_closed_form` — closed-form, local, predictive-coding, or statistics-based adaptation that avoids a conventional end-to-end backward update; separately record whether it installs persistent adapters, classifiers, class statistics, memory states, or calibration profiles
- `related_prompt_agent` — gradient-free search over prompts, agent skills/workflows/harnesses, memory, scripts, rewards, model composition, or other external artifacts; separately record model-weight updates, external-artifact persistence, and unknown component training
- `related_unverified` — boundary work with a concrete LLM/VLM optimization or self-improvement connection whose official abstract does not establish whether an independent gradient-free mechanism, first-order training path, or persistent update exists; state the unresolved mechanism explicitly and do not present it as verified ES/ZO or hybrid optimization
- `related_forward_gradient` — forward-gradient, directional-derivative, forward-mode automatic-differentiation, or other backpropagation-free adaptation that still computes derivative information; do not call it strict zeroth-order optimization unless the primary source establishes a function-value-only estimator

Use the exact category keys from `data/papers.json`; the labels above describe where each key appears in the README.

## Style

Use the existing JSON records as the format reference. Keep both descriptions factual and to one sentence, and preserve Markdown links in the two `resources_*` fields.

If an implementation cannot be verified, write `code not located`. Do not copy abstracts verbatim.
