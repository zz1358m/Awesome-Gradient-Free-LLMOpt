# 面向大语言模型的无梯度优化论文精选

[English](README.md) | [简体中文](README_zh.md)

本仓库精选使用 **进化策略（Evolution Strategies, ES）** 与 **零阶优化（Zeroth-Order Optimization, ZO）**，在不对任务目标进行反向传播的情况下优化大语言模型参数的研究。

本列表关注持久化模型参数，包括完整权重、适配器、低秩子空间和量化权重；有意排除提示词演化、思维链搜索、候选答案演化以及其他仅优化模型外部对象的方法。

**最近一次文献核查：** 2026-09-01

**发表信息约定：** ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) 表示已经确认的会议或期刊发表信息。尚未核实正式发表去向的预印本不添加徽标。

## 目录

- [ES 与 ZO 的使用方式不同](#es-与-zo-的使用方式不同)
- [进化策略](#进化策略)
  - [预训练](#预训练)
  - [单轮推理与对齐](#单轮推理与对齐)
  - [多轮与智能体推理](#多轮与智能体推理)
  - [理解 ES](#理解-es)
- [零阶优化](#零阶优化)
  - [单轮监督微调与适配](#单轮监督微调与适配)
  - [多轮智能体适配](#多轮智能体适配)
  - [机理理解与系统](#机理理解与系统)
- [收录范围](#收录范围)
- [参与贡献](#参与贡献)

## ES 与 ZO 的使用方式不同

ES 和双点 ZO 都可以看作平滑目标函数的估计方法，但现有大语言模型文献通常将二者用于明显不同的场景。

| | 进化策略（ES） | 零阶优化（ZO） |
|---|---|---|
| 主要目标 | 直接任务奖励：`max E[R(model rollout)]` | 监督损失：`min CE/NLL(model(x), y)` |
| 评估单元 | 一组受扰动模型，每个模型分别生成新的 rollout | 通常在 `theta + eps*z` 和 `theta - eps*z` 上进行一次或少量成对前向评估 |
| 反馈信号 | 精确匹配/验证器得分、环境回报、偏好或对齐奖励 | token 级 CE/NLL、困惑度或其他相对平滑的损失 |
| 本列表中的主要用途 | 推理后训练和长时程智能体 | 内存高效的监督微调与参数高效适配 |
| 代表性数据集 | Countdown、GSM8K、MATH 类评测、Sudoku、ARC-AGI、PRM800K、IFEval；智能体场景还包括 WebArena-Lite | SST-2、RTE、BoolQ、WiC、CB、COPA、SNLI/MNLI/QNLI、SQuAD、DROP 和常识问答 |

这种区分很重要：终局推理奖励通常是稀疏、离散且随机的，因为每次扰动都会生成新的 rollout。种群评估、适应度归一化或排序以及奖励加权的 ES 更新正是为这类场景设计的。成对双点 ZO 则在两个函数值高度相关时最有效，例如在同一 minibatch 上计算确定性的监督微调损失。

这里描述的是主流实践中的分类，而不是数学上的硬性限制。ES 也可以最小化监督损失；当基于奖励的 ZO 使用大量扰动时，其形式也会逐渐接近 ES。

<!-- GENERATED CATALOG:START -->
## 进化策略

### 预训练

| 日期 | 论文 | 核心贡献 | 资源 |
|---|---|---|---|
| 2025-10 | **EA4LLM: A Gradient-Free Approach to Large Language Model Optimization via Evolutionary Algorithms** | 以真实下一 token 的平均对数概率作为适应度，使用全参数 ES 进行预训练；实验覆盖 0.5B 至 32B 参数规模的 Qwen3 风格模型。 | [论文](https://arxiv.org/abs/2510.10603) · 未找到代码 · 2025-10 |

### 单轮推理与对齐

| 日期 | 论文 | 核心贡献 | 资源 |
|---|---|---|---|
| 2026 | **Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning** | 采用全参数、种群并行的 ES，直接优化 Countdown、数学推理、数独、简洁性和 ARC-AGI 等任务的奖励。 | [论文](https://openreview.net/forum?id=i0P4ew9GpS) · [代码](https://github.com/VsonicV/es-at-scale) · [早期实现](https://github.com/VsonicV/es-fine-tuning-paper) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2026-08 | **Hyper-ES: Effective Evolution Strategies for LLM Reasoning via Descent Direction Merging** | 先通过少量梯度训练获得下降方向，再使用 CMA-ES 优化 DARE-TIES 的逐层合并系数；在六个数学推理数据集上进行评测。 | [论文](https://arxiv.org/abs/2608.05541) · [代码占位仓库](https://github.com/kuangrepi/Hyper-ES) · 2026-08 |
| 2026 | **Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights** | RandOpt 对参数扰动进行采样，保留表现最好的专家并集成其预测；在论文报告的等计算量设置下，Iterative RandOpt 使用 OLMo-3-7B 在 GSM8K 上达到 92.9%。 | [论文](https://openreview.net/forum?id=92oF5bU4cU) · [RandOpt 代码](https://github.com/sunrainyg/RandOpt) · [Iterative RandOpt 分支](https://github.com/sunrainyg/RandOpt/tree/iterative-randopt) · ![ICML 2026 Spotlight](https://img.shields.io/badge/ICML_2026-Spotlight-orange) |
| 2026-02 | **Quantized Evolution Strategies: High-precision Fine-tuning of Quantized LLMs at Low-precision Cost** | 在离散量化权重上进行直接奖励优化，并结合误差反馈和随机种子重放；在 Countdown 上进行评测。 | [论文](https://arxiv.org/abs/2602.03120) · [代码](https://github.com/dibbla/Quantized-Evolution-Strategies) · 2026-02 |
| 2026-02 | **ESSAM: A Novel Competitive Evolution Strategies Approach to Reinforcement Learning for Memory Efficient LLMs Fine-Tuning** | 面向内存高效推理微调的竞争式奖励 ES，主要在 GSM8K 上训练，并评估数学与代码任务的迁移能力。 | [论文](https://arxiv.org/abs/2602.01003) · [代码](https://github.com/szs777/ESSAM) · 2026-02 |
| 2026-02 | **Fine-Tuning Language Models to Know What They Know** | ESMA 直接优化元认知校准和对齐奖励。 | [论文](https://arxiv.org/abs/2602.02605) · [代码](https://github.com/cosmoquester/ESMA) · 2026-02 |
| 2025 | **Evolutionary System 2 Reasoning: An Empirical Proof** | ERO 通过演化模型参数，增强模型的 System 2 reasoning 能力。 | [论文](https://doi.org/10.66361/jiss.38) · [代码](https://github.com/MetaEvo/ERO) · ![JISS 2025](https://img.shields.io/badge/JISS-2025-orange) |
| 2026 | **Evolution Strategies at the Hyperscale** | EGGROLL 使用低秩扰动降低开销，同时通过种群聚合保留高秩更新，以支持可扩展的推理后训练。 | [论文](https://openreview.net/forum?id=bfVJ4GsHrO) · [Transformer/vLLM 代码](https://github.com/ESHyperscale/eggroll-vllm) · [JAX ES 核心](https://github.com/ESHyperscale/HyperscaleES) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2025-07 | **ESSA: Evolutionary Strategies for Scalable Alignment** | 对 LoRA 适配器的奇异值坐标进行演化，并支持低精度推理；在 GSM8K、PRM800K 和 IFEval 上进行评测。 | [论文](https://arxiv.org/abs/2507.04453) · 未找到代码 · 2025-07 |

### 多轮与智能体推理

| 日期 | 论文 | 核心贡献 | 资源 |
|---|---|---|---|
| 2026-08 | **Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements** | 全参数 ES 使用环境奖励评估完整智能体轨迹，无需逐步信用分配即可获得轨迹级参数归因。实验涵盖 15/45 轮数独、ReAct 风格的数学和 DocVQA、WebArena-Lite，以及启发式算法的自动设计。 | [论文](https://arxiv.org/abs/2608.17310) · [代码](https://github.com/zz1358m/Agentic-ESOpt) · 2026-08 |

### 理解 ES

| 日期 | 论文 | 核心贡献 | 资源 |
|---|---|---|---|
| 2026-08 | **Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO** | 从验证器投影后的种群多样性解释 ES 更高的 Pass@K，并将其与 GRPO 的熵坍缩进行对比；还研究了顺序式 GRPO–ES 训练、函数更新稀疏性、遗忘和种群规模扩展。 | [论文](https://arxiv.org/abs/2608.27351) · [代码](https://github.com/yunpengba7/understanding-es) · 2026-08 |
| 2026-02 | **The Blessing of Dimensionality in LLM Fine-tuning: A Variance-Curvature Perspective** | 从较低的有效曲率和先升后降的训练动态解释小规模 ES 种群为何能在极高维空间中工作；实验覆盖 Qwen2.5 的多个规模以及 GSM8K、ARC-C 和 WinoGrande。 | [论文](https://arxiv.org/abs/2602.00170) · 未找到代码 · 2026-02 |
| 2026-04 | **Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training** | 比较 ES 与 GRPO 在推理准确率相近时仍然存在差异的更新几何。 | [论文](https://arxiv.org/abs/2604.01499) · [代码](https://github.com/Bhoy1/ESvsGRPO) · 2026-04 |
| 2026-01 | **Evolutionary Strategies Lead to Catastrophic Forgetting in LLMs** | 分析 ES 后训练过程中模型既有能力退化的问题。 | [论文](https://arxiv.org/abs/2601.20861) · 未找到代码 · 2026-01 |
| 2026-05 | **Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies** | 将遗忘重新表述为性能漂移，并提出锚定权重衰减方法。 | [论文](https://arxiv.org/abs/2605.30148) · 未找到代码 · 2026-05 |
| 2026-08 | **Beyond the Best Guess: Improving LLM Solution Coverage with Evolution Strategies** | 说明 ES 不仅影响 pass@1，还会改变推理解法的多样性和 pass@k。 | [论文](https://arxiv.org/abs/2608.12679) · [代码](https://github.com/conorfhayes/beyond-the-best-guess) · 2026-08 |

## 零阶优化

除非条目另有说明，这些方法通常通过纯前向函数值评估优化监督式 CE/NLL 目标。其主要贡献是使监督微调能够在激活内存、优化器状态或黑盒访问受限的条件下进行。

### 单轮监督微调与适配

#### 基线、稀疏更新与子空间

| 日期 | 论文 | 核心贡献 | 资源 |
|---|---|---|---|
| 2023 | **Fine-Tuning Language Models with Just Forward Passes** | MeZO 引入原位参数扰动和随机种子重放，使纯前向监督微调达到与推理相当的内存占用。 | [论文](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a627810151be4d13f907ac898ff7e948-Abstract-Conference.html) · [代码](https://github.com/princeton-nlp/MeZO) · ![NeurIPS 2023](https://img.shields.io/badge/NeurIPS-2023-orange) |
| 2025 | **Sparse MeZO: Less Parameters for Better Performance in Zeroth-Order LLM Fine-Tuning** | 仅扰动经过选择的一部分参数坐标，以提高监督适配效率。 | [论文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1e5c2efbddc02c1d971e2f19ccdb07d0-Abstract-Conference.html) · [代码](https://github.com/NUS-HPC-AI-Lab/SparseMeZO) · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2024 | **Zeroth-Order Fine-Tuning of LLMs with Extreme Sparsity** | 选择 Fisher 敏感参数进行更新，并以低精度保存冻结权重。 | [论文](https://icml.cc/virtual/2024/39663) · [代码](https://github.com/GarlGuo/SensZOQ) · ![ICML 2024 Workshop](https://img.shields.io/badge/ICML_2024-ES--FoMo_II-orange) |
| 2025 | **Enhancing Zeroth-order Fine-tuning for Language Models with Low-rank Structures** | LOZO 用结构化低秩扰动替代稠密随机方向。 | [论文](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9ccc9d814d3dee4750debaf23061e733-Abstract-Conference.html) · [代码](https://github.com/optsuite/LOZO) · ![ICLR 2025](https://img.shields.io/badge/ICLR-2025-orange) |
| 2025 | **Zeroth-Order Fine-Tuning of LLMs in Random Subspaces** | SubZero 构造逐层低秩随机子空间，在其中进行纯前向适配。 | [论文](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Zeroth-Order_Fine-Tuning_of_LLMs_in_Random_Subspaces_ICCV_2025_paper.html) · [代码](https://github.com/zimingyy/SubZero) · ![ICCV 2025](https://img.shields.io/badge/ICCV-2025-orange) |
| 2025 | **TeZO: Empowering the Low-Rankness on the Temporal Dimension in the Zeroth-Order Optimization for Fine-tuning LLMs** | 利用连续多个 ZO 估计之间共享的时间低秩结构。 | [论文](https://arxiv.org/abs/2501.19057) · 未找到代码 · 2025 |
| 2026 | **RoZO: Geometry-Aware Zeroth-Order Fine-Tuning on Low-Rank Adapters for Black-Box Large Language Models** | 在 LoRA 流形的切空间中使用扰动、回缩和向量传输。 | [论文](https://aclanthology.org/2026.eacl-long.80/) · 未找到代码 · ![EACL 2026](https://img.shields.io/badge/EACL-2026-orange) |
| 2026-07 | **ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces** | 一次性构建由激活信息引导的子空间，随后在该空间中执行 ZO 监督微调；使用 Llama-3-8B 和 OPT-13B 在语言理解、问答和常识推理任务上评测。 | [论文](https://arxiv.org/abs/2607.01125) · 未找到代码 · 2026-07 |
| 2026-08 | **SubZero+: Efficient Zeroth-Order LLM Fine-Tuning via Large Learning Rates** | 结合多查询估计、修正后的 Haar 子空间和子空间 Adam。 | [论文](https://arxiv.org/abs/2608.15665) · 未找到代码 · 2026-08 |

#### 更优方向与更低方差

| 日期 | 论文 | 核心贡献 | 资源 |
|---|---|---|---|
| 2024 | **Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models** | MeZO-SVRG 在监督 ZO 微调中加入基于锚点的控制变量。 | [论文](https://proceedings.mlr.press/v235/gautam24a.html) · [代码](https://github.com/amazon-science/mezo_svrg) · ![ICML 2024](https://img.shields.io/badge/ICML-2024-orange) |
| 2025 | **Harmony in Divergence: Towards Fast, Accurate, and Memory-efficient Zeroth-order LLM Fine-tuning** | DiZO 在分析一阶与零阶优化的逐层差异后，对 ZO 更新进行逐层投影和重缩放。 | [论文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ffd4f5a2ea6b93e9bf5af9264d568cf2-Abstract-Conference.html) · [代码](https://github.com/Skilteee/DiZO) · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2025 | **KerZOO: Kernel Function Informed Zeroth-Order Optimization for Accurate and Accelerated LLM Fine-Tuning** | 使用核函数加权扰动修正估计器。 | [论文](https://arxiv.org/abs/2505.18886) · 未找到代码 · 2025 |
| 2025 | **Towards Fast LLM Fine-tuning through Zeroth-Order Optimization with Projected Gradient-Aligned Perturbations** | P-GAP 使低秩扰动与投影后的梯度估计方向对齐。 | [论文](https://arxiv.org/abs/2510.18228) · 未找到代码 · 2025 |
| 2026 | **ConMeZO: Adaptive Descent-Direction Sampling for Gradient-Free Finetuning of Large Language Models** | 从以动量估计为中心的锥形区域中采样搜索方向。 | [论文](https://proceedings.mlr.press/v300/behric26a.html) · [代码](https://github.com/LejsDeen/ConMeZO) · ![AISTATS 2026](https://img.shields.io/badge/AISTATS-2026-orange) |
| 2026 | **Low-Rank Curvature for Zeroth-Order Optimization in LLM Fine-Tuning** | LOREN 将低秩分块对角曲率建模与留一估计相结合。 | [论文](https://ojs.aaai.org/index.php/AAAI/article/view/39715) · [代码](https://github.com/hseung88/loren) · ![AAAI 2026](https://img.shields.io/badge/AAAI-2026-orange) |
| 2026 | **Robust and Efficient Zeroth-Order LLM Fine-Tuning via Adaptive Bayesian Subspace Optimizer** | ABSO 使用贝叶斯优化器聚合带噪声的子空间观测。 | [论文](https://arxiv.org/abs/2601.01452) · 未找到代码 · 2026 |
| 2026 | **Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning** | PIZOO 使采样方向偏向一个能够自适应更新的先验方向。 | [论文](https://arxiv.org/abs/2601.04710) · 未找到代码 · 2026 |
| 2026 | **AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning** | 使用前向激活信息塑造扰动方向。 | [论文](https://openreview.net/forum?id=zfVxpXEZti) · [实现](https://github.com/Yining-Jiang/ActivationGuidedZO-NPU) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2026 | **Zero-Order Optimization for LLM Fine-Tuning via Learnable Direction Sampling** | ZO-LDSD 学习一个非各向同性的方向分布。 | [论文](https://arxiv.org/abs/2602.13659) · [代码](https://github.com/brain-lab-research/zo_ldsd) · 2026 |
| 2026 | **Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization** | ZO-Muon 对子空间估计应用谱正交化。 | [论文](https://arxiv.org/abs/2602.17155) · [代码](https://github.com/OPTML-Group/ZO-Muon) · 2026 |
| 2026 | **CurvZO: Adaptive Curvature-Guided Sparse Zeroth-Order Optimization for Efficient LLM Fine-Tuning** | 将曲率感知的稀疏采样与概率校正结合起来。 | [论文](https://openreview.net/forum?id=L35b2JZ8gS) · 未找到代码 · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |
| 2026 | **Learning a Zeroth-Order Optimizer for Fine-Tuning LLMs** | 学习可以在同一模型上重复使用的扰动策略。 | [论文](https://openreview.net/forum?id=bRS5iwbqlC) · [代码](https://github.com/ASTRAL-Group/ZO_Fine_tuner) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |

#### 内存系统、预条件与量化

| 日期 | 论文 | 核心贡献 | 资源 |
|---|---|---|---|
| 2025 | **Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer** | HiZOO 使用纯前向计算估计对角曲率。 | [论文](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6bf82cc56a5fa0287c438baa8be65a70-Abstract-Conference.html) · [代码](https://github.com/Yanjun-Zhao/HiZOO) · ![ICLR 2025](https://img.shields.io/badge/ICLR-2025-orange) |
| 2025 | **Scalable Zeroth-Order Fine-Tuning for Extremely Large Language Models with Limited GPU Memory** | ZO2 通过参数卸载和执行重叠支持大模型 ZO 监督微调。 | [论文](https://openreview.net/forum?id=s0p9xpORgP) · [代码](https://github.com/liangyuwang/zo2) · ![COLM 2025](https://img.shields.io/badge/COLM-2025-orange) |
| 2026 | **High-Throughput and Memory-Efficient Zeroth-Order Fine-tuning LLMs with Distributed Parallel Computing** | DistZO2 分布式执行扰动评估，并且只聚合标量结果。 | [论文](https://aclanthology.org/2026.findings-acl.2128/) · [ZO2/DistZO2 代码](https://github.com/liangyuwang/zo2) · ![Findings of ACL 2026](https://img.shields.io/badge/Findings_of_ACL-2026-orange) |
| 2025 | **HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization** | 引入逐层裁剪和退火机制。 | [论文](https://aclanthology.org/2025.emnlp-main.1323/) · 未找到代码 · ![EMNLP 2025](https://img.shields.io/badge/EMNLP-2025-orange) |
| 2025 | **QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models** | 将量化整合到纯前向监督微调中。 | [论文](https://aclanthology.org/2025.emnlp-main.271/) · [代码](https://github.com/lloo099/QuZO) · ![EMNLP 2025](https://img.shields.io/badge/EMNLP-2025-orange) |
| 2026 | **Hi-ZFO: Hierarchical Zeroth- and First-Order LLM Fine-Tuning via Importance-Guided Tensor Selection** | 根据张量重要性为其分配一阶或零阶更新。 | [论文](https://aclanthology.org/2026.findings-acl.239/) · 未找到代码 · ![Findings of ACL 2026](https://img.shields.io/badge/Findings_of_ACL-2026-orange) |
| 2026 | **AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments** | 无需保存完整的优化器状态即可近似自适应矩估计。 | [论文](https://openreview.net/forum?id=XLc102wbnT) · [代码](https://github.com/shawnnn3di/AdaMeZO) · ![ICML 2026](https://img.shields.io/badge/ICML-2026-orange) |

### 多轮智能体适配

| 日期 | 论文 | 核心贡献 | 资源 |
|---|---|---|---|
| 2026-08 | **Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents** | 对 LoRA 参数施加扰动并使用答案困惑度进行评分，再将成功的深度研究轨迹作为监督微调数据形成闭环。该方法属于多轮智能体适配，但其 ZO 信号仍然是平滑的监督微调代理，而不是稀疏终局奖励。 | [论文](https://arxiv.org/abs/2608.09292) · [代码](https://github.com/hidk1911/ZOForLLMAgents) · 2026-08 |

### 机理理解与系统

| 日期 | 论文 | 核心贡献 | 资源 |
|---|---|---|---|
| 2024 | **Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark** | ZO-Bench 在代表性的语言理解和生成任务上比较不同目标函数、可训练接口和模型系列。 | [论文](https://proceedings.mlr.press/v235/zhang24ad.html) · [代码](https://github.com/ZO-Bench/ZO-LLM) · ![ICML 2024](https://img.shields.io/badge/ICML-2024-orange) |
| 2025 | **Zeroth-Order Optimization Finds Flat Minima** | 将随机 ZO 动力学与偏向平坦极小值的隐式偏置联系起来，并包含语言模型微调实验。 | [论文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ebc62a3af9342eb4ebc728e5c5bc4cca-Abstract-Conference.html) · [代码](https://github.com/Liang137/FlatZero) · ![NeurIPS 2025](https://img.shields.io/badge/NeurIPS-2025-orange) |
| 2026 | **LLM Zeroth-Order Fine-Tuning is an Inference Workload** | 说明重复的 ZO 评分过程可以围绕推理服务运行时重新组织。 | [论文](https://arxiv.org/abs/2605.28760) · [代码](https://github.com/playeriv65/zo-vllm) · 2026 |
<!-- GENERATED CATALOG:END -->

## 收录范围

收录的方法必须通过 ES 种群、进化选择或零阶/函数值评估来优化大语言模型的持久化参数或参数高效模块。完整权重、LoRA/适配器、结构化子空间和量化参数均在收录范围内。

以下内容不在收录范围内：

- 提示词、指令、思维链、候选答案、技能、记忆和推理状态的演化；
- 不包含参数空间 ES/ZO 贡献的通用强化学习或智能体自我改进方法；
- 不训练或适配大语言模型参数的架构搜索或超参数搜索；
- 仅面向视觉或语音的应用。

## 参与贡献

欢迎补充论文或提交更正。请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并使用论文请求 issue 模板。每个条目都应包含主要论文链接；如果存在官方代码，也应提供相应链接，否则请明确标注“未找到代码”。

参考文献记录见 [papers.bib](papers.bib)。

最新的论文与 GitHub 代码可用性审查记录见 [CODE_AUDIT_zh.md](CODE_AUDIT_zh.md)。

## 致谢

本仓库最初的参考文献来自本地综述 *Gradient-Free Optimization for LLM Reasoning*。仓库结构参考了 [Awesome-Latent-CoT](https://github.com/EIT-NLP/Awesome-Latent-CoT)；论文说明以及 ES/ZO 的任务分类由本仓库独立整理。
