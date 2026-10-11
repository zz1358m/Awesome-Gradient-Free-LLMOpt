# ICLR 2027 方法定向检索候选审查：Batch 5

- 范围：`review-batch-5.json` 的 30 条官方 OpenReview note。候选来自明确方法短语查询；短语命中只作为发现入口。
- 审查方式：逐篇阅读官方摘要，区分论文自身机制、基线和背景；只收录与 LLM/VLM/语言代理优化有具体关联者。
- 结果：收录 4 条，排除 26 条。作者均按匿名投稿记录；OpenReview `odate` 与跨平台首次公开日期分开。

## 收录

### Learning While Generating in a Single Forward Pass

- OpenReview：[G8GNLtlyAV](https://openreview.net/forum?id=G8GNLtlyAV)
- 查询命中：forward gradient
- 核心贡献：提出 One-Pass Forward-Trace Adaptation（OFTA）：在 LLM 生成时沿随机参数方向记录响应对数概率的变化，反馈到达后直接把该记录转换为参数更新，从而省去反馈后的第二次模型运行。
- 方法：在单次生成前向中记录随机参数方向的 forward-gradient 方向导数；反馈后以该导数轨迹形成无反向传播的更新。摘要称它与反馈后另跑一遍得到相同方向导数，并保留 forward-gradient 方法的无偏估计；这使用导数信息，摘要未证明是仅凭函数值查询的严格零阶方法。
- 优化对象：Qwen3 系列语言模型参数与每次响应的方向导数记录；具体参数子集、完整更新式和检查点保存策略仅凭摘要待核实。
- 反向传播：官方摘要明确 OFTA 适配更新不使用 backpropagation 或保留激活；“无需反向传播”不等于“无需任何梯度/导数”。官方 PDF 的合法入口本次均返回 HTTP 403，forward-mode AD/JVP 的具体实现待核实；底座模型原始训练不在摘要核验范围内。
- 持久状态：模型参数会随连续反馈被更新，因而存在跨交互持久模型状态；摘要未说明更新参数范围及存储粒度。
- 仓库关联：直接面向部署中 LLM 的 forward-gradient 随机方向导数适配；归入 `related_forward_gradient`，不作为严格 ZO 主分类，也没有证据将其写成一阶/零阶混合方法。
- 待核实：作者身份、跨平台首次公开日期、代码、forward-mode AD/JVP 具体实现、更新参数范围、检查点持久化与评审结果待核实；实验结果仅按作者摘要记录。

### Shrinkage in Zeroth-Order Optimization: Estimation Risk and Expected Descent

- OpenReview：[CiCNIXROuS](https://openreview.net/forum?id=CiCNIXROuS)
- 查询命中：zeroth-order
- 核心贡献：研究有限随机方向批次下 anchored ridge shrinkage 对零阶更新的估计风险与选步后期望下降的不同影响，并在冻结 OPT-125M 检查点上用拟合损失步长搜索检验理论预测。
- 方法：对随机方向零阶更新施加 anchored ridge shrinkage，比较欧氏估计风险与各自优化步长后的二次下降；OPT-125M 实验通过扩展步长搜索评估更新。
- 优化对象：冻结 OPT-125M 检查点附近的零阶更新及拟合损失；摘要未说明是否把实验更新持久保存为模型检查点。
- 反向传播：零阶探测依赖函数值和随机方向；摘要没有说明 OPT 实验的损失评估是否涉及其他反向传播组件，待核实。
- 持久状态：理论对象是模型参数更新；实验是否形成持久模型权重以及具体更新轮次，摘要未交代。
- 仓库关联：以 OPT-125M 为实证对象分析零阶梯度估计改进为何不必然带来更好优化下降，属于 LLM 零阶优化理论边界。
- 待核实：作者身份、跨平台首次公开日期、代码（如摘要未列）、完整实现细节与评审结果待核实；实验结果仅按作者摘要记录。

### When Are Nearby Experts Composable? Cross-Task Model Merging in Neural Thickets

- OpenReview：[lXiUD5V7wG](https://openreview.net/forum?id=lXiUD5V7wG)
- 查询命中：finite difference
- 核心贡献：研究共享检查点附近、由随机权重扰动得到的跨任务专家何时可合并，并提出 quality-constrained spectral selection，通过跨任务筛选、分层几何、独立验证与回退选择可组合专家对。
- 方法：随机权重扰动生成候选任务专家；选择阶段利用精确有限差分分解和谱排序比较专家对。摘要没有把该有限差分描述为梯度估计，也未说明候选专家如何被训练或搜索。
- 优化对象：来自共享检查点的任务专家权重及其合并/选择；实验包含至少 1.5B 参数模型，关键词明确为 Large Language Models。
- 反向传播：合并与选择过程的摘要未报告反向传播；候选任务专家的生成或训练是否包含反向传播待核实。
- 持久状态：输出是合并后的模型权重或回退到 base，属于持久模型状态；专家池本身也是持久外部资产。
- 仓库关联：真实涉及 LLM 权重扰动专家及无梯度的模型合并选择，但不是零阶梯度估计，作为模型合并/闭式选择边界收录。
- 待核实：作者身份、跨平台首次公开日期、代码（如摘要未列）、完整实现细节与评审结果待核实；实验结果仅按作者摘要记录。

### ZO-COSMO: Index-Free One-Hop Mixing for Decentralized Zeroth-Order Optimization

- OpenReview：[XhdOPTxLyT](https://openreview.net/forum?id=XhdOPTxLyT)
- 查询命中：zeroth-order
- 核心贡献：提出 ZO-COSMO，把两查询零阶估计与保持平均值的 masked consensus 结合，在无需显式坐标索引的一跳通信中完成稀疏去中心化更新，并在八个逻辑 Qwen LoRA worker 上验证。
- 方法：每个 worker 使用两次函数查询估计零阶方向；公共随机性与 masked consensus 只传每条活跃边 q 个数，支持全局支撑或成对匹配更新。
- 优化对象：八个逻辑 Qwen2-7B QNLI LoRA worker 的 LoRA 参数，以及合成去中心化目标；摘要未说明底座是否完全冻结，但明确实验优化 LoRA。
- 反向传播：核心 ZO-COSMO 使用两查询函数值估计而非目标反传；函数评估内部是否训练其他模块摘要未说明。
- 持久状态：各 worker 持久更新 LoRA 参数及稀疏动量/共识状态。
- 仓库关联：直接以 Qwen2-7B LoRA 为对象研究通信高效的去中心化零阶优化，属于主线 ZO 参数优化。
- 待核实：作者身份、跨平台首次公开日期、代码（如摘要未列）、完整实现细节与评审结果待核实；实验结果仅按作者摘要记录。

## 排除

| OpenReview | 标题 | 查询命中 | 具体理由 |
|---|---|---|---|
| [mrISpV3Pax](https://openreview.net/forum?id=mrISpV3Pax) | Adaptation as Memory: Learning to Correct Time Series Foundation Models | without backpropagation | 方法只适配时间序列基础模型（TSFM）的预测修正记忆；没有语言模型、VLM或语言代理优化关联。 |
| [v5JpKDwFAO](https://openreview.net/forum?id=v5JpKDwFAO) | AlphaG-OPD: Reliability-Gated Sibling Counterfactuals for On-Policy Distillation in Symbolic Alpha Factor Discovery | forward gradient | 研究符号量化因子发现的 GFlowNet 局部教学；“forward-gradient balancing”是其权重平衡术语，摘要没有 LLM/VLM 对象或梯度无关语言模型优化。 |
| [OMX73ebh7p](https://openreview.net/forum?id=OMX73ebh7p) | Building Neural Policies through Developmental Rewiring | neuroevolution | R-NDP 以 neuroevolution 构造一般强化学习控制策略网络，仅实验五个控制任务；无语言模型关联。 |
| [mlVqTuV7b8](https://openreview.net/forum?id=mlVqTuV7b8) | Closing the Loop on Masking Difficulty for Joint-Embedding Predictive Learning | gradient-free | 梯度无关传感器仅反馈控制 I-JEPA 图像遮罩数量，实验为 ImageNet/CLEVR 视觉表示学习；无语言模型优化。 |
| [0e6fe2MG5z](https://openreview.net/forum?id=0e6fe2MG5z) | Continual Learning on Graphs via Gradient-free Condensation | gradient-free | STREAMCGL 是图持续学习的单遍图凝聚算法，优化对象为 Weisfeiler–Leman 特征点集；无语言模型关联。 |
| [a9jMLEKM50](https://openreview.net/forum?id=a9jMLEKM50) | DACS: From Historical Inertia to Forward Evidence for Behavioral Authentication | forward-only | DACS 用导数自由的前向评估适配行为生物认证 verifier；任务与模型均无语言模型/VLM 关联。 |
| [2KFNPsh1y4](https://openreview.net/forum?id=2KFNPsh1y4) | DifferenceFlow: Dynamic Implicit Differences for One-Step Generative Modeling | finite difference | finite difference 替换生成模型的时间导数，实验是 ImageNet 图像生成且仍进行模型训练/微调；无语言模型关联。 |
| [9O4ySWc0G1](https://openreview.net/forum?id=9O4ySWc0G1) | EnRep: Energy-Induced Representations for Classification without Backpropagation | without backpropagation | EnRep 是手写数字与组织病理图像分类的能量表示和闭式分类器；无语言模型关联。 |
| [qNhfYunjC7](https://openreview.net/forum?id=qNhfYunjC7) | FASE: Factor-Aware Spectral Evolution for Gradient-Free Continuation of Diffusion Post-Training | gradient-free, CMA-ES, evolution strategies | FASE 对 Stable Diffusion 3.5 的 LoRA 奇异值做 CMA-ES 延续优化，属于纯图像扩散后训练；摘要没有语言模型或视觉语言模型优化。 |
| [CADnUczyZQ](https://openreview.net/forum?id=CADnUczyZQ) | Forward-Only Learning Across Black-Box Interfaces: State Persistence and Pilot Recovery | forward-only | 研究 Forward-Forward/DeeperForward ResNet 跨黑盒接口的状态持久性和 pilot 恢复；实验是一般视觉表示，无语言模型关联。 |
| [s5Es57znPS](https://openreview.net/forum?id=s5Es57znPS) | GenInv: Generative Inverse Learning for Cell Perturbation Prediction | forward-only | “forward-only”指细胞扰动预测的对照模型，论文自身以共享网络联合训练正向与逆向任务；无语言模型关联。 |
| [6wHdHqhDuM](https://openreview.net/forum?id=6wHdHqhDuM) | Gradient-Free Sampling from Generative Models via Stochastic Bounded Extremum Seeking | gradient-free | 无梯度 extremum-seeking 采样用于 CelebA-HQ/CIFAR-10 的图像生成模型；摘要未涉及 LLM/VLM 或语言代理优化。 |
| [PnuDAO3uyl](https://openreview.net/forum?id=PnuDAO3uyl) | How Sparsity Allocation Shapes Label-Free Post-Pruning Recoverability | gradient-free | 研究 ResNet 图像分类剪枝后的无标签、无梯度修复与稀疏分配；没有语言模型关联。 |
| [baKjpOzPGt](https://openreview.net/forum?id=baKjpOzPGt) | KSOS-BO: Improving Sampling in Bayesian Optimization via Kernel Sum of Squares | CMA-ES | CMA-ES 仅作为通用 Bayesian optimization acquisition 优化基线；所提 KSOS-BO 是核半定规划，且无语言模型对象。 |
| [KzW87to1Wm](https://openreview.net/forum?id=KzW87to1Wm) | Learning from Historical Overlap Errors: Adaptive Pointwise Reweighting for Time Series Forecasting | gradient-free | HORW 的“gradient-free sequential pass”只构建时间序列误差记忆，下一 epoch 仍以加权损失训练预测模型；无语言模型关联。 |
| [HDeeHC6So7](https://openreview.net/forum?id=HDeeHC6So7) | NearestPDE: Structured Backward Error for Ambiguity-Aware PDE Diagnosis | finite difference | finite-difference 只描述 PDE 数值场，所提方法诊断 PDE 系数/边界/几何误差；无语言模型关联。 |
| [fbvBYNTB0C](https://openreview.net/forum?id=fbvBYNTB0C) | NyS-Binary: A Feature-Free, Algebraic Framework for Binary Node Representation Learning | gradient-free | NyS-Binary 是图节点二值表示；“gradient-free learning”只出现在下游脉冲分类器兼容性讨论，无语言模型对象。 |
| [enaDfCn4w0](https://openreview.net/forum?id=enaDfCn4w0) | Partially Informed Stochastic Optimization via Zeroth-Order Residual Tracking | zeroth-order | PISO 是通用部分已知梯度加零阶残差跟踪理论，并测试 performative RL/路由；摘要没有 LLM/VLM 实例。 |
| [Ne1CKI7ey9](https://openreview.net/forum?id=Ne1CKI7ey9) | PhysibleMDM: Enforcing Inference-Time Physical Feasibility Constraints on Motion Diffusion Models via Noise Optimization | CMA-ES | Sep-CMA-ES 优化人体动作扩散模型的推理噪声与物理约束；无语言模型或语言骨干关联。 |
| [KdCdB5V6ku](https://openreview.net/forum?id=KdCdB5V6ku) | PotentialEP: Backprop-Free Training of CIFAR-Scale Generative Models via Equilibrium Propagation | backpropagation-free, without backpropagation | Equilibrium Propagation 训练 CIFAR 尺度卷积生成模型；尽管无反向传播，但没有语言模型/VLM 关联。 |
| [XfKMDwoz1B](https://openreview.net/forum?id=XfKMDwoz1B) | Q-Guided Drifting Policy: Value-Guided Target Construction for One-Step Offline Reinforcement Learning | zeroth-order | QGD 用 learned Q-function 对离线 RL 行为动作作零阶局部细化，再训练 drifting actor；实验为 OGBench/D4RL，无语言代理/模型关联。 |
| [HdeuL9qztS](https://openreview.net/forum?id=HdeuL9qztS) | Rollback and Repair: Reusing Trajectory Assets for Test-Time Scaling in Protein Design | derivative-free | TRACER 是蛋白质扩散生成的训练免测试时轨迹修复；“derivative-free”描述既有测试时方法，且无语言模型关联。 |
| [aiqFcQWTWT](https://openreview.net/forum?id=aiqFcQWTWT) | Searchability of Gene-Encoded Spiking Controllers under a Forward-and-Reproduction Energy Ledger | gradient-free, neuroevolution | MED-SNN 用遗传算法直接编码脉冲控制器拓扑、权重和代谢参数，实验仅 CartPole；无语言模型关联。 |
| [IA3PSttexX](https://openreview.net/forum?id=IA3PSttexX) | State-Aware Zeroth-Order Search for DR-Submodular Maximization | zeroth-order | SDS 是通用 DR-submodular maximization 的零阶直接搜索理论；无语言模型应用。 |
| [5H9yPPYAla](https://openreview.net/forum?id=5H9yPPYAla) | Tangent On-Policy Distillation: Local-Direction Supervision Beyond Outputs | finite difference | TOPD 的 finite difference 是相邻 token/层隐藏状态方向的监督量，并与点态匹配损失一起训练学生；它不是梯度无关参数优化，摘要也未声称免反向传播。 |
| [74gLFx6JkB](https://openreview.net/forum?id=74gLFx6JkB) | UNACT: GRADIENT-FREE UNLEARNING VIA TARGETED ACTIVATION INTERVENTION | gradient-free | UnAct 仅在 ResNet/ViT 图像分类上按激活衰减连接做类别遗忘；摘要没有语言模型或语言任务关联。 |

## 数据边界

本文件只证明这 30 条方法定向候选已逐摘要审查。它不证明 ICLR 2027 全会场或所有语言模型投稿已覆盖。论文结果只按作者官方摘要记录，未独立复现实验。
