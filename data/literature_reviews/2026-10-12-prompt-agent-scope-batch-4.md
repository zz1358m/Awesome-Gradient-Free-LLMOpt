# 2026-10-12 提示词与智能体范围审查：批次 4（语义修正版）

本批次逐篇审查 73 条。语义修正版按真实机制判定，不以是否自称 agent/harness、原类别名或关键词规避范围。

## 统计

- `defer_agent_no_model_training`：2 条
- `defer_agent_training_unverified`：2 条
- `defer_prompt_core`：9 条
- `keep_agent_model_training`：19 条
- `keep_unaffected`：41 条

## 逐篇决定

### 1. Hyper-ES: Effective Evolution Strategies for LLM Reasoning via Descent Direction Merging

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：混合方法：先通过梯度训练获得下降方向，再以 CMA-ES 优化 DARE-TIES 逐层合并系数；第一阶段仍使用反向传播。
- 模型参数/组件边界：模型/优化器更新边界沿用现有论文记录；本次范围调整不改变其技术分类。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://arxiv.org/abs/2608.05541
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 2. Continual Test-Time Learning with Evolution Strategies

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：用局部参数扰动策略群体生成轨迹，并以无标签组相对信号持续更新中央学生。
- 模型参数/组件边界：扰动策略与 central student 都涉及模型状态；central student 更新的反传实现待正文核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=LOwG4xUpfa
- 官方摘要证据：Large language models increasingly operate in open-ended environments, where they are expected to continually adapt to evolving tasks and distributions, often without access to external supervision. However, existing continual learning approaches often rely on external supervision, such as labeled data, demonstrations, or reward signals, which can be costly and unavailable in practice. In contrast, repeated test-time adaptation using self-generated supervision can lead to policy collapse, degraded reasoning, and catastrophic forgetting. In this paper, we propose **Evolution Strategy Reinforcement Learning (ESRL)**, a continual test-time learning framework designed to mitigate catastrophic forgetting during label-free continual adaptation. Specifically, ESRL constructs a population of locally perturbed policies around the current model to explore multiple neighboring parameter regions throughout adaptation, and then samples trajectories from those regions. Unlike trajectory-space exploration from a single evolving policy, this parameter-space population maintains diverse sources of self-generated supervision even when the central policy begins to drift. The resulting trajectories are aggregated into label-free group-relative learning signals to update the central student. Through extensive experiments on single-task test-time adaptation and multi-task continual learning across mathematical reasoning, general knowledge, and medical domains, ESRL achieves relative gains of up to 31.7% over the base model and 16.6% over the second-best method. Notably, ESRL substantially reduces catastrophic forgetting and maintains the strongest final performance at the end of continual learning.

### 3. Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：混合贡献：除 ES 分析外，论文还提出两种顺序的 sequential ES–GRPO training。
- 模型参数/组件边界：ES 与 GRPO 分支均持久更新模型参数；各阶段衔接细节待正文核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=OF8CUj7TD8
- 官方摘要证据：Evolution Strategies (ES) have recently emerged as a memory-efficient post-training paradigm for LLM reasoning. However, the optimization behavior of ES remains understudied, making it hard to define its advantage scope compared to mainstream post-training paradigms (e.g., Group Relative Policy Optimization (GRPO)). This paper systematically investigates the behavior and design of ES post-training. $\textbf{First,}$ we $\textbf{identify a performance advantage of ES over GRPO}$: broader reasoning coverage that better exploits the reasoning capabilities of pretrained LLMs. Empirically, ES generally improves Pass@1 over the base model and achieves higher Pass@$K$ than GRPO, which can exhibit entropy collapse. Theoretically, we derive sufficient conditions under which an ES update improves the center policy's Pass@$K$. We further propose a sequential ES–GRPO training method in both orders, which can combine GRPO's Pass@1 strength with ES's Pass@$K$ gains. $\textbf{Second,}$ we find that despite substantial parameter drift, removing most small coordinate updates of ES largely preserves target-task Pass@1 performance. Held-out evaluations further show that this large drift need not imply broad forgetting. $\textbf{Finally,}$ we study how ES design choices affect its effectiveness, finding that comparable training rewards can be maintained with smaller ES populations in larger LLMs. These findings position ES as a distinct post-training paradigm for LLM reasoning rather than a less effective, memory-efficient alternative to GRPO. Our code is available at https://anonymous.4open.science/r/understanding-es-3D73.

### 4. Accelerating LLM Pretraining with Zeroth-Order Curvature on Idle Serving Compute

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：在空闲纯前向设备上以零阶查询估计曲率，用其精炼主训练端的一阶全参数更新。
- 模型参数/组件边界：预训练模型参数由一阶训练持久更新；ZO 设备只提供曲率信息。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=qh1N46HjOP
- 官方摘要证据：LLM pretraining is increasingly compute-intensive, while substantial inference serving compute remains idle during off-peak periods.
However, such serving hardware is difficult to use for conventional first-order training due to its memory, networking and other system requirements.
Zeroth-order (ZO) optimization offers a natural interface to this forward-only compute resource, but its gradient estimates break down in pretraining.
Unlike fine-tuning, which can confine updates to a small parameter subspace, pretraining must update every parameter, and the alignment of a ZO gradient estimate with the true gradient shrinks as the number of updated parameters grows.
We make a different observation: noisy ZO estimates can still provide useful curvature information, even when they are too inaccurate to serve as gradients.
Based on this insight, we propose ZO-Curv, which leverages idle forward-only devices to estimate curvature and uses it to adapt and refine the update used during first-order training, thereby accelerating the process.
We provide convergence guarantees that characterize the effect of finite-query curvature estimation.
Experiments on LLMs from 125M to 1.5B parameters show that ZO-Curv consistently accelerates pretraining.
At 770M parameters, ZO-Curv reaches AdamW's 20K-step validation loss in 3.9 hours instead of 7.5 hours, while achieving a lower final loss of 2.70 versus 2.84 under the same step budget.
These results show that idle model serving compute can accelerate LLM pretraining when zeroth-order queries are used to estimate curvature rather than gradients directly.

### 5. Zero-Order Optimization via Learnable Direction Sampling for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：混合方向学习：finite-difference ZO 更新 LLM，REINFORCE 同时适配 Gaussian perturbation distribution。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件/优化器状态：摘要未明说者待核实
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=CZqew9w981
- 官方摘要证据：Zeroth-order (ZO) optimization estimates gradients through function evaluations along sampled perturbation directions. Standard isotropic sampling yields weak expected gradient alignment, limiting estimator quality and introducing dimension-dependent convergence rates. We propose a plug-and-play framework that learns the perturbation distribution to improve directional alignment. Our design follows from a descent bound that identifies expected gradient alignment as the objective for adapting the mean of a Gaussian sampling distribution. For an idealized directional algorithm with exact policy updates, we characterize the evolution of alignment and derive convergence guarantees with no explicit dimension dependence. Building on this formulation, we develop a practical finite-difference algorithm that updates the sampling policy using REINFORCE estimates and integrates with existing ZO optimizers. The resulting framework is particularly relevant to large language model (LLM) fine-tuning, where avoiding backpropagation reduces training memory requirements. Experiments demonstrate consistent improvements across models, ZO optimizers, and fine-tuning schemes under matched forward-evaluation budgets, supporting learned direction sampling as an effective mechanism for improving ZO fine-tuning. Our code is available at [https://anonymous.4open.science/r/zo\_ldsd](https://anonymous.4open.science/r/zo_ldsd).

### 6. Geometric-Steering Muon for Online Large Language Model Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：GS-Muon 在 Newton–Schulz 变换间加入几何 steering，使动量方向适应在线目标的一阶或零阶信号。
- 模型参数/组件边界：模型参数由 GS-Muon 持久更新；信号可来自一阶或零阶，具体实验配置待正文核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=APkYU4FkeR
- 官方摘要证据：Fine-tuning is a fundamental approach for adapting pretrained large language models (LLMs) to downstream tasks and evolving application requirements.
Although Muon has recently attracted increasing attention as a matrix-structured optimizer for LLM training and fine-tuning, existing studies have largely focused on conventional offline settings, leaving its behavior under online adaptation comparatively underexplored.
In online LLM fine-tuning, evolving objectives can render accumulated momentum increasingly inconsistent with the current optimization signal, yet Muon's Newton--Schulz (NS) transformation primarily reshapes the spectral structure inherited from momentum without explicitly adapting its update orientation to the current objective.
We therefore propose Geometric-Steering Muon (GS-Muon), which introduces Geometric-Steering Newton--Schulz (GS-NS) to explicitly couple Muon's spectral transformation with the current optimization signal.
GS-NS decouples orientation adaptation from spectral orthogonalization: a short NS prefix establishes a near-orthogonal geometry, a tangent-inspired steering step redirects the momentum-inherited orientation toward the current optimization signal, and a final NS correction restores the orthogonalization structure.
Theoretically, we establish geometric stability properties of GS-NS and derive variation-dependent nonconvex regret guarantees for GS-Muon under both first-order and zeroth-order signal access, explicitly characterizing the effects of momentum tracking and zeroth-order signal estimation.
Finally, we establish a unified streaming evaluation protocol across two model scales and eleven NLP datasets, covering single-dataset streams, sequential within-family task shifts, and heterogeneous cross-task streams.

### 7. FoRA: Forward-Only Residual Adaptation for Federated Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：FoRA 从冻结前向 LLM 骨干分离表征，并以一阶联邦优化训练轻量因子化 residual。
- 模型参数/组件边界：LLM backbone 权重：frozen；外接 factorized residual 参数：一阶持久更新。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=ACuCPfyRs1
- 官方摘要证据：Federated fine-tuning of large language models (LLMs) faces a tension between avoiding client-side backpropagation through the LLM backbone and retaining first-order optimization for effective adaptation. Existing methods either keep trainable modules inside the backbone, preserving first-order gradients at the cost of backbone backpropagation, or adopt zeroth-order optimization for forward-only execution at the cost of gradient-estimation error. We propose FoRA, a federated fine-tuning framework that keeps the LLM backbone forward-only while preserving first-order optimization for the trainable adaptation. FoRA detaches compact multi-level representations from a frozen backbone, learns a lightweight factorized residual with a direct Split branch and a globally weighted Bridge branch, and regularizes local training against a fixed global reference in function space. Our analysis verifies the execution-graph memory separation, characterizes the local Jacobian geometry of the auxiliary parameterization, characterizes the local dynamics induced by global-reference regularization under a fixed-tangent model, and establishes non-convex convergence for the federated protocol. Empirically, FoRA reduces peak allocated client GPU memory by 27.3\%-59.2\% over first-order baselines while achieving comparable quality, and outperforms FedMeZO by 6.99-18.37 points in Final-10 Accuracy on classification and 4.74 points in Final-10 ROUGE-L on generation, with 65.8\%-74.7\% less training time.

### 8. Evaluate Before You Commit: Label-Free Candidate-Update Utility for Test-Time Adaptation

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：以仅前向的 probe-view utility 评估暂定适配更新，再事务式提交或回滚。
- 模型参数/组件边界：基础适配器可能持久更新模型；controller 决定提交或回滚，具体生成器与模型参数边界待核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=JEeD6leWDn
- 官方摘要证据：Test-time adaptation (TTA) can improve performance under distribution shift, yet deciding where to adapt does not determine whether the resulting parameter update is worth retaining. We formulate candidate-update utility: after a base adaptation operator produces a tentative state, should that realized update enter persistent model state? We introduce a label-free evaluate-before-commit controller that allocates candidate-generation compute using forward-only screening, evaluates each tentative update on independently sampled probe views using held-out predictive consistency and drift from a frozen pretrained reference, and transactionally rolls back low-utility candidates. Across CLIP and DINOv2 under synthetic corruption, natural domain shift, and a cross-hospital stress test, the proposed utility estimator improves harmful-update AUROC from 0.589 to 0.750 and AUPRC from 0.305 to 0.492 relative to predictive entropy. At the principal operating point, Utility-Aware control reduces the harmful committed-update rate (HCUR) from 27.0% to 11.0% while increasing the accuracy gain from +2.20 to +2.40 percentage points, halving candidate-update backward passes, and reducing adaptation-specific wall-clock time by 28±3%. Post-proposal verification also complements strong pre-update selection: adding Utility-Aware verification after Cross-Augmentation Similarity (CAS) reduces HCUR from 15.2% to 8.2%, while the proposed score achieves next-window harmful-update AUROC of 0.738 versus 0.641 for CAS. These results support pre-update selection and post-proposal candidate commitment as distinct and complementary control levels for TTA.

### 9. DRAM: Memory-Efficient Muon via Rank Reallocation in Principal-Random Subspaces

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：DRAM 在一阶 Muon 中组合随机梯度的主奇异方向与正交随机方向，并随训练阶段重分配两者的 rank budget，同时保留 momentum。
- 模型参数/组件边界：持久模型权重与 Muon momentum/optimizer state 均随一阶训练更新；子空间 rank schedule 是优化器配置。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=RbXMY0agox
- 官方摘要证据：Memory-efficient Muon methods aim to reduce storage overhead while preserving strong performance, yet existing approaches compromise either convergence guarantees or practical efficiency. In this paper, we focus on subspace optimization for Muon, where the choice of subspace determines the gradient information retained for updating. To preserve dominant information while providing the coverage needed for stochastic convergence guarantees, we construct a principal-random subspace that combines leading singular directions of the stochastic gradient with random directions sampled from their orthogonal complement. Under a fixed rank budget, there is a trade-off between principal exploitation and complementary coverage, making rank allocation important for practical optimization.
Our key observation is that the preferred balance shifts from principal-heavy early in training to random-heavy later. Motivated by this shift, we propose DRAM, a memory-efficient Muon optimizer that reallocates principal and random ranks across stages while maintaining momentum and performing matrix-sign normalization entirely in the subspace. Theoretically, we establish convergence guarantees for general rank-allocation schedules with nondecreasing coverage factors, obtaining rates of $O(T^{-1/4})$ in the stochastic setting and $O(T^{-1/2})$ in the deterministic setting, with fixed allocation as a special case. Using a simple linear reallocation schedule, DRAM achieves the best low-memory performance across three pre-training scales and nine fine-tuning settings.

### 10. Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：混合 ZFO 使用反向传播得到的一阶方向及两次额外函数评估，选择曲率感知步长；训练仍需任务梯度，作为关联研究收录。
- 模型参数/组件边界：模型/优化器更新边界沿用现有论文记录；本次范围调整不改变其技术分类。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://arxiv.org/abs/2610.02190
- 官方摘要证据：原始 review 记录未嵌入摘要。

### 11. When Safety Fails Collectively: Robust Alignment Against Harmful Fine-Tuning via Joint Weight Perturbations

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：JWP 从当前模型估计 harmful weight perturbation，组合遮蔽其不同部分构造训练状态，再做监督安全训练以抵抗扰动累积。
- 模型参数/组件边界：模型安全对齐权重：持久训练更新；masked harmful perturbation combinations：训练时状态。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=CRHLdRAVgK
- 官方摘要证据：Harmful fine-tuning can rapidly erode the safety alignment of large language models, creating substantial risks when aligned models are adapted to downstream tasks. Existing alignment-stage defenses use harmful examples and simulated harmful perturbations during safety alignment to prepare models for later harmful fine-tuning, yet the collective effects of harmful weight perturbations remain underexplored. We identify a collective failure pattern: disjoint parts of a harmful perturbation have limited effects in isolation, but their joint application increases the model's harmfulness beyond the sum of their individual effects. Guided by this observation, we propose Joint Weight Perturbations (JWP), an alignment-stage defense that masks different parts of a harmful perturbation estimated from the current model and trains the model to respond safely in the resulting states. This exposes the model to different combinations of harmful perturbations and reduces its sensitivity to their accumulation during subsequent harmful fine-tuning. Experiments across downstream tasks and model families show that JWP offers stronger resistance to harmful fine-tuning than prior defenses while largely preserving task performance. Our code is available at \url{https://anonymous.4open.science/r/JWP-D977}.

### 12. Turning Abliteration into Model Self-Destruction in Open-Weight LLMs

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：该防御在 refusal direction 的随机子空间中模拟 abliteration，并监督模型在强移除时崩溃、在部分移除时保持拒绝。
- 模型参数/组件边界：对齐后模型权重持久更新；refusal-direction random subspaces 是训练时攻击样本构造。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=ErcCQSs93S
- 官方摘要证据：Open-weight LLMs can be easily un-censored through abliteration, which is a method that works by removing the refusal direction from the residual stream. In this paper, we contribute an abliteration defense that makes the attack backfire. We ensure removing the refusal direction leads to either model collapse or persistent refusal, while leaving the clean model intact. During alignment we supervise the model on simulated abliteration in random subspaces of the refusal direction, training the model to emit a collapse token with strong abliteration and maintain refusal under gentle partial abliteration. On Llama-3.1-8B, abliteration attack-success (HarmBench) falls from 0.72 to 0.00, and we show the effect generalizes across multiple model families and to out-of-distribution and capability-preserving adaptive abliteration. We also provide a discussion of the field, as well as future work that can build off of our method.

### 13. Train Small, Guide Large: Optimization Scouting for Efficient LLM Post-Training

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：OptScout 通过小模型强化学习与梯度探测得到方向，再用纯前向奖励选择一次性的大模型持久更新；因方向阶段含梯度而归入混合方法。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件/优化器状态：摘要未明说者待核实
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=7hs0vjh7L4
- 官方摘要证据：Reinforcement learning with verifiable rewards (RLVR) can substantially improve LLM reasoning, but its computational cost increases rapidly with model scale. This work investigates whether low-cost RL on a smaller source model can replace full RL training for a larger target model. We find that transferable optimization signals already emerge at relatively early stages of source-model RL and can be used to derive effective parameter updates without costly iterative optimization on the target model.
Building on these findings, we propose Optimization Scouting (OptScout), a framework for reusing RL-induced optimization signals across model scales. OptScout extracts evolving policy shifts during source-model RL and translates them into stable, target-specific update directions through low-rank gradient probing and cross-split consistency filtering. It then uses forward-only reward evaluation to select the best update direction and magnitude, and stops scouting once further source-model RL no longer improves transfer performance. Finally, the selected update is applied to the target model only once.
Experiments across different source-side RL algorithms and target-model settings show that OptScout achieves higher average performance than direct target-side RL on multiple reasoning benchmarks, while providing up to a \(6.32\times\) end-to-end speedup.

### 14. SynKer: Synthesize, Kernelize, Reinforce - Teaching GPU Kernel Generation to Small Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：进化生成操作任务并搜索可执行 kernel，再用验证后的 kernel 档案进行 SFT 和 RL 后训练。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件/优化器状态：摘要未明说者待核实
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=nZQqqpYQ0Y
- 官方摘要证据：Combining test-time scaling with verifier execution feedback has demonstrated glimpses of frontier language models (LMs) being able to generate GPU kernels. However, small LMs still lack the capability to robustly produce compilable backend-specific code.
We argue that this is largely due to a lack of diverse training environments and validated kernel datasets, representative of the target domain.
To this end, we introduce SynKer, a general recipe for improving LM kernel generation capabilities via synthetic task and solution generation: By evolving and translating natural-language task descriptions, we generate a large-scale set of diverse target operations.
We then leverage evolutionary test-time search to generate an end-to-end validated kernel dataset across target backends.
Finally, we use the resulting dataset to post-train open-source LMs of different families and scales using supervised fine-tuning and reinforcement learning.
The resulting set of task environments contains 2365 validated and configurable synthetic tasks and a kernel archive consisting of approximately 100k kernels across three backends.
We demonstrate that the synthetic data enables effective post-training across a range of LMs.
We further find that, under supervised fine-tuning (SFT), increased task diversity improves both validation performance and generalization to the held-out task, while the resulting SFT checkpoints provide better initializations for the subsequent reinforcement learning process.
Together, these results indicate that SynKer offers a practical and effective pipeline to improve the LMs kernel generation capabilities.

### 15. Structured Algebraic Adapters for Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：在固定分块带符号排列算子族上学习适配系数，以冻结骨干进行残差状态或权重空间适配。
- 模型参数/组件边界：任务 LLM/骨干权重：据摘要 frozen；持久外部工件/优化器状态：摘要未明说者待核实
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=j51J8bLIFh
- 官方摘要证据：Parameter-efficient fine-tuning restricts the trainable update space of a pretrained model, commonly through low-rank factorization. We study Structured Algebraic Adapters (SAA), which instead learn coefficients over a fixed family of blockwise signed-permutation operators. This parameterization supports residual-state and weight-space adaptation without imposing an explicit low-rank bottleneck, while keeping the pretrained backbone frozen. We evaluate SAA against LoRA at approximately matched trainable-parameter budgets on mathematical supervised fine-tuning, data-to-text generation, and reinforcement learning with verifiable rewards.

On Ministral-3B with canonical-boxed training targets, weight-space SAA reaches 76.6\% GSM8K accuracy under a MetaMathQA-aligned evaluation prompt, compared with 74.2\% for projection-level LoRA. However, improvements in answer formatting do not imply uniform gains in mathematical correctness, and neither method improves MATH performance over the frozen backbone in this setting. On GPT-2 Medium, selected SAA and LoRA configurations achieve comparable E2E generation scores. In our Qwen3-0.6B RL experiments, SAA obtains higher answer accuracy than LoRA and the frozen backbone on all four evaluations. These single-seed results motivate structured operator parameterizations as an alternative to low-rank adaptation, while revealing task- and placement-dependent trade-offs.

### 16. Reshaping Guidance Objective with Large Language Models

- 决定：`defer_agent_no_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：JOR 用 LLM 做 guidance objective 的结构改写，并以任务反馈和零阶数值搜索共同优化外部目标函数；持久结果是目标程序/结构与潜变量，不是模型参数。
- 模型参数/组件边界：guidance objective 的结构、代码/表达式与重参数化潜变量；LLM 参数未训练。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=mL3MYH1pYu
- 官方摘要证据：Optimization problems typically have well-defined task objectives, yet the guidance objectives used to steer optimization algorithms toward high-quality solutions are often hand-designed or manually tuned and may be suboptimal. In this paper, we study *guidance objective reshaping* with large language models (LLMs), aiming to improve optimization outcomes while accounting for structural–numerical coupling and objective alignment, and reducing reliance on manual human effort. To this end, we formulate guidance objective reshaping as a structural-numerical optimization problem and propose *Joint Objective Reshaping (JOR)*. Specifically, JOR combines LLM-driven structural adaptation with zeroth-order numerical optimization over a reparameterized latent space, while aligning the reshaped objective by improving downstream performance and proximity to the high-quality solution region. This design enables structural–numerical modifications to translate more reliably into improvements under the task objective. Extensive experiments across combinatorial optimization, LLM inference acceleration, Bayesian optimization, and reinforcement learning reward shaping show that the guidance objectives discovered by JOR consistently steer algorithms or solvers toward better solutions across diverse settings. Further analysis demonstrates that the reshaped guidance objectives primarily improve the optimization landscape without substantially altering the high-quality solution region under the task objective. Our work establishes guidance objective reshaping as a promising paradigm for LLM-assisted search, learning, and optimization.

### 17. Recursive Self-Improvement through Multi-Agent Self-Supervision

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：官方摘要明确交替进行 multi-agent workflow evolutionary optimization 与在自生成轨迹上的 supervised fine-tuning。
- 模型参数/组件边界：单一基础模型在优化工作流的执行轨迹上做监督微调，模型权重持久更新；工作流图另经外部进化搜索。反向传播实现未明说。
- 训练算法：官方摘要明确交替进行 multi-agent workflow evolutionary optimization 与在自生成轨迹上的 supervised fine-tuning。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=lHLch9v09X
- 官方摘要证据：Recursive self-improvement (RSI) of a model on non-verifiable tasks, such as open-ended research, faces a supervision bottleneck when its outputs exceed what even human experts can reliably assess, leaving the model itself (optimizee) as the best available optimizer and evaluator. However, a single model instance often struggles to reliably critique and improve its own complex reasoning under this homogeneous loop. To address this, we propose Multi-Agent Self-Supervision (MASS), an RSI method that alternates between evolutionary workflow optimization and supervised fine-tuning on self-generated trajectories. Guided by early findings that multi-agent topologies excel at complex reasoning, MASS prompts a single base model to iteratively propose, execute, and self-evaluate multi-agent workflows. Through an evolutionary search constrained by structural guardrails, the model optimizes these computational-graph-like orchestrations, discovering the most effective distinct roles and information routing for a given task. Across multiple open-ended research tasks, the same model on these optimized multi-agent execution traces yields higher performance per training token than training on single-agent trajectories. Because the improved model subsequently acts as a better optimizer and evaluator, this alternating framework enables a continuous, recursive bootstrapping of the model’s capabilities. These findings suggest that jointly learning orchestration and bounded subagent execution from multi-agent trajectories can provide an effective signal for RSI.

### 18. RaSTA: Random Subspace Tuning Adaptation

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：RaSTA 冻结跨层共享随机子空间，只学习 dense basis mixing 或 Walsh–Hadamard mixing 下的逐 basis scaling。
- 模型参数/组件边界：持久 adapter 参数：RaSTA-DM mixing matrix 或 RaSTA-HS scaling vectors；冻结 bases 不存入 adapter checkpoint。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=dP6UvaqrT0
- 官方摘要证据：Parameter-efficient fine-tuning (PEFT) methods such as LoRA specialize a pretrained model by learning a small additive update to its frozen weights. However, LoRA's trainable parameter count is tied to the shape of each adapted matrix, costing at least the sum of its input and output dimensions even at rank one. We propose Random Subspace Tuning Adaptation (RaSTA), which adapts the model within frozen random subspaces shared across layers and learns only how their directions interact, allowing trainable parameter budgets well below rank-one LoRA without storing the frozen directions in the adapter checkpoint. Its two variants trade off the expressivity of the interactions against the number of directions reached under a matched budget. RaSTA-DM learns a dense mixing matrix between the bases, while RaSTA-HS fixes the mixing as a Walsh-Hadamard transform and learns one scaling vector per basis. To our knowledge, this is the first use of the Walsh-Hadamard transform for this purpose. The latter is somewhat more costly but performs better and degrades more gracefully as the budget shrinks. Across mathematical reasoning, commonsense reasoning, and code generation with 7-8B models, as well as natural-language understanding with RoBERTa-large, both variants remain competitive with rank-one LoRA, and sometimes with higher-rank LoRA, at budgets ranging from less than half to about one tenth of its parameter count. Both variants also train faster and use less peak memory than rank-one LoRA, except for RaSTA-HS at its largest considered budget.

### 19. RLSR: Reinforcement Learning with Self-Reflection for Large Language Models Self-Improvement

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：筛选经群组成功验证的自反思轨迹，并在统一 policy-gradient 目标下分别为直接回答与反思纠错分配信用。
- 模型参数/组件边界：LLM policy 被持续优化并内化反思能力。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=ZjYHBdhwoj
- 官方摘要证据：Reinforcement learning (RL) can distill capacities that emerge with test-time self-reflection and incentivize large language models (LLMs) to self-improve. However, existing approaches fail to co-evolve self-reflection with direct policy optimization and instead condition the privileged self-teacher on unverified hindsight, causing self-improvement to plateau or even reverse. In this paper, we propose RLSR, a framework that optimizes and distills self-reflecting LLMs to achieve persistent self-improvement with RL. To generate endogenous learning signals, RLSR samples rollouts via grouped multi-turn self-reflection and retains only instances that achieve group-level aggregate success, grounding the privileged self-teacher in verified rather than assumed hindsight. RLSR also optimizes the policy via a dual-track co-evolutionary mechanism: a direct track internalizes breakthroughs incurred by self-reflection into the direct policy via sign-adaptive counterfactual advantage reshaping, and a reflect track assigns turn-level advantages via a log-odds belief calibration that tracks pivotal corrective transitions, actively reinforcing error correction to safeguard the self-reflection engine against degradation. These two tracks are optimized under a unified policy-gradient objective, establishing a sample-efficient self-reinforcing co-evolutionary cycle that remains stable throughout training. Across eight mathematics and code synthesis benchmarks, RLSR outperforms or matches RLVR and state-of-the-art self-distillation baselines in single-turn pass rate with evolved test-time reflection capacities.

### 20. Privacy-Preserving Federated Fine-Tuning of Language Models under Non-IID Data

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：LSSCA 将 stochastic controlled averaging 与数据无关固定随机子空间滤波结合，保留参考分量并衰减差分隐私联邦 LLM 更新中的正交噪声。
- 模型参数/组件边界：全局与本地语言模型参数、control states 持久更新；固定随机 filter 本身由非私有随机方式构造。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=aIKLwLGFfG
- 官方摘要证据：Differentially private federated fine-tuning enables collaborative adaptation of language models while protecting sensitive training records, but its utility is challenged by client heterogeneity and privacy-induced noise. Control variates mitigate client drift, yet noisy updates also perturb local trajectories and subsequent control states. We propose \texttt{LSSCA}, a federated fine-tuning framework that combines stochastic controlled averaging with fixed random subspace filtering. Constructed independently of private data without requiring public reference data, the filter preserves reference-subspace components and attenuates orthogonal components of the complete control-corrected noisy update. An exact signal--noise decomposition characterizes the trade-off between noise reduction and signal distortion, without assuming that the random subspace aligns with useful gradients. Under the stated assumptions, including inactive clipping, we establish an $\mathcal{O}(T^{-1/2})$ non-convex stationarity rate at a fixed noise scale without an additional gradient-dissimilarity assumption. The analysis explicitly accounts for noise propagation through local trajectories and control states, retaining the costs of filtering in the convergence constants. Experiments across NLP benchmarks, privacy budgets, and client heterogeneity levels demonstrate improved privacy--utility trade-offs over the evaluated DP-FL baselines.

### 21. Noisy Replicator-Mutator Dynamics in Multi-Agent Learning

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：论文从 stochastic policy-gradient updates 推导多智能体动力学，并据此构造 PRPG，属于策略参数训练而非只改文本工件。
- 模型参数/组件边界：多智能体 policy 通过 policy-gradient/PRPG 更新；摘要未给出具体反传实现和参数化范围。
- 训练算法：论文从 stochastic policy-gradient updates 推导多智能体动力学，并据此构造 PRPG，属于策略参数训练而非只改文本工件。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=qtwq8fbHB0
- 官方摘要证据：Evolutionary game theory predicts where a population of learning agents ends up, but the classical replicator equation is derived for a payoff matrix that does not change. Two recent lines of work relax it in different ways. Wang et al. (2026) show that global payoff noise adds a multiplicative term $(\sigma_C-\sigma_D)^2(\frac{1}{2}-x)$, with $\sigma$ the intensity of the payoff fluctuation, to the replicator equation, stabilising coexistence and generating stable limit cycles; Bauer et al. (2026) show that an additive mutation term $M(c-x)$ turns it into a replicator-mutator system whose interior equilibria are last-iterate attracting, which yields convergence guarantees for multi-agent reinforcement learning. The two perturbations have been analysed on their own; their interaction has not been studied. We derive the system that carries both, which we call Noisy Replicator-Mutator Dynamics (NRMD), from a stochastic policy-gradient update; the two terms act on different quantities, so they can be set independently. Our contributions are threefold: (i) we give a complete two-strategy theory of NRMD, consistent with its $n$-strategy form at $n=2$; (ii) we validate the effect of noise in multi-agent experiments; and (iii) we propose a novel algorithm, Population-Replicator Policy Gradient (PRPG), that exploits NRMD. Code and data will be released.

### 22. MaRR: Map-Based Rotation Reasoning for Vision--Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：MaRR 以教师轨迹微调 VLM，使对象特定表征配合共享空间关系旋转与候选匹配程序。
- 模型参数/组件边界：Qwen3.5-4B 经过微调，存在持久模型参数更新；具体参数子集待正文核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=8Zil1NPWtd
- 官方摘要证据：Forward mental rotation requires predicting an object’s unseen
  pose after a specified rotation, rather than recognizing a visible
  configuration. Our controlled diagnostics show that frozen vision–
  language model features contain decodable rotation information and
  support a supplied transformation, while inferring and reusing
  transformations across objects remains unreliable. Building on
  this insight, we introduce MaRR (Map-based Rotation Reasoning), a
  teacher-guided self-distillation framework that combines object-
  adaptive representations with a shared, object-independent
  transformation procedure. Using teacher traces, MaRR teaches VLMs
  to map object-specific features, rotate their spatial relations,
  and match the predicted configuration to candidate images. Fine-
  tuning Qwen3.5-4B with this supervision improves held-out CAD
  accuracy, with gains extending to shifted CAD renderings and block
  objects, although transfer to public benchmarks remains selective.
  A matched comparison shows that trace design introduces tradeoffs:
  natural teacher responses yield stronger OOD transfer and
  physical-choice consistency, while standardized MaRR traces
  achieve higher accuracy under candidate permutation. Together,
  these findings suggest that structured supervision can help VLMs
  organize and use their latent spatial knowledge, while the way the
  procedure is expressed in teacher traces affects transfer and
  robustness.

### 23. MA-RL-VLA: Counterfactual Credit-Aware PPO for Multi-Agent Reinforcement Fine-Tuning of Vision-Language-Action Models

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：MA-RL-VLA 将反事实信用权重置入 PPO 两个分支，明确训练多智能体 VLA 导航策略。
- 模型参数/组件边界：VLA policy 参数由 PPO 持久更新；精确动作枚举用于信用分配，不等同于整个流程无反向传播。
- 训练算法：MA-RL-VLA 将反事实信用权重置入 PPO 两个分支，明确训练多智能体 VLA 导航策略。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=MtYTLgYRmu
- 官方摘要证据：Reinforcement learning (RL) has proven effective for fine-tuning \emph{single-agent}
		vision-language-action (VLA) models, yet extending this paradigm to
		\emph{multi-agent} vision-language navigation (MA-VLN) remains largely unexplored.
		We present \textbf{MA-RL-VLA}, a centralized-training / decentralized-execution
		(CTDE) framework whose core design is a mathematically consistent integration of
		counterfactual credit into PPO for VLA-scale actors. The counterfactual baseline is
		\emph{identical in form} to COMA's policy-marginalized baseline, and because one
		actor pass already yields the full distribution over the four discrete navigation
		actions, it is computed by \emph{exact enumeration} at the cost of four small-critic
		evaluations per agent step. The detached, clipped credit weight is folded \emph{inside}
		both PPO branches as a combined advantage $\Act_i=\sg[\tilde w_i]\bA_i$, preserving
		PPO's pessimistic clipping under negative credit and thereby suppressing free-riding.
		The reward separates a policy-invariant potential-based progress term (fixed, never
		tuned) from auxiliary coordination terms with fixed weights selected on training-split
		tuning scenes. On CoNavBench (Habitat, $N{=}3$) with 8 matched seeds, MA-RL-VLA
		improves Team Success Rate by $+19.1$ points over behavior cloning (95\% CI
		$[16.3,21.9]$) and $+6.4$ points over standard COMA-style credit ($[3.9,8.9]$;
		exact paired permutation $p{=}0.008$), and cuts exploration redundancy by $40.7\%$.
		Controlled ablations attribute the gain to the credit signal ($+8.0$), the objective
		form ($+2.3$ over the legacy outer-weight surrogate), and the exact estimator. Our
		evidence is confined to one simulated benchmark and one VLA backbone; we state
		precisely which guarantees do and do not transfer to the deployed update.

### 24. Local proxies for memory-efficient training

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：每个 Transformer block 通过蒸馏训练局部 proxy，并在该 proxy 内独立反传以近似全局梯度、降低激活内存。
- 模型参数/组件边界：Transformer blocks 与 proxy networks 均通过局部训练产生持久参数更新。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=bbhfFx9iqO
- 官方摘要证据：Local learning algorithms can reshape resource requirements of artificial intelligence. The memory bottleneck of standard end-to-end backpropagation lies in the need to store all network activations until the loss gradient has been propagated back through. Local learning avoids this, but typically at a cost in accuracy. We study how to achieve accurate and memory efficient local learning in transformers. For each transformer block, we train a local proxy network to predict the global network output via distillation. Gradients can be independently propagated through this local proxy while estimating well the backpropagation gradients. In theory, this approach is exact for deep linear networks; in non-linear residual models, the gradient error can be bounded when using the appropriate residual proxy. We verify this numerically and demonstrate that optimizing the distillation loss improves gradient estimation. Evaluating the performance of proxy propagation on CIFAR-100 in vision transformers, we find that it achieves a better accuracy/memory trade-off compared to other local algorithms. Finally, we show that the method is further relevant for fine-tuning large language models on a small memory budget. Our method trains faster and achieves higher performance than zeroth-order memory-efficient learning algorithms with comparable memory cost.

### 25. LoLoRA: Locally Fine-Tuned Low Rank Adapters

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：LoLoRA 在前向过程中依据每层输入对 LoRA 矩阵 A 做局部 gradient-free 更新，省去 A 的反传激活存储，同时保留其余 adapter 训练路径。
- 模型参数/组件边界：LoRA A 持久更新；LoRA B 与基础模型权重的持久更新范围待正文核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=nvUl5uZXor
- 官方摘要证据：Low-Rank Adaptation (LoRA) is a memory-efficient fine-tuning method for large language models (LLMs) that approximates weight updates as $\Delta W = BA$, where $B \in \mathbb{R}^{n \times r}$, $A \in \mathbb{R}^{r \times m}$ and $r ≪ min(m, n)$. To maximize memory savings, one can freeze matrix $A$, avoiding the storage of its input activations, but this often degrades performance. In this work, we mitigate this trade-off by introducing gradient-free updates to matrix $A$ during the forward pass. Our method computes these updates based on the layer’s immediate input, allowing it to adapt to input distribution shifts without storing activations for the backward pass. Experiments show that our approach achieves fine-tuning accuracy comparable to standard LoRA, while reducing peak memory consumption by up to 20% on LlaMA3-8B.

### 26. Learning to Predict Distributions over Weight Updates for Test-Time Adaptation

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：query-conditioned distributional hypernetwork 以可微 Monte Carlo 损失训练 LoRA 分布，并在测试时采样权重更新形成多个适配模型。
- 模型参数/组件边界：hypernetwork 参数持久训练；测试时 query-conditioned LoRA samples 为实例级适配权重，是否跨 query 保存待核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=JXYRjlh1Wh
- 官方摘要证据：Hypernetworks have recently shown success in dynamically adapting the parameters of Large Language Models (LLMs) at runtime based on signals such as task descriptions or additional demostrations. Here we ask: how much adaptation signal can be obtained using only the input query to an LLM?. To answer this, we study query-conditioned Hypernetworks for LoRA estimation. Further, we introduce distributional Hypernetworks, able to produce not only point estimates of parameter adaptors, but also a distribution over possible LoRAs. For this we propose a simple end-to-end loss using a differentiable Monte Carlo approximation and explore multiple distribution parametrizations including regression and convex combination variants. Results show that even using the mean of the learned distribution can outperform deterministic hypernetworks.
Crucially, the learned distribution enables a different form of test-time scaling: instead of spending additional compute only by sampling more token sequences from a fixed model, we sample weight updates, yielding multiple adapted models for the same query. Performance improves as more weight samples are considered and remains stronger than corresponding token-sampling adaptation baselines. Finally, we find that generated updates can transfer across queries, suggesting that the hypernetwork learns reusable structure in how the model should adapt. Together, these results show that query-conditioned distributions over weight updates can support both adaptation and test-time scaling.

### 27. Learning to Elicit: Co-Evolving Routing and Information Disclosure in Societies of Language Agents

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：Co-Adapt 用 RL 与 privileged on-policy distillation 学习联系路由和私有信息披露。
- 模型参数/组件边界：智能体 routing/disclosure policy 由 RL 与蒸馏持久训练；各模块是否共享语言模型参数及反传细节待正文核实。
- 训练算法：Co-Adapt 用 RL 与 privileged on-policy distillation 学习联系路由和私有信息披露。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=xupjJh9hXG
- 官方摘要证据：Multi-agent language models increasingly operate in societies of agents characterized by information asymmetry, where the information required to solve a task is distributed across agents. Effective coordination therefore depends not only on solving the task but also on deciding what information to elicit and from whom. We study this problem in a multi-agent meeting environment where agents possess private facts and must communicate over a shared public record to reach a verifiable settlement. We introduce ElicitBench, a benchmark in which agents hold distributed private information and must reveal the relevant facts through interaction before a designated decision maker can reach the correct outcome. We then propose Co-Adapt, a co-evolutionary training framework that jointly learns routing and agent information disclosure through reinforcement learning and privileged on-policy distillation. The router learns which agents to engage, while agents learn which private information to reveal. On the held-out test set, Co-Adapt raises the fraction of settlement checks passed from 0.65 to 0.81 and the strict success rate from 14% to 25%. Gains are largest on domains unseen during training, where the fraction of settlement checks passed increases from 0.57 to 0.78. Ablation studies further demonstrate that the gains arise from jointly learning information routing and information disclosure, rather than from either component alone.

### 28. Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：TFlow 明确训练 parameter generator，由 sender 隐状态生成 receiver-specific 低秩 LoRA 扰动。
- 模型参数/组件边界：parameter generator 参数被训练；receiver 基座冻结，但生成的 LoRA 扰动在单次生成中改变模型参数状态。训练算法和反传边界待核实。
- 训练算法：TFlow 明确训练 parameter generator，由 sender 隐状态生成 receiver-specific 低秩 LoRA 扰动。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=tDrV3iV2Zb
- 官方摘要证据：Multi-agent LLM systems usually collaborate by exchanging natural-language messages. This interface is simple and interpretable, but it forces each sender's intermediate computation to be serialized into tokens and then reprocessed by the receiver, thereby increasing the generated-token cost, prefill overhead, and KV-cache memory. We study an alternative communication interface: instead of appending a sender's message to the receiver's context, compile the sender's hidden states into a transient, receiver-specific weight perturbation. We introduce **TFlow** (Thought Flow), a weight-space communication framework for a known and fixed receiver architecture. For each query, frozen role-prompted sender agents process the input, and a learned parameter generator maps their internal activations into low-rank LoRA perturbations targeting the receiver's modules. These perturbations are fused and applied only during the receiver's generation, enabling instance-level adaptation without permanently changing the model or enlarging the receiver's text context.
With three Qwen3-4B agents, **TFlow** improves over a standalone receiver by up to 8.5 accuracy points across five benchmarks while reducing processed tokens by up to 32.69%. Compared with a text-based three-agent baseline, it reduces total processed tokens by up to 83.27% and the wall-clock inference time by up to 4.6$\times$, while maintaining competitive accuracy on four of five benchmarks. These results suggest that transient low-rank weight perturbations can serve as an executable communication medium for efficient multi-agent LLM collaboration.

### 29. GPU Forecasters: Language Models as Speculative Surrogates for Kernel Runtime Optimization

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：该工作用 LLM surrogate 预测 kernel 运行时以筛选 GPU 实测候选，并另以 RL 训练 surrogate 的校准能力。
- 模型参数/组件边界：存在持久的 RL-trained surrogate 更新；另持久保存 kernel 候选与 12,388 个实测样本
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=x23LuMrBJo
- 官方摘要证据：GPU kernels are the workhorse of modern deep learning, and optimizing them (via evolutionary search or coding agents) usually requires repeated measurement on target hardware. While these measurements provide the ground-truth signal necessary for kernel search, they are costly, because each evaluation of a kernel requires compilation and repeated execution on a GPU. As improvements in LLM inference reduce the cost of writing novel kernels and LLM-driven searches scale to large search budgets, on-device evaluation becomes a bottleneck. To address this, we study how LLMs can serve as calibrated, speculative surrogates of the GPU: probabilistic performance models that forecast the speedup of a candidate kernel from its source. During a kernel search algorithm’s generation phase, the surrogate forecasts runtimes for generated kernel, and only the top-ranked kernels are scored by the GPU. The search uses the speculative forecasts by the surrogate as scores for the remaining kernels. We first evaluate four off-the-shelf LLMs as surrogates. We find that LLMs can act as effective surrogates, helping searches find fast kernels while measuring only a fraction of generated candidates on the GPU. On 1,347 parent-child pairs from real searches, LLMs identify discovery moments, i.e., children that are much faster than their parents, at rates above chance. We then integrate a surrogate into evolutionary kernel search to prioritize candidates for GPU measurement. Measuring only the most promising generated candidates, this search matches or outperforms GPU-only search on most benchmark tasks. Finally, we train a surrogate with reinforcement learning and find that calibration rewards improve calibration without hurting ranking, while correctness rewards alone make confidence less reliable. We release the 12,388 measured LLM-generated kernels produced by these searches. These results suggest that LLMs can play a broader role in kernel optimization, by acting as virtual models of a GPU rather than solely as kernel generators for search.

### 30. Entropy Targeting in Sequential Reinforcement Fine-Tuning of Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：分析顺序强化微调中哪些一致性信号真正进入策略更新，并识别 entropy targeting 的作用。
- 模型参数/组件边界：顺序 reinforcement fine-tuning 会持续更新语言模型策略；摘要未给出具体参数子集。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=E4354yeoTt
- 官方摘要证据：Sequential reinforcement fine-tuning asks a language model to keep improving as its tasks change, yet the auxiliary signals added to stabilize such training are rarely checked for whether they reach the policy update at all. We study this question in AdaCoT-CL, a group-relative sequential learner that combines three consistency signals (entropy targeting on the reasoning span, alignment between reasoning and answer representations, and answer agreement) with replay, and we reanalyze 63 recorded runs on a five-task reasoning stream, 59 of them with Qwen3-8B. We first show that the agreement signal supplies no direct policy gradient: its group-shared reward bonus cancels whenever rewards are centered within each prompt group, and its auxiliary loss is detached. This result partitions the seven ablation variants into four effective objectives and motivates a grouped comparison. In that comparison, configurations with entropy targeting improve on average and those without it decline. On fixed monitoring panels, the 12 runs with entropy targeting gain 13.2 accuracy points from initialization to the end of the sequence, while the 9 runs without it lose 8.7 points (difference 21.8 points, exact permutation $p=8.8\times10^{-5}$; a contrast averaged within seed and alignment blocks gives 24.1 points, $p=1.7\times10^{-4}$), and the primary comparison replicates this direction against five baselines. The largest divergence occurs between the end of the LogiQA phase and step 32 of the final task, a block that combines training on the new task with replay of earlier prompts: mean accuracy on the earlier panels rises by 27 points on average with entropy targeting, and the smallest such rise, 16.7 points, exceeds the largest without it, 4.2 points. The evidence has clear boundaries: the panels are drawn from training prompts, initial accuracy is low under a 512-token completion budget, the benefit shrinks under other task orders, and the same objective collapses Llama-3.1-8B-Instruct. We therefore present entropy targeting as the consistency signal that distinguishes improving from declining configurations of this learner, and we specify the held-out protocol needed to establish it as a continual-learning method.

### 31. CoEvoMed: Co-Evolving Supervision Principles and Medical Vision–Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：随医学 VLM 能力变化共同更新监督样例构造原则与课程预算，并以这些监督训练模型。
- 模型参数/组件边界：摘要明确使用该框架训练 8B 模型并报告 32B 结果，因此学习者存在持久参数更新；具体参数与优化器未说明。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=GeL7NntZTU
- 官方摘要证据：Training medical vision–language models requires supervision that adapts as the learner's capabilities change across tasks. Existing pipelines typically rely on repeated manual error analysis and task-specific training data construction, making this adaptation costly. We introduce CoEvoMed, a co-evolutionary framework that couples a medical vision–language learner with a multi-agent supervision process integrating the evolution of construction principles with curriculum allocation. These reusable principles define question intent, guide how responses draw on medical evidence, and clarify conceptual distinctions in training examples. A revision agent updates these principles in response to the learner's evolving task-specific capabilities, guided by comparisons of factual consistency and task alignment between examples generated from the same medical evidence. Under fixed budgets for each task, curriculum allocation adjusts construction effort according to the learner's capability profile and learning progress. Using CoEvoMed, we train an 8B model supporting both 2D and 3D medical tasks. It surpasses Hulu-Med-7B by 1.15–4.80 percentage points on four 2D VQA benchmarks and achieves higher RaTEScore on MIMIC-CXR and IU-Xray, while delivering strong performance on 3D recognition, question answering, and report generation. Results at 32B further support the scalability of the framework.

### 32. CoER: Defending against Adaptive Indirect Prompt Injection via Adversarial Co-Evolution and Refinement

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 论文特定依据：CoER 的核心任务是 adaptive indirect prompt injection：攻击者反复生成/适配注入内容，虽同时以 BA-RL 和 fine-tuning 训练 defender，仍命中“提示词相关暂缓”例外。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=SUxaNjKUP8
- 官方摘要证据：Language-model agents are vulnerable to indirect prompt injection (IPI) during tool use: adversarial instructions hidden in untrusted tool outputs can covertly redirect legitimate task execution. Existing work often trains and evaluates defenses against fixed attacks that do not adapt to the defender's behavior, so the resulting defenses may struggle against adaptive attacks in real-world settings. We argue that a strong defense against adaptive IPI must adapt during training to a continually evolving attacker. Building on this insight, we propose CoER, a verifier-grounded co-evolution and refinement framework that models interleaved tool calls and adaptive injections within a task as a general-sum Markov game: the defender advances the task through successive tool calls, while the attacker can inject multiple times within the same task and adapt subsequent attacks to the defender's responses and prior execution traces. After initializing the attacker from successful trajectories, bilateral adversarial reinforcement learning (BA-RL) retains historical policies from both roles as opponent populations and mixes current and historical opponents, extending training beyond the latest matchup. Attackers from these populations are then reused to challenge teacher agents, and only demonstrations verified for both safety and task completion are used to fine-tune the co-evolved defender. Across seven domains and three evaluation seeds, CoER reduces adaptive attack success from 41.3\% to 0.2\% and raises safe task completion from 39.6\% to 76.2\%; external benchmarks also show improved attack resistance. Further experiments validate the effectiveness of bilateral historical-opponent mixing and population-guided refinement. Attacker analyses show that co-evolution strengthens attack capabilities and that the trained attacker uses execution feedback to adapt subsequent injections.

### 33. Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：PPol 的 persona 程序由进化 coding agent 搜索；摘要另明确用 PPol 数据 fine-tuning agents 并报告真人交互提升。
- 模型参数/组件边界：persona generation program 是外部搜索工件；下游语言 agent 明确经过 fine-tuning，具体参数子集和反传实现未说明。
- 训练算法：PPol 的 persona 程序由进化 coding agent 搜索；摘要另明确用 PPol 数据 fine-tuning agents 并报告真人交互提升。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=HJaoIZVSzM
- 官方摘要证据：Large Language Model (LLM) agents are increasingly deployed in settings where they interact with diverse users, including those who are unclear, impatient, or reluctant to share information. However, collecting real interaction data at scale remains expensive. The field has turned to LLM-based user simulators as stand-ins, but these simulators inherit the behavior of their underlying models: cooperative and homogeneous. As a result, agents that appear strong in simulation often fail in real human interactions. To narrow this gap, we introduce Persona Policies (PPol), a plug-and-play control layer that induces realistic behavioral variation in user simulators while preserving original task goals. Rather than hand-crafting personas, we employ an evolutionary coding agent to discover persona generation programs optimized for human-likeness and behavioral coverage over real user conversations. The evolved program generates diverse, human-like personas for any task in the domain. Across 4 benchmarks---including $\tau^2$-bench Retail and Airline, ColBench, and WildChat---evolved PPol yield 28-72\% absolute gains in fitness score over the baseline simulator. In blinded evaluations, annotators judged PPol users as 'human' 80.4% of the time, nearly 2x more than the baseline simulators. Training agents with PPol also improves real-world performance: our user study with live human--agent interactions showed that fine-tuning with our method boosted task success by $+23$% over default baselines. PPol thus offers a novel approach to strengthen simulator-based evaluation and training without changing underlying tasks.

### 34. Beyond Alignment: Enhancing LLM Safety Robustness via Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：在常规一阶安全对齐后追加少量零阶鲁棒性精炼步骤，因此归入一阶与零阶混合方法。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件/优化器状态：摘要未明说者待核实
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=9Lrcxvs7GS
- 官方摘要证据：Safety alignment for large language models (LLMs) aims to reduce harmful or unsafe behavior while preserving general utility. However, recent findings reveal that alignment effects can be fragile: lightweight post-alignment manipulations, such as parameter noise, activation noise, or quantization, can easily weaken the intended safety behavior. Prior efforts to improve robustness have primarily focused on data curation, modified alignment objectives, and safety-critical parameter identification, leaving the role of the optimizer itself largely unexplored.

In this paper, we are the first to study the robustness of safety alignment from the perspective of the base optimizer. This optimizer-centric view naturally points to zeroth-order optimization, which provides a robustness-oriented signal by evaluating safety alignment under perturbations. Based on this insight, we propose a hybrid framework that first performs standard first-order safety alignment and then applies zeroth-order refinement to improve robustness. Both theoretically and empirically, we show that only a few zeroth-order refinement steps can enhance robustness while preserving safety alignment. We further improve the efficiency of zeroth-order refinement by exploiting its inherent perturbation-based evaluations to estimate layer-wise robustness sensitivity, enabling the refinement process to concentrate updates on robustness-critical layers with modest training overhead.

### 35. AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：AgentSafeEvo 是 attacker–defender co-evolutionary RL，摘要明确攻击者和防御者均学习任务/执行策略。
- 模型参数/组件边界：attacker 与 defender 的语言智能体策略由 RL 持久更新；task weighting 是信用/课程机制，具体反传实现待核实。
- 训练算法：AgentSafeEvo 是 attacker–defender co-evolutionary RL，摘要明确攻击者和防御者均学习任务/执行策略。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=9wUe4gLzDm
- 官方摘要证据：Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce unsafe actions. Adversarial co-evolution has emerged as an effective approach to strengthening LLM safety, but existing work primarily focuses on language-level safety or indirect prompt injection in web tasks. In this paper, we introduce \textbf{AgentSafeEvo}, a co-evolutionary reinforcement learning framework for agent safety built on an attacker–defender game spanning diverse tasks and attack types. The attacker learns to construct adversarial agent tasks that expose weaknesses in the defender's tool use, while the defender learns to complete tasks safely under these attacks. We further introduce learnability-guided task weighting, which uses within-task defender-reward variability to adjust each task's contribution to attacker and defender updates. Extensive experiments on agent safety and general capability benchmarks demonstrate that our method improves adversarial robustness while maintaining general agent capabilities.

### 36. ACE-Guard: Automated Co-Evolutionary Guardrails for LLM Security via Inference-Time Natural Language Gradients

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 论文特定依据：ACE-Guard 的核心是 prompt injection 防御与 natural-language prompt steering，且摘要明确 ΔΘ=0；属于提示词核心。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=8YtHcGc4sq
- 官方摘要证据：Prompt injection attacks pose a persistent threat to Large Language Model (LLM) deployments by embedding malicious instructions that override system controls. Existing defenses rely on static rules or require costly model fine-tuning, leaving them exposed when adversarial strategies shift over time. We present ACE-Guard, an automated co-evolutionary security framework that adapts defensive policies entirely without modifying model parameters ($\Delta\Theta = 0$). ACE-Guard operates through a dual-phase architecture: an offline co-evolutionary calibration phase that models security adaptation as a repeated game among an Adversary LLM exploring nine structural injection strategies, a Defense LLM equipped with a deterministic Multi-Signal Prompt Inspector (MSPI), and an Evaluation LLM providing bidirectional natural language gradients, followed by an online pre-execution serving phase that enforces safety in a single forward pass. Across 20 co-evolutionary calibration rounds, ACE-Guard achieves an average Defense Success Rate of 83.4\% and a Benign Acceptance Rate of 91.9\%, yielding a Balanced Harmonic Score ($S_{\text{bal}}$) of 87.4\%. Extensive evaluations across out-of-distribution attack benchmarks confirm that natural language prompt steering maintains long-term stability, resists adversarial mode collapse, and achieves robust runtime protection without retraining overhead.

### 37. ReLaDrift: Recurrent Language Generation via Drifting for Test-Time Scaling

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：ReLaDrift 递归修正 Drifting Model 草稿，并只在随机选取的一轮上施加 drifting loss、避免跨轮 BPTT，但仍保留该单轮训练组件。
- 模型参数/组件边界：模型权重：存在持久训练更新但参数范围待核实；推理草稿：轮间暂态。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=C1HGhWNaYZ
- 官方摘要证据：The original Drifting Model generates a sample with a single function evaluation, which makes it attractive for fast parallel language generation, but its one-step formulation does not include iterative refinement.
We propose Recurrent Language Generation via Drifting (ReLaDrift), which applies one Drifting Model recurrently: each round after the first corrects the draft of the previous round, and training applies the drifting loss to one randomly chosen round without backpropagation through time.
On two reasoning tasks with ground-truth answers, Sudoku Hard and GSM8K, the accuracy of ReLaDrift increases with the number of function evaluations (NFE) in the few-step regime (NFE < 32); a single round is already at least as accurate as a single-round Drifting Model trained in the same way, and a few more rounds make it far more accurate.
At every NFE from 4 to 32, ReLaDrift outperforms diffusion and flow language models of comparable size trained on the same data, reaching 92.1\% on Sudoku Hard at NFE=16 and 29.1\% on GSM8K at NFE=4, versus 77.5\% and 9.4\% for the best of them.

### 38. Super Neurons Answer Before VLMs Speak

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：无梯度筛选少量 VLM 语言模块神经元，以其标量激活在自回归生成前直接完成分类 VQA。
- 模型参数/组件边界：discovery 阶段不更新 backbone；持久保存 neuron indices/readout；可选微调分支持久更新参数范围待核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=r9LXL9LP7B
- 官方摘要证据：Vector-level representations in pretrained vision-language models can be repurposed for prediction, but how small can these representations be? We show that direct scalar readouts from a handful of neural units (e.g. 10) in the LLMs of VLMs can outperform the full, billion-parameter model from which they are selected on categorical visual question-answering tasks. Notably, these super neurons can be identified in a gradient-free setting, using a single GPU. We thoroughly analyze super neurons and find that they satisfy key properties of effective predictors: they do not seem to exploit spurious biases and generalize well. Therefore, they enable diverse applications. Since they are discovered during prefill encoding, their predictions are able to bypass the autoregressive generation process of the LLM, dramatically reducing runtime by up to 27.8× on Qwen3-VL-8b-Instruct. Since they are sparse, they enable lightweight finetuning, preserving some of the VLM’s general capabilities while improving its performance on a target task. Our code will be released upon acceptance.

### 39. Sample the Order, Not the Token: Test-Time Scaling for Masked Diffusion Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：OSE 在测试时扰动掩码扩散模型的解掩码顺序进行集成，不更新模型参数；其另行报告的 GRPO 实验属于一阶训练。
- 模型参数/组件边界：OSE 不更新模型；GRPO 分支持久更新 policy。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=mISIJ9ktNq
- 官方摘要证据：Standard test-time scaling methods like temperature-sampled self-consistency are highly effective for autoregressive models, but we show it is not true for masked diffusion language models (dLLMs). Attempting to scale dLLMs via temperature sampling collapses generation length and plummets accuracy (e.g., from 35\% to 6\% on MATH500), failing to yield the diversity required for ensembling. Motivated by this misalignment, we propose Order-Space Exploration (OSE), a novel decoding strategy demonstrating that dLLM diversity should originate from the order of token generation, not the token distribution itself. We first observe that a perfect model's answer distribution is invariant to unmasking order, thus shuffling this schedule yields "free" diversity driven entirely by the model's internal disagreement across generation paths, avoiding the accuracy penalty of temperature scaling.
OSE introduces a one-parameter Plackett–Luce perturbation of the sampler's position ranking and aggregates the N draws with a majority vote over their answers.
Empirically, OSE raises answer diversity by
2-5$\times$ while leaving single-draw accuracy unchanged.
This unlocks test-time scaling for dLLMs, beating standard self-consistency on Dream by up to 45.5 points on a variety of downstream tasks.
Additionally, OSE rollouts restore the learning signal in GRPO, removing nearly all zero-gradient steps on generation tasks and about half on multiple choice. It improves the trained policy where the base model has room to learn (+7.6 on MATH500, +8.5 on Countdown), with no change to the model or the inference cost.

### 40. Pharos: Augmenting Lighthouse Attention with Adaptive Budgets, Cross-Level Guidance, Tidal Momentum, and Uncertainty-Aware Fallback

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：Pharos 为分层长上下文注意力加入自适应 head 预算、跨尺度指导、跨层动量和低置信回退。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件：若仅当次推理状态则不跨任务持久；是否保存校准状态待核实
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=v1SEW28Ij4
- 官方摘要证据：Lighthouse Attention proposed a symmetric hierarchical pooling and gradient-free selection mechanism that accelerates long-context pre-training by 1.4–1.7× end-to-end while recovering dense-attention quality after a brief SDPA resume phase. Despite these gains, three structural rigidities limit its potential: (i) a fixed per-layer top-k budget that ignores head-to-head variance in selection entropy; (ii) independent scoring across pyramid levels, discarding the strong prior that coarse-level selections should bias fine-level routing; (iii) no mechanism to carry selection state across transformer layers, even though empirical evidence shows that important tokens tend to recur across depth. We address all three limitations in Pharos, a drop-in augmentation to Lighthouse Attention built around four coordinated mechanisms: Depth-Sounding Budget Allocation (DBA) redistributes the global k budget across heads proportional to per-head selection entropy; Range Light Cross-Level Guidance (RCG) injects upsampled coarse selection scores as a learned additive bias into fine-level logits before top-k; Tidal Momentum Selection (TMS) maintains an exponential moving average of selection logits across layers, creating a persistent prior over globally important tokens; and Fog Gate Confidence Fallback (FCF) dynamically widens the attention beam for low-confidence heads via a learned binary threshold. We prove that DBA strictly tightens the selection-recall bound of Lighthouse Attention under any non-uniform head-entropy profile, and that TMS provably reduces cross-layer selection variance. All four mechanisms are implemented as a drop-in wrapper over the existing selection interface with no asymptotic overhead.

### 41. BiTFlow: Efficient Coreset Selection for Instruction Tuning via Balanced Token Flow Matching

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：将候选样本的中间层 token 残差流与目标原型作二分匹配，并以平衡覆盖聚合完成前向筛选。
- 模型参数/组件边界：selection 阶段不更新模型；持久输出 coreset；随后 instruction-tuning 会更新模型参数。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=QFIRgU2Gex
- 官方摘要证据：Coreset selection for instruction tuning aims to reduce fine-tuning computation
while preserving downstream performance. Forward-only selection methods avoid costly model updates and backward passes by comparing hidden-state fingerprints, most often from the last layer. However, samples with highly similar last-layer states can induce different intermediate token updates, a phenomenon we call *last-layer similarity collapse*, indicating that intermediate layers carry information beyond the last-layer state. We capture this information with residual flows, the residual updates of each token between selected layers. Building on these flows, we introduce BiTFlow, a forward-only coreset selection algorithm that compares candidate samples with a small set of target-task samples at the token level. BiTFlow summarizes target residual flows into token-level prototypes and aligns candidate tokens to them via one-to-one bipartite matching. A balanced aggregation then scores each sample by both how well its tokens match and how many distinct target token IDs are covered. At a 5% selection budget on the LESS (0.27M samples) and
SmolTalk (1.04M samples) pools, BiTFlow achieves the highest average performance and exceeds full-data fine-tuning on multiple benchmarks, and its selections transfer across model scales and families. Scoring requires no backward passes or warmup training and is $\sim$18$\times$ faster than gradient-based methods.

### 42. Word-Level Text Unmixing via Evidence-Preserving Ownership Routing with Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：EPoR 训练因果语言模型预测词所有权路由，再用受约束解码和确定性重建保证证据完整。
- 模型参数/组件边界：路由模型经过训练，故存在持久模型适配；具体参数范围和训练方法待正文核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=5ASvyn7llP
- 官方摘要证据：Text from multiple sources can become interleaved into a single sequence when attribution metadata is lost, such as overlapping speech transcripts, complex document reading flows, or concurrent agent streams. While all observed words remain present, their underlying source ownership is unknown. We formalize this challenge as Word-Level Text Unmixing: given an interleaved lexical stream and the source count K, recover the original source sequences while preserving every word occurrence and its within-source order exactly. Conventional large language model (LLM) paradigms approach this by generating separated source texts directly. However, coupling latent ownership inference with lexical regeneration frequently causes LLMs to omit, duplicate, or hallucinate words, violating the exact-reconstruction objective. To resolve this, we propose Evidence-Preserving Ownership Routing (EPoR), a framework that cleanly separates ownership prediction from sequence reconstruction. During training, EPoR adapts a causal LLM to predict canonical ownership routes conditioned on the interleaved stream and prior routing decisions, inducing dynamic, history-conditioned source contexts without lexical regeneration. At inference, EPoR pairs completion-safe constrained decoding with deterministic indexed reconstruction, guaranteeing structurally valid K-source partitions that preserve every observed token occurrence exactly once. For systematic evaluation, we introduce UnMixBench, spanning controlled synthetic mixtures, timestamp-derived speech from AMI and ICSI, layout-derived document streams from ReadingBank, and simulated concurrent digital outputs. Across five evaluation tracks, a 4B EPoR model achieves the lowest minimum-permutation word error rate (MP-WER) among finetuned baselines, reducing the five-track mean by 22.3% relative to compact source-array generation and competing favorably with zero-shot frontier LLMs. These findings indicate that when lexical evidence is fully observed, decoupling ownership routing from sequence reconstruction can provide a more reliable and structurally sound alternative to generative decoders.

### 43. When to Prompt, When to Update: Context-Parameter Allocation for Language Agents

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 论文特定依据：论文直接研究 prompt information 与 parameter writes 的分配，并以 controller 投影/维护 prompt state；即使会触发参数更新，也属于提示词核心。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=OTIZLTbN5q
- 官方摘要证据：Language agents must follow structured protocols, adapt to evolving environments, and operate under memory, latency and cost constraints. Adaptation then requires deciding where task-relevant information should live; in the prompt, which is fast and reversible but bounded, or in the parameters, which is persistent but expensive to write. We formalize this as an information-allocation problem. Two limits make the trade-off concrete: parameter writes have diminishing returns, while the usable prompt is bounded not by the context window but by attention dilution, for which we derive and empirically validate a scaling law that provides a measurable prompt-side constraint. We propose an oracle-student-controller architecture that acts on this analysis. A compact student is first distilled to acquire the desired output schema. During deployment a controller preserves the schema by construction, projects the semantic state into a feasible prompt domain with an approximation guarantee, and triggers oracle-supervised parameter updates only on persistent error. The trigger is computable from student and environment observable signals alone, so the oracle is never queried in order to decide whether to use it. Across Multi-Fidelity Bayesian Optimization, all 812 WebArena tasks, and both ALFWorld splits, we studied Llama-3.1-8B and Mistral-7B performance as students. Experimental results show improvement of their baseline performance by integrating the adaptive allocation schema, which is also compared against current state-of-the-art methods.

### 44. Safe Alone, Unsafe Together: Compositional Curvature Safety Alignment for Prompt Robustness

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 论文特定依据：论文核心对象是 compositional prompt transformations、prompt safety lattice 与 prompt robustness；参数子空间修复不改变其提示词核心范围。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=uXUOE1j8px
- 官方摘要证据：Safety-aligned language models are typically evaluated against isolated prompt
transformations or sampled attack compositions. We identify a distinct failure
mode in which transformations that preserve appropriate behavior individually
interact to cross the model's safety boundary. We formalize compositional prompt
safety over a lattice of policy-preserving factors and introduce
\emph{adverse safety curvature}, the negative part of the mixed discrete
derivative of a sequence-level appropriate-response margin. We show that
factor-pair-specific curvature bounds yield a lower bound on every composed
margin and a certified composition order on an exhaustively verified finite
lattice. Guided by this result, we propose $C^{2}SA$, which discovers violated
base-margin, singleton, curvature, and utility conditions and applies
minimum-change updates in an editable parameter subspace. During alignment,
$C^{2}SA$ evaluates curvature contexts of size at most three, requiring lattice
nodes only through order five; orders six through eight are reserved
exclusively for higher-order extrapolation. Across three open-weight model
families and eight prompt factors, $21.7\%$ of harmful requests that are safe
under every singleton transformation fail at one or more test-only orders.
Adverse curvature predicts these failures with an AUROC of $0.85$. Relative to
the strongest curvature-hinge baseline, $C^{2}SA$ reduces ASR across orders six
through eight from $22.0\%$ to $18.0\%$ and SCFR from $9.5\%$ to $7.5\%$,
while changing benign helpfulness by only $0.3$ points. Pair-specific
certification covers $75.5\%$ of test prompts through order three, and the
robustness gains persist under unseen factor realizations, held-out factor
families, factor-order permutations, and adaptive post-repair attacks. These
results establish adverse safety curvature as a measurable and controllable
source of compositional alignment failure.

### 45. Rent or Recompute?: Learning-Augmented Placement of Agent KV Caches Across Memory and Shared Storage Tiers

- 决定：`defer_agent_no_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：核心是 agent KV-cache 在 GPU/主存/存储层之间的放置策略；语言智能体和 LLM 参数均不更新。
- 模型参数/组件边界：仅训练 idle-gap predictor；该预测器服务缓存调度，不是语言智能体 policy、LLM、LoRA 或 adapter，因此不满足保留条件。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=5MJgRASpik
- 官方摘要证据：LLM agents keep contexts of 100K tokens or more alive across dozens of turns. Most of that time, they sit idle, waiting on tool calls, sub-agents, and people. Each idle gap forces a serving system to decide whether a session's KV cache is worth keeping and where it should live. Production traces show that prefix-cache hit rates collapse once a session idles for minutes, and a miss costs several times the pre-fill for the next turn. Today, this decision is made based on recency or fixed time-to-live rules. We show that placing an idle session's KV cache across GPU memory, host memory, and storage is an instance of multi-state dynamic power management. Each tier is a state with a rent rate. Returning from a tier, by reload or by recomputation, is its wake-up cost. This lets us import learning-augmented ski-rental guarantees directly: a policy that consumes a predicted idle gap is $(1+\lambda)$-consistent and $(1+1/\lambda)$-robust per gap, for a trust parameter $\lambda$. We train an idle-gap predictor on features observable when a request finishes, and evaluate it on 346K idle gaps from 4,265 real coding-agent sessions, split by user. Whether a gap ends in a tool result or a human reply is observable, and it matters (seconds versus minutes). The length of the gap within each kind is only weakly predictable: 42% of tool gaps and 24% of human gaps fall within $2\times$ of the prediction, against 26% and 23% for a per-tool lookup table. On held-out users, the learning-augmented policy meets its per-gap bounds exactly. At a reference parameter set, a hedged policy with a validation-tuned trust parameter uses 11\% fewer GPU-seconds than the best prediction-free policy; exact predictions would save 20\%. Using the same predictions without hedging costs $7.6\times$ the clairvoyant optimum. A closed-form crossover context length, $K^\star = (\text{bytes/token}\,/\,B_{\mathrm{eff}} - a)/b$, says when a storage tier beats recomputation. We measured its inputs with vLLM for an 8B model on H100, A100, and L40 GPUs, and for a 72B model on four H100S GPUs, across five kinds of storage paths from seven clients on three clusters. The binding quantity is usually the client's network link, not the storage system: tiers cap at the link (1.2\,GB/s on 10\,GbE nodes, 3.0\,GB/s on 25\,GbE). At measured prefill costs, an L40 breaks even against every mount we measured; an A100 against a 10\,GbE NFS mount at 34K tokens; and an H100 against a 25\,GbE mount at 32K tokens, or a node-local NVMe at every length. The 72B model prefills $6.8\times$ slower than the 8B model because tensor parallelism over PCIe returns only a third of the four GPUs. It therefore needs only 1.1\,GB/s, and a 1.3\,GB/s NFS mount beats recomputing it at every length. Re-running the policy comparison with the measured parameters, where prefill is 4--28$\times$ costlier per token than the assumed reference set, removes the learned policy's advantage (0-3%). With a 1\,s host-memory round trip against a 9-32s re-prefill, the decision points move into the tails, where the predictor has no skill. Our analysis identifies this as the regime where prediction has the least to decide, and the advantage returns (10%) only when host memory becomes expensive. Because the policy consumes only the predicted tier, the measurements turn into targets: a predictor must flag the long tool calls that a regression on gap length misses, and a link must deliver 2.5\,GB/s to an H100 for storage to pay. We release the harness, simulator, and predictor as a testbed for both.

### 46. Positional Inference for Stronger Attacks on Language Models

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 论文特定依据：论文优化 adversarial token 的 prefix/infix/suffix 位置，并转移 position posterior；优化对象是攻击 prompt 的 token placement。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=uh7b7doBNd
- 官方摘要证据：Optimization-based adversarial attacks on large language models (LLMs) perform coordinate descent over a fixed set of token positions. While seminal works focus exclusively on suffix-based attacks, recent studies suggest that inserting tokens into alternate positions (prefix and infix) can achieve higher attack success rates (ASR). Although methods that move beyond suffixes often improve ASR, their position selection usually relies on architecture-dependent heuristics. We cast position selection as Bayesian inference: intermediate optimizer evaluations that existing attacks discard serve as observations about which positions are worth attacking, and existing heuristics can be formulated as prior beliefs about impactful positions. Because the resulting posteriors are Gaussian, beliefs inferred from individual attacks can be merged in closed form, so computation spent attacking one model becomes a positional prior for attacking another. Across 12 LLMs ranging from 0.6B to 32B parameters, and despite the exploration cost of jointly inferring positions and optimizing tokens, our attack improves mean ASR by 11.1 percentage points over suffix-based GCG and 3.6 points over attention-guided SlotGCG. The inferred posteriors reveal that vulnerability concentrates at both ends of the prompt, reconciling conflicting reports that favor suffixes or prefixes, yet correlates only weakly with the attention signal current heuristics rely on. Most interestingly, we find that positional knowledge transfers: in leave-one-model-out experiments, using posteriors merged from the other 11 models as a prior improves a gradient-free attack on the held-out model by 9–11 points over suffix placement and 6–7 points over transferred attention heuristics, matching suffix-only ASR with roughly a quarter of the query budget. Our results suggest that where to attack is learnable, transferable, and enables an important form of adaptive attacks for language models.

### 47. P$^2$O: Joint Policy and Prompt Optimization

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 论文特定依据：P²O 明确交替进行 prompt evolution 与 policy update，GEPA 搜索 reasoning prompts；提示词优化是核心组成。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=XywNH2Ca3U
- 官方摘要证据：Reinforcement Learning with Verifiable Rewards (RLVR) enhances Large Language Model (LLM) reasoning but is suffer from advantage collapse: when all rollouts of a query receive identical rewards, the group variance vanishes, most damagingly on hard samples, where scaling rollout budgets yields little. We introduce Joint Policy and Prompt Optimization (P$^2$O) to mitigate this collapse by alternating continuous policy updates with discrete prompt evolution. P$^2$O mines hard samples with a success-rate threshold, evolves reasoning prompts for them with GEPA, and internalizes the elicited trajectories via context distillation, which optimizes each trajectory under the original query and thus removes inference-time prompting, with a Context Ratio Mask (CRM) filtering out extreme likelihood ratios. P$^2$O restores critical advantage signals and surpasses the GRPO baseline by up to 8.2 points in average accuracy on six held-out benchmarks across all training datasets and backbones, while also outperforming DAPO and other baselines. The gains are especially pronounced on hard benchmarks, reaching up to 16.3 points above GRPO on average across AIME24 and AIME25. Our findings expose the limits of standard exploration in sparse-reward environments, illuminating the potential of unifying evolutionary algorithms with reinforcement learning. This integration of discrete semantic search and continuous parameter updates provides a self-reinforcing framework that facilitates more effective LLM alignment.

### 48. Off-Diagonal Hessian Sensitivity for Post-Training Quantization of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：ODES 从 task-loss Hessian 的 off-diagonal interaction 推导 projection-pair precision reallocation 排名，用 compressed probe-centered estimator 在 LLM 规模估计该敏感度，再把 mixed-precision bit allocation 缩减为对重分配 pair 数的一维候选搜索。
- 模型参数/组件边界：全精度模型权重：摘要未提出训练；持久模型表示：projection-pair bit allocation 与由 RTN/HQQ/GPTQ 实例化的量化权重。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=nYra38pdbe
- 官方摘要证据：Mixed-precision post-training quantization (MP-PTQ) is a promising approach for improving resource efficiency under constrained computational and memory budgets through effective bit allocation.
MP-PTQ methods based on independently optimized layer-wise or module-wise surrogate objectives are computationally efficient, but primarily rely on local quantization errors and therefore do not explicitly account for cross-layer interactions under the task loss.
In contrast, search-based methods treat mixed-precision allocation as a black-box optimization problem, leading to costly exploration of a large search space.
To address these limitations, we propose Off-Diagonal Energy Sensitivity (ODES), which captures interactions within and across projections through the off-diagonal structure of the task-loss Hessian.
Starting from a second-order expansion of the task loss, we separate its off-diagonal interaction term. Then, we derive a sufficient condition under which ODES-guided precision reallocation reduces the second moment of the off-diagonal task-loss contribution. To estimate ODES at LLM scale without materializing the Hessian, we develop a compressed probe-centered (CPC) estimator. CPC reduced estimator state memory by approximately \(126\times\) while producing ODES estimates that closely matched those obtained with the direct Welford estimator.
Using the estimated ODES ranking, we reduce mixed-precision bit allocation to a one-dimensional search over the number of reallocated projection pairs and evaluate these candidates using HQQ as a lightweight quantization proxy. This reduced the total allocation time by 36--50\% relative to search-based methods while maintaining comparable performance in downstream accuracy and perplexity. ODES-guided allocations also improved over uniform allocation with RTN, HQQ, and GPTQ, indicating that the ODES ranking transfers across different quantizers.

### 49. MIMUS: Post-Hoc Refinement of Frozen Rewards via Residual Evolution

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：以 CMA-ES 演化零初始化的低秩奖励残差，并用候选奖励下训练策略的表现计算适应度。
- 模型参数/组件边界：base reward 冻结；low-rank reward residual 持久演化；候选/最终 policy 的持久与训练细节待核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=Kra8djk0Ys
- 官方摘要证据：Reinforcement learning systems often rely on rewards that are costly to redesign and may not fully capture task objectives. Inspired by inheritance and variation in natural evolution, we introduce MIMUS, a post-hoc reward refinement framework that freezes an existing base reward and evolves a compact, low-rank additive neural residual. The residual is initialized to output zero, ensuring that evolution starts exactly from the base reward. Before evolution, a Signal Gate checks whether candidate reward comparisons reveal a reliable optimization signal amid policy-training noise. The residual is subsequently evolved using Covariance Matrix Adaptation Evolution Strategy (CMA-ES), guided by teaching fitness computed from the native returns or task-aligned metrics of policies trained under candidate rewards. This approach enables reward optimization without residual supervision or differentiation through policy training. Beyond the evolutionary search, long-horizon audits guide reward selection for final policy training. We evaluate MIMUS on four tasks in Gymnax and MJX with handcrafted, LLM-generated, and learned neural base rewards. Across these tasks and reward sources, MIMUS improves downstream policy performance while leaving the base rewards unchanged, demonstrating that residual evolution offers a practical complement to reward design.

### 50. Large Language Models as Generative Bayesian Policies

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：该稿以 LLM embedding 上 deep-kernel-learned Gaussian-process critic 的 acquisition function 生成 preference signal，再对 LLM actor 做 preference fine-tuning，使其生成分布逐轮向高效用科学候选移动并摊销 BO acquisition search。
- 模型参数/组件边界：GP critic 与 LLM actor 均存在训练后的持久状态；actor 具体全参/参数高效微调范围待核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=fbzXTjTZ9x
- 官方摘要证据：Bayesian optimization is the dominant framework for sample-efficient scientific discovery, providing principled uncertainty estimates that guide expensive experiments. However, its reliance on hand-crafted, domain-specific representations limits broad applicability. Large language models (LLMs) offer flexibility as many experimental setups can be described in text, but they lack the calibrated uncertainty required in high-stakes scientific applications. Here we ask whether Bayesian optimization can supply the training signal for preference-based LLM alignment. We train a Gaussian process critic through deep kernel learning on the LLM's own embeddings. The same critic's acquisition function then provides a preference signal that trains the LLM to act as a generative Bayesian policy: candidates favored by the acquisition function become "preferred" completions for preference-based finetuning. The actor learns to generate high-utility candidates directly, thereby amortizing the acquisition search of standard Bayesian optimization into the language model itself. We evaluate on three scientific optimization benchmarks spanning reaction optimization, molecular and peptide design under a budget of ~100 experiments. The actor's generation distribution shifts progressively toward higher-utility regions across iterations, and the trained model outperforms feature-based Bayesian optimization, LLM-guided optimization, and their union at different levels of integration. These results suggest that calibrated uncertainty can be the training signal that aligns language models with the decision-making demands of experimental discovery.

### 51. Explicit Trajectory Diversity for RL-Based Post-Training of LLM Agents

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：TJPO 在 single-policy group-based RL 中以 trajectory-level signals 直接优化智能体 policy。
- 模型参数/组件边界：单一 LLM agent policy 经 group-based RL 持久更新；trajectory descriptors 是用户指定的行为表示，不是被训练的模型。
- 训练算法：TJPO 在 single-policy group-based RL 中以 trajectory-level signals 直接优化智能体 policy。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=WDqlWS75gR
- 官方摘要证据：Large language model (LLM) agents often admit multiple high-quality solutions to the same task, differing in reasoning structure, tool-use pattern, or interaction trajectory. Yet existing notions of diversity in LLM post-training are mostly implicit, arising from general stochasticity and regularization mechanisms rather than explicitly targeting task-relevant behavioral variation. While such implicit diversity can be useful, it does not directly specify which forms of behavioral variation should be encouraged for a given task. In this work, we study explicit trajectory diversity in RL-based post-training for LLMs. Our key idea is to define diversity through user-specified, task-specific trajectory descriptors, which map each sampled trajectory to an interpretable behavioral representation, and then measure diversity as a set-level functional over the resulting descriptor matrix. Building on this formulation, we introduce Trajectory-guided Joint Policy Optimization (TJPO), a single-policy framework that optimizes explicit diversity over sampled trajectory groups, avoiding the need for population-based policy training, and instantiate it within group-based policy optimization through trajectory-level learning signals. This design makes the diversity objective both interpretable and controllable: practitioners can specify whether diversity should correspond to action composition, location visitation, spatial coverage, or other task-relevant behavioral dimensions. Experiments across different environments, including Sokoban and agentic tasks, show that TJPO consistently improves explicit diversity over strong group-based RL baselines while maintaining strong task performance. Further analysis shows that different descriptors induce different forms of behavioral variation, confirming that the learned diversity is aligned with the intended task-specific definition rather than generic randomness. These results suggest that explicit, task-aligned diversity can be effectively optimized in a unified RL framework for LLMs.

### 52. EvoComp-2: Learning to Compress Audio-Video Tokens for Omnimodal Large Language Models via Topic-Guided Evolutionary Labeling

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：通过主题引导的时间聚类和进化式 token 保留标注构造监督，再训练压缩器学习时间区域与模态的重要性。
- 模型参数/组件边界：压缩器参数被持久训练；进化生成的 token-retention 与 modality-importance 标签为训练工件。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=ZPkgIda8N5
- 官方摘要证据：Omnimodal Large Language Models (OmniLLMs) achieve strong performance on audio-video tasks but incur substantial computational overhead due to the large number of audio and video tokens. EvoComp proposes to adopt evolutionary search to construct token-retention supervision and train a lightweight compressor for visual token compression. In this work, we extend EvoComp to OmniLLMs and propose EvoComp-2 for efficient audio-video token compression. Extending EvoComp from static visual inputs to synchronized audio-video sequences introduces new challenges arising from temporal redundancy and query-dependent modality importance. To address them, EvoComp-2 introduces topic-guided temporal clustering that  adapts a topic model to video frames and partitions audio-video sequences into semantically coherent intervals before evolutionary labeling, enabling more structured and efficient token selection. We further construct modality-level importance supervision to capture the relative contribution of audio and video to different queries. For compressor training, we introduce a temporal-window reweighting loss to emphasize information-rich temporal regions and a modality-level importance loss to learn query-dependent modality preference, together with the GHM loss inherited from EvoComp. Extensive experiments demonstrate that EvoComp-2 achieves favorable accuracy-efficiency trade-offs. On WorldSense, EvoComp-2 preserves 98.7\% of the original accuracy while retaining only 35\% of the audio-video tokens. In terms of inference efficiency, it achieves a 1.6x end-to-end speedup on DailyOmni with 3.3x token compression.

### 53. EviGate: Evidence-Gated Inheritance for Self-Evolving Program-Repair Agents

- 决定：`defer_agent_training_unverified`
- 原分类：`related_hybrid`
- 论文特定依据：摘要只称存在 parameter adaptation 和 parameter children，但没有说明参数属于 LLM、adapter、神经 policy/controller，还是程序/外部配置；在参数类型确认前暂缓。
- 模型参数/组件边界：已确认：门控继承 parameter children；待核实：参数表示、训练算法及是否为智能体模型参数。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=gU0o6s2tHP
- 官方摘要证据：Large language model agents can generate patches, execute tests, and reuse repair trajectories, making program repair a natural setting for studying agents that adapt from their own interaction histories. Yet passing the evidence available on one task does not establish a reliable improvement: additional rollouts help only when their outcomes can be selected correctly, while local lessons may overfit visible tests and cause regressions when inherited through memory or parameters. We introduce EviGate, an evidence-gated inheritance framework that treats self-evolution as a sequence of separately authorized state transitions. EviGate combines execution-grounded candidate selection, staged experience consolidation, and parameter adaptation whose proposed children are retained only after promotion, regression, and safety checks, with append-only lineage connecting every decision. On 100 seeds and 17 fixed EvoCodeGym tasks, uninformed three-candidate sampling adds only $+0.39/75$ private cases, whereas executable selection gains $+11.05$ (seed$\times$task 95\% CI $[7.22,15.22]$). Memory, parameter, fresh-task, and repository-level evaluations further expose negative transfer and weak proposal coverage, establishing EviGate as an auditable inheritance protocol and empirical boundary map rather than a demonstration of repeated capability growth.

### 54. DIA-GRPO: Guiding Policy Optimization with Cross-Prompt Diagnosis

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：把跨提示能力诊断转为响应级 advantage，并与原生 GRPO advantage 混合用于策略更新。
- 模型参数/组件边界：LLM policy 参数持久更新；诊断状态持久性待核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=lXuaseCyXd
- 官方摘要证据：Group Relative Policy Optimization (GRPO) improves reasoning in large language models through efficient, group-based reinforcement learning. However, its prompt-local advantage construction leaves a key source of learning information untapped: how successes and failures across prompts jointly reveal the model's evolving capabilities and inform how individual outcomes should contribute to its overall improvement. To address this limitation, we introduce Diagnosis-Informed Advantage for GRPO (DIA-GRPO), which translates diagnosis of the LLM's evolving capabilities into training feedback. By jointly modeling training-sample attributes and the LLM's evolving capabilities, DIA-GRPO translates cross-prompt observations and a population improvement objective into response-level advantages. Specifically, DIA-GRPO evaluates each outcome against the model's expected performance and uses the overall improvement objective to determine how that outcome contributes to policy updates. DIA-GRPO is lightweight and plug-and-play: online diagnosis operates in a low-dimensional capability space, and the resulting advantages are mixed with native GRPO advantages within the existing policy optimization objective, requiring no additional verifier or policy-scale critic. Theoretically, under explicit local conditions, we show that the expected unclipped diagnostic update recovers the policy gradient of a population log-success objective. Experiments on mathematical reasoning show that DIA-GRPO improves overall mean correctness by 2.96 and 2.05 percentage points on Qwen3-1.7B and Qwen3-8B, respectively. The diagnostic module also delivers consistent gains across different policy optimization methods with less than 2\% additional training time.

### 55. DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 论文特定依据：DARWIN-Attack 以遗传变异、选择和组合持续优化 jailbreak attack strategies/prompt variants；虽训练 guardrail，仍属提示词/越狱提示搜索核心。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=UmzQqgrCPV
- 官方摘要证据：Most existing LLM safety evaluation and defense methods follow a static formulation: jailbreak vulnerabilities are evaluated with fixed attack methods, and guardrails are trained on fixed malicious prompt datasets. However, real-world adversaries continuously evolve their attack capabilities and expand the attack space.
To address this challenge, we propose DARWIN, an evolutionary attack-defense framework that formulates jailbreaking as a continual evolutionary process and continuously updates guardrails through an attack-defense loop.
We propose DARWIN-Attack as an evolutionary adversary that expands its attack capabilities through strategy discovery, mutation, and selection.
DARWIN-Attack discovers new attack strategies from broad external sources, generates new variants through self-reflection and genetic evolution, and filters effective strategies according to their performance against aligned LLMs.
During the attack execution phase, DARWIN-Attack adaptively selects and composes evolved strategies according to feedback from target LLMs and guardrails.
Through continuous evolution, DARWIN-Attack achieves state-of-the-art attack success rates against frontier LLMs and guardrails,
e.g., nearly 100\% on DeepSeek-V4-Pro, over 90\% on GPT-5.5 and nearly 100\% on YuFeng-XGuard, outperforming recent evolving frameworks such as LSA and MAGIC.
The continued evolution of DARWIN-Attack exposes new safety vulnerabilities and requires timely corresponding updates to safety defenses.
Therefore, on the defense side, we introduce DARWIN-Guard, an online adversarial guardrail training paradigm, which iteratively trains the guardrail on the emerging adversarial samples generated by DARWIN-Attack.
To improve robustness without sacrificing utility, DARWIN-Guard jointly learns from malicious and benign disguised queries, encouraging the guardrail to recognize underlying intent rather than superficial attack patterns.
Through continuous evolution, DARWIN-Guard achieves an average unsafe recall of 95.0\% across multiple safety evaluation benchmarks, outperforming recent advanced guardrails such as YuFeng and Nemotron.
Meanwhile, DARWIN-Guard maintains an average benign pass rate of nearly 100\% on standard benign benchmarks and achieves the best performance on over-refusal benchmarks.
Our code and model are available at https://anonymous.4open.science/r/DARWIN-D8A6.

### 56. CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：CoHARL 明确在 harness population 上用 population-based RL 训练 shared policy。
- 模型参数/组件边界：shared LLM policy 由 RL 持久更新；harness proposer 修订代码，proposer 自身是否训练待核实。
- 训练算法：CoHARL 明确在 harness population 上用 population-based RL 训练 shared policy。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=Iiw1WtkMkZ
- 官方摘要证据：Large language model (LLM) agents interact with their environments
through executable harnesses that govern tool use and feedback.
Optimizing a harness for a fixed policy overlooks how its behavior
changes during learning, while training a policy under a fixed harness
leaves the interface that generates its training experience unchanged.
This motivates adapting the harness throughout policy training.
We introduce CoHARL, a population-based reinforcement learning framework
that co-evolves a shared policy and a population of executable harnesses.
The policy learns from rollouts across the population, and a proposer
uses its execution traces to revise harness code during training.
CoHARL achieves a 27.6\% mean resolved rate on SWE-rebench, improving
over harness-only search by 6.4 percentage points. Experiments on
SWE-bench Verified and Terminal-Bench~2.0 show gains in software
engineering and terminal-based tasks. Under matched training budgets,
CoHARL also outperforms searching for a harness once before RL and
alternating policy updates with revisions to a single active harness.

### 57. CoDeL: Co-Evolutionary Defense against Indirect Prompt Injection in LLM-based Agents

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 论文特定依据：CoDeL 的 co-evolving prober 搜索 injection rounds、attack methods 与 payloads，核心是 indirect prompt injection；LoRA-GDPO defender 训练不解除提示词暂缓规则。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=ywkbERYvpx
- 官方摘要证据：Large language model (LLM)-based agents increasingly rely on external tools and content, exposing them to indirect prompt injection (IPI). This threat has motivated a wide range of defenses, among which training-based defenses are often regarded as most reliable. However, existing training-based defenses are typically optimized on a static distribution of explicit injections. They learn surface-form cues rather than the boundary between serving the user and obeying an injected objective, and therefore fail when malicious intent is folded into a plausible workflow and deferred for several turns. We present CoDeL, a defense that hardens agent against an attack distribution it reshapes as it trains. The defender is updated each round via LoRA-based GDPO under a decoupled reward over safety, task progress, and format compliance, so refusing injections and completing the user's task jointly define fitness. To keep supplying it with the failures worth learning from, a co-evolving prober searches over injection rounds, attack methods, and payloads for injections that still penetrate the current defender, guided jointly by attack success and attack latency so that it preferentially mines breaches the defender notices too late. Each defender update invalidates part of the attack population and forces the next round onto a new frontier, turning the defender's own failures into a moving curriculum. Extensive experiments on three IPI benchmarks, nine baselines, and two base models show that CoDeL reduces attack success rate (ASR) by 88.5% and outperforms other baselines largely (+38.0%). Codes are available.

### 58. Breaking the Pseudo-Multi-Agent Illusion: A Parasite–Immune Multi-Agent Trading Framework

- 决定：`defer_agent_training_unverified`
- 原分类：`related_hybrid`
- 论文特定依据：PI-MAT 以固定视角的 LLM alpha agents 生成信号，并称在线反馈驱动的 meta-learning arbiter 调整信号和资金；摘要未说明 arbiter 是否为可训练参数模型。
- 模型参数/组件边界：未证实语言智能体模型、策略模型或适配器参数被训练/持久更新；也不能反向断言完全不训练，故转入训练证据待核实。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=xiaccTalhi
- 官方摘要证据：Large language model (LLM) based multi-agent systems offer a new paradigm for collaborative decision-making in complex financial environments. However, existing systems often exhibit a ''pseudo-multi-agent illusion'': despite differing role labels, prompts, or names, agents rely on nearly identical information perspectives and produce highly correlated strategies. To address this issue, we propose a parasite-immune multi-agent trading (PI-MAT) framework. PI-MAT organizes trend-following, mean-reversion, and event-driven alpha agents into a heterogeneous cognitive ecosystem. Agents generate complementary signals from dedicated information perspectives, while parasitic replication, controlled mutation, and symbiotic complementarity expand strategic diversity. An online-performance-feedback-driven meta-learning arbiter forms the framework's cognitive immune layer, dynamically suppressing low-quality signals and reallocating capital to enable adaptive strategy integration in non-stationary markets. In a preregistered out-of-sample evaluation covering 2020--2023, PI-MAT achieved an annualized net return of \(18.72\%\), a Sharpe ratio of \(0.729\), and a maximum drawdown of \(28.61\%\). Relative to a price-only baseline, PI-MAT improved annualized net returns by \(3.52\) percentage points, with a paired \(95\%\) confidence interval of \([0.51, 6.89]\) percentage points. The code for PI-MAT is publicly available at https://github.com/cxw0928/parasite-immune-framework-corecode.

### 59. AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Harness

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：AIProver 明确 jointly post-trains a 119B open-weight language model，并交替进行模型 fine-tuning/RL 与 HarnessEvolve。
- 模型参数/组件边界：119B 模型参数通过 fine-tuning 和 alternating RL 持久更新；harness control flow 另由证书驱动进化搜索。具体反传实现待核实。
- 训练算法：AIProver 明确 jointly post-trains a 119B open-weight language model，并交替进行模型 fine-tuning/RL 与 HarnessEvolve。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=R9kJupcBxE
- 官方摘要证据：Proof auto-formalization translates natural-language (NL) theorems and proofs into a formal language (FL) such as Lean, enabling mechanical verification. Despite rapid progress, research-level proofs often depend on concepts missing from leading proof assistant libraries (e.g., Lean's Mathlib), and successful compilation does not guarantee that a translation preserves the theorem's meaning or the proof's reasoning. Furthermore, aligned NL-FL training data are scarce, and leading agents often rely on costly frontier models and manually engineered harnesses.

To address the above issues, we present AIProver, an agentic framework for autonomous proof auto-formalization and proof synthesis (AFPS) that jointly post-trains a 119B open-weight language model and evolves its agentic, tool-calling harness with HarnessEvolve. Verifiers assess type correctness, proof completeness, and semantic correctness, returning rewards and diagnostic certificates that drive model fine-tuning and alternating reinforcement learning via symbolic feedback and HarnessEvolve, a certificate-driven evolutionary search over the whole harness control flow that re-tailors the harness to the updated model. HarnessEvolve retains and generalizes rejected designs as negative evidence to steer later mutations away from unproductive parts of the search. For research-level training and evaluation, we introduce LoCoBench, 58.9k instances from Mathlib, CSLib, Mizar Math Library, and a bounded-arithmetic textbook, combining 18.8k labelled NL-Lean pairs and 40.1k unlabelled NL-Mizar pairs with a 771-instance validation split whose theorem-proof pairs have no public Lean formalization. Against 39 frameworks spanning AFPS agents, frontier LLMs, and coding agents, AIProver lifts pass@4 semantic correctness over its Leanstral-1.5 base from 15.7\% to 36.7\% and outperforms every other open-weight system and Aristotle. As a Claude Code and Codex skill, it lifts their semantic correctness from 41.9\% and 34.1\% to 79.8\% and 62.4\%, respectively, outperforming Numina-Lean-Agent (72.5\% and 44.5\%) and OpenGauss (54.3\% and 41.9\%) in that role. Further, it is also 24\% cheaper than Numina-Lean-Agent, pushing the accuracy-cost frontier of research-level AFPS.

### 60. $\pi$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Labeled QA Data

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：π-Play 将 QCP 转为 token-level supervision 做 self-distillation，以持续改进搜索智能体模型。
- 模型参数/组件边界：语言模型/策略通过 token-level self-distillation 持久更新；摘要未说明优化器和反向传播实现。
- 训练算法：π-Play 将 QCP 转为 token-level supervision 做 self-distillation，以持续改进搜索智能体模型。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=KOqQs63l7Q
- 官方摘要证据：Deep search agents remain difficult to train at scale due to limited labeled data and weak credit assignment in long-horizon search. Self-play offers a scalable way to reduce data dependence, but conventional approaches optimize models only with sparse outcome rewards, limiting learning efficiency. We find that the task-generation process in self-play can itself serve as a scalable source of privileged supervision for self-distillation. Specifically, self-play naturally produces a Question Construction Path (QCP), which captures the reverse solution process and provides rich intermediate signals for self-distillation without curated privileged information. Leveraging this insight, we propose Privileged Information Self-Play ($\pi$-Play), a self-evolution framework that couples self-play with self-distillation by directly exploiting privileged information generated during task construction. In $\pi$-Play, self-play generates training tasks together with QCPs for self-distillation in a low-cost and scalable manner, while self-distillation converts QCPs into token-level supervision to accelerate self-play evolution. This closed-loop interaction enables more efficient model improvement without relying on labeled QA data or curated privileged information. Across multiple benchmarks and model scales, data-free $\pi$-Play surpasses fully supervised search agents and improves evolutionary efficiency by 1.5–3.1$\times$ over conventional self-play.

### 61. $R_Q$-Evolve: LLMs Evolve Their Own Generator Programs for Self-Improvement

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：R_Q-Evolve 同时突变 generator programs，并用 group-relative RL 训练 Solver。
- 模型参数/组件边界：Solver 模型参数经 group-relative RL 持久更新；generator-program archive 经 mutation、fitness ranking 与 retention 更新。
- 训练算法：R_Q-Evolve 同时突变 generator programs，并用 group-relative RL 训练 Solver。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=B8oWwVLeGz
- 官方摘要证据：In group-relative reinforcement learning with binary verifiable rewards, all-correct or all-incorrect response groups contribute no reward-driven policy gradient. Sustained self-improvement therefore requires problem instances that continue to yield both correct and incorrect responses as the Solver changes.
We introduce \RQEvolve{}, which retains \emph{generator programs} in an archive, each representing a task family of problem instances sharing the same structure. Each iteration, the Solver reassesses retained programs on newly sampled instances and, as the Evolver, mutates them into child programs. \emph{Reasoning Quality} ($R_Q$) estimates the current usefulness of retained programs and their children by multiplying learnability, measured as verifier reward variance, by uncertainty, measured as mean token entropy. We motivate this product by deriving an upper bound on the squared norm of a centered-reward surrogate gradient in output-logit space. Fitness ranks eligible retained programs for training, while retention confines competition to cells defined by mathematical domain and output form, leaving programs in other cells available for later reassessment and mutation.
With Qwen3-4B-Base and Qwen3-8B-Base, \RQEvolve{} achieves final mathematical benchmark gains of $5.24$ and $6.12$ percentage points over the base models. Both scales reach their highest averages late in training, and the final 8B checkpoint exceeds R-Zero's peak by $1.06$ points. Classified generated instances remain broadly distributed across domains and output forms late in the 8B run.

### 62. GEAR: Co-evolving Grounded VLM Agents with Environment-Aligned Rubrics

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：GEAR 官方摘要明确 jointly optimizes a VLM policy and a rubricator，并与 RL 轨迹分布共同演化。
- 模型参数/组件边界：VLM policy 与 rubricator 均为训练组件；摘要未说明参数子集和各自是否/如何反向传播。自然语言 rubrics 是外部工件。
- 训练算法：GEAR 官方摘要明确 jointly optimizes a VLM policy and a rubricator，并与 RL 轨迹分布共同演化。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=0AdawuC1tj
- 官方摘要证据：Training multi-turn VLM agents from environment feedback remains challenging because outcome rewards indicate whether a trajectory succeeds, but provide limited supervision for why intermediate visual reasoning steps and actions succeed or fail.
Existing dense process rewards are often manually specified or fixed, which makes them difficult to adapt to the evolving trajectory distribution induced by RL.
We propose \textbf{GEAR} (\textbf{G}rounded \textbf{E}nvironment-\textbf{A}ligned \textbf{R}ubrics), a co-evolutionary training framework that jointly optimizes a VLM policy and a rubricator that self-generates grounded rubrics for spatial grounding, action legality, temporal consistency, and transition progress.
Each rubric is used as an auxiliary process reward only when its satisfaction is statistically aligned with grounded environment feedback, such as task success, return, legality, or progress, which prevents self-generated supervision from drifting toward textual self-consistency.
Experiments on multi-turn VLM agent benchmarks show that \textbf{GEAR} improves over SFT and outcome-centric RL baselines, with ablations confirming that environment-aligned rubric evolution is important for stable and interpretable policy improvement.

### 63. Heterogeneous Agentic Coevolution

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：HACE 明确以 supervised learning 改进 specialist，并以 on-policy RL 训练 LLM agent。
- 模型参数/组件边界：specialist foundation model 与 agent policy 均持久训练；interaction harness 另经 evolutionary search，具体反传路径待核实。
- 训练算法：HACE 明确以 supervised learning 改进 specialist，并以 on-policy RL 训练 LLM agent。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=E1rsriszaM
- 官方摘要证据：Recent advances in self-improving LLM agents have demonstrated the potential of AI systems that drive their own intelligence. However, many domain-specific applications rely on specialized foundation models that possess strong domain expertise but remain dependent on human-designed improvements. Extending recursive self-improvement to these models presents a key challenge: as a specialist improves, the strategies used to advance it must also adapt. To address this challenge, we propose Heterogeneous Agentic Coevolution (HACE), a framework that jointly evolves specialized foundation models and LLM agents through reciprocal learning. HACE improves the specialist through supervised learning while training the agent with on-policy reinforcement learning, guided by verified performance gains on the current specialist. The agent's exploration, in turn, informs subsequent specialist training, enabling both models to adapt to each other's progress. To sustain this reciprocal learning, HACE further employs evolutionary search to optimize their interaction harness, adapting how the models exchange information and select training experiences as their capabilities evolve. We evaluate HACE across three challenging domains: recommendation systems, protein function prediction in biology, and crystal stability prediction in material discovery. We show that HACE outperforms the evaluated self-improving methods on the primary task metrics across all three domains. These results shed light on heterogeneous coevolution as a universal approach to improving specialized foundation models through reciprocal interaction with a learning agent.

### 64. Outcome-Ranked Proposal Tuning: Training LLMs to Transfer Experience Across Bayesian Optimization Tasks

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：按初始化候选对后续贝叶斯优化的影响训练 LLM 提议模型，而非按候选自身目标值训练。
- 模型参数/组件边界：模型/策略或训练组件：摘要显示存在持久训练/部署更新；具体参数子集待核实。外部搜索工件：LLM proposal-model weights and BO initialization proposals。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=MaP2KsIEzp
- 官方摘要证据：Bayesian optimization (BO) is widely used for expensive black-box optimization.
When related optimization problems arise repeatedly, experience from previous tasks can improve optimization on new ones. We aim to train a large language model (LLM) to transfer the knowledge from the prior tasks to new ones through BO initialization.
We introduce Outcome-Ranked Proposal Tuning (ORPT), which trains an LLM to propose initialization points based on how they affect the subsequent BO process.
ORPT trains the LLM to favor initialization candidates based on their effect on subsequent BO, rather than their standalone objective values. We further mathematically show that these learned preferences are linearly connected to the expected outcome of downstream BO.
Experiments on synthetic Branin optimization and antimicrobial peptide design show that ORPT outperforms a broad range of single-task, multi-task, and LLM-based BO baselines, yielding stronger initializations and better downstream optimization.
These gains persist through subsequent BO, while ablations confirm that downstream BO outcomes provide a stronger training signal than candidate objective values alone.
Overall, our results show that learned initialization is an effective mechanism for transferring experience across related optimization tasks.

### 65. Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：PCPO 提出 parametric self-evolution，以 hybrid policy update 将自生成算法内化到 algorithm-design agent。
- 模型参数/组件边界：agent policy 参数经 PCPO 持久更新；算法 population 是外部工件。摘要未交代梯度/反传实现。
- 训练算法：PCPO 提出 parametric self-evolution，以 hybrid policy update 将自生成算法内化到 algorithm-design agent。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=Y3u3Z56znq
- 官方摘要证据：Large language models are increasingly participating in complex real-world tasks in the form of algorithm-design agents, designing and refining algorithms. Many successful algorithm-design agents adopt pure in-context evolutionary frameworks, but they may quickly plateau in domains that require specialized knowledge. Parametric adaptation offers a way to internalize specialized knowledge, but conventional training requires abundant domain-specific corpora while high-quality algorithms are scarce in complex algorithm-design scenarios. In this paper, we propose sample-efficient parametric self-evolution where agents can explore and learn from self-generated algorithms. First, we characterize in-context evolutionary stagnation and analytically propose the Improvement Chain proposition, showing how learning successive self-generated algorithms can locally increase the likelihood of neighboring algorithms. Motivated by this local-transfer perspective, we further propose Population-Curated Policy Optimization (PCPO) to utilize a global population and a hybrid policy update scheme for retaining and reusing high-quality, diverse self-generated algorithms, shifting the policy towards stronger algorithms. In the task of learning rate schedule design for global placement in electronic design automation, trained only on 4 chip cases, PCPO outperforms the state-of-the-art in-context evolutionary methods (e.g., OpenEvolve and ShinkaEvolve) on average across 16 chip cases. With an 8B-size base model, PCPO achieves competitive performance compared to frontier closed-source models such as GPT-5.5. PCPO also reduces inference-time token cost by internalizing grounded domain knowledge and prompt distillation. Moreover, PCPO achieves significant speedups on four GPU kernel designs, with an average of 8.27$\times$ speedup against the PyTorch Eager baseline. Our code is available at https://anonymous.4open.science/r/PCPO-222D/.

### 66. Meta-Rubrics: Learning to Discover Rubrics at Deployment for Efficient Task Adaptation

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：Meta-Rubrics 明确用 branched-rollout RL jointly optimizes rubric generator and LLM judge。
- 模型参数/组件边界：rubric generator 与 LLM judge 参数经 RL 持久训练；部署期自然语言 rubric/候选排序是外部状态，反传实现待核实。
- 训练算法：Meta-Rubrics 明确用 branched-rollout RL jointly optimizes rubric generator and LLM judge。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=g5tssaW2qj
- 官方摘要证据：Large language model (LLM) agents are increasingly deployed in open-ended environments where task objectives are under-specified and no task-specific evaluator is available. Reinforcement learning (RL) and inference-time search have driven major gains in verifiable domains such as math and coding, but these gains rely on a verification–generation (VG) gap: checking a solution is easier than producing one. In open-ended tasks,  however, this gap cannot be assumed, because a verifier must first infer what constitutes success. This raises a central question: can an agent can construct or widen such a gap at deployment time from a small amount of environment interaction and use this gap to aid policy adaptation? We formulate this as a reward discovery setting and propose a framework, Meta-Rubrics, which infers a reward function, represented as a natural-language rubric, which can accurately assign credit to guide policy behavior at deployment time. In this framework, a rubric generator infers task-specific evaluation criteria, and an LLM judge applies these criteria to produce scalar scores and criterion-level feedback for candidate trajectories. The generator and judge are jointly optimized with RL over branched rollouts so that induced scores recover oracle reward orderings on held-out trajectories. At deployment time, this inferred reward can rank candidate responses or supply a signal for lightweight policy optimization with RL. We evaluate Meta-Rubrics on user simulation in Human-LM and curating data for a language model for an unseen task with a fixed fine-tuning budget. In both settings, Meta-Rubrics outperforms the highest non-oracle adaptation approaches such as in-context learning, evolutionary search, and rubric-based fine-tuning baselines.

### 67. OpenMLE: Training LLMs for Evolutionary Search in Machine Learning Engineering

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：OpenMLE-Train 明确先 execution-verified SFT、再以执行奖励 RL post-train 单一模型，之后把它作为进化搜索 variation engine。
- 模型参数/组件边界：程序修订语言模型通过 SFT 和 RL 持久更新；OpenMLE-Evo 的长期 population/search state 另行更新。
- 训练算法：OpenMLE-Train 明确先 execution-verified SFT、再以执行奖励 RL post-train 单一模型，之后把它作为进化搜索 variation engine。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=nSuEq47kb9
- 官方摘要证据：Large language models have progressed from conversational assistants to reasoners
and autonomous agents, and are now entering a stage in which they contribute
to discovery itself, including the development of AI: AI that trains AI. Frontier
labs have begun pursuing automated AI research, yet the open community lacks
the training data and testbeds needed to study it: existing machine learning en-
gineering (MLE) resources contain at most a few hundred tasks and are built for
evaluation rather than training. We present OpenMLE, an open full-stack frame-
work for AI-train-AI in executable MLE. First, OpenMLE-Gym provides, to
our knowledge, the first large-scale AI-train-AI testbed: 5,758 quality-gated exe-
cutable tasks spanning broad machine learning problems, with isolated execution,
task-specific evaluators, and verified evolutionary trajectories. Second, OpenMLE-Train post-trains a single model for the discovery loop, where an agent repeatedly
drafts, improves, debugs, and recombines solutions under delayed, noisy feedback:
execution-verified SFT, then RL on per-task calibrated execution rewards, teaches it
to serve as the shared program-revision operators. Third, OpenMLE-Evo deploys
the trained model as the variation engine of long-horizon evolutionary search. On
MLE-Bench Lite, post-training Qwen3.6-35B-A3B into OpenMLE-35B raises
Medal Average from 39.39% to 60.61% with the harness fixed. With the model
fixed, OpenMLE-EVO raises it from 53.03% under original AIRA-Evo to 60.61%.
Adding benchmark-disjoint experience priors and asynchronous parallel search to
OpenMLE-EVO, at the same total sandbox budget, brings the system to 71.21%
with 3B active parameters, on par with GPT-5.5 with Codex (68.18%) under the
same budget. Results on held-out NatureBench Lite show transfer to scientific
reproduction tasks.

### 68. EdgeEdit: An Edge-Oriented Multimodal Knowledge Editing Framework for On-Device MLLMs

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：EdgeEdit 用零阶敏感度和动态规划配置端侧混合精度量化，并以显著性引导的视觉 token 裁剪保留编辑证据。
- 模型参数/组件边界：混合精度量化产生持久部署配置/模型表示；摘要未说明通过训练更新原始 MLLM 权重
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=szkL8iUTnD
- 官方摘要证据：On-device multimodal large language models (MLLMs) are increasingly enabling multimodal applications, yet updating their static encoded knowledge efficiently remains a critical challenge. In-context editing (ICE) provides an efficient and lightweight approach for fine-grained knowledge updates. However, on-device deployment typically demands joint model and input compression, introducing severe obstacles for ICE: model quantization impairs the model’s ability to utilize contextualized edited knowledge, while edit-agnostic token reduction inadvertently discards edit-critical visual evidence. To address these challenges, we propose EdgeEdit, an edge-oriented multimodal knowledge editing framework that coordinates offline model deployment with online inference. Specifically, EdgeEdit introduces Edit-Aware Mixed-Precision Quantization for offline model deployment, which conducts zeroth-order sensitivity profiling and budget-constrained dynamic programming to preserve contextualized edited knowledge utilization. For online inference, EdgeEdit employs EvidenceSaliency Guided Token Reduction, combining cross-modal saliency attribution with semantic relevance to progressively remove redundant visual tokens while retaining edit-critical visual evidence. Extensive experiments demonstrate that EdgeEdit maintains competitive editing performance while substantially reducing system costs. Compared with the strongest competing baseline for each efficiency metric, EdgeEdit achieves average reduction factors of 2.9×/1.5×/2.5× in memory usage, editing latency, and energy consumption on the server, and 2.0×/2.2×/2.0× on mobile devices, respectively.

### 69. HarnessNet: From Engineered Harnesses to a Unified Neural Controller for Self-Evolving Agents

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：HarnessNet 保持 LLM 冻结，但明确训练持久 neural feedback controller：先模仿 engineered harness，再按同任务多次尝试结果改进。
- 模型参数/组件边界：LLM 权重冻结；作为智能体执行策略的 HarnessNet 神经控制器参数持久训练，且不穿过 LLM/环境求梯度。第二阶段优化细节待正文核实。
- 训练算法：HarnessNet 保持 LLM 冻结，但明确训练持久 neural feedback controller：先模仿 engineered harness，再按同任务多次尝试结果改进。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=cFcaAi8dtG
- 官方摘要证据：An LLM agent is shaped not only by its language model, but also by the harness that runs it: the control logic that decides what context the model sees, which proposed commands are executed, when to call the model again, and when to stop. These decisions are central to long-horizon agent performance, yet existing harnesses are typically hand-engineered or obtained through search over harness programs, and remain fixed after deployment. We introduce HarnessNet, a neural feedback controller that learns the harness while keeping the LLM frozen. At each step, HarnessNet reads the interaction history and emits one executable control: request the LLM, execute a previously proposed command, read an environment output, or finish. Controls can reference earlier replies or observations instead of regenerating them, allowing long outputs to be reused exactly. The controller is first trained to imitate an engineered harness, then improved from task success by comparing multiple attempts on the same task, without gradients through the LLM or environment. On AppWorld, HarnessNet matches and then surpasses engineered control. Imitation alone reaches 86.0% success on all 57 development tasks, matching the Meta-Harness baseline under the same budgets. Two reward-driven updates from only 48 training attempts raise success to 91.2%, outperforming both the imitation controller in the same evaluation and the engineered harness. The newly solved tasks mainly come from cases where imitation previously produced invalid controls or exhausted its interaction budget, showing that learning improves how the agent is run rather than the frozen LLM itself.

### 70. When Can First-Order Models of Fine-Tuning Bound Forgetting?

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：有限差分探针拟合响应 surrogate，为本身采用一阶 SGD 的 LoRA 微调遗忘提供概率界。
- 模型参数/组件边界：SGD 会持久更新 LoRA；response coefficients 和界是诊断产物，不是模型更新。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=pOcuwMjDc0
- 官方摘要证据：Fine-tuning a language model on new data can make it forget facts that it should keep. We ask whether measurements taken at the start of a fine-tuning run can bound, for each protected fact, the probability that the run makes the model forget it. In LoRA fine-tuning with stochastic gradient descent on models from 0.6B to 14B parameters, a first-order response model estimated by finite-difference probes predicts changes of per-fact margins with correlation 0.974–0.998. Predictions of forgetting built on this model nevertheless failed; in Qwen3-0.6B, forgetting requires parameter changes far outside the region in which the model was validated. The probes can, however, bound the probability that a margin first falls below a boundary near zero: we derive Freedman and Azuma first-passage bounds for a linear surrogate of the margin and test on new runs whether they hold for the model. The bounds contain a term R that measures how much the response coefficients change during the run. The simplified Freedman bound, which sets R = 0, certified most facts but was violated in 14 of 112 conditions, and in these conditions every fact on which it was violated had R ≥ a, where a is the distance of the fact's margin to the boundary. The complete Freedman bound certifies only facts with R < a, and it held in every condition. On the violated facts, the spread of the margin across test runs was a median of 14.6 times the prediction of the response model, so the failures are breakdowns of the model, and in our data they occurred only where R ≥ a. We found this pattern post hoc and tested it in two preregistered confirmatory studies with 43 new conditions: the complete bound held in all of them, and the simplified bound failed there on only 3 facts, each with R ≥ a. A screen that decided for a whole condition whether to use the simplified bound failed on new starting states. First-order models of fine-tuning can thus bound forgetting on the facts whose response coefficients change by less than their distance to the boundary.

### 71. Don't Retrain, Remix: Adaptation of Web Agents using Mixture Hypernetworks

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 论文特定依据：WebMix 用预训练 LoRA bank 与 router 在部署时合成为新 adapter；虽无目标域梯度更新，但明确形成用于智能体推理的新模型适配参数。
- 模型参数/组件边界：源 LoRA 与 router 预先训练；目标域以一次 router 前向持久合成/配置新 adapter，基础模型不做目标域反向传播。
- 训练算法：WebMix 用预训练 LoRA bank 与 router 在部署时合成为新 adapter；虽无目标域梯度更新，但明确形成用于智能体推理的新模型适配参数。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=Eq74LwgkjR
- 官方摘要证据：The web is not static or uniform. Websites that serve the same purpose can look and navigate very differently. Even within a single site, successive redesigns can change how familiar features are presented and accessed. Humans adapt to this by recognizing familiar interaction patterns and reusing what they already know. We give web agents a similar ability with WebMix, a mixture hypernetwork that adapts them to unseen interfaces by composing previously trained low-rank adapters. WebMix begins with a bank of adapters trained on source interfaces. At deployment, a scout agent explores the target interface and summarizes its observations into a compact manual. A lightweight router uses this manual to predict mixing coefficients over the adapter bank, which combine the existing adapters into a new one for inference. Adapting to a new interface takes only a scouting run and a forward pass, without gradient updates on the target. With Qwen and Llama models, we evaluate *domain transfer* on TimeWarp and WebArena-Lite-v2, and *version transfer* on TimeWarp. In all three settings, WebMix matches or outperforms in-context learning and LoRA baselines, often matching the average success of specialists trained directly on those interfaces. On TimeWarp domain transfer, it gains about 8 percentage points on average over the best baseline with both models. These gains do not come at the cost of seen interfaces, where WebMix keeps its lead, and extend to version transfer. Adapting to a new interface can therefore rely on exploration and composition instead of retraining.

### 72. Eliciting Model Behaviors by Optimizing the Latent Posterior

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 论文特定依据：Posterior Prefix Tuning 优化 hard-prompt 分布以诱导模型行为，优化对象明确是 prompt。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=hw82nCsx4L
- 官方摘要证据：In the \emph{latent posterior model} of transformer behavior, the next-token distribution arises from a posterior over latent predictive models conditioned on the context, mixed to generate continuations. We exploit this model in settings where it is exact, namely Bayes-filtered transformers (BFTs) meta-trained on sequences from a hierarchical prior, to introduce \textbf{Posterior Prefix Tuning (PPT)}, a new method for \emph{eliciting} behavior from a transformer: given a utility function on continuations, find a prompt under which the model's expected utility is large. For a BFT, the elicitation objective factors through the latent posterior, and we show that the gradient of a tilted surrogate is a covariance over the tilted posterior between the per-model utility and the score of the tilt. PPT optimizes the parameters of a distribution over hard prompts, drawing latent-model samples once from the BFT's prior via predictive Monte Carlo (PMC) and computing its gradient by importance sampling. The inner loop performs no transformer forwards and no backpropagation through the model, and the prior samples are utility-independent, so the cost of characterizing the BFT amortizes across utilities. We validate PPT and a Rao--Blackwellized variant on Beta--Bernoulli and reinforced urn BFTs across three utility families (reverse cross-entropy, frequency matching, Dyck validity).

### 73. HO-FL: Hybrid-Order Federated Learning for Heterogeneous Edge Devices

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 论文特定依据：不属于提示词核心或需按智能体参数规则移出的研究：提出 HO-FL：各客户端按内存预算选择模型分段边界，用 ZO 训练底段、FO 训练顶段，并针对不同边界带来的更新质量与数据代表性权衡设计客户端采样近似；摘要报告了语言任务实验。
- 模型参数/组件边界：持久更新全局模型权重，且各客户端本地多步更新后参与聚合；order boundary 可按设备内存选择。
- 训练算法：不适用或原始来源未说明。
- 反向传播：原始来源未进一步说明。
- 待核实：无本次范围相关未决事项。
- 原始来源：https://openreview.net/forum?id=iVQu1sp529
- 官方摘要证据：Federated learning (FL) on memory-constrained edge devices faces a dilemma: first-order (FO) optimization (i.e., backpropagation) demands substantial memory, whereas zeroth-order (ZO) optimization suffers from severe convergence slowdown. To resolve this dilemma, we introduce HO-FL, a hybrid-order FL framework that trains a model's bottom segment with ZO optimization and its top segment with FO optimization. Each device can flexibly select its order boundary according to its memory budget while participating in the training of the same global model. Moreover, our convergence analysis reveals a new, fundamental trade-off: clients with larger FO-trained segments can provide more accurate updates, but favoring them can underrepresent other clients' data. We connect this trade-off to the bias and variance of actual multi-step local updates, yielding a sampling optimization problem and a practical dimension-aware approximation with direct model averaging. Experiments on language tasks examine task performance, client memory, and sampling under data heterogeneity. The results show that hybrid-order local training can retain much of the full-FO performance with substantially lower client memory requirements. Our code is available at https://anonymous.4open.science/r/ICLR-HO-FL/.
