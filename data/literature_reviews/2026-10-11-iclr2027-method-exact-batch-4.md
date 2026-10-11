# ICLR 2027 方法定向 exact 查询候选审查（批 4）

- 审查日期：2026-10-11（Asia/Shanghai）
- 来源：OpenReview `ICLR.cc/2027/Conference`、`source=forum` 的方法定向 exact 查询缓存。
- 范围：本批 30 条；逐条阅读缓存中的官方投稿摘要。
- 结果：收录 1 条，排除 29 条。排除只表示不符合本仓库“梯度无关机制与语言模型优化存在具体关联”的范围，不是论文质量判断。
- 证据限制：机制、实验和状态均据官方投稿摘要/元数据；未读取正文或独立核验实现。全部记录的 OpenReview `odate` 为 `2026-10-03T12:42:08.286Z`，只表示 OpenReview 平台公开时间，不等于跨平台首次公开日期。

## 收录

### HO-FL: Hybrid-Order Federated Learning for Heterogeneous Edge Devices (`iVQu1sp529`)

- 查询命中：`zeroth-order`
- 分类：`related_hybrid`
- 贡献：HO-FL 让客户端按内存预算选择模型分段边界，以 ZO 训练底段、FO 训练顶段；其分析把分段大小造成的更新质量与客户端数据代表性联系起来，并给出采样近似。摘要明确报告语言任务实验。
- 方法和对象：ZO 持久更新模型底段参数，FO 持久更新顶段参数，服务器直接平均本地模型；客户端采样也会调整。
- 反向传播：顶段明确使用 FO，摘要把 FO 等同于 backpropagation；底段使用 ZO。采样近似是否含其他训练模块待核实。
- 待核实：摘要未列具体语言数据集、模型架构和 ZO 估计器；匿名代码链接尚未核验实现。
- 原文：https://openreview.net/forum?id=iVQu1sp529

## 排除

| OpenReview ID | 标题 | 方法查询 | 逐条理由 |
|---|---|---|---|
| `RsMuuQsUtz` | Accelerated Methods for Nonconvex Optimization Using Comparisons | zeroth-order | 比较 oracle 的一般非凸优化理论；虽以比较结果估计方向，但无 LLM/VLM 应用。 |
| `Gty08pINJE` | AESplat: Advancing Pose-Free Feed-Forward 3D Gaussian Splatting via Decoupled Appearance Modeling | zeroth-order | “zeroth-order”指球谐零阶系数，不是 ZO 优化；任务为 3DGS。 |
| `Qa7SpKjN6C` | Budget-Aware Step Selection for Forward-Only Recovery of Analog Accelerators | forward-only | 面向模拟交叉阵列漂移恢复的步长选择，无语言模型。 |
| `G6fuD02eUD` | Causal Discovery via complexity-gated spiking neural networks | gradient-free | 固定脉冲 reservoir 与 WTA 可塑性做时间序列因果发现，无语言模型。 |
| `foulTd1ZUb` | Constrained Diffusion from Binary Evaluations via Learned Doob h-Functions | derivative-free | 所提方法以平方误差训练约束头；derivative-free selection 只是基线，且为扩散生成。 |
| `JQwie0bKBb` | Correcting Trajectory Drift in Flow Matching Models | finite difference | 有限差分估计采样轨迹加速度并调时间步，不是语言模型参数或外部工件优化。 |
| `fuXZocOUBF` | Detecting Audio-Visual Deepfakes Outside the Generator Objective | zero-order | zero-order cosine 是音视频检测统计量，不是语言模型优化。 |
| `mPl8sAMr9g` | EG-Opt: Efficient Learning for Nonlinear Programming via Explicit Gradients from Sample-Calibrated Linear Surrogates | zeroth-order | 所提方法使用显式梯度；ZO 仅为工程优化比较基线。 |
| `i2EdO6YkEj` | Exposing Local Vulnerabilities in Neural Routing Solvers with an Efficient Black-Box Attack | evolution strategies | Adam-ES 搜索 TSP/CVRP 对抗实例，后续微调路由求解器；无语言模型。 |
| `JadfZVJabx` | First-Order Bilevel Optimization for Non-truthful Auction Design | zeroth-order | 所提拍卖算法明确为 fully first-order，ZO 只是基线，也无语言模型。 |
| `iP3mhGLBfO` | Generative Refinement for Low-Budget Black Box Optimization | evolutionary optimization | 固定生成采样器辅助通用低预算黑盒搜索；摘要无 LLM/VLM 应用。 |
| `tAxD9PKXww` | Gradient Estimation View of Zeroth-Order Optimizers | zeroth-order; derivative-free; evolution strategies; finite difference | 统一 ZO 更新的理论工作，没有语言模型应用实例。 |
| `jDFuw9smxN` | JANUS: Online Jacobian-Aligned Infill for Black-Box Optimization | CMA-ES | 为 CMA-ES 等宿主在线估局部 Jacobian，实验为 BBOB、路径规划等，无语言模型。 |
| `zkIJpaca3W` | Learnable Membrane Time Constants for Structure Dynamics in Recurrent Spiking Neural Networks | backpropagation-free; forward gradient | DCFO 更新 RSNN 连接和膜时间常数，实验为 Brax 控制，无语言模型。 |
| `tkUqPJJvZk` | Learning Where to Search: Evolutionary Embedding Search for High-Dimensional Bayesian Optimization | derivative-free | 导数无关进化搜索 BO 嵌入，应用为轨迹规划和 SVM，无语言模型。 |
| `I3q1ZdbQow` | MetaLearnNCA: Few-Shot Offline Meta-Learning via Interacting Neural Cellular Automata | gradient-free | NCA 在推理时更新二维 spatial program，实验均为图像分类。 |
| `JzjNi4rkcX` | Not Every Correction Helps: Gain-Guided Continual Test-Time Adaptation | backpropagation-free; without backpropagation | GAIN 以一维优化调节视觉预测校正并更新目标统计；无 LLM/VLM 实验。 |
| `KlnPPPCCiO` | Parallel Memristive-Friendly Reservoirs for Gradient-Free Long-Sequence Classification | gradient-free | 冻结 reservoir、岭回归读出用于时间序列分类；“sequence model”不等于语言模型。 |
| `e8tYFmI6d8` | PHASE: Packet-level Hierarchical Adversarial Semantic Exploitation for Targeted Steering of Retrieval-Augmented Diffusion Models | gradient-free | 训练/梯度无关地搜索扩散模型 conditioning packet，但摘要没有语言或视觉语言模型证据。 |
| `JzPDBEz1rL` | PoSTCache: From Forecasting to Postdictive Smoothing for Revisable Diffusion Caching | forward-only | “forward-only”描述旧缓存的信息流；所提方法回修图像/视频扩散缓存，不是梯度无关语言优化。 |
| `fXrQoDssZW` | Procedural Adversarial Training | zeroth-order | ZO 搜索程序化视觉场景参数，学习器训练视觉模型；无语言模型。 |
| `pqw6kWr6kt` | Risk Decomposition for Hallucination-Aware Video Sampling | finite difference | 有限差分用于 CNF divergence 评分估计，任务为视频物理采样。 |
| `55geiEe08j` | SCULPT: Backpropagation-Free Linear-Head Adaptation with Symbolic Constraints | backpropagation-free | 机制确为冻结表征上的线性头适配，但任务仅路由、视觉数独与数字加法，摘要无 LLM/VLM。 |
| `pwseyFaKAp` | Sharpen Your Flow: Sharpness-Aware Sampling for Flow Matching | finite difference | 有限差分建立 flow 轨迹锐度剖面来排时间步，无语言模型应用。 |
| `d7T8HVLoWJ` | Stabilizing Variational Information Bottleneck Under Covariance Shift | finite difference | 有限差分只是视觉 VIB 的 Jacobian 正则代理，并非独立梯度无关优化。 |
| `1UIq0cjyZB` | SWAGES: System-Wide Attention and Guided Evolution for Dynamic Workflow Scheduling | evolution strategies | critic 梯度引导 ES 搜索云调度策略，既是混合方法又无语言模型关联。 |
| `axMSdpe80b` | Touch2Predict: Learning Physical Properties from a Single Tactile Interaction | derivative-free | 姿态做导数无关搜索、材料参数用 adjoint，属于机器人逆物理。 |
| `D8E6bb0Ioc` | When and Why Can Test-Time Adaptation Succeed? | backpropagation-free | PRISM 为视觉 TTA 的 optimization-free 方法；没有语言模型应用。 |
| `WwFl5oMZuN` | Zeroth-Order SGD with Momentum Resetting Achieves Dimension-Dependent Optimality in Nonsmooth Nonconvex Optimization | zeroth-order | 一般非光滑非凸 ZO-SGDM 理论，没有 LLM/VLM 应用。 |

机器可读逐条证据：`/tmp/iclr2027-catalog-20261011-attempt10/method-exact-all/review-batch-4-decisions.json`。
