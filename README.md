# Awesome Gradient-Free Optimization for LLMs

[English](README.md) | [简体中文](README_zh.md)

A curated collection of **evolution strategies (ES)** and **zeroth-order optimization (ZO)** for optimizing LLM parameters without backpropagating through the task objective.

This list covers persistent model parameters: full weights, adapters, low-rank subspaces, and quantized weights. It deliberately excludes prompt evolution, chain-of-thought search, candidate-answer evolution, and other object-level optimization.

**Last literature check:** 2026-10-09

[Latest review and inclusion decisions](data/literature_reviews/2026-10-09.json).

**Venue convention:** ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) denotes a confirmed conference or journal venue. Preprints without a verified venue remain unbadged.

## Contents

- [ES and ZO are used differently](#es-and-zo-are-used-differently)
- [Evolution strategies](#evolution-strategies)
  - [Pretraining](#pretraining)
  - [Single-turn reasoning and alignment](#single-turn-reasoning-and-alignment)
  - [Multi-turn and agentic reasoning](#multi-turn-and-agentic-reasoning)
  - [Understanding ES](#understanding-es)
- [Zeroth-order optimization](#zeroth-order-optimization)
  - [Pretraining](#pretraining-1)
  - [Single-turn SFT and adaptation](#single-turn-sft-and-adaptation)
  - [Preference alignment](#preference-alignment)
  - [Multi-turn agent adaptation](#multi-turn-agent-adaptation)
  - [Understanding and systems](#understanding-and-systems)
- [Related research](#related-research)
- [Scope](#scope)
- [Contributing](#contributing)

## ES and ZO are used differently

ES and two-point ZO can both be viewed as estimators of a smoothed objective, but the LLM literature uses them in noticeably different regimes.

| | Evolution strategies (ES) | Zeroth-order optimization (ZO) |
|---|---|---|
| Predominant objective | Direct task reward: `max E[R(model rollout)]` | Supervised loss: `min CE/NLL(model(x), y)` |
| Evaluation unit | A population of perturbed models, each producing fresh rollouts | Usually one or a few paired forward evaluations at `theta + eps*z` and `theta - eps*z` |
| Feedback | Exact-match/verifier score, environment return, preference or alignment reward | Token-level CE/NLL, perplexity, or another relatively smooth loss |
| Main use in this list | Reasoning post-training and long-horizon agents | Memory-efficient SFT and parameter-efficient adaptation |
| Representative datasets | Countdown, GSM8K, MATH-style suites, Sudoku, ARC-AGI, PRM800K, IFEval; WebArena-Lite for agents | SST-2, RTE, BoolQ, WiC, CB, COPA, SNLI/MNLI/QNLI, SQuAD, DROP and commonsense QA |

Why this split matters: a terminal reasoning reward is often sparse, discrete, and stochastic because every perturbation generates a fresh rollout. Population evaluation, fitness normalization/ranking, and reward-weighted ES updates are designed for that setting. Paired two-point ZO is most effective when the two function values are strongly correlated, as they usually are for deterministic SFT loss on the same minibatch.

This is a taxonomy of prevailing practice, not a mathematical prohibition. ES can minimize a supervised loss, and reward-based ZO with many perturbations begins to look like ES.

<!-- GENERATED CATALOG:START -->
## Evolution strategies

### Pretraining

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2025-10 | **EA4LLM: A Gradient-Free Approach to Large Language Model Optimization via Evolutionary Algorithms** | Full-parameter ES pretraining that uses mean next-token log-probability as fitness; demonstrated on Qwen3-style models from 0.5B to 32B parameters. | [paper](https://arxiv.org/abs/2510.10603) · code not located · 2025-10 |

### Single-turn reasoning and alignment

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-10 | **DART-ES: Difficulty-Aware Reweighting and Targeted Replay for Fine-Tuning LLMs with Evolution Strategies** | Uses population pass rates and historical difficulty estimates to reweight rewards and replay rarely solved samples during forward-only full-parameter ES fine-tuning; evaluated on mathematical reasoning, instruction tuning, code generation, and Countdown. | [paper](https://arxiv.org/abs/2610.06993) · [code](https://github.com/szs777/DART-ES-Code) · 2026-10 |
| 2026-08 | **Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets?** | Uses Gaussian-process-guided Bayesian optimization in a random linear weight subspace to select a single deployable expert without LLM backpropagation; preliminary reasoning experiments use Qwen2.5-Instruct 0.5B–3B. | [paper](https://arxiv.org/abs/2608.10867) · code not located · 2026-08 |
| 2026-05 | **Consolidating Rewarded Perturbations for LLM Post-Training** | CoRP consolidates rewarded parameter perturbations into one deployable model through reward and compatibility reweighting, held-out validation, and step-size calibration, with no LLM backpropagation. | [paper](https://arxiv.org/abs/2605.31494) · [code](https://github.com/oooranz/CoRP) · 2026-05 |
| 2026 | **Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning** | Full-parameter, population-parallel ES that directly optimizes rewards for Countdown, math reasoning, Sudoku, conciseness, and ARC-AGI. | [paper](https://openreview.net/forum?id=i0P4ew9GpS) · [code](https://github.com/VsonicV/es-at-scale) · [earlier implementation](https://github.com/VsonicV/es-fine-tuning-paper) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2026-08 | **Hyper-ES: Effective Evolution Strategies for LLM Reasoning via Descent Direction Merging** | Uses a few gradient runs to create descent directions, then applies CMA-ES to DARE-TIES layer-wise merging coefficients; evaluated on six mathematical-reasoning datasets. | [paper](https://arxiv.org/abs/2608.05541) · [code placeholder](https://github.com/kuangrepi/Hyper-ES) · 2026-08 |
| 2026 | **Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights** | RandOpt samples parameter perturbations, selects top experts, and ensembles predictions. The Iterative RandOpt blog extension adds gradient-based distillation and repeats the search, reporting 92.9% on GSM8K with OLMo-3-7B under matched compute; the applicability blog explores sequence-length effects in a sine-wave MLP toy experiment. | [paper](https://openreview.net/forum?id=92oF5bU4cU) · [RandOpt code](https://github.com/sunrainyg/RandOpt) · [Iterative RandOpt branch](https://github.com/sunrainyg/RandOpt/tree/iterative-randopt) · [Iterative RandOpt blog](https://thickets.mit.edu/blogs/iter_randopt.html) · [When does RandOpt work? blog](https://kindxiaoming.github.io/blog/2026/randopt/) · ![ICML 2026 Spotlight](https://img.shields.io/badge/ICML_2026-Spotlight-orange) |
| 2026-02 | **Quantized Evolution Strategies: High-precision Fine-tuning of Quantized LLMs at Low-precision Cost** | Direct-reward ES over discrete quantized weights with error feedback and seed replay; evaluated on Countdown. | [paper](https://arxiv.org/abs/2602.03120) · [code](https://github.com/dibbla/Quantized-Evolution-Strategies) · 2026-02 |
| 2026-02 | **ESSAM: A Novel Competitive Evolution Strategies Approach to Reinforcement Learning for Memory Efficient LLMs Fine-Tuning** | Competitive reward-based ES for memory-efficient reasoning fine-tuning, centered on GSM8K with math/code transfer evaluation. | [paper](https://arxiv.org/abs/2602.01003) · [code](https://github.com/szs777/ESSAM) · 2026-02 |
| 2026-02 | **Fine-Tuning Language Models to Know What They Know** | ESMA directly optimizes metacognitive calibration and alignment rewards. | [paper](https://arxiv.org/abs/2602.02605) · [code](https://github.com/cosmoquester/ESMA) · 2026-02 |
| 2025 | **Evolutionary System 2 Reasoning: An Empirical Proof** | ERO evolves model parameters toward deliberative System-2 reasoning behavior. | [paper](https://doi.org/10.66361/jiss.38) · [code](https://github.com/MetaEvo/ERO) · ![JISS 2025](https://img.shields.io/badge/JISS-2025-orange) |
| 2026 | **Evolution Strategies at the Hyperscale** | EGGROLL generates low-rank perturbations while retaining a high-rank population update for scalable reasoning post-training. | [paper](https://openreview.net/forum?id=bfVJ4GsHrO) · [Transformer/vLLM code](https://github.com/ESHyperscale/eggroll-vllm) · [JAX ES core](https://github.com/ESHyperscale/HyperscaleES) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2025-07 | **ESSA: Evolutionary Strategies for Scalable Alignment** | Evolves singular-value coordinates of LoRA adapters and supports low-precision inference; evaluated on GSM8K, PRM800K, and IFEval. | [paper](https://arxiv.org/abs/2507.04453) · code not located · 2025-07 |

### Multi-turn and agentic reasoning

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-08 | **Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements** | Full-parameter ES evaluates complete agent trajectories with environment rewards, giving trajectory-level parameter attribution without step-level credit assignment. Experiments include 15/45-turn Sudoku, ReAct-style Math and DocVQA, WebArena-Lite, and automatic heuristic design. | [paper](https://arxiv.org/abs/2608.17310) · [code](https://github.com/zz1358m/Agentic-ESOpt) · 2026-08 |

### Understanding ES

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-08 | **Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO** | Explains ES's higher Pass@K through verifier-projected population diversity, contrasts it with GRPO entropy collapse, and studies sequential GRPO–ES training, functional update sparsity, forgetting, and population scaling. | [paper](https://arxiv.org/abs/2608.27351) · [code](https://github.com/yunpengba7/understanding-es) · 2026-08 |
| 2026-02 | **The Blessing of Dimensionality in LLM Fine-tuning: A Variance-Curvature Perspective** | Explains why small ES populations can work in very high dimensions through low effective curvature and a rise-then-decay dynamic; studies GSM8K, ARC-C, and WinoGrande across Qwen2.5 sizes. | [paper](https://arxiv.org/abs/2602.00170) · code not located · 2026-02 |
| 2026-04 | **Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training** | Compares ES and GRPO update geometry even when their reasoning accuracy is similar. | [paper](https://arxiv.org/abs/2604.01499) · [code](https://github.com/Bhoy1/ESvsGRPO) · 2026-04 |
| 2026-01 | **Evolutionary Strategies Lead to Catastrophic Forgetting in LLMs** | Diagnoses prior-capability degradation during ES post-training. | [paper](https://arxiv.org/abs/2601.20861) · code not located · 2026-01 |
| 2026-05 | **Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies** | Reframes forgetting as performance drift and proposes anchored weight decay. | [paper](https://arxiv.org/abs/2605.30148) · code not located · 2026-05 |
| 2026-08 | **Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies** | Shows how ES affects reasoning diversity and pass@k rather than only pass@1. | [paper](https://arxiv.org/abs/2608.12679) · [code](https://github.com/conorfhayes/beyond-the-best-guess) · 2026-08 |

## Zeroth-order optimization

Unless an entry says otherwise, these methods optimize a supervised CE/NLL-style objective with forward-only function evaluations. Their main contribution is making SFT feasible under activation-memory, optimizer-state, or black-box constraints.

### Pretraining

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-10 | **Dust: Pretraining Transformers Without Backpropagation** | Trains transformer language-model weights using token-wise activation perturbations and loss-based credit assignment, with weight-space ES for residual mixing scalars; large-population comparisons require more compute and the claimed EGGROLL efficiency gains include extrapolation. | [research article](https://qlabs.sh/research/dust) · [code](https://github.com/qlabs-eng/dust) · 2026-10 (month only; first-publication day unverified) |

### Single-turn SFT and adaptation

#### Baselines, sparse updates, and subspaces

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-09 | **AIM-ZO: Activation-Informed Subspace Maintenance for Zeroth-Order LLM Fine-Tuning** | Maintains an evolving activation-informed parameter subspace and samples a narrower active set of directions for forward-only ZO updates; evaluated across five LLMs and eleven downstream tasks under matched forward-evaluation budgets. | [paper](https://arxiv.org/abs/2609.35257) · [code](https://github.com/EkkoXy/AIM-ZO) · 2026-09 |
| 2026-09 | **MpSub: A Momentum p-Dimensional Subspace Trust-Region Method for Derivative-Free Fine-Tuning of Large Language Models** | Combines momentum and random directions in a low-dimensional subspace, estimates gradients by central differences, and adapts a trust-region radius; evaluated on OPT-125M/350M with CommitmentBank. | [paper](https://arxiv.org/abs/2609.07666) · code not located · 2026-09 |
| 2026 | **LOZO+: Provably Efficient Zeroth-Order Fine-Tuning via Greedy Low-Rank Subspace Selection** | Uses loss-based feedback and adaptive thresholds to greedily retain effective low-rank subspace directions for forward-only LLM fine-tuning. | [paper](https://proceedings.mlr.press/v306/fang26k.html) · code not located · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2025-11 | **MaZO: Masked Zeroth-Order Optimization for Multi-Task Fine-Tuning of Large Language Models** | Uses parameter importance and multi-task update masks to reduce the search dimension and task conflicts in ZO fine-tuning. | [paper](https://aclanthology.org/2025.emnlp-main.935/) · code not located · ![EMNLP 2025](https://img.shields.io/badge/EMNLP-2025-orange) |
| 2023 | **Fine-Tuning Language Models with Just Forward Passes** | MeZO introduced in-place perturbation and seed replay, reaching inference-level memory for forward-only SFT. | [paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a627810151be4d13f907ac898ff7e948-Abstract-Conference.html) · [code](https://github.com/princeton-nlp/MeZO) · ![NeurIPS 2023](https://img.shields.io/badge/NeurIPS-2023-orange) |
| 2025 | **Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning** | Perturbs a selected coordinate subset for more efficient supervised adaptation. | [paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1e5c2efbddc02c1d971e2f19ccdb07d0-Abstract-Conference.html) · [code](https://github.com/NUS-HPC-AI-Lab/SparseMeZO) · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2024 | **Zeroth-Order Fine-Tuning of LLMs with Extreme Sparsity** | Selects Fisher-sensitive parameters and keeps frozen weights at low precision. | [paper](https://icml.cc/virtual/2024/39663) · [code](https://github.com/GarlGuo/SensZOQ) · ![ICML 2024 Workshop](https://img.shields.io/badge/ICML_2024-ES--FoMo_II-orange) |
| 2025 | **Enhancing Zeroth-order Fine-tuning for Language Models with Low-rank Structures** | LOZO replaces dense random directions with structured low-rank perturbations. | [paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9ccc9d814d3dee4750debaf23061e733-Abstract-Conference.html) · [code](https://github.com/optsuite/LOZO) · ![ICLR 2025](https://img.shields.io/badge/ICLR-2025-orange) |
| 2025 | **Zeroth-Order Fine-Tuning of LLMs in Random Subspaces** | SubZero constructs layer-wise low-rank random subspaces for forward-only adaptation. | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Zeroth-Order_Fine-Tuning_of_LLMs_in_Random_Subspaces_ICCV_2025_paper.html) · [code](https://github.com/zimingyy/SubZero) · ![ICCV 2025](https://img.shields.io/badge/ICCV-2025-orange) |
| 2025 | **TeZO: Empowering the Low-Rankness on the Temporal Dimension in the Zeroth-Order Optimization for Fine-tuning LLMs** | Exploits temporal low-rank structure shared across successive ZO estimates. | [paper](https://arxiv.org/abs/2501.19057) · code not located · 2025 |
| 2026 | **RoZO: Geometry-Aware Zeroth-Order Fine-Tuning on Low-Rank Adapters for Black-Box Large Language Models** | Uses tangent-space perturbations, retraction, and vector transport on the LoRA manifold. | [paper](https://aclanthology.org/2026.eacl-long.80/) · code not located · ![EACL 2026](https://img.shields.io/badge/EACL-2026-orange) |
| 2026-07 | **ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces** | Builds an activation-informed subspace once, then performs ZO SFT in that space; evaluated on language understanding, QA, and commonsense reasoning with Llama-3-8B and OPT-13B. | [paper](https://arxiv.org/abs/2607.01125) · code not located · 2026-07 |
| 2026-08 | **SubZero+: Efficient Zeroth-Order LLM Fine-Tuning via Large Learning Rates** | Combines multi-query estimation, corrected Haar subspaces, and subspace Adam. | [paper](https://arxiv.org/abs/2608.15665) · code not located · 2026-08 |

#### Better directions and lower variance

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-07 | **Universally Empowering Zeroth-Order Optimization via Adaptive Layer-wise Sampling** | AdaLeZO uses non-stationary bandit layer selection and inverse-probability-weighted sampling with replacement to improve ZO estimates and runtime; evaluated on LLaMA/OPT models from 6.7B to 30B. | [paper](https://aclanthology.org/2026.findings-acl.1999/) · code not located · ![ACL Findings 2026](https://img.shields.io/badge/ACL_Findings-2026-orange) |
| 2025-11 | **Private Zeroth-Order Optimization with Public Data** | PAZO uses public-data first-order gradients to guide private ZO estimates for differential privacy; text experiments include RoBERTa-base prompt-tuning on MNLI, distinct from preconditioned PaZO. | [paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/54de3c17e1a2457658a22ad801c721db-Abstract-Conference.html) · [code](https://github.com/xuchengong/PAZO) · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2025-11 | **MUZO: Leveraging Multiple Queries and Momentum for Zeroth-Order Fine-Tuning of Large Language Models** | Averages multiple finite-difference estimates and combines them with Adam for lower-variance forward-only fine-tuning. | [paper](https://aclanthology.org/2025.emnlp-main.432/) · code not located · ![EMNLP 2025](https://img.shields.io/badge/EMNLP-2025-orange) |
| 2024 | **Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models** | MeZO-SVRG adds an anchor-based control variate to supervised ZO fine-tuning. | [paper](https://proceedings.mlr.press/v235/gautam24a.html) · [code](https://github.com/amazon-science/mezo_svrg) · ![ICML 2024](https://img.shields.io/badge/ICML-2024-orange) |
| 2025 | **Harmony in Divergence: Towards Fast, Accurate, and Memory-efficient Zeroth-order LLM Fine-tuning** | DiZO uses layer-wise projection and rescaling after analyzing FO/ZO layer divergence. | [paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ffd4f5a2ea6b93e9bf5af9264d568cf2-Abstract-Conference.html) · [code](https://github.com/Skilteee/DiZO) · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2025 | **KerZOO: Kernel Function Informed Zeroth-Order Optimization for Accurate and Accelerated LLM Fine-Tuning** | Corrects the estimator using kernel-weighted perturbations. | [paper](https://arxiv.org/abs/2505.18886) · code not located · 2025 |
| 2025 | **Towards Fast LLM Fine-tuning through Zeroth-Order Optimization with Projected Gradient-Aligned Perturbations** | P-GAP aligns low-rank perturbations with a projected gradient estimate. | [paper](https://arxiv.org/abs/2510.18228) · code not located · 2025 |
| 2026 | **ConMeZO: Adaptive Descent-Direction Sampling for Gradient-Free Finetuning of Large Language Models** | Samples directions from a cone centered on a momentum estimate. | [paper](https://proceedings.mlr.press/v300/behric26a.html) · [code](https://github.com/LejsDeen/ConMeZO) · ![AISTATS 2026](https://img.shields.io/badge/AISTATS-2026-orange) |
| 2026 | **Low-Rank Curvature for Zeroth-Order Optimization in LLM Fine-Tuning** | LOREN combines low-rank block-diagonal curvature with leave-one-out estimation. | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/39715) · [code](https://github.com/hseung88/loren) · ![AAAI 2026](https://img.shields.io/badge/AAAI-2026-orange) |
| 2026 | **Robust and Efficient Zeroth-Order LLM Fine-Tuning via Adaptive Bayesian Subspace Optimizer** | ABSO aggregates noisy subspace measurements with a Bayesian optimizer. | [paper](https://arxiv.org/abs/2601.01452) · code not located · 2026 |
| 2026 | **Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning** | PIZOO biases samples toward an adaptive prior direction. | [paper](https://arxiv.org/abs/2601.04710) · code not located · 2026 |
| 2026 | **AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning** | Shapes perturbation directions with forward activations. | [paper](https://openreview.net/forum?id=zfVxpXEZti) · [implementation](https://github.com/Yining-Jiang/ActivationGuidedZO-NPU) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2026 | **Zero-Order Optimization for LLM Fine-Tuning via Learnable Direction Sampling** | ZO-LDSD learns a non-isotropic direction distribution. | [paper](https://arxiv.org/abs/2602.13659) · [code](https://github.com/brain-lab-research/zo_ldsd) · 2026 |
| 2026 | **Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization** | ZO-Muon applies spectral orthogonalization to subspace estimates. | [paper](https://arxiv.org/abs/2602.17155) · [code](https://github.com/OPTML-Group/ZO-Muon) · 2026 |
| 2026 | **CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning** | Combines curvature-aware sparse sampling with probability correction. | [paper](https://openreview.net/forum?id=L35b2JZ8gS) · code not located · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2026 | **Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs** | Learns reusable model-specific perturbation strategies. | [paper](https://openreview.net/forum?id=bRS5iwbqlC) · [code](https://github.com/ASTRAL-Group/ZO_Fine_tuner) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |

#### Memory systems, preconditioning, and quantization

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-10 | **VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models** | Adapts persistent action-side parameters in vision-language-action models using ZO finite differences, frozen vision-language state reuse, and schedule-aware prefetching; evaluated on LIBERO shifts with the language backbone frozen. | [paper](https://arxiv.org/abs/2610.06271) · code not located · 2026-10 |
| 2026-09 | **ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning** | Replays seed-and-scalar update logs in a CPU shadow process to build consistent recovery images and persist checkpoints off the GPU critical path for ZO LLM fine-tuning. | [paper](https://arxiv.org/abs/2609.27189) · code not located · 2026-09 · SC26 accepted (author-reported) |
| 2026-07 | **Global Adaptive Momentum Meets Local Personalized Perturbation: Efficient Federated LLM Fine-Tuning with Zeroth-Order Gradients** | Combines local personalized perturbations, ZO gradient transmission and global reconstruction with adaptive momentum aggregation to improve federated LLM fine-tuning under heterogeneous client data. | [paper](https://aclanthology.org/2026.acl-long.1851/) · code not located · ![ACL 2026](https://img.shields.io/badge/ACL-2026-orange) |
| 2026 | **HO-SFL: Hybrid-Order Split Federated Learning with Backprop-Free Clients and Dimension-Free Aggregation** | Combines client-side ZO updates with server-side first-order backpropagation for split federated LoRA fine-tuning, reducing client memory and model-aggregation traffic; split activations still require communication. | [paper](https://proceedings.mlr.press/v306/chen26fd.html) · code not located · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2026 | **Converge Faster, Talk Less: Hessian-Informed Federated Zeroth-Order Optimization** | HiSo reconstructs a global diagonal curvature preconditioner from ZO updates to accelerate federated LLM fine-tuning while exchanging only scalars and random seeds. | [paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3e8b1835833ef809059efa74b9df6805-Abstract-Conference.html) · [code](https://github.com/ZidongLiu/DeComFL) · ![ICLR 2026](https://img.shields.io/badge/ICLR-2026-orange) |
| 2025-11 | **MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines** | Parallelizes multi-query ZO estimation with Multi-Perturbed LoRA and integrates with ExecuTorch for on-device fine-tuning. | [paper](https://aclanthology.org/2025.emnlp-main.1022/) · [code](https://github.com/leigao97/MobiZO) · ![EMNLP 2025](https://img.shields.io/badge/EMNLP-2025-orange) |
| 2025-10 | **Improving the Straight-Through Estimator with Zeroth-Order Information** | FOGZO combines first-order STE gradients with ZO updates for quantization-aware pretraining, reducing estimator bias and ZO computation; language experiments cover LLaMA models up to 0.3B parameters. | [paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f49d76cf84df83a611883c621c96d2d9-Abstract-Conference.html) · [code](https://github.com/1733116199/fogzo) · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2025 | **Bilevel ZOFO: Efficient LLM Fine-Tuning and Meta-Training** | Combines ZO updates of the full backbone with FO adapter updates in a bilevel formulation for fine-tuning and meta-training. | [paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5f999632c48f87cffb214e575581e4a9-Abstract-Conference.html) · code not located · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2025 | **PaZO: Preconditioned Accelerated Zeroth-Order Optimization for Fine-Tuning LLMs** | Uses preconditioned SPSA with diagonal Hessian estimation and moving averages to stabilize and accelerate ZO fine-tuning. | [paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a14193e9d9fb0b03af0b717de1cac8ac-Abstract-Conference.html) · code not located · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2025 | **Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer** | HiZOO estimates diagonal curvature using forward passes. | [paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6bf82cc56a5fa0287c438baa8be65a70-Abstract-Conference.html) · [code](https://github.com/Yanjun-Zhao/HiZOO) · ![ICLR 2025](https://img.shields.io/badge/ICLR-2025-orange) |
| 2025 | **Scalable Zeroth-Order Fine-Tuning for Extremely Large Language Models with Limited GPU Memory** | ZO2 adds parameter offloading and execution overlap for large-model ZO SFT. | [paper](https://openreview.net/forum?id=s0p9xpORgP) · [code](https://github.com/liangyuwang/zo2) · ![COLM 2025](https://img.shields.io/badge/COLM-2025-orange) |
| 2026 | **High-Throughput and Memory-Efficient Zeroth-Order Fine-tuning LLMs with Distributed Parallel Computing** | DistZO2 distributes perturbation evaluations and aggregates only scalar results. | [paper](https://aclanthology.org/2026.findings-acl.2128/) · [ZO2/DistZO2 code](https://github.com/liangyuwang/zo2) · ![Findings of ACL 2026](https://img.shields.io/badge/Findings_of_ACL-2026-orange) |
| 2025 | **HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization** | Adds layer-wise clipping and annealing. | [paper](https://aclanthology.org/2025.emnlp-main.1323/) · code not located · ![EMNLP 2025](https://img.shields.io/badge/EMNLP-2025-orange) |
| 2025 | **QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models** | Integrates quantization into forward-only SFT. | [paper](https://aclanthology.org/2025.emnlp-main.271/) · [code](https://github.com/lloo099/QuZO) · ![EMNLP 2025](https://img.shields.io/badge/EMNLP-2025-orange) |
| 2026 | **Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection** | Assigns FO or ZO updates according to tensor importance. | [paper](https://aclanthology.org/2026.findings-acl.239/) · code not located · ![Findings of ACL 2026](https://img.shields.io/badge/Findings_of_ACL-2026-orange) |
| 2026 | **AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments** | Approximates adaptive moments without full optimizer states. | [paper](https://openreview.net/forum?id=XLc102wbnT) · [code](https://github.com/shawnnn3di/AdaMeZO) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |

### Preference alignment

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2025 | **ComPO: Preference Alignment via Comparison Oracles** | Aggregates parameter perturbations using one-bit preference comparisons for ZO alignment, combined with gradient-based DPO/SimPO in practice; evaluated on UltraFeedback with AlpacaEval 2, Arena-Hard, and MT-Bench, with a 2026 extension adding online KL control. | [paper](https://arxiv.org/abs/2505.05465) · [2026 extension](https://arxiv.org/abs/2609.19144) · [code](https://github.com/PeterLauLukChen/ComparisonPO) · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |

### Multi-turn agent adaptation

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-08 | **Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents** | Perturbs LoRA parameters and scores them with answer perplexity, using the successful deep-research trajectories as SFT data to close the loop. This is multi-turn agent adaptation, but its ZO signal remains a smooth SFT-style proxy rather than a sparse terminal reward. | [paper](https://arxiv.org/abs/2608.09292) · [code](https://github.com/hidk1911/ZOForLLMAgents) · 2026-08 |

### Understanding and systems

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026 | **Zeroth-Order Optimization at the Edge of Stability** | Characterizes mean-square linear stability of two-point ZO methods through the Hessian spectrum and derives bounds using its top eigenvalue and trace; empirical edge-of-stability evidence comes from full-batch vision training. | [paper](https://proceedings.mlr.press/v306/song26ac.html) · code not located · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2026 | **Position: Zeroth-Order Optimization in Deep Learning Is Underexplored, Not Underpowered** | Position paper advocating algorithmic, systems, and evaluation research for ZO deep learning, including subspace structure and query-variance tradeoffs; broader than LLMs and not a new optimizer. | [paper](https://proceedings.mlr.press/v306/liu26gv.html) · code not located · ![ICML 2026 Position](https://img.shields.io/badge/ICML_2026-Position-orange) |
| 2026 | **Learning Dynamics of Zeroth-Order Optimization: A Kernel Perspective** | Analyzes one-step ZO-SGD learning dynamics through a randomly projected empirical neural tangent kernel, relating kernel approximation fidelity to perturbation count and output size under the analysis assumptions. | [paper](https://proceedings.mlr.press/v306/li26in.html) · code not located · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2024 | **Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark** | ZO-Bench compares objectives, trainable interfaces, and model families across representative language-understanding and generation tasks. | [paper](https://proceedings.mlr.press/v235/zhang24ad.html) · [code](https://github.com/ZO-Bench/ZO-LLM) · ![ICML 2024](https://img.shields.io/badge/ICML-2024-orange) |
| 2025 | **Zeroth-Order Optimization Finds Flat Minima** | Connects stochastic ZO dynamics to flat-minimum bias and includes language-model fine-tuning experiments. | [paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ebc62a3af9342eb4ebc728e5c5bc4cca-Abstract-Conference.html) · [code](https://github.com/Liang137/FlatZero) · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2026 | **LLM Zeroth-Order Fine-Tuning is an Inference Workload** | Shows that repeated ZO scoring can be reorganized around an inference-serving runtime. | [paper](https://arxiv.org/abs/2605.28760) · [code](https://github.com/playeriv65/zo-vllm) · 2026 |

## Related research

These companion entries include methods that retain backpropagation or do not update persistent model parameters; each entry states that boundary explicitly.

### Hybrid first- and zeroth-order methods

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-10 | **Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM Fine-Tuning** | Hybrid ZFO uses a backpropagation-based first-order direction and two additional objective evaluations to choose a curvature-aware step; it retains task-gradient computation and is included as related research rather than forward-only training. | [paper](https://arxiv.org/abs/2610.02190) · [code](https://github.com/nizswan/Zeroth-First-Order-Framework) · 2026-10 (venue not independently verified) |

### Inference-time calibration without parameter updates

| Date | Paper | Contribution | Resources |
|---|---|---|---|
| 2026-10 | **HeadEdit: Calibrating Language Model Behavior Through the Frozen Unembedding Matrix** | Extracts a low-rank behavioral subspace from paired completions and applies input-dependent vocabulary-wide corrections at inference time through a frozen unembedding matrix; no persistent model parameters are updated. | [paper](https://arxiv.org/abs/2610.01170) · code not located · 2026-10 |
<!-- GENERATED CATALOG:END -->

## Scope

Vision-language-action adaptation is included when ZO updates persistent action-side parameters; the language backbone may remain frozen. The separate **Related research** section includes explicitly labeled hybrid methods and inference-time calibration without parameter updates.

Included methods must optimize persistent LLM parameters or parameter-efficient modules through ES populations, evolutionary selection, or zeroth-order/function-evaluation estimates. Full weights, LoRA/adapters, structured subspaces, and quantized parameters are in scope.

Out of scope:

- prompt, instruction, chain-of-thought, candidate-answer, skill, memory, and reasoning-state evolution;
- generic RL or agent self-improvement without a parameter-space ES/ZO contribution;
- architecture or hyperparameter search that does not train/adapt the LLM parameters;
- vision-only and speech-only applications.

## Contributing

Paper additions and corrections are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and use the paper-request issue template. Every entry should include a primary paper URL and its official code entry when one exists; otherwise write `code not located` so missing implementations are explicit.

Bibliographic records are available in [papers.bib](papers.bib).

The latest paper-and-GitHub code availability review is recorded in [CODE_AUDIT.md](CODE_AUDIT.md).

## Acknowledgements

The initial bibliography was derived from the local *Gradient-Free Optimization for LLM Reasoning* survey. The repository layout is inspired by [Awesome-Latent-CoT](https://github.com/EIT-NLP/Awesome-Latent-CoT); descriptions and the ES/ZO task taxonomy are specific to this collection.
