# Awesome Gradient-Free Optimization for LLMs

A curated collection of papers and implementations on **evolution strategies (ES)** and **zeroth-order optimization (ZO)** for large language models.

The list focuses on methods that optimize LLM weights, adapters, quantized parameters, prompts, or reasoning states from scalar evaluations without ordinary end-to-end backpropagation through the task objective. It is built from the local *Gradient-Free Optimization for LLM Reasoning* survey and independently checked against primary paper or proceedings pages.

**Last literature check:** 2026-09-01

> 中文说明：主列表严格限定在 ES × LLM 与 ZO × LLM。普通强化学习、泛化的 agent self-evolution、仅名称中含有 “evolution” 的工作均不收录；prompt/trace evolution 单列为 object-level optimization。

## Contents

- [Scope and taxonomy](#scope-and-taxonomy)
- [New since the survey](#new-since-the-survey)
- [Evolution strategies for LLM optimization](#evolution-strategies-for-llm-optimization)
- [Zeroth-order LLM fine-tuning](#zeroth-order-llm-fine-tuning)
- [Prompt and reasoning-state optimization](#prompt-and-reasoning-state-optimization)
- [Implementations](#implementations)
- [Contributing](#contributing)

## Scope and taxonomy

| Family | Optimized object | Typical feedback | Included examples |
|---|---|---|---|
| Weight-space ES | Full weights, LoRA, low-rank or quantized coordinates | Task reward, verifier, alignment score | ES-at-Scale, EGGROLL, ESSA, QES |
| Parameter-space ZO | Full weights, sparse coordinates, adapters, subspaces | Loss or task metric from forward passes | MeZO, LOZO, SubZero, HiZOO |
| Object-level ES/ZO | Prompt, chain of thought, candidate answer, search distribution | Verifier or black-box score | Evolutionary CoT, GEPA, AOZPT |

ES and two-point ZO are closely related estimators of a smoothed objective. The practical distinction used here is that ES usually emphasizes population evaluation, fitness shaping, selection, and parallelism, while ZO fine-tuning usually emphasizes finite-difference gradient estimation and optimizer-style sequential updates.

Legend: `weights`, `adapters`, `quantized`, `reasoning`, `alignment`, `systems`, `theory`, `prompt`.

## New since the survey

These papers were found during the 2026-09-01 update and were not in the local survey bibliography.

- **SubZero+: Efficient Zeroth-Order LLM Fine-Tuning via Large Learning Rates** — Multi-query estimation, subspace Adam, and corrected Haar subspaces. [paper](https://arxiv.org/abs/2608.15665) · 2026-08 · `ZO` `subspace` `adapters`
- **Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies** — Studies how ES preserves pass@k coverage during reasoning post-training. [paper](https://arxiv.org/abs/2608.12679) · [code](https://github.com/conorfhayes/beyond-the-best-guess) · 2026-08 · `ES` `reasoning`
- **Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents** — Uses LoRA perturbations to discover successful trajectories on difficult agent tasks. [paper](https://arxiv.org/abs/2608.09292) · [code](https://github.com/hidk1911/ZOForLLMAgents) · 2026-08 · `ZO` `agents` `adapters`
- **Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies** — Reframes forgetting as performance drift and proposes anchored weight decay. [paper](https://arxiv.org/abs/2605.30148) · 2026-05 · `ES` `continual-learning`
- **LLM Zeroth-Order Fine-Tuning is an Inference Workload** — Reorganizes ZO evaluation around a serving runtime. [paper](https://arxiv.org/abs/2605.28760) · 2026-05 · `ZO` `systems`
- **Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs** — Learns reusable, model-specific perturbation strategies. [paper](https://openreview.net/forum?id=bRS5iwbqlC) · [code](https://github.com/ASTRAL-Group/ZO_Fine_tuner) · ICML 2026 · `ZO` `learning-to-optimize`

## Evolution strategies for LLM optimization

### Scaling and core algorithms

- **Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning** — Full-parameter, population-parallel ES for billion-parameter LLM post-training. [paper](https://arxiv.org/abs/2509.24372) · [code](https://github.com/VsonicV/es-at-scale) · ICML 2026 · `weights` `reasoning` `systems`
- **Evolution Strategies at the Hyperscale** — EGGROLL replaces dense matrix perturbations with low-rank factors while retaining a high-rank population update. [paper](https://arxiv.org/abs/2511.16652) · 2025 · `weights` `low-rank` `systems`
- **ESSA: Evolutionary Strategies for Scalable Alignment** — Evolves singular-value coordinates of LoRA adapters and supports low-precision inference. [paper](https://arxiv.org/abs/2507.04453) · 2025 · `adapters` `alignment` `quantized`
- **EA4LLM: A Gradient-Free Approach to Large Language Model Optimization via Evolutionary Algorithms** — Population-based evolutionary optimization at one-billion-parameter scale. [paper](https://arxiv.org/abs/2510.10603) · 2025 · `weights` `pretraining`
- **When Evolution Strategy Meets Language Models Tuning** — Output-conditioned evolutionary tuning with centered rewards. [paper](https://aclanthology.org/2025.coling-main.357/) · COLING 2025 · `reasoning` `alignment`
- **ESSAM: A Novel Competitive Evolution Strategies Approach to Reinforcement Learning for Memory Efficient LLMs Fine-Tuning** — Competitive ES update designed for memory-efficient tuning. [paper](https://arxiv.org/abs/2602.01003) · 2026 · `weights` `reasoning`
- **Derivative-Free Optimization for Low-Rank Adaptation in Large Language Models** — C-LoRA/F-LoRA use CMA-ES or the Fireworks Algorithm in projected LoRA spaces. [paper](https://doi.org/10.1109/TASLP.2024.3477330) · IEEE/ACM TASLP 2024 · `adapters` `low-rank`
- **Quantized Evolution Strategies: High-precision Fine-tuning of Quantized LLMs at Low-precision Cost** — Full-parameter ES in a discrete quantized space with error feedback and seed replay. [paper](https://arxiv.org/abs/2602.03120) · 2026 · `weights` `quantized`

### Reasoning, alignment, and model behavior

- **Evolutionary System 2 Reasoning: An Empirical Proof** — Evolves model populations toward improved System-2 reasoning. [paper](https://arxiv.org/abs/2512.05760) · 2025 · `weights` `reasoning`
- **Fine-Tuning Language Models to Know What They Know** — Evolution Strategy for Metacognitive Alignment (ESMA). [paper](https://arxiv.org/abs/2602.02605) · 2026 · `alignment` `metacognition`
- **Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights** — RandOpt selects and ensembles useful one-step random weight perturbations. [paper](https://arxiv.org/abs/2603.12228) · 2026 · `weights` `selection`
- **Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training** — Compares parameter-space geometry and update behavior. [paper](https://arxiv.org/abs/2604.01499) · 2026 · `theory` `reasoning`
- **Evolutionary Strategies Lead to Catastrophic Forgetting in LLMs** — Diagnoses prior-task degradation during ES fine-tuning. [paper](https://arxiv.org/abs/2601.20861) · 2026 · `analysis`
- **Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies** — Stabilizes prior-task performance with anchored weight decay. [paper](https://arxiv.org/abs/2605.30148) · 2026 · `analysis` `continual-learning`
- **Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies** — Compares ES and RL through solution diversity and pass@k. [paper](https://arxiv.org/abs/2608.12679) · [code](https://github.com/conorfhayes/beyond-the-best-guess) · 2026 · `reasoning` `diversity`

## Zeroth-order LLM fine-tuning

### Foundations, benchmarks, and systems

- **Fine-Tuning Language Models with Just Forward Passes** — MeZO: in-place perturbation and seed replay at inference-level memory. [paper](https://arxiv.org/abs/2305.17333) · [code](https://github.com/princeton-nlp/MeZO) · 2023 · `weights` `baseline`
- **Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark** — ZO-Bench evaluates objectives, trainable interfaces, and model families. [paper](https://arxiv.org/abs/2402.11592) · 2024 · `benchmark`
- **ZO2: Scalable Zeroth-Order Fine-Tuning for Extremely Large Language Models with Limited GPU Memory** — Parameter offloading and overlap for large-model ZO. [paper](https://arxiv.org/abs/2503.12668) · 2025 · `systems`
- **DistZO2: High-Throughput and Memory-Efficient Zeroth-Order Fine-tuning LLMs with Distributed Parallel Computing** — Distributed perturbation evaluation and scalar aggregation. [paper](https://arxiv.org/abs/2507.03211) · 2025 · `systems`
- **LLM Zeroth-Order Fine-Tuning is an Inference Workload** — Executes repeated ZO scoring through an inference-serving runtime. [paper](https://arxiv.org/abs/2605.28760) · 2026 · `systems`

### Sparse, low-rank, and structured search

- **Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning** — Perturbs a selected coordinate subset. [paper](https://arxiv.org/abs/2402.15751) · 2024 · `sparse`
- **Zeroth-Order Fine-Tuning of LLMs with Extreme Sparsity** — Fisher-informed sensitive parameters plus low-bit frozen weights. [paper](https://arxiv.org/abs/2406.02913) · 2024 · `sparse` `quantized`
- **Enhancing Zeroth-order Fine-tuning for Language Models with Low-rank Structures** — LOZO uses structured low-rank perturbations. [paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9ccc9d814d3dee4750debaf23061e733-Abstract-Conference.html) · ICLR 2025 · `low-rank`
- **Zeroth-Order Fine-Tuning of LLMs in Random Subspaces** — SubZero builds layer-wise low-rank random subspaces. [paper](https://arxiv.org/abs/2410.08989) · [code](https://github.com/zimingyy/SubZero) · ICCV 2025 · `subspace`
- **TeZO: Empowering the Low-Rankness on the Temporal Dimension in the Zeroth-Order Optimization for Fine-tuning LLMs** — Exploits temporal low-rank structure across estimates. [paper](https://arxiv.org/abs/2501.19057) · 2025 · `low-rank` `temporal`
- **RoZO: Geometry-Aware Zeroth-Order Fine-Tuning on Low-Rank Adapters for Black-Box Large Language Models** — Tangent-space perturbations, retraction, and transport on the LoRA manifold. [paper](https://aclanthology.org/2026.eacl-long.80/) · EACL 2026 · `adapters` `geometry`
- **SubZero+: Efficient Zeroth-Order LLM Fine-Tuning via Large Learning Rates** — Multi-query subspace estimation and subspace Adam. [paper](https://arxiv.org/abs/2608.15665) · 2026 · `subspace` `preconditioning`

### Variance reduction and informed directions

- **Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models** — MeZO-SVRG adds an anchor-based control variate. [paper](https://arxiv.org/abs/2404.08080) · ICML 2024 · `variance-reduction`
- **Harmony in Divergence: Towards Fast, Accurate, and Memory-efficient Zeroth-order LLM Fine-tuning** — DiZO applies layer-wise projection and rescaling. [paper](https://arxiv.org/abs/2502.03304) · 2025 · `projection`
- **KerZOO: Kernel Function Informed Zeroth-Order Optimization for Accurate and Accelerated LLM Fine-Tuning** — Kernel-weighted estimator correction. [paper](https://arxiv.org/abs/2505.18886) · 2025 · `estimator`
- **Towards Fast LLM Fine-tuning through Zeroth-Order Optimization with Projected Gradient-Aligned Perturbations** — P-GAP aligns low-rank perturbations with a projected gradient estimate. [paper](https://arxiv.org/abs/2510.18228) · 2025 · `projection` `low-rank`
- **ConMeZO: Adaptive Descent-Direction Sampling for Gradient-Free Finetuning of Large Language Models** — Samples perturbations from a cone around a momentum direction. [paper](https://arxiv.org/abs/2511.02757) · 2025 · `direction-sampling`
- **Low-Rank Curvature for Zeroth-Order Optimization in LLM Fine-Tuning** — LOREN uses low-rank block-diagonal curvature and leave-one-out estimation. [paper](https://arxiv.org/abs/2511.07971) · AAAI 2026 · `curvature` `variance-reduction`
- **Robust and Efficient Zeroth-Order LLM Fine-Tuning via Adaptive Bayesian Subspace Optimizer** — Bayesian aggregation of noisy subspace measurements. [paper](https://arxiv.org/abs/2601.01452) · 2026 · `bayesian` `subspace`
- **Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning** — PIZOO biases samples toward an adaptive prior. [paper](https://arxiv.org/abs/2601.04710) · 2026 · `direction-sampling`
- **AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning** — Uses forward activations to shape perturbation directions. [paper](https://arxiv.org/abs/2601.17261) · 2026 · `activation-guided`
- **Zero-Order Optimization for LLM Fine-Tuning via Learnable Direction Sampling** — ZO-LDSD learns a non-isotropic sampling distribution. [paper](https://arxiv.org/abs/2602.13659) · 2026 · `direction-sampling`
- **Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization** — ZO-Muon adds spectral orthogonalization to subspace estimates. [paper](https://arxiv.org/abs/2602.17155) · 2026 · `orthogonalization`
- **CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning** — Curvature-aware sparse sampling with probability correction. [paper](https://arxiv.org/abs/2603.21725) · 2026 · `curvature` `sparse`
- **Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs** — Learns adaptive perturbation variances once per base model. [paper](https://openreview.net/forum?id=bRS5iwbqlC) · [code](https://github.com/ASTRAL-Group/ZO_Fine_tuner) · ICML 2026 · `learning-to-optimize`

### Preconditioning, quantization, and hybrid updates

- **Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer** — HiZOO estimates diagonal curvature from forward passes. [paper](https://arxiv.org/abs/2402.15173) · 2024 · `curvature` `preconditioning`
- **HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization** — Layer-wise clipping and annealing. [paper](https://aclanthology.org/2025.emnlp-main.1323/) · EMNLP 2025 · `preconditioning`
- **QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models** — Integrates quantization into forward-only fine-tuning. [paper](https://aclanthology.org/2025.emnlp-main.271/) · EMNLP 2025 · `quantized`
- **Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection** — Assigns FO or ZO updates based on tensor importance. [paper](https://aclanthology.org/2026.findings-acl.239/) · Findings of ACL 2026 · `hybrid`
- **AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments** — Approximates adaptive moments without full optimizer states. [paper](https://arxiv.org/abs/2605.00650) · 2026 · `preconditioning`
- **Quantized Evolution Strategies: High-precision Fine-tuning of Quantized LLMs at Low-precision Cost** — ES/ZO bridge for discrete low-precision weights. [paper](https://arxiv.org/abs/2602.03120) · 2026 · `quantized` `ES`

### LLM-agent adaptation

- **Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents** — Perturbs LoRA parameters, discovers trajectories, and closes the loop with supervised fine-tuning. [paper](https://arxiv.org/abs/2608.09292) · [code](https://github.com/hidk1911/ZOForLLMAgents) · 2026 · `agents` `adapters`

## Prompt and reasoning-state optimization

These methods use an ES/EA/ZO-style black-box loop, but optimize ephemeral language objects rather than persistent model weights. They are separated to avoid conflating test-time search with training-time ES/ZO.

- **Zero-Shot Chain-of-Thought Reasoning Guided by Evolutionary Algorithms in Large Language Models** — Evolves candidate chains of thought from task feedback. [paper](https://arxiv.org/abs/2402.05376) · 2024 · `reasoning` `prompt`
- **Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution** — Evolves both task prompts and mutation prompts. [paper](https://arxiv.org/abs/2309.16797) · 2023 · `prompt`
- **Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers** — EvoPrompt combines LLM generation with GA/DE-style search. [paper](https://arxiv.org/abs/2309.08532) · 2023 · `prompt`
- **GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning** — Uses reflective textual feedback to evolve prompts and programs. [paper](https://arxiv.org/abs/2507.19457) · 2025 · `prompt` `agents`
- **DEBATE, TRAIN, EVOLVE: Self-Evolution of Language Model Reasoning** — Evolves reasoning through debate-generated supervision. [paper](https://arxiv.org/abs/2505.15734) · 2025 · `reasoning`
- **Population-Evolve: A Parallel Sampling and Evolutionary Method for LLM Math Reasoning** — Population-based sampling, scoring, and evolution for mathematical reasoning. [paper](https://arxiv.org/abs/2512.19081) · 2025 · `reasoning`
- **Online Black-Box Prompt Optimization with Regret Guarantees under Noisy Feedback** — AOZPT is an online zeroth-order prompt tuner with adaptive uncertainty scaling. [paper](https://openreview.net/forum?id=7MzaG8dHRv) · ICLR 2026 · `ZO` `prompt`

## Implementations

| Project | Methods | Notes |
|---|---|---|
| [ES-at-Scale](https://github.com/VsonicV/es-at-scale) | Full-parameter ES | Ray + vLLM population-parallel training |
| [MeZO](https://github.com/princeton-nlp/MeZO) | MeZO | Reference forward-only fine-tuning implementation |
| [SubZero](https://github.com/zimingyy/SubZero) | MeZO, SubZero | Random-subspace ZO across multiple tuning interfaces |
| [ZO Fine-tuner](https://github.com/ASTRAL-Group/ZO_Fine_tuner) | Learned ZO optimizer | Learn once per base model and reuse across tasks |
| [ZO for LLM Agents](https://github.com/hidk1911/ZOForLLMAgents) | LoRA ZO | Self-evolving agent trajectory discovery |
| [Beyond the Best Guess](https://github.com/conorfhayes/beyond-the-best-guess) | ES pass@k evaluation | Evaluation harness and released ES-tuned models |

## Selection policy

A paper belongs in the main list when all of the following hold:

1. The method explicitly uses ES, an evolutionary population update, or a zeroth-order/function-evaluation estimator.
2. The optimized model or search object is part of an LLM/language-model pipeline.
3. A primary paper page can be verified.

Generic derivative-free optimization, ordinary RL, architecture search without an ES/ZO contribution, and self-evolving agents without a black-box optimizer are out of scope. Speech-only and vision-only applications are also excluded from the main list.

## Contributing

Paper additions and corrections are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and use the paper-request issue template. Include a primary paper link, a one-sentence scope justification, and an official code link when available.

Bibliographic records for the core list are available in [papers.bib](papers.bib).

## Acknowledgements

The initial taxonomy and bibliography were derived from the local *Gradient-Free Optimization for LLM Reasoning* survey. The repository layout is inspired by community-maintained awesome paper lists such as [Awesome-Latent-CoT](https://github.com/EIT-NLP/Awesome-Latent-CoT); all descriptions here were written specifically for this collection.

