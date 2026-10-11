# ICLR 2027 提示词与智能体范围收紧：批次 4

本批逐篇审查原 `related_hybrid` 的 73 条现行目录记录。判断以仓库保存的 OpenReview 官方摘要为主；Hyper-ES 与 ZFO 两条缺主审查记录，使用目录中已有的原文链接及已核实方法说明。本批未进行新文献检索。

## 统计

- `keep_unaffected`：42
- `keep_agent_model_training`：20
- `defer_prompt_core`：9
- `defer_agent_no_model_training`：1
- `defer_agent_training_unverified`：1

## 逐篇决定

### 1. Hyper-ES: Effective Evolution Strategies for LLM Reasoning via Descent Direction Merging

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：混合方法：先通过梯度训练获得下降方向，再以 CMA-ES 优化 DARE-TIES 逐层合并系数；第一阶段仍使用反向传播。
- 模型参数/组件边界：模型/优化器更新边界沿用现有论文记录；本次范围调整不改变其技术分类。
- 原始来源：https://arxiv.org/abs/2608.05541
- 证据依据：该条缺少主审查记录；依据现有 arXiv 原文链接及目录中已核实的方法说明判断，未进行广泛检索。

### 2. Continual Test-Time Learning with Evolution Strategies

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：用局部参数扰动策略群体生成轨迹，并以无标签组相对信号持续更新中央学生。
- 模型参数/组件边界：扰动策略与 central student 都涉及模型状态；central student 更新的反传实现待正文核实。
- 原始来源：https://openreview.net/forum?id=LOwG4xUpfa
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 3. Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：混合贡献：除 ES 分析外，论文还提出两种顺序的 sequential ES–GRPO training。
- 模型参数/组件边界：ES 与 GRPO 分支均持久更新模型参数；各阶段衔接细节待正文核实。
- 原始来源：https://openreview.net/forum?id=OF8CUj7TD8
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 4. Accelerating LLM Pretraining with Zeroth-Order Curvature on Idle Serving Compute

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：在空闲纯前向设备上以零阶查询估计曲率，用其精炼主训练端的一阶全参数更新。
- 模型参数/组件边界：预训练模型参数由一阶训练持久更新；ZO 设备只提供曲率信息。
- 原始来源：https://openreview.net/forum?id=qh1N46HjOP
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 5. Zero-Order Optimization via Learnable Direction Sampling for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：混合方向学习：finite-difference ZO 更新 LLM，REINFORCE 同时适配 Gaussian perturbation distribution。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件/优化器状态：摘要未明说者待核实
- 原始来源：https://openreview.net/forum?id=CZqew9w981
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 6. Geometric-Steering Muon for Online Large Language Model Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：GS-Muon 在 Newton–Schulz 变换间加入几何 steering，使动量方向适应在线目标的一阶或零阶信号。
- 模型参数/组件边界：模型参数由 GS-Muon 持久更新；信号可来自一阶或零阶，具体实验配置待正文核实。
- 原始来源：https://openreview.net/forum?id=APkYU4FkeR
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 7. FoRA: Forward-Only Residual Adaptation for Federated Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：FoRA 从冻结前向 LLM 骨干分离表征，并以一阶联邦优化训练轻量因子化 residual。
- 模型参数/组件边界：LLM backbone 权重：frozen；外接 factorized residual 参数：一阶持久更新。
- 原始来源：https://openreview.net/forum?id=ACuCPfyRs1
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 8. Evaluate Before You Commit: Label-Free Candidate-Update Utility for Test-Time Adaptation

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：以仅前向的 probe-view utility 评估暂定适配更新，再事务式提交或回滚。
- 模型参数/组件边界：基础适配器可能持久更新模型；controller 决定提交或回滚，具体生成器与模型参数边界待核实。
- 原始来源：https://openreview.net/forum?id=JEeD6leWDn
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 9. DRAM: Memory-Efficient Muon via Rank Reallocation in Principal-Random Subspaces

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：DRAM 在一阶 Muon 中组合随机梯度的主奇异方向与正交随机方向，并随训练阶段重分配两者的 rank budget，同时保留 momentum。
- 模型参数/组件边界：持久模型权重与 Muon momentum/optimizer state 均随一阶训练更新；子空间 rank schedule 是优化器配置。
- 原始来源：https://openreview.net/forum?id=RbXMY0agox
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 10. Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM Fine-Tuning

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：混合 ZFO 使用反向传播得到的一阶方向及两次额外函数评估，选择曲率感知步长；训练仍需任务梯度，作为关联研究收录。
- 模型参数/组件边界：模型/优化器更新边界沿用现有论文记录；本次范围调整不改变其技术分类。
- 原始来源：https://arxiv.org/abs/2610.02190
- 证据依据：该条缺少主审查记录；依据现有 arXiv 原文链接及目录中已核实的方法说明判断，未进行广泛检索。

### 11. When Safety Fails Collectively: Robust Alignment Against Harmful Fine-Tuning via Joint Weight Perturbations

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：JWP 从当前模型估计 harmful weight perturbation，组合遮蔽其不同部分构造训练状态，再做监督安全训练以抵抗扰动累积。
- 模型参数/组件边界：模型安全对齐权重：持久训练更新；masked harmful perturbation combinations：训练时状态。
- 原始来源：https://openreview.net/forum?id=CRHLdRAVgK
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 12. Turning Abliteration into Model Self-Destruction in Open-Weight LLMs

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：该防御在 refusal direction 的随机子空间中模拟 abliteration，并监督模型在强移除时崩溃、在部分移除时保持拒绝。
- 模型参数/组件边界：对齐后模型权重持久更新；refusal-direction random subspaces 是训练时攻击样本构造。
- 原始来源：https://openreview.net/forum?id=ErcCQSs93S
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 13. Train Small, Guide Large: Optimization Scouting for Efficient LLM Post-Training

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：OptScout 通过小模型强化学习与梯度探测得到方向，再用纯前向奖励选择一次性的大模型持久更新；因方向阶段含梯度而归入混合方法。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件/优化器状态：摘要未明说者待核实
- 原始来源：https://openreview.net/forum?id=7hs0vjh7L4
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 14. SynKer: Synthesize, Kernelize, Reinforce - Teaching GPU Kernel Generation to Small Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：进化生成操作任务并搜索可执行 kernel，再用验证后的 kernel 档案进行 SFT 和 RL 后训练。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件/优化器状态：摘要未明说者待核实
- 原始来源：https://openreview.net/forum?id=nZQqqpYQ0Y
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 15. Structured Algebraic Adapters for Fine-Tuning of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：在固定分块带符号排列算子族上学习适配系数，以冻结骨干进行残差状态或权重空间适配。
- 模型参数/组件边界：任务 LLM/骨干权重：据摘要 frozen；持久外部工件/优化器状态：摘要未明说者待核实
- 原始来源：https://openreview.net/forum?id=j51J8bLIFh
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 16. Reshaping Guidance Objective with Large Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：结合 LLM 结构改写与重参数化潜空间的零阶数值优化，联合重塑下游求解器的指导目标。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件/优化器状态：摘要未明说者待核实
- 原始来源：https://openreview.net/forum?id=mL3MYH1pYu
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 17. Recursive Self-Improvement through Multi-Agent Self-Supervision

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：官方摘要明确交替进行 multi-agent workflow evolutionary optimization 与在自生成轨迹上的 supervised fine-tuning。
- 模型参数/组件边界：单一基础模型在优化工作流的执行轨迹上做监督微调，模型权重持久更新；工作流图另经外部进化搜索。反向传播实现未明说。
- 原始来源：https://openreview.net/forum?id=lHLch9v09X
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 18. RaSTA: Random Subspace Tuning Adaptation

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：RaSTA 冻结跨层共享随机子空间，只学习 dense basis mixing 或 Walsh–Hadamard mixing 下的逐 basis scaling。
- 模型参数/组件边界：持久 adapter 参数：RaSTA-DM mixing matrix 或 RaSTA-HS scaling vectors；冻结 bases 不存入 adapter checkpoint。
- 原始来源：https://openreview.net/forum?id=dP6UvaqrT0
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 19. RLSR: Reinforcement Learning with Self-Reflection for Large Language Models Self-Improvement

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：筛选经群组成功验证的自反思轨迹，并在统一 policy-gradient 目标下分别为直接回答与反思纠错分配信用。
- 模型参数/组件边界：LLM policy 被持续优化并内化反思能力。
- 原始来源：https://openreview.net/forum?id=ZjYHBdhwoj
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 20. Privacy-Preserving Federated Fine-Tuning of Language Models under Non-IID Data

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：LSSCA 将 stochastic controlled averaging 与数据无关固定随机子空间滤波结合，保留参考分量并衰减差分隐私联邦 LLM 更新中的正交噪声。
- 模型参数/组件边界：全局与本地语言模型参数、control states 持久更新；固定随机 filter 本身由非私有随机方式构造。
- 原始来源：https://openreview.net/forum?id=aIKLwLGFfG
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 21. Noisy Replicator-Mutator Dynamics in Multi-Agent Learning

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：论文从 stochastic policy-gradient updates 推导多智能体动力学，并据此构造 PRPG，属于策略参数训练而非只改文本工件。
- 模型参数/组件边界：多智能体 policy 通过 policy-gradient/PRPG 更新；摘要未给出具体反传实现和参数化范围。
- 原始来源：https://openreview.net/forum?id=qtwq8fbHB0
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 22. MaRR: Map-Based Rotation Reasoning for Vision--Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：MaRR 以教师轨迹微调 VLM，使对象特定表征配合共享空间关系旋转与候选匹配程序。
- 模型参数/组件边界：Qwen3.5-4B 经过微调，存在持久模型参数更新；具体参数子集待正文核实。
- 原始来源：https://openreview.net/forum?id=8Zil1NPWtd
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 23. MA-RL-VLA: Counterfactual Credit-Aware PPO for Multi-Agent Reinforcement Fine-Tuning of Vision-Language-Action Models

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：MA-RL-VLA 将反事实信用权重置入 PPO 两个分支，明确训练多智能体 VLA 导航策略。
- 模型参数/组件边界：VLA policy 参数由 PPO 持久更新；精确动作枚举用于信用分配，不等同于整个流程无反向传播。
- 原始来源：https://openreview.net/forum?id=MtYTLgYRmu
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 24. Local proxies for memory-efficient training

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：每个 Transformer block 通过蒸馏训练局部 proxy，并在该 proxy 内独立反传以近似全局梯度、降低激活内存。
- 模型参数/组件边界：Transformer blocks 与 proxy networks 均通过局部训练产生持久参数更新。
- 原始来源：https://openreview.net/forum?id=bbhfFx9iqO
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 25. LoLoRA: Locally Fine-Tuned Low Rank Adapters

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：LoLoRA 在前向过程中依据每层输入对 LoRA 矩阵 A 做局部 gradient-free 更新，省去 A 的反传激活存储，同时保留其余 adapter 训练路径。
- 模型参数/组件边界：LoRA A 持久更新；LoRA B 与基础模型权重的持久更新范围待正文核实。
- 原始来源：https://openreview.net/forum?id=nvUl5uZXor
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 26. Learning to Predict Distributions over Weight Updates for Test-Time Adaptation

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：query-conditioned distributional hypernetwork 以可微 Monte Carlo 损失训练 LoRA 分布，并在测试时采样权重更新形成多个适配模型。
- 模型参数/组件边界：hypernetwork 参数持久训练；测试时 query-conditioned LoRA samples 为实例级适配权重，是否跨 query 保存待核实。
- 原始来源：https://openreview.net/forum?id=JXYRjlh1Wh
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 27. Learning to Elicit: Co-Evolving Routing and Information Disclosure in Societies of Language Agents

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：Co-Adapt 用 RL 与 privileged on-policy distillation 学习联系路由和私有信息披露。
- 模型参数/组件边界：智能体 routing/disclosure policy 由 RL 与蒸馏持久训练；各模块是否共享语言模型参数及反传细节待正文核实。
- 原始来源：https://openreview.net/forum?id=xupjJh9hXG
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 28. Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：TFlow 明确训练 parameter generator，由 sender 隐状态生成 receiver-specific 低秩 LoRA 扰动。
- 模型参数/组件边界：parameter generator 参数被训练；receiver 基座冻结，但生成的 LoRA 扰动在单次生成中改变模型参数状态。训练算法和反传边界待核实。
- 原始来源：https://openreview.net/forum?id=tDrV3iV2Zb
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 29. GPU Forecasters: Language Models as Speculative Surrogates for Kernel Runtime Optimization

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：该工作用 LLM surrogate 预测 kernel 运行时以筛选 GPU 实测候选，并另以 RL 训练 surrogate 的校准能力。
- 模型参数/组件边界：存在持久的 RL-trained surrogate 更新；另持久保存 kernel 候选与 12,388 个实测样本
- 原始来源：https://openreview.net/forum?id=x23LuMrBJo
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 30. Entropy Targeting in Sequential Reinforcement Fine-Tuning of Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：分析顺序强化微调中哪些一致性信号真正进入策略更新，并识别 entropy targeting 的作用。
- 模型参数/组件边界：顺序 reinforcement fine-tuning 会持续更新语言模型策略；摘要未给出具体参数子集。
- 原始来源：https://openreview.net/forum?id=E4354yeoTt
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 31. CoEvoMed: Co-Evolving Supervision Principles and Medical Vision–Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：随医学 VLM 能力变化共同更新监督样例构造原则与课程预算，并以这些监督训练模型。
- 模型参数/组件边界：摘要明确使用该框架训练 8B 模型并报告 32B 结果，因此学习者存在持久参数更新；具体参数与优化器未说明。
- 原始来源：https://openreview.net/forum?id=GeL7NntZTU
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 32. CoER: Defending against Adaptive Indirect Prompt Injection via Adversarial Co-Evolution and Refinement

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 范围证据：CoER 的核心任务是 adaptive indirect prompt injection：攻击者反复生成/适配注入内容，虽同时以 BA-RL 和 fine-tuning 训练 defender，仍命中“提示词相关暂缓”例外。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 原始来源：https://openreview.net/forum?id=SUxaNjKUP8
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 33. Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：PPol 的 persona 程序由进化 coding agent 搜索；摘要另明确用 PPol 数据 fine-tuning agents 并报告真人交互提升。
- 模型参数/组件边界：persona generation program 是外部搜索工件；下游语言 agent 明确经过 fine-tuning，具体参数子集和反传实现未说明。
- 原始来源：https://openreview.net/forum?id=HJaoIZVSzM
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 34. Beyond Alignment: Enhancing LLM Safety Robustness via Zeroth-Order Optimization

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：在常规一阶安全对齐后追加少量零阶鲁棒性精炼步骤，因此归入一阶与零阶混合方法。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件/优化器状态：摘要未明说者待核实
- 原始来源：https://openreview.net/forum?id=9Lrcxvs7GS
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 35. AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：AgentSafeEvo 是 attacker–defender co-evolutionary RL，摘要明确攻击者和防御者均学习任务/执行策略。
- 模型参数/组件边界：attacker 与 defender 的语言智能体策略由 RL 持久更新；task weighting 是信用/课程机制，具体反传实现待核实。
- 原始来源：https://openreview.net/forum?id=9wUe4gLzDm
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 36. ACE-Guard: Automated Co-Evolutionary Guardrails for LLM Security via Inference-Time Natural Language Gradients

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 范围证据：ACE-Guard 的核心是 prompt injection 防御与 natural-language prompt steering，且摘要明确 ΔΘ=0；属于提示词核心。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 原始来源：https://openreview.net/forum?id=8YtHcGc4sq
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 37. ReLaDrift: Recurrent Language Generation via Drifting for Test-Time Scaling

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：ReLaDrift 递归修正 Drifting Model 草稿，并只在随机选取的一轮上施加 drifting loss、避免跨轮 BPTT，但仍保留该单轮训练组件。
- 模型参数/组件边界：模型权重：存在持久训练更新但参数范围待核实；推理草稿：轮间暂态。
- 原始来源：https://openreview.net/forum?id=C1HGhWNaYZ
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 38. Super Neurons Answer Before VLMs Speak

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：无梯度筛选少量 VLM 语言模块神经元，以其标量激活在自回归生成前直接完成分类 VQA。
- 模型参数/组件边界：discovery 阶段不更新 backbone；持久保存 neuron indices/readout；可选微调分支持久更新参数范围待核实。
- 原始来源：https://openreview.net/forum?id=r9LXL9LP7B
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 39. Sample the Order, Not the Token: Test-Time Scaling for Masked Diffusion Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：OSE 在测试时扰动掩码扩散模型的解掩码顺序进行集成，不更新模型参数；其另行报告的 GRPO 实验属于一阶训练。
- 模型参数/组件边界：OSE 不更新模型；GRPO 分支持久更新 policy。
- 原始来源：https://openreview.net/forum?id=mISIJ9ktNq
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 40. Pharos: Augmenting Lighthouse Attention with Adaptive Budgets, Cross-Level Guidance, Tidal Momentum, and Uncertainty-Aware Fallback

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：Pharos 为分层长上下文注意力加入自适应 head 预算、跨尺度指导、跨层动量和低置信回退。
- 模型参数/组件边界：持久模型权重：待核实；持久外部工件：若仅当次推理状态则不跨任务持久；是否保存校准状态待核实
- 原始来源：https://openreview.net/forum?id=v1SEW28Ij4
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 41. BiTFlow: Efficient Coreset Selection for Instruction Tuning via Balanced Token Flow Matching

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：将候选样本的中间层 token 残差流与目标原型作二分匹配，并以平衡覆盖聚合完成前向筛选。
- 模型参数/组件边界：selection 阶段不更新模型；持久输出 coreset；随后 instruction-tuning 会更新模型参数。
- 原始来源：https://openreview.net/forum?id=QFIRgU2Gex
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 42. Word-Level Text Unmixing via Evidence-Preserving Ownership Routing with Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：EPoR 训练因果语言模型预测词所有权路由，再用受约束解码和确定性重建保证证据完整。
- 模型参数/组件边界：路由模型经过训练，故存在持久模型适配；具体参数范围和训练方法待正文核实。
- 原始来源：https://openreview.net/forum?id=5ASvyn7llP
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 43. When to Prompt, When to Update: Context-Parameter Allocation for Language Agents

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 范围证据：论文直接研究 prompt information 与 parameter writes 的分配，并以 controller 投影/维护 prompt state；即使会触发参数更新，也属于提示词核心。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 原始来源：https://openreview.net/forum?id=OTIZLTbN5q
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 44. Safe Alone, Unsafe Together: Compositional Curvature Safety Alignment for Prompt Robustness

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 范围证据：论文核心对象是 compositional prompt transformations、prompt safety lattice 与 prompt robustness；参数子空间修复不改变其提示词核心范围。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 原始来源：https://openreview.net/forum?id=uXUOE1j8px
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 45. Rent or Recompute?: Learning-Augmented Placement of Agent KV Caches Across Memory and Shared Storage Tiers

- 决定：`defer_agent_no_model_training`
- 原分类：`related_hybrid`
- 范围证据：核心是 agent KV-cache 在 GPU/主存/存储层之间的放置策略；语言智能体和 LLM 参数均不更新。
- 模型参数/组件边界：仅训练 idle-gap predictor；该预测器服务缓存调度，不是语言智能体 policy、LLM、LoRA 或 adapter，因此不满足保留条件。
- 原始来源：https://openreview.net/forum?id=5MJgRASpik
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 46. Positional Inference for Stronger Attacks on Language Models

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 范围证据：论文优化 adversarial token 的 prefix/infix/suffix 位置，并转移 position posterior；优化对象是攻击 prompt 的 token placement。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 原始来源：https://openreview.net/forum?id=uh7b7doBNd
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 47. P$^2$O: Joint Policy and Prompt Optimization

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 范围证据：P²O 明确交替进行 prompt evolution 与 policy update，GEPA 搜索 reasoning prompts；提示词优化是核心组成。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 原始来源：https://openreview.net/forum?id=XywNH2Ca3U
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 48. Off-Diagonal Hessian Sensitivity for Post-Training Quantization of Large Language Models

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：ODES 从 task-loss Hessian 的 off-diagonal interaction 推导 projection-pair precision reallocation 排名，用 compressed probe-centered estimator 在 LLM 规模估计该敏感度，再把 mixed-precision bit allocation 缩减为对重分配 pair 数的一维候选搜索。
- 模型参数/组件边界：全精度模型权重：摘要未提出训练；持久模型表示：projection-pair bit allocation 与由 RTN/HQQ/GPTQ 实例化的量化权重。
- 原始来源：https://openreview.net/forum?id=nYra38pdbe
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 49. MIMUS: Post-Hoc Refinement of Frozen Rewards via Residual Evolution

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：以 CMA-ES 演化零初始化的低秩奖励残差，并用候选奖励下训练策略的表现计算适应度。
- 模型参数/组件边界：base reward 冻结；low-rank reward residual 持久演化；候选/最终 policy 的持久与训练细节待核实。
- 原始来源：https://openreview.net/forum?id=Kra8djk0Ys
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 50. Large Language Models as Generative Bayesian Policies

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：该稿以 LLM embedding 上 deep-kernel-learned Gaussian-process critic 的 acquisition function 生成 preference signal，再对 LLM actor 做 preference fine-tuning，使其生成分布逐轮向高效用科学候选移动并摊销 BO acquisition search。
- 模型参数/组件边界：GP critic 与 LLM actor 均存在训练后的持久状态；actor 具体全参/参数高效微调范围待核实。
- 原始来源：https://openreview.net/forum?id=fbzXTjTZ9x
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 51. Explicit Trajectory Diversity for RL-Based Post-Training of LLM Agents

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：TJPO 在 single-policy group-based RL 中以 trajectory-level signals 直接优化智能体 policy。
- 模型参数/组件边界：单一 LLM agent policy 经 group-based RL 持久更新；trajectory descriptors 是用户指定的行为表示，不是被训练的模型。
- 原始来源：https://openreview.net/forum?id=WDqlWS75gR
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 52. EvoComp-2: Learning to Compress Audio-Video Tokens for Omnimodal Large Language Models via Topic-Guided Evolutionary Labeling

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：通过主题引导的时间聚类和进化式 token 保留标注构造监督，再训练压缩器学习时间区域与模态的重要性。
- 模型参数/组件边界：压缩器参数被持久训练；进化生成的 token-retention 与 modality-importance 标签为训练工件。
- 原始来源：https://openreview.net/forum?id=ZPkgIda8N5
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 53. EviGate: Evidence-Gated Inheritance for Self-Evolving Program-Repair Agents

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：EviGate 官方摘要明确包含 parameter adaptation，并仅在 promotion、regression、safety checks 后保留 parameter children。
- 模型参数/组件边界：通过门控的参数子代可持久继承；摘要未说明 parameter adaptation 的优化器、参数范围或反传实现。
- 原始来源：https://openreview.net/forum?id=gU0o6s2tHP
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 54. DIA-GRPO: Guiding Policy Optimization with Cross-Prompt Diagnosis

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：把跨提示能力诊断转为响应级 advantage，并与原生 GRPO advantage 混合用于策略更新。
- 模型参数/组件边界：LLM policy 参数持久更新；诊断状态持久性待核实。
- 原始来源：https://openreview.net/forum?id=lXuaseCyXd
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 55. DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 范围证据：DARWIN-Attack 以遗传变异、选择和组合持续优化 jailbreak attack strategies/prompt variants；虽训练 guardrail，仍属提示词/越狱提示搜索核心。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 原始来源：https://openreview.net/forum?id=UmzQqgrCPV
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 56. CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：CoHARL 明确在 harness population 上用 population-based RL 训练 shared policy。
- 模型参数/组件边界：shared LLM policy 由 RL 持久更新；harness proposer 修订代码，proposer 自身是否训练待核实。
- 原始来源：https://openreview.net/forum?id=Iiw1WtkMkZ
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 57. CoDeL: Co-Evolutionary Defense against Indirect Prompt Injection in LLM-based Agents

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 范围证据：CoDeL 的 co-evolving prober 搜索 injection rounds、attack methods 与 payloads，核心是 indirect prompt injection；LoRA-GDPO defender 训练不解除提示词暂缓规则。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 原始来源：https://openreview.net/forum?id=ywkbERYvpx
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 58. Breaking the Pseudo-Multi-Agent Illusion: A Parasite–Immune Multi-Agent Trading Framework

- 决定：`defer_agent_training_unverified`
- 原分类：`related_hybrid`
- 范围证据：PI-MAT 以固定视角的 LLM alpha agents 生成信号，并称在线反馈驱动的 meta-learning arbiter 调整信号和资金；摘要未说明 arbiter 是否为可训练参数模型。
- 模型参数/组件边界：未证实语言智能体模型、策略模型或适配器参数被训练/持久更新；也不能反向断言完全不训练，故转入训练证据待核实。
- 原始来源：https://openreview.net/forum?id=xiaccTalhi
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 59. AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Harness

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：AIProver 明确 jointly post-trains a 119B open-weight language model，并交替进行模型 fine-tuning/RL 与 HarnessEvolve。
- 模型参数/组件边界：119B 模型参数通过 fine-tuning 和 alternating RL 持久更新；harness control flow 另由证书驱动进化搜索。具体反传实现待核实。
- 原始来源：https://openreview.net/forum?id=R9kJupcBxE
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 60. $\pi$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Labeled QA Data

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：π-Play 将 QCP 转为 token-level supervision 做 self-distillation，以持续改进搜索智能体模型。
- 模型参数/组件边界：语言模型/策略通过 token-level self-distillation 持久更新；摘要未说明优化器和反向传播实现。
- 原始来源：https://openreview.net/forum?id=KOqQs63l7Q
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 61. $R_Q$-Evolve: LLMs Evolve Their Own Generator Programs for Self-Improvement

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：R_Q-Evolve 同时突变 generator programs，并用 group-relative RL 训练 Solver。
- 模型参数/组件边界：Solver 模型参数经 group-relative RL 持久更新；generator-program archive 经 mutation、fitness ranking 与 retention 更新。
- 原始来源：https://openreview.net/forum?id=B8oWwVLeGz
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 62. GEAR: Co-evolving Grounded VLM Agents with Environment-Aligned Rubrics

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：GEAR 官方摘要明确 jointly optimizes a VLM policy and a rubricator，并与 RL 轨迹分布共同演化。
- 模型参数/组件边界：VLM policy 与 rubricator 均为训练组件；摘要未说明参数子集和各自是否/如何反向传播。自然语言 rubrics 是外部工件。
- 原始来源：https://openreview.net/forum?id=0AdawuC1tj
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 63. Heterogeneous Agentic Coevolution

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：HACE 明确以 supervised learning 改进 specialist，并以 on-policy RL 训练 LLM agent。
- 模型参数/组件边界：specialist foundation model 与 agent policy 均持久训练；interaction harness 另经 evolutionary search，具体反传路径待核实。
- 原始来源：https://openreview.net/forum?id=E1rsriszaM
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 64. Outcome-Ranked Proposal Tuning: Training LLMs to Transfer Experience Across Bayesian Optimization Tasks

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：按初始化候选对后续贝叶斯优化的影响训练 LLM 提议模型，而非按候选自身目标值训练。
- 模型参数/组件边界：模型/策略或训练组件：摘要显示存在持久训练/部署更新；具体参数子集待核实。外部搜索工件：LLM proposal-model weights and BO initialization proposals。
- 原始来源：https://openreview.net/forum?id=MaP2KsIEzp
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 65. Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：PCPO 提出 parametric self-evolution，以 hybrid policy update 将自生成算法内化到 algorithm-design agent。
- 模型参数/组件边界：agent policy 参数经 PCPO 持久更新；算法 population 是外部工件。摘要未交代梯度/反传实现。
- 原始来源：https://openreview.net/forum?id=Y3u3Z56znq
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 66. Meta-Rubrics: Learning to Discover Rubrics at Deployment for Efficient Task Adaptation

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：Meta-Rubrics 明确用 branched-rollout RL jointly optimizes rubric generator and LLM judge。
- 模型参数/组件边界：rubric generator 与 LLM judge 参数经 RL 持久训练；部署期自然语言 rubric/候选排序是外部状态，反传实现待核实。
- 原始来源：https://openreview.net/forum?id=g5tssaW2qj
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 67. OpenMLE: Training LLMs for Evolutionary Search in Machine Learning Engineering

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：OpenMLE-Train 明确先 execution-verified SFT、再以执行奖励 RL post-train 单一模型，之后把它作为进化搜索 variation engine。
- 模型参数/组件边界：程序修订语言模型通过 SFT 和 RL 持久更新；OpenMLE-Evo 的长期 population/search state 另行更新。
- 原始来源：https://openreview.net/forum?id=nSuEq47kb9
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 68. EdgeEdit: An Edge-Oriented Multimodal Knowledge Editing Framework for On-Device MLLMs

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：EdgeEdit 用零阶敏感度和动态规划配置端侧混合精度量化，并以显著性引导的视觉 token 裁剪保留编辑证据。
- 模型参数/组件边界：混合精度量化产生持久部署配置/模型表示；摘要未说明通过训练更新原始 MLLM 权重
- 原始来源：https://openreview.net/forum?id=szkL8iUTnD
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 69. HarnessNet: From Engineered Harnesses to a Unified Neural Controller for Self-Evolving Agents

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：HarnessNet 保持 LLM 冻结，但明确训练持久 neural feedback controller：先模仿 engineered harness，再按同任务多次尝试结果改进。
- 模型参数/组件边界：LLM 权重冻结；作为智能体执行策略的 HarnessNet 神经控制器参数持久训练，且不穿过 LLM/环境求梯度。第二阶段优化细节待正文核实。
- 原始来源：https://openreview.net/forum?id=cFcaAi8dtG
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 70. When Can First-Order Models of Fine-Tuning Bound Forgetting?

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：有限差分探针拟合响应 surrogate，为本身采用一阶 SGD 的 LoRA 微调遗忘提供概率界。
- 模型参数/组件边界：SGD 会持久更新 LoRA；response coefficients 和界是诊断产物，不是模型更新。
- 原始来源：https://openreview.net/forum?id=pOcuwMjDc0
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 71. Don't Retrain, Remix: Adaptation of Web Agents using Mixture Hypernetworks

- 决定：`keep_agent_model_training`
- 原分类：`related_hybrid`
- 范围证据：WebMix 用预训练 LoRA bank 与 router 在部署时合成为新 adapter；虽无目标域梯度更新，但明确形成用于智能体推理的新模型适配参数。
- 模型参数/组件边界：源 LoRA 与 router 预先训练；目标域以一次 router 前向持久合成/配置新 adapter，基础模型不做目标域反向传播。
- 原始来源：https://openreview.net/forum?id=Eq74LwgkjR
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 72. Eliciting Model Behaviors by Optimizing the Latent Posterior

- 决定：`defer_prompt_core`
- 原分类：`related_hybrid`
- 范围证据：Posterior Prefix Tuning 优化 hard-prompt 分布以诱导模型行为，优化对象明确是 prompt。
- 模型参数/组件边界：按用户 2026-10-12 范围例外暂缓；若论文同时训练 defender/policy，该训练事实仍保留在归档，不把暂缓误写为“无模型训练”。
- 原始来源：https://openreview.net/forum?id=hw82nCsx4L
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。

### 73. HO-FL: Hybrid-Order Federated Learning for Heterogeneous Edge Devices

- 决定：`keep_unaffected`
- 原分类：`related_hybrid`
- 范围证据：不属于提示词核心或需按智能体参数规则移出的研究：提出 HO-FL：各客户端按内存预算选择模型分段边界，用 ZO 训练底段、FO 训练顶段，并针对不同边界带来的更新质量与数据代表性权衡设计客户端采样近似；摘要报告了语言任务实验。
- 模型参数/组件边界：持久更新全局模型权重，且各客户端本地多步更新后参与聚合；order boundary 可按设备内存选择。
- 原始来源：https://openreview.net/forum?id=iVQu1sp529
- 证据依据：依据已保存的 OpenReview 官方摘要逐篇判断；未进行新检索。
