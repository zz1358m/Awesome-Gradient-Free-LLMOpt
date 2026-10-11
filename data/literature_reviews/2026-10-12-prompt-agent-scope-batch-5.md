# 2026-10-12 提示词与智能体范围审查：批次 5（语义修正版）

本批次逐篇审查 40 条。语义修正版按真实机制判定，不以是否自称 agent/harness、原类别名或关键词规避范围。

## 统计

- `defer_agent_no_model_training`：2 条
- `defer_agent_training_unverified`：1 条
- `defer_prompt_core`：3 条
- `keep_unaffected`：34 条

## 逐篇决定

### 1. Forward-Only LoRA-MoE Allocation via Module Activation Geometry

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=HFXtAkQ0YH
- 官方摘要证据：Low-rank adaptation (LoRA) mixtures of experts (LoRA-MoE) increase adaptation capacity through conditional expert activation. However, many conventional LoRA-MoE methods adopted in large language models (LLMs) typically restrict MoE placement to predefined modules, such as the feed-forward networks (FFNs), and use uniform expert configurations across them. This design overlooks that different modules may need different computational capacity for a downstream task. For a more adaptive and more efficient solution, we introduce BLAde (Budget-constrained LoRA
Mixture-of-Experts Adaptive Allocation), a task-adaptive framework that jointly determines where MoE capacity should be introduced and how the available factor budget should be allocated across LoRA modules. Using lightweight statistics collected from forward activations, BLAde identifies promising modules for conditional expert specialization, adaptively determines their number of experts and top-$k$ routing configurations, and reallocates LoRA ranks across the remaining modules under a factor budget. In this way, BLAde reformulates LoRA-MoE design from a manually specified, architecture-wide configuration into a task-adaptive and budget-aware allocation problem, allocating conditional capacity according to module activation geometry.

### 2. ThinQuant: Scalable Rotation Learning For Weight And Activation Quantization

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=EQuFNpm6gc
- 官方摘要证据：Learned rotations play an important role in enabling low-bit weight and activation quantization of
large language models by smoothing outliers in the activation distribution. State-of-the-art approaches include gradient-based procedures such as SpinQuant and computationally friendlier gradient-free
approaches such as DartQuant, but both remain hard to scale to the largest architectures.
To address the computational bottlenecks in gradient-free rotation learning, we introduce two ideas for efficiency, (i) a data selection procedure which reduces the required number of calibration data points, and (ii) an exact reduction of the associated optimization on this reduced calibration set. Our data selection procedure exploits the geometric structure of the convex hull of the activations. Using this idea, we show that a carefully selected calibration set with several orders of magnitude fewer activations than state-of-the-art rotation-based methods can match their performance in low-bit quantization settings. Under this extreme data efficiency, the selected activations span an
$r$-dimensional subspace with $r<d$, making optimization over a $d\times d$ rotation equivalent to optimizing a
$d\times r$ matrix on the Stiefel manifold. We solve this reduced problem using an efficient ADMM algorithm that iteratively
employs thin matrix updates at every step, hence the name ThinQuant.
For Llama-3-70B with W4A4KV4 quantization, ThinQuant completes the entire rotation calibration in under 12 minutes and achieves a WikiText-2 perplexity of 5.63, compared with 7.55 for DartQuant, which requires 111 minutes. Unlike SpinQuant and DartQuant, ThinQuant also scales to Llama-3.1-405B on a single H200 GPU, completing rotation calibration in just over 2 hours and achieving WikiText-2 perplexity of 2.97 at W4A4, compared with 3.48 for GPTAQ+QuaRoT.

### 3. SchurQuant: Groupwise Discrete Optimization for Layer-Wise LLM Quantization

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=mBjfVGFp8m
- 官方摘要证据：Weight-only post-training quantization (PTQ) enables the deployment of large language models under tight memory budgets, but accuracy often collapses at 2--3 bits.
Existing backpropagation-free PTQ optimizers have two limitations: group decisions ignore the correction that the remaining continuous suffix can absorb, and discrete refinements typically keep the affine quantization grid fixed.
We introduce SchurOpt, which analytically eliminates the suffix's optimal continuous response, yielding an exact groupwise quadratic with Schur-complement curvature.
It then alternates closed-form row-wise scale/zero-point refitting with coordinate descent over integer codes. With the GPTQ objective fixed, SchurOpt improves mean zero-shot accuracy on 2-bit Qwen3-4B by 11.88 percentage points (pp).
At higher precision, however, tighter reconstruction does not consistently improve end-model metrics.
SchurQuant therefore combines SchurOpt with quantized-prefix teacher reconstruction, reference-weight regularization, residual-add targets, and teacher-decision token weighting.
Across eight Llama and Qwen models, SchurQuant achieves the highest mean zero-shot accuracy among the evaluated backpropagation-free PTQ baselines, outperforming the strongest baseline by 9.65 pp at 2 bits.

### 4. ReQuant: Fixed-Grid Discrete Refinement for Post-Training Quantization

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=PdHbXU64LT
- 官方摘要证据：Post-training quantization (PTQ) is widely used to reduce the memory and computational cost of large language models. Existing PTQ methods typically initialize quantized models with heuristic rules or greedy optimization, and usually treat the resulting integer assignments as final. We introduce ReQuant, a backpropagation-free fixed-grid refinement stage *within* PTQ that optimizes an executable quantized model while preserving its format. Agnostic to the PTQ initializer, ReQuant starts from an existing feasible quantized model and iteratively revisits its discrete weight assignments on the fixed quantization grid. Accepted updates strictly reduce the mean squared reconstruction error and remain on the original grid. ReQuant thus integrates with existing PTQ pipelines as a plug-and-play post-processing stage. Experiments across diverse model families, bit-widths, and downstream tasks show that ReQuant consistently improves quantized models from heterogeneous PTQ initializers, with especially large gains on simple initializers and lower bit-widths. Notably, ReQuant can refine a simple round-to-nearest initialization across multiple sweeps until it approaches or surpasses GPTAQ under the same quantization format.

### 5. KLIQ: KL-Informed Low-Bit Quantization via Attention-Distribution-Aware Fisher-Kronecker Curvature

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=3zKL0tfzM3
- 官方摘要证据：Post-training quantization (PTQ) reduces the memory and computation costs of large language models (LLMs), but preserving accuracy at very low bit-widths remains challenging. Existing reconstruction-based curvature approximations in second-order PTQ can overlook the distribution-dependent sensitivity of attention probabilities to query and key quantization errors. We introduce KLIQ, a backpropagation-free PTQ method that uses KL divergence between full-precision and quantized attention distributions to guide curvature estimation, quantization parameter selection, and error compensation. KLIQ introduces three key innovations: (1) a Fisher-Kronecker curvature surrogate that maps a diagonal approximation of the attention-score categorical Fisher to query and key weight spaces; (2) staged functional calibration that conditions key quantization parameter selection on already quantized and compensated queries to account for query-key error interactions; and (3) KL-derived compensation statistics for compensating quantization errors propagated from preceding layers. Extensive experiments across multiple model families show that, when combined with conventional outlier-suppression techniques, KLIQ achieves state-of-the-art performance on language modeling and downstream tasks under low-bit weight-only and weight-activation quantization. The source code is available at https://anonymous.4open.science/r/KLIQ-7440/.

### 6. JARQ: Joint Alternating Refinement for Quantization

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=9lEvG6Tfku
- 官方摘要证据：Group-wise post-training quantizers for large language models round weights onto a grid that is not refit to the resulting integer codes. We show that this leaves accuracy on the table: the best grid depends on the codes, input correlations couple the errors of different groups, and useful code changes often involve many codes at once. We propose JARQ (Joint Alternating Refinement for Quantization), a plug-in refinement that starts from any group-wise quantizer and alternates a joint least-squares fit of all group scales with bounded Babai proposals that move many codes of a group together on the current grid. The problem is a bilinear box-constrained mixed-integer least-squares problem; the solver is backpropagation-free, does not increase the layer-wise objective under exact scale solves, and keeps the host's bit width, groups, zero points, and inference cost. Across Llama-2, Llama-3, and Qwen models with RTN, GPTQ, OmniQuant, and AWQ hosts, JARQ lowers perplexity in 90 of 96 comparisons, cuts three-bit RTN perplexity by up to 36%, raises mean multiple-choice accuracy in 23 of 24 configurations, and improves QEP, QuaRot, and OJBKQ outputs, at under a minute per 7B block.

### 7. BRACE: Error-Guided Mixed-Precision LLM Quantization Without Backpropagation

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=XnF8RSUPxE
- 官方摘要证据：Post-training quantization (PTQ) reduces the deployment costs of large language models (LLMs). Uniform-precision quantization remains a widely used approach, but it often incurs substantial quality degradation at ultra-low bit-widths. In contrast, mixed precision quantization offers a better accuracy–budget trade-off by selectively assigning precision. However, at ultra-low precision, a quantization error cannot be judged by its local magnitude alone. Its significance also depends on the stage-specific response it should induce. This observation motivates a common design principle for bit allocation, error compensation, and quantizer calibration: quantization error should not merely be minimized locally, but should guide the response taken at each stage. Our approach builds on this observation and introduces three key components: (i) Curvature-Conditioned Residual Transport (CCRT) allocates bits using a joint curvature-conditioned cost that combines the error committed at a group with the one-step correction burden transported to its immediate successor; (ii) Block-Anchored Ridge Compensation (BARC) pairs reference and quantized paths within each block to derive a ridge-stabilized correction for propagated error before applying GPTQ to the corrected center under a metric with a ridge term; and (iii) Residual-Feedback Grid Refinement (RFGR) converts the elementwise errors of curvature-weighted first-pass grids into weights for a second scale and zero-point fit at the assigned bit-width, with adjacent-bit error reductions providing the feedback signal. Built on a GPTQ backbone, BRACE uses only a small calibration set and local layer-wise statistics, without backpropagation or iterative retraining. Extensive experiments on language modeling and zero-shot commonsense reasoning across the Llama2, Llama3, Qwen3, and OLMo3 model families show that BRACE achieves state-of-the-art performance among comparable backpropagation-free PTQ methods under 2- and 3-bit weight-only quantization settings. Code will be released upon acceptance.

### 8. Functional Memory Compilation: Behavior-Level Migration of Aggregate LoRA Memory

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=fKWM0tmEOE
- 官方摘要证据：When a language model is upgraded, facts accumulated in its memory adapter may become inaccessible through the successor. Migration is difficult when the original interaction history is unavailable. Parameter mappings need not preserve individual answers, while response distillation requires target gradient training. We study migration from an already-trained aggregate low-rank adaptation (LoRA) memory. The source model and retained questions remain accessible, but the questions' original answers are unavailable. We propose Functional Memory Compilation (FMC), which transfers the source's observable answers rather than its parameter coordinates. FMC recovers responses at retained questions and retokenizes them for the successor. It turns selected answer positions into joint constraints on the target's output. Batched forward computation followed by one analytic low-rank fit installs a target-native output-head adapter without backpropagation or optimizer steps. Across the evaluated memory tasks, FMC improves task scores and lowers fixed-pool target installation cost over same-content distillation at the evaluated limited training budget.

### 9. Towards Unbiased Test-Time Adaptation for Vision–Language Models

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=yngr3bVtsX
- 官方摘要证据：Statistics-based test-time adaptation (TTA) provides an efficient way to adapt vision-language models (VLMs) by summarizing test streams into fixed-size class statistics without backpropagation or instance storage. However, there are two limitations in this paradigm. First, persistent class-wise prediction preferences can repeatedly misallocate incoming features, leading to prediction-biased accumulation in the class states. Second, additive feature aggregation can retain class-shared components, leading to classifier homogenization even under correct class allocation. To address these issues, we propose _**U**nbiased **T**est-Time **A**daptation_ (**UTA**), which jointly regulates class allocation and classifier construction. Specifically, to mitigate prediction-biased accumulation, a *History-Guided Allocation Debiasing* mechanism is designed to regulate class allocation using historical class responses, thereby reducing allocation errors in the accumulated class states. Furthermore, to alleviate classifier homogenization, we introduce an *Activity-Conditioned Classifier Construction* strategy to reweight accumulated class states according to stream-wide coordinate activity, which limits shared-component dominance and preserves class-specific distinctions. Extensive experiments demonstrate strong adaptation performance across multiple settings while preserving 95% of zero-shot CLIP throughput on large-scale ImageNet-1K. Moreover, the proposed components can serve as lightweight plug-ins for existing statistics-based TTA methods.

### 10. Block-Level Positional Reconstruction for Sparse Long-context Prefilling

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=2jfW67zbil
- 官方摘要证据：Long-context inference has become a defining capability of large language models, but exact dense attention remains costly due to its quadratic scaling with sequence length.
Block-sparse attention offers a hardware-friendly alternative by selecting a small set of relevant key blocks for each query block, yet estimating block importance accurately without model retraining or costly token-level search remains challenging.
Existing block estimators often pool RoPE-rotated token representations, causing within-block phase variation to induce frequency-dependent cancellation and distort position-sensitive block affinities.
We empirically find that, although unrotated block summaries cannot exactly recover the omitted phase-aware interaction, its predictable component follows a frequency- and distance-conditioned response that transfers across input sequences.
Based on this observation, we propose \textbf{RePhase}, which combines current unrotated block interactions with a reusable positional-response profile and the exact relative RoPE phase.
The profile is fitted once from unlabeled forward-pass statistics without backpropagation or model-parameter updates, and enables direct block-level scoring at inference without token-level search.
Experiments on long-context text and video tasks show that RePhase approaches full-attention performance across 4K--128K contexts, keeps block-estimation overhead below 3.4 ms, and achieves a 5.03$\times$ speedup over FlashAttention at 128K.

### 11. DeltaNet-PC: Test-Time Memory Without Backpropagation Through Time

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=I0AW0dp7WL
- 官方摘要证据：Test-time memorization of sequential information is a foundational capability for any intelligent system that needs to rapidly store and retrieve data, as demonstrated by the attention mechanism in large language models. However, Transformers and linear attention variants are trained via backpropagation through time (BPTT), which has drawbacks such as its enormous memory requirements. Predictive coding (PC)—an algorithm that optimizes a prediction-error energy function with local updates—offers a compelling solution but still lacks test-time memory for sequential data. We develop a solution to this problem by treating the per-step memory update $\Delta\boldsymbol{S}_t$ as a latent variable, as opposed to a slow weight to be learned. By taking the log probability of a standard PC-based probabilistic model, we derive a PC-native solution for verbatim sequence memory, and relate our update rule to common choices in the linear attention literature (e.g., DeltaNet). We present an extensive set of empirical tests to probe our system's properties, including its scaling capacity, memory footprint, and ability to infer a context from evidence (e.g., bank (river) vs. bank (money)). We show how DeltaNet-PC can be used for storing single sequences of data, multiple sequences of data, and key-value associative memory pairs with perfect recall accuracy.

### 12. Budget-Constrained Test-Time Adaptation for Vision-Language Models: A Protocol, Diagnosis, and Lightweight Fix

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=vUT5dDG1HY
- 官方摘要证据：Test-time adaptation (TTA) promises label-free robustness for vision-language models (VLMs) deployed in shifting environments, yet recent audits report that accuracy gains are marginal and come at the cost of trustworthiness---and none of the existing benchmarks measures the compute budget that real deployments must respect. We introduce BUDGET-TTA, an evaluation protocol with T4-GPU-hours as a first-class cost axis, covering batch=1 streaming $\times$ label shift $\times$ trustworthiness (ECE, OOD detection, stability), with checkpoint-resume support for low-cost cloud quotas. Using this protocol, we audit cache-based gradient-free VLM TTA and find that calibration degrades by up to 6.2$\times$ without accuracy gains---on ImageNet-V2, a simplified TDA variant matches zero-shot accuracy (52.87 vs. 52.93) while inflating ECE 6.2$\times$ (2.65 $\rightarrow$ 16.50); the same pattern holds on ImageNet-R. We then propose GATE-TTA, a fully backprop-free method combining confidence gating (skip when confident), smooth cache voting, sliding-window label-shift debiasing, and zero-shot anchored calibration---interpolating the adapted distribution toward the well-calibrated zero-shot one ($\lambda=0.7$). GATE-TTA repairs 32--66\% of the ECE degradation at negligible accuracy cost, and its zero-shot-gated cache admission (7.2\% OOD admission rate, 0.73 MSP-AUROC) makes it nearly immune to the cache contamination that inflates unanchored TDA's ECE by $+10.4$ points under paired 5\% OOD injection, and adds only 0.0036 T4-hours of adaptation overhead per 10k samples---orders of magnitude cheaper than gradient-based TPT (~185$\times$ cheaper end-to-end). Our results carry a practical message: under tight budgets, skip adaptation unless the shift is severe; if you adapt, anchor to zero-shot to keep calibration.

### 13. Are We Measuring the Right Angles? Spherical Test-Time Adaptation of Vision-Language Models

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=GW2ZqLgLdX
- 官方摘要证据：Test-time adaptation (TTA) for vision--language models (VLMs) aims to improve robustness under distribution shifts by exploiting unlabeled test data during inference. Existing CLIP-TTA methods either optimize prompts through backpropagation or estimate Euclidean statistics from normalized CLIP features, despite CLIP performing classification through cosine similarity on the unit hypersphere. We propose \textbf{STRA}, a \textbf{S}pherical \textbf{T}est-\textbf{T}ime \textbf{R}obust \textbf{A}daptation framework for closed-form, backpropagation-free online CLIP adaptation. Our central view is that closed-form CLIP-TTA should recover a target-domain angular coordinate system under a pullback-vMF model, rather than fit an ambient Euclidean classifier. STRA instantiates this view through label-free geometry calibration from streaming second-order statistics and text-anchored spherical prototype updates driven by sparse soft pseudo-labels. This design avoids raw-feature caching and the selection bias induced by confidence-filtered geometry, decouples marginal geometry estimation from semantic pseudo-label updates, and couples them only through a shared bilateral angular map, while maintaining a single fixed configuration across datasets and backbones. Extensive experiments across natural distribution shifts, fine-grained recognition, and corruption robustness demonstrate consistent improvements over recent CLIP-TTA baselines with favorable computational efficiency. The code is available at \url{https://anonymous.4open.science/r/STRA}.

baselines at favorable computational cost.

### 14. HeadEdit: Calibrating Language Model Behavior Through the Frozen Unembedding Matrix

- 决定：`keep_unaffected`
- 原分类：`related_inference`
- 论文特定依据：非提示词核心且非智能体范围：该论文处理推理校准、激活编辑、VLM统计适配或推理系统机制。
- 模型参数/组件边界：按原摘要更新激活、统计量、缓存/注意力配置或其他推理对象；本次范围规则不自动排除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=pHZvxtuPkK
- 官方摘要证据：Alignment does not eliminate behavioral errors in language models. Models may still refuse benign requests, call unnecessary tools, or yield to false user claims.
Current methods mitigate such errors as a computation problem, and rarely explore if the desired behavior is already encoded in the model's representation.
Motivated by the observation that behavior-relevant information remains linearly decodable from the final hidden state even when the resulting logits produce the undesired behavior,  we introduce HeadEdit, a gradient-free method that calibrates model behavior through the unembedding.
HeadEdit extracts a low-rank behavioral subspace from paired completions and uses each prompt’s coordinates within it to generate a vocabulary-wide correction, thereby implementing implicitly adaptive steering without manually specified target tokens or parameter updates.
HeadEdit improves all nine experimental settings across three tasks and three model families, with negligible inference overhead and no systematic loss of general capabilities.
It also reveals a connection to gradient-based alignment. HeadEdit's low-dimensional representation partly predicts how preference tuning changes output logits on unseen prompts.
The subspace learned from the model can also be reused after tuning, improving performance without re-extracting or retuning.
These results show that HeadEdit provides a practical, lightweight, and interpretable way to calibrate model behavior through the unembedding.

### 15. ZOSteer: Steering Language Models from Scalar Rewards Alone

- 决定：`keep_unaffected`
- 原分类：`related_inference`
- 论文特定依据：非提示词核心且非智能体范围：该论文处理推理校准、激活编辑、VLM统计适配或推理系统机制。
- 模型参数/组件边界：按原摘要更新激活、统计量、缓存/注意力配置或其他推理对象；本次范围规则不自动排除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=aKo2pnRE0y
- 官方摘要证据：Activation steering controls a language model by adding a fixed vector to its residual stream, but existing methods derive this vector from contrastive prompt pairs or differentiable objectives, leaving behaviors specified only by a scalar, non-differentiable reward largely out of reach. We introduce ZOSteer, which estimates a steering vector as the zeroth-order gradient of the reward in activation space. We inject isotropic Gaussian perturbations at a single layer, score each perturbed model with the reward, and take the cross-covariance between perturbations and rewards. This estimates the gradient of the Gaussian-smoothed reward from forward passes alone, without contrastive data or backpropagation. Because the reward is an average over items, the same perturbations also yield a gradient for every training item at no extra cost. The residual spectrum of these item gradients reveals sub-populations whose gradients conflict with the majority, and reweighting them repairs the pooled direction without new forward passes. Across three 1B-scale models and four benchmarks, ZOSteer gives the largest gains on GSM8K for every model, and its reweighted variant closes most of the gap to the strongest baseline on bAbI QA20 and surpasses it on CUTE SubChar, typically with fewer perturbations than the hidden dimension. These results suggest that what a single vector can steer depends on how a task's items agree, not only on how the model represents the capability.

### 16. You Only Reprogram Once: Rethinking Prolonged Training for Visual Reprogramming

- 决定：`defer_prompt_core`
- 原分类：`related_closed_form`
- 论文特定依据：论文以 visual reprogramming 为研究对象：主方案从冻结模型响应构造下游映射，扩展方案直接优化 visual prompt；其适配对象是输入/视觉提示而非模型参数。
- 模型参数/组件边界：基础模型冻结；BDM 更新统计映射，YORO-FP 更新 visual prompt，摘要未报告语言/视觉模型权重训练。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=1Ijpq0Nino
- 官方摘要证据：Visual reprogramming is a parameter-efficient method for adapting pretrained models, yet its training can remain computationally expensive: even with a frozen backbone, visual prompts are often optimized through the full model for hundreds of epochs. Before changing what the pretrained model sees, we ask whether we are fully using what it already tells us. We find that modeling the full source response can already yield strong downstream predictions without prompt optimization. Motivated by this observation, we introduce You Only Reprogram Once (YORO), which constructs a downstream predictor from the frozen response space in a single forward-only traversal. Its Bayesian Discriminant Mapping (BDM) derives a covariance-aware affine mapping from streaming class statistics, requiring no backpropagation, optimizer updates, or repeated visits to the training set. When further input adaptation helps, YORO-FP optionally refines the visual prompt for 20 epochs. BDM also extends naturally to CLIP by treating attribute-prompt similarities as source responses. Across three full-data settings, YORO improves average accuracy over the strongest prior gradient-free mapping by 18.4--24.4\%. On 16-shot CLIP, it raises the four-backbone average from 71.4\% to 77.2\%. YORO-FP provides further gains on selected tasks, while validation often retains the one-pass predictor. These results suggest a different default for visual reprogramming: read out the frozen response first, and optimize the input only when needed.

### 17. Test-Time Safety Alignment

- 决定：`defer_prompt_core`
- 原分类：`related_inference`
- 论文特定依据：核心机制是在测试时用零阶安全分数优化输入 embeddings，属于软提示/输入提示优化。
- 模型参数/组件边界：模型权重不更新；更新对象为当前输入 embeddings，不形成模型参数训练。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=dcWHMLpYZE
- 官方摘要证据：Recent work has shown that a model's input word embeddings can serve as effective control variables for steering its behavior toward outputs that satisfy desired properties. However, this has only been demonstrated for pretrained text-completion models on the relatively simple objective of reducing surface-level profanity in short continuations. A natural and practically important question is how well input embeddings can control aligned models, which produce an imbalanced bimodal refuse-or-comply output distribution rather than the smooth distribution characteristic of open-ended generation. We explore this in the context of safety, showing that input word embeddings can be optimized in a sub-lexical manner to minimize the semantic harmfulness of aligned model responses. Our approach uses zeroth-order gradient estimation of a black-box text-moderation API with respect to the input embeddings, and then applies gradient descent on these embeddings to minimize the harmfulness of the generated text. Experiments show that the proposed method neutralizes every safety-flagged response on standard safety benchmarks for four of the five evaluated models, and reduces the number of flagged responses on the fifth.

### 18. Rethinking Neural Thickets Without Weight Perturbations

- 决定：`keep_unaffected`
- 原分类：`related_inference`
- 论文特定依据：非提示词核心且非智能体范围：该论文处理推理校准、激活编辑、VLM统计适配或推理系统机制。
- 模型参数/组件边界：按原摘要更新激活、统计量、缓存/注意力配置或其他推理对象；本次范围规则不自动排除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=imjxSp8e1N
- 官方摘要证据：The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen and adding a random bias to its output logits matches or exceeds full-weight perturbations on most reasoning tasks. This suggests an alternative explanation based on output diversity, validation-based selection, and voting. We formalize this view as Perturb-Select-Vote (PSV), a general procedure that generates perturbed predictors, selects high-performing members on a small validation set, and aggregates their predictions.

This interpretation connects Neural Thickets to established inference-time methods, including sampling, self-consistency, and verifier-guided selection. A first-order analysis further shows that small weight perturbations act primarily through their induced logit shifts. We extend this analysis to vision, where logit PSV substantially improves performance under domain shift, including on Earth observation, while full-weight perturbations provide little additional benefit. Together, these results suggest that the gains attributed to nearby weight-space experts can instead be obtained through output diversity, selection, and voting. Logit PSV realizes these benefits with a fully frozen model, providing a simple, training-free alternative to full-weight perturbation ensembles across language and vision.

### 19. Modular Norm RandOpt: Population-Efficient Ensembling through Architecture-Aware Perturbations

- 决定：`keep_unaffected`
- 原分类：`related_inference`
- 论文特定依据：非提示词核心且非智能体范围：该论文处理推理校准、激活编辑、VLM统计适配或推理系统机制。
- 模型参数/组件边界：按原摘要更新激活、统计量、缓存/注意力配置或其他推理对象；本次范围规则不自动排除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=isaVxUY5zV
- 官方摘要证据：RandOpt samples weight-perturbed language models and ensembles
top-ranked candidates through plurality voting, but its global
perturbation scale ignores heterogeneous module geometry.
We propose Modular Norm RandOpt, an
architecture-aware sampling method using module-wise natural norms
and calibrated scales while preserving selection and voting.
It outperforms RandOpt using $3\times$ fewer candidates on Countdown
and at least $12\times$ fewer on GSM8K, with corresponding
wall-clock savings.
Evaluations across seven tasks and three Qwen scales
($0.5$B--$3$B) show higher mean accuracy than RandOpt on Countdown,
GSM8K, and MATH-500 at every scale.
The gains extend to Llama 3.2 $3$B and Gemma 3 $4$B on Countdown
and GSM8K.
On Qwen2.5-1.5B, our ensembles also achieve higher mean accuracy
than iterative baselines on both tasks at comparable main-run
evaluation budgets.
On GSM8K, a tail-density diagnostic implies only a
$1.2$--$1.8\times$ candidate reduction, while most ensemble
improvement is associated with more favorable correct-expert support.
These results highlight perturbation geometry as a key design
choice for population-efficient, gradient-free search around
pretrained models.

### 20. ActivationSMC: Sequential Monte Carlo for Optimizing Activation Steering

- 决定：`keep_unaffected`
- 原分类：`related_inference`
- 论文特定依据：非提示词核心且非智能体范围：该论文处理推理校准、激活编辑、VLM统计适配或推理系统机制。
- 模型参数/组件边界：按原摘要更新激活、统计量、缓存/注意力配置或其他推理对象；本次范围规则不自动排除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=yMxixVoJCr
- 官方摘要证据：Activation steering controls pretrained language models and beyond at inference by modifying internal activations, but its effectiveness hinges on jointly deciding where and how strongly to intervene. This creates a hard optimization over a mixed discrete-continuous space with coupled layer choices and often non-differentiable rewards, poorly handled by fixed grids or greedy decoupled search. We introduce {\bf ActivationSMC}, a derivative-free black-box framework based on Sequential Monte Carlo that maintains a population of full steering configurations. It guides the population toward high-reward regions via reweighting, resampling, and stochastic mutation that preserves diverse modes, with a multi-fidelity schedule that uses small subsets for cheap early exploration and larger subsets for precise refinement. Without updating model weights, ActivationSMC configures off-the-shelf activation steering operators such as COLD-Steer, AUSteer, CAA, and Spherical Steering. Across TruthfulQA, R-Bench, AMBER, as well as text-to-image generation using Stable Diffusion, ActivationSMC consistently outperforms native tuning. It improves collapsed baselines by up to 28.9 percentage points, raises compositional text-to-image alignment by 20–30 percentage points across four steering operators, and substantially widens its lead as joint multi-layer optimization exposes the breakdown of decoupled heuristics.

### 21. Inference-Time Machine Unlearning via Gated Activation Redirection

- 决定：`keep_unaffected`
- 原分类：`related_inference`
- 论文特定依据：非提示词核心且非智能体范围：该论文处理推理校准、激活编辑、VLM统计适配或推理系统机制。
- 模型参数/组件边界：按原摘要更新激活、统计量、缓存/注意力配置或其他推理对象；本次范围规则不自动排除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=FjGiCaa2p1
- 官方摘要证据：Large Language Models (LLMs) memorize vast amounts of training data, raising concerns regarding privacy, copyright infringement, and safety.
Machine unlearning seeks to remove the influence of a targeted forget set \mathcal{D}_f while preserving model performance, ideally approximating a model retrained from scratch without \mathcal{D}_f.  Once an LLM is in use, every new request to make it forget specific content demands updating its weights. However, unlearning through parameter updates is expensive, hard to audit, and can be undone by quantization.
We show that unlearning can be enforced entirely at inference time, without training, gradients, or weight changes. We introduce Inference-Time Unlearning via Gated Activation Redirection (GUARD-IT), a training- and gradient-free method that unlearns via input-dependent activation steering at inference time.
\gls{guard} stores the content to be forgotten as a small library of activation directions, and during inference, it routes each query through a similarity gate that activates only for relevant directions and applies them as a norm-preserving rotation of the residual stream, while unrelated queries pass through the unmodified model.
The same design carries across three model families and nine checkpoints from 0.8B to 8B parameters, and new forget requests are absorbed by one offline pass of forward passes.
On TOFU, against 16 gradient-based and inference-time baselines, and on MUSE and WMDP, GUARD-IT forgets without breaking the model, and on TOFU it is the only method that suppresses memorization in every Llama configuration without collapsing: it keeps utility and fluent generation in every configuration, moves the model's output distribution closest to a model that never saw the forgotten data on the \texttt{forget01} split, survives 4- and 8-bit quantization and ten sequential forget requests, and holds under jailbreak attacks.

### 22. Modulating LLM Behavioral Preferences by Reweighting Just a Few Weights

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=IuMamxh76q
- 官方摘要证据：Post-training can instill dispositional behaviors in large language models (e.g., refusal & sycophancy behaviors). We find that such behavioral preferences can be removed or mitigated by removing or downweighting just a few corresponding weights, or even amplified by upweighting the few. Our proposed approach, BLADE (Behavioral Localization via Activation-Difference Estimation), is a gradient-free, forward-only method that scores weights and identifies those that contribute to behavioral preferences across layers, enabling removal or modulation of an LLM’s behavioral preferences to a desired direction. We show that, through extensive experiments on various behaviors and models, our approach effectively and efficiently modulates the model’s behavioral preferences.

### 23. HIRE: Hippocampal Replay for Test-Time Agentic Reinforcement Learning

- 决定：`defer_agent_no_model_training`
- 原分类：`related_inference`
- 论文特定依据：HIRE 是智能体测试时强化学习，但官方摘要明确不更新模型参数；它通过 replay 与优势重加权适配冻结策略。
- 模型参数/组件边界：智能体 policy 冻结；持久/外部状态是成功轨迹 replay 与重估优势，没有模型参数更新。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=kbCX1FVPSj
- 官方摘要证据：Gradient-free test-time reinforcement learning (RL) adapts large language model
(LLM) agents through experience without updating model parameters, avoiding
the weight-access requirements and parameter-optimization costs of training-time RL.
In this paper, we identify a discovery--consolidation gap in test-time RL:
agents can discover high-return behavior yet fail to sustain the achieved
returns in later rollouts. In existing advantage-based methods, each update
reweights the same frozen policy using re-estimated advantages, which can
reverse action preferences that previously led to success.
Inspired by complementary learning systems theory, we observe that
advantage-based adaptation statistically integrates past experience but lacks
a complementary hippocampus-like mechanism for recovering successful behavior.
We therefore propose HIRE (HIppocampal REplay), which uses replay to
recover successful behavior, allowing the adapted policy to build on
previously achieved progress rather than rediscover it.
We prove that HIRE satisfies a return consolidation criterion, yielding an expected-return lower bound
that is non-decreasing as the best verified return increases for a fixed
exploration rate.
Experiments on ScienceWorld and WebChoreArena show that HIRE achieves the
best overall performance among the evaluated methods. Our code is available at https://anonymous.4open.science/r/HIRE-D54E.

### 24. QK-Wanda: Coupling Queries and Keys for Unstructured Pruning

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=HXmRkbSJCb
- 官方摘要证据：Wanda (Sun et al., 2024) prunes large language models by scoring each weight by its magnitude times its input activation, treating every linear projection independently. Self-attention violates this assumption: queries and keys enter the model only through their product, so the importance of a query weight depends on the keys, and vice versa. We introduce QK-Wanda, an unstructured pruning method that scores query and key weights by how much their removal perturbs the joint query-key product rather than either projection alone. Starting from a reconstruction loss on the causally masked query-key product, we derive a closed-form importance score for deleting a single weight; the result is Wanda's magnitude-activation criterion augmented with a term from the opposite projection. Scores are computed from a small calibration set without gradients or retraining, adding only 31-37% to Wanda's calibration and scoring time. On the Llama 3 family, QK-Wanda consistently reduces query-key reconstruction error and lowers perplexity relative to Wanda in most model-sparsity settings, with the largest gains at high sparsity.

### 25. RAZOR: Pruning Replaceable Experts in LLMs

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=OLS3NKUhWz
- 官方摘要证据：Mixture-of-experts (MoE) models activate few experts per token but store the
full expert pool. Pruning aims to reduce this burden at a fixed budget while
preserving output distributions and, for reasoning models, reasoning ability.
Deletion damage depends on functional replaceability by surviving computation,
not usage or contribution magnitude alone. We introduce RAZOR,
a training-free method that scores functional replaceability using consensus
residuals, the deviations of expert outputs from the original weighted mixture. At a
fixed layer input, an exact single-deletion identity accounts for survivor
renormalization and router-selected refill. We aggregate these local scores over
calibration tokens for budgeted pruning without gradients or recovery training.
On GLM-4.7-Flash, Qwen3.6-35B-A3B, DeepSeek-V4-Flash-0731, and Hy3 at 25\% and 50\%
expert removal, RAZOR achieves the highest nine-task macro average among the
evaluated pruning methods in all eight settings. On the two backbones with
matched REAP benchmark runs, it exceeds REAP by 2.12--5.59 points and wins all 36
paired task comparisons.
It also lowers reverse KL relative to REAP in all four matched
GLM-4.7-Flash and Qwen3.6-35B-A3B model--budget settings. Responses generated by
Qwen3.6-35B-A3B nevertheless change in diversity, formatting, and termination,
showing that task retention and predictive fidelity do not ensure generation
stability.

### 26. RC-VQ: Recovering What Calibration Discards with Vector-Quantized Residual Correction

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=HXmiKD1kS0
- 官方摘要证据：Calibration data decides what training-free LLM compression keeps. In activationaware
factorization and post-training quantization alike, a small calibration set
defines an importance measure over the weights, and whatever it does not certify
is discarded as a residual. We argue that failing the calibration proxy does not
make weights unimportant, and that the discarded residual should be recovered.
The standard recovery tool, a low-rank adapter, is structurally mismatched to this
task. On LLaMA-2 7B the residuals are dense and spectrally flat. Quantization
residuals are statistically indistinguishable from a Marchenko–Pastur noise bulk,
and truncation residuals form a gapless spectral continuum without isolated spikes,
so a rank-r corrector recovers a vanishing fraction of either. Across four model
families, the energy a low-rank corrector recovers grows only linearly in its rank.
We propose RC-VQ, a full-rank vector-quantized corrector fitted to the residual
without gradients or recovery data, which composes with SVD factors, INT4
weights, and their stacked combination. On structural compression of LLaMA-2
7B, LLaMA-3 8B, and Qwen3 8B, RC-VQ reduces perplexity degradation by
3–13× against the strongest reported structured baseline at matched checkpoint
size. On the INT4-AWQ quantization gap of Qwen3.5 4B, it recovers 96% of the
distance to FP16 at three bits per parameter, a budget at which an identically sized
low-rank corrector recovers under 40% and a scalar residual branch needs 37%
more bits to match. Sweeping codebook objectives across structural, quantization,
and stacked residuals, we show that each pure objective has a failure regime, while
the hierarchical direction-then-refinement objective, PolarVQ, never collapses,
making it the robust default when residual geometry is unknown.

### 27. Scalar Smoothness Is One Point on a Besov Spectrum

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=osd72MlzL5
- 官方摘要证据：Studies of neural network generalization and robustness often summarize smoothness with a single number, such as a Lipschitz constant or a Hessian curvature statistic. However, Lipschitz constants summarize global worst-case sensitivity and Hessian statistics summarize local curvature; neither captures how model responses vary with the size, direction, and location of perturbations encountered in real-world deployment. To measure smoothness under these perturbations, we introduce a finite-difference roughness spectrum that profiles model responses across these conditions. Our roughness spectrum generalizes scalar smoothness measures, bringing Lipschitz sensitivity and directional Hessian curvature into a common framework across perturbation scales. We connect this spectrum to classical Besov theory, which describes how a function's variation changes with scale. Our theoretical analysis also proves that a larger output shift can cause less task damage than a smaller one, and that local curvature alone can miss the blocks most vulnerable to finite perturbations. In image classification, Roughness Source Control (RSC) suppresses margin roughness along noise directions and improves noise robustness in a comparison of 80 checkpoints across four model--dataset combinations. In post-training quantization, we identify blocks that need higher precision by measuring task-loss increases from perturbations matched to the size and direction of each block's quantization error. Our mixed-precision allocation achieves lower perplexity than the Hessian-based HAWQ-V2 baseline under the same GPTQ weights and bit budgets in all 14 settings across seven held-out large language models.

### 28. RESCOM: ACTIVATION RESIDUAL COMPENSATION FOR LARGE LANGUAGE MODEL QUANTIZATION

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=KzeQR3Rqgi
- 官方摘要证据：Low-bit weight–activation quantization reduces the memory and computation needed to deploy large language models, but activation rounding can still degrade accuracy after calibration. Reconstruction from rounded inputs cannot distinguish activations within the same quantization bin. We propose ResCom, a low-rank correction that uses the activation rounding residual to compensate for the resulting layer-output error. An output-aware calibration procedure selects residual directions by their contribution to output reconstruction and computes the correction in closed form, without gradient training or updates to the calibrated weights. On Llama-3-8B with four-bit weights and activations, rank-32 attention corrections reduce WikiText-2 perplexity from 7.708 to 7.147, improve MMLU by 2.89 percentage points, and raise five-shot GSM8K accuracy from 23.96 to 36.16 percent. Evaluations on models from 1B to 70B parameters and on held-out C4 test the method beyond this setting. On B200, the evaluated FP32 implementation adds 2.25 percent to 4K prefill time; a separate compact-storage implementation retains a 27.7 percent peak-memory reduction relative to FP16.

### 29. Beyond Parameter Space: Closed-Form Cross-Trajectory Repair After Harmful Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=bLQ22POBgo
- 官方摘要证据：Safety-aligned language models are routinely adapted after deployment to improve downstream task performance, yet the fine-tuning process may be vulnerable to a small fraction of harmful examples that compromise their safety alignment. Existing safety repair methods intervene through diverse mechanisms, including parameter or update modification, model merging, and additional optimization. However, harmful fine-tuning can also change the internal representations propagated through the model, so the aligned reference and attacked models may reach the same module with different representations even for the same input. Motivated by this observation, we propose CCTR (Closed-Form Cross-Trajectory Repair), a post-hoc repair method that fits the full cross-trajectory output residual on representations produced by the attacked model while constraining output drift on task-agnostic utility activations. For each target linear module, these two objectives form a regularized least-squares problem with a closed-form solution, enabling repair without gradient-based optimization or downstream-task supervision. Compared with the strongest state-of-the-art safety repair method, CCTR lowers the average Harmful Score from 2.30% to 0.38% across varying harmful-data ratios. In experiments on different downstream tasks, it lowers the score from 2.85% to 0.77% and improves average task accuracy by 3.53%.

### 30. SHIFT-LLM: Distribution Shift Correction in Depth-Pruned LLMs

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=rfbv29Wa3V
- 官方摘要证据：Depth pruning removes entire Transformer blocks to reduce the inference cost
of large language models, but disrupts the hidden-state distributions expected by
downstream layers, leading to significant accuracy loss. We introduce SHIFT-
LLM, a training-free post-pruning correction framework that inserts a Linear
Residual Adapter (LRA) at each pruning site. Each LRA preserves the identity
pathway of the original residual block and adds a lightweight affine residual
correction. This correction is calibrated via closed-form least-squares regression
on a small held-out set, without gradient computation, to approximate the missing
residual update produced by the pruned block. Together with the preserved identity
pathway, the resulting LRA output approximates the hidden state produced by the
original block, thereby mitigating the distributional mismatch introduced by layer
removal while avoiding the expensive attention and feed-forward computations
of the removed blocks. The resulting LRAs support low-rank factorization and
exact merging across consecutive pruned layers for additional compression, and
combine naturally with parameter-efficient fine-tuning for further recovery beyond
fine-tuning the pruned model alone. Experiments on five model families, six
layer-selection criteria, and seven zero-shot benchmarks show that SHIFT-LLM
consistently recovers accuracy lost to depth pruning across most configurations,
achieving gains up to +15.7 points on Llama-3.1-8B-Instruct while requiring only
a few hundred calibration samples and no gradient computation.

### 31. Layer-Specialized Model Merging for Training-Free Cross-Modal Reasoning Transfer

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=AYwu267x63
- 官方摘要证据：Text-only reasoning LLMs are strong multi-step problem solvers, but transferring this behavior to multimodal LLMs (MLLMs) usually requires costly multimodal post-training and scarce verifiable reasoning supervision. We study a training-free alternative: fusing a text-only reasoning decoder with a homologous MLLM decoder while keeping the MLLM visual encoder and projector unchanged. This setting is more delicate than standard model merging because the fused decoder must integrate reasoning behavior from a text-only model while continuing to interpret visual inputs. We introduce \method{} (\textbf{A}ttention-calibrated \textbf{N}orm-\textbf{O}rthogonal merging), a layer-specialized fusion method for cross-modal reasoning transfer. \method{} represents the two decoders as task vectors relative to a shared base model and computes closed-form, label-free fusion weights from task-vector salience. To account for depth-dependent visual-token use, it calibrates these weights with the MLLM's layer-wise visual-attention decay, using a continuous prior that favors the vision branch in shallow layers and the reasoning branch in deeper layers. Across homologous MLLM--reasoner pairs, \method{} improves reasoning-heavy multimodal benchmarks without gradient updates or labeled multimodal reasoning data. We also evaluate the boundary of this transfer: MME-RW perception results and MathVista performance reveal task-dependent tradeoffs between reasoning gains and visual capabilities. Together, the results suggest that layer-specialized merging is a practical route for training-free cross-modal reasoning transfer within the studied homologous model families.

### 32. Diagnosing Failure Regimes in LLM Agent Memory with Extraction-Pass Disagreement

- 决定：`defer_agent_no_model_training`
- 原分类：`related_inference`
- 论文特定依据：RRC 是 LLM agent memory 的 training-free 配置层，通过多次记忆整合分歧路由投票预算、检索深度和回答策略。
- 模型参数/组件边界：固定 backbone；更新的是结构化记忆、投票/检索配置和回答策略配置，摘要明确 without gradient updates。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=vpahOt8lBU
- 官方摘要证据：LLM agents build long-term memory by consolidating interaction history into a structured store, and this consolidation is lossy in two ways. In the first, a stochastic pass drops information that another pass may keep, and computation removes the error. In the second, a capability-limited backbone compresses history into a low-rank sketch, and the bias it introduces is beyond the reach of computation. The two failures look the same in aggregate accuracy, so existing systems apply the same remedy to both. We propose Regime-Routed Construction (RRC), a training-free configuration layer whose routing follows the diagnosed failure regime. RRC repeats consolidation on the same history and reads how much the passes disagree. The disagreement estimator, combined with backbone capability, routes the vote budget, the retrieval depth, and the answer policy. A noisy reading brings more extraction passes merged by majority vote. A quiet reading deepens retrieval and calibrates the answer policy when the backbone sits above its capability threshold, and declines what the store cannot support below it. A Fano-type argument shows that below a capability threshold, error on relational questions is irreducible. Across two benchmarks and backbones from 1.5B to frontier API models, RRC improves on the strongest published LoCoMo result by +4.7 F1 and outperforms the RL-trained Memory-R1 at matched backbones without gradient updates. On LongMemEval, the gains are small and insignificant, consistent with a diagnosis of little headroom.

### 33. Do Shared VLM Coordinates Imply Shared Calibration? A Study through Few-Shot Class-Incremental Learning

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=9gVp0VCEPN
- 官方摘要证据：Pretrained vision-language models place visual and textual class references in shared coordinates, but alignment does not determine their compatibility with downstream geometric calibration. We expose this distinction through training-free few-shot class-incremental learning, where support-derived visual estimates and pretrained textual anchors are evaluated against the same image queries. Crossing visual- and text-derived diagonal calibration transforms with the two isolated scorers reveals a reproducible role-dependent calibration asymmetry. Across three encoders and four benchmarks, visual-derived calibration is more favorable to visual than textual scoring in all 12 settings. Textual accuracy decreases in every setting, even when the calibration uses textual statistics from base classes or all currently known classes. Our geometric analysis and source-matched counterexample explain the key distinction: calibration replaces native cosine with an affine Mahalanobis-like cosine, and matching reference marginals does not ensure preservation of image-to-reference class ordering. These results motivate source-preserving scoring: calibrate the empirical visual estimate, preserve the pretrained textual anchor, and compose their class evidence. We instantiate this principle as Dual-Space Product-of-Experts (DS-PoE), combining a base-calibrated visual expert and a native textual expert through fixed logit addition, without gradient updates, replay, or dataset-specific modality weights. Across four benchmarks, DS-PoE achieves state-of-the-art performance, attaining the best mean session accuracy on every benchmark and a four-benchmark mean of 78.6% under the evaluated training-free protocol. Our code is included in the supplementary material.

### 34. CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention

- 决定：`keep_unaffected`
- 原分类：`related_inference`
- 论文特定依据：非提示词核心且非智能体范围：该论文处理推理校准、激活编辑、VLM统计适配或推理系统机制。
- 模型参数/组件边界：按原摘要更新激活、统计量、缓存/注意力配置或其他推理对象；本次范围规则不自动排除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=UpR5uTu7JV
- 官方摘要证据：As context becomes grows, LLM inference becomes increasingly expensive because attention repeatedly reads a growing key-value (KV) history.
We introduce Chunk-Indexed Sparse Attention (CISA), a method for retrofitting pretrained dense attention models without gradient updates.
CISA selects fixed-size chunks of the KV history using compact summaries derived from the model's existing keys, avoiding token-level indexing and a separate full-length index cache.
For indexing, CISA uses a single query per KV group and shares the selected chunks across the query in that group.
During prefill, we reuse chunk selections across adjacent queries to reduce indexing cost and improve KV reuse and GPU utilization.
We call this technique *QShare*.

We evaluate CISA on the NVIDIA Nemotron~3 Nano and Ultra models, as well as on Inkling-Small.
In one-layer BF16 benchmarks at batch size 32 using Ultra's per-device attention dimensions, CISA accelerates core attention by $11.7\times$ for prefill queries near the end of a 1M-token prompt and $13.0\times$ during decode.
Including chunk scoring, selection, and all other measured GPU work, the corresponding speedups are $8.6\times$ and $3.0\times$.
On Ultra NVFP4, at $k_{\mathrm{chunks}}=4{,}096$, CISA keeps aggregate scores within 1.5 percentage points of dense attention on MRCR, LongBench v2, and GraphWalks.
RULER sweeps on Nano and Ultra BF16 up to one million tokens show scores within 2.05 percentage points of dense attention with 8--16$\times$ fewer KV reads.

When serving million-token prompts with 32 concurrent requests and 4K output tokens per request, CISA achieves $2.29\times$ the end-to-end throughput of dense attention using Nemotron~3 Ultra NVFP4 on four NVIDIA B300 GPUs.
Selecting fewer chunks increases throughput to $2.61\times$ compared with dense attention; in separate GraphWalks evaluations, the smaller budget widens the aggregate score gap from 1.49 to 3.59 percentage points. These results expose a practical quality--speed tradeoff without requiring sparse training.

### 35. scCoLLM: An LLM-Based Model Using Context-Space Adaptation for Single-Cell Analysis under Domain Shift

- 决定：`defer_prompt_core`
- 原分类：`related_inference`
- 论文特定依据：scCoLLM 把适配从参数空间转为 context space，检索并组装 Bio-Context 供固定 GPT 条件生成，核心属于上下文/提示构造。
- 模型参数/组件边界：无模型参数访问或梯度更新；更新对象为检索得到的 Bio-Context。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=ICtYd1vctM
- 官方摘要证据：Deep learning has been adopted throughout single-cell analysis with remarkable success. However, once the target data to be analyzed depart from the distribution a single-cell model was trained on, current single-cell models exhibit marked performance degradation. Such domain shift is the rule rather than the exception in practice: newly profiled data routinely come from unfamiliar cell types, tissues, and donors. We attribute much of this degradation to a missing conditioning signal: existing methods predict each query cell from its own expression profile alone, ignoring the target-domain-specific biological context carried by the target dataset itself. Closing this gap by training or fine-tuning on the target domain is often infeasible, since every such remedy requires an additional training run for each new target, its supervised variants further require ground truth annotations that a newly profiled dataset does not carry, and the strongest models may not release their weights. We therefore recast target-domain adaptation from parameter space to context space. We introduce **s**ingle-**c**ell **Co**ntext **LLM** (**scCoLLM**), a training-free framework that performs **Context-Space Adaptation** on top of general-purpose LLMs such as GPT. Given a query cell, scCoLLM retrieves a query-conditioned biological context set from the unlabeled target data, selected to balance query-level local relevance against target-domain global representativeness, yielding a set of cell--profile pairs through zero-shot reasoning. The resulting cell–profile pairs form the **Bio-Context**. Conditioned on this Bio-Context, scCoLLM analyzes the query cell while aware of the biological context of the target domain, and thereby adapts to that domain without gradient updates, ground-truth labels, or access to model parameters. Under three domain shift tasks---cross-cell type, cross-tissue, and cross-donor---scCoLLM attains state-of-the-art performance, improving on the strongest of 12 baselines by up to 9\%. Further experiments confirmed the soundness of the Bio-Context design and its decisive role in improvement, as well as the robustness and transferability of scCoLLM.

### 36. Suppressing a Rejected Action Costs a KL: Closed-Form Test-Time Updates for LLM Agents

- 决定：`defer_agent_training_unverified`
- 原分类：`related_closed_form`
- 论文特定依据：TALE 面向 LLM agent 的失败动作恢复，并对输出侧表示施加低秩编辑；但摘要没有说明该表示是否是可训练模型参数、适配器参数或仅为会话内状态，不能据 model editing 推断参数训练。
- 模型参数/组件边界：无需反向传播；编辑影响后续尝试，但是否写入模型/适配器参数以及是否跨会话持久化均待原文核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=e4pspmOVIV
- 官方摘要证据：Large language models are widely deployed as agents that interact with external environments through structured actions such as shell commands, tool calls, or search queries. Once the model emits an action that the environment cannot execute, the interaction step is interrupted. In-place recovery then faces a dilemma: with frozen weights, stateless resampling tends to fall back into similar invalid outputs and repeat the same failure; with weight updates after every rejection, gradient-based adaptation introduces substantial latency and compute cost. We propose TALE (Test-time Adaptation via Likelihood Enforcement). TALE turns an observed rejection into an exact likelihood-suppression target and applies a low-rank representation edit at the model's output side; the update direction is determined analytically and the suppression intensity is fixed by a one-dimensional monotone root-finding procedure, with no backpropagation. The edit reshapes the local probability space and moves subsequent attempts away from the failed neighborhood. Across four benchmarks covering terminal commands, tool calls, and web search, at three model scales, TALE reduces the unresolved rate of interaction steps relative to update-free resampling and saves a large fraction of model calls; relative to gradient-based test-time adaptation methods, it attains comparable or higher task success while cutting end-to-end latency by a factor of several, with negligible additional GPU memory.

### 37. GS-MoE: Training-Free MoE Compression via Groupwise Subspace Sharing and Pruning

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=mDDEcTyT5B
- 官方摘要证据：Mixture-of-Experts (MoE) models reduce computation through sparse activation, but storing their expert parameters remains a major memory bottleneck. We introduce GS-MoE, a training-free compression framework that addresses redundancy across and within experts through two compression axes: shared-subspace rank and expert intermediate width. Groupwise low-rank representations capture shared structure across experts while retaining expert-specific projections, and Nystr\"om-based neuron compression reduces intermediate width within each expert. For fixed shared subspaces, we derive per-expert retained-energy gains from the reconstruction objective and use these gains to guide expert grouping. A gradient-free layer-importance score guides the allocation of rank and width budgets across layers, with non-uniform ranks across groups and intermediate widths across experts. Experiments show that compression along both axes achieves higher accuracy than compression along either axis alone. On DeepSeek-MoE-16B-Base, at a 60\% reduction in routed-expert parameters, GS-MoE retains over 92\% of the uncompressed model's average reasoning performance, compared with 73\% for D$^2$-MoE, while achieving 30\% lower out-of-domain perplexity.

### 38. Does Scaling Reinforcement Learning Really Require More Training?

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=a04cCyok2x
- 官方摘要证据：Scaling reasoning typically spends more compute on reinforcement learning (RL) or on inference. We show that a completed RL training history can yield policies stronger than the checkpoints visited by its optimizer. We call this *policy-space scaling*: expanding the deployable policy set accessible from a fixed RL history, without extending training or increasing per-query inference computation. We instantiate it with SURGE (Scaling Up RL Gradient-free via Eigenspace fusion). SURGE combines two checkpoints from the same RL run: a high-accuracy anchor and a competitive donor that generates shorter responses. It expresses both checkpoints as changes from their shared initialization, then spectrally decomposes the anchor's update to retain its dominant component and incorporate the donor's complementary component. With a fixed target for how much of the anchor update to retain, SURGE determines the block size from the weights without testing candidate policies. We evaluate two 1.5B mathematical-reasoning histories, DeepSeek and Nemotron, and one 7B coding history, OLMo. SURGE improves benchmark-average accuracy over both input checkpoints while using fewer reasoning tokens than the anchor. It reaches 54.17\% on DeepSeek AIME24 against a measured native maximum of 50.83\%, and 83.7\% on OLMo HumanEval+ against 82.8\%. These gains exceed the observed training curves. Geometric controls support the importance of RL-update structure beyond weight displacement or token reduction alone. Each constructed model runs as a single policy. Our findings identify stored RL history as a reusable scaling resource: the capability available from a training run need not end at its best checkpoint.

### 39. Learning While Generating in a Single Forward Pass

- 决定：`keep_unaffected`
- 原分类：`related_forward_gradient`
- 论文特定依据：非提示词核心、非智能体范围：该论文以 forward-gradient 方向导数更新语言模型参数。
- 模型参数/组件边界：OFTA 将生成时记录的参数方向导数转成模型参数更新；无需反向传播。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=G8GNLtlyAV
- 官方摘要证据：Deployed LLMs constantly receive feedback from users, verifiers, and task outcomes. Test-time adaptation uses this feedback so that each interaction improves the next one. Today, this learning needs a second pass after feedback arrives, which either reruns the model over the response or keeps all of its activations until then. We observe that the model computation in this second pass does not depend on the feedback, so it can be done in the forward pass that generates the response. Based on this observation, we propose **One-Pass Forward-Trace Adaptation (OFTA)**, which learns while generating in a single forward pass. As the model generates each token, OFTA also records how the log-probability of the response changes along a random parameter direction. This design brings three benefits. First, it removes the second pass. When feedback arrives, OFTA turns the record into an update with a few simple operations, without running the adapting model again, using backpropagation, or keeping activations. Second, the record works for immediate and delayed feedback, and one record supports many feedback losses. Third, moving the computation into generation costs nothing in update quality. Theoretically, OFTA gives the same directional derivative as a separate pass after feedback, so it keeps the unbiased estimate of forward-gradient methods. Experiments on Qwen3 series models show that, in the tested settings and counting all extra work, OFTA lowers request time, applies updates almost as soon as feedback arrives, uses much less memory than backpropagation, and learns as well as a separate pass. In simpler terms, OFTA lets a model learn from a response in the same pass that writes it.

### 40. When Are Nearby Experts Composable? Cross-Task Model Merging in Neural Thickets

- 决定：`keep_unaffected`
- 原分类：`related_closed_form`
- 论文特定依据：非提示词核心、非智能体范围：该论文处理模型量化、压缩、合并或解析模型适配。
- 模型参数/组件边界：按原记录更新持久模型表示/结构或统计校准对象；不因本次提示词/智能体收紧而移除。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=lXiUD5V7wG
- 官方摘要证据：Random perturbations around a shared checkpoint can produce experts for distinct tasks, but shared origin does not ensure that their gains survive composition. We formulate expert-pair selection for joint base-relative retention, measured by strict joint success and worst-task gain with unconditional abstention accounting. An exact finite-difference decomposition and an arbitrarily small orthogonal counterexample show why proximity and orthogonality alone are insufficient. We instantiate this formulation with quality-constrained spectral selection, a fixed-budget framework combining cross-task screening, layerwise pair geometry, separate validation, and Base fallback. Across six checkpoints, 21 task pairs, and five independent perturbation pools, the procedure improves strict joint success over Top-1 averaging throughout and leads the four-method model-scale comparison on four of six checkpoints. For the five models with at least 1.5B parameters, matched quality-only, global-cosine, and spectral ranking attain 49.1%, 50.5%, and 53.1% joint success. Under this matched protocol, the spectral selector also yields the highest worst-task gain and Weak Pareto rate and the lowest regression rate. Mean worst-task gain reaches +0.61 percentage points, while 17.1% regression and 13.0% abstention show that composability remains conditional. Project page: https://anonymous.4open.science/r/Thickets-Merge/.
