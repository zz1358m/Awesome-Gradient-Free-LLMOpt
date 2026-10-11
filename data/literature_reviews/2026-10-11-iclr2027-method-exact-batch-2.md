# ICLR 2027 方法定向 exact/content=all 审查：批次 2

- 审查日期：2026-10-11
- 范围：`review-batch-2.json` 的 30 条官方 OpenReview 投稿摘要；每条均来自明确方法短语查询，不来自裸 `language model`/`LLM` 全语料。
- 结论：纳入 0，排除 30。这里的“排除”仅指与“梯度无关语言模型优化”目录范围不符，不评价论文质量。
- 状态：30 条的 `venueid` 均为 `ICLR.cc/2027/Conference/Submission`；官方 `odate` 均为 `2026-10-03T12:42:08.286Z`。该日期只表示 OpenReview 平台在线时间，不代表跨平台首次公开日。
- 完整逐模块判断：`/tmp/iclr2027-catalog-20261011-attempt10/method-exact-all/review-batch-2-decisions.json`。

| OpenReview | 定向命中 | 决定 | 逐摘要理由 |
|---|---|---|---|
| [A Decodability-Grounded Audit of Clinical Prediction Claims in PPG Foundation Models](https://openreview.net/forum?id=WGmQvuKFU7) | derivative-free | 排除 | “target-derivative-free adjustment”是临床协变量调整术语；对象为PPG/ECG表征审计，不是DFO或语言模型优化。 |
| [Adversarial Nonlinear Semi-Bandits: Hidden Interactions and Amplitude-Sensitive Regret](https://openreview.net/forum?id=upWPVRvJgl) | finite difference | 排除 | finite-difference certificate是理论交互强度证书；纯semi-bandit遗憾理论，无语言模型应用。 |
| [Beyond Endpoint Flatness: Policy Scale Dynamics Shape Robustness in SAM-PPO](https://openreview.net/forum?id=PLRaAvjC3v) | parameter perturbation | 排除 | 扰动属于一阶SAM-PPO；实验为MuJoCo控制，无语言模型对象。 |
| [Capturing Inter-Task Reinforcement Learning Dynamics for Adaptive Task-Sampling](https://openreview.net/forum?id=nM3Mq6pJKX) | evolution strategies | 排除 | DynATS确以ES训练任务采样器，但仅用于网格、MuJoCo和Meta-World的多任务RL。 |
| [CoFlow: Coordinated Few-Step Flow for Offline Multi-Agent Decision Making](https://openreview.net/forum?id=fY24M8lXXp) | finite difference | 排除 | 有限差分近似一致性训练修正项；对象为MPE/SMAC多智能体轨迹生成。 |
| [Control-Guided Molecular Diffusion for Training-Free Conditional 3D Molecule Generation](https://openreview.net/forum?id=1DyQYjjUM3) | zeroth-order | 排除 | ZO梯度恢复是被绕开的既有方法；所提控制引导用于3D分子扩散。 |
| [Decentralized Zeroth-Order Gradient Tracking For Bilevel Optimization](https://openreview.net/forum?id=NCqeOwpR0z) | zeroth-order | 排除 | 真实ZO双层优化，但摘要只有一般共享模型/超参数问题，没有语言模型应用。 |
| [Do Not Cross the Boundary: Within-Class Whitening for Test-Time Adaptation](https://openreview.net/forum?id=RRmA0m7gUL) | without backpropagation | 排除 | WCW是不反传的类内协方差白化插件，但摘要未给出LLM/VLM或语言任务。 |
| [Evolving Hybrid Quantum–Classical Architectures for Image Classification](https://openreview.net/forum?id=w5DM9caMRz) | neuroevolution | 排除 | 遗传搜索量子电路结构，实验仅为图像分类。 |
| [FENCE: Enforcing Mixed Functional Constraints in Neural Fields](https://openreview.net/forum?id=uZh7BlEzg3) | finite difference | 排除 | 有限差分仅用于约束验证检查；方法是可微QP神经场，应用为热设计和动作重定向。 |
| [GCAM-Gym: A Benchmark for AI-Driven Climate Policy Design](https://openreview.net/forum?id=YJvSS3wCbn) | CMA-ES | 排除 | CMA-ES真实搜索气候政策，但没有语言模型优化对象。 |
| [GFlowNets build feasible designs for directed evolution campaigns](https://openreview.net/forum?id=kFVK8WyNiQ) | CMA-ES | 排除 | CMA-ES只是EvoGFN的对比管线；对象是蛋白质序列而非语言模型。 |
| [HermiteTwin: Bicubic Hermite Shell Digital Twins for Contact-Rich Deformable Manipulation](https://openreview.net/forum?id=0QXB9nl5QA) | CMA-ES | 排除 | CMA-ES后接伴随法辨识材料/接触参数；纯机器人可变形物体数字孪生。 |
| [Interaction Steering for Compositional Robustness in Vision Models](https://openreview.net/forum?id=fYBjJWGrNR) | finite difference | 排除 | 有限差分隔离视觉因素交互并构造辅助损失；纯视觉监督。 |
| [Latent Space Planning with Sequential Monte Carlo](https://openreview.net/forum?id=EsBS8s9n6I) | zero-order | 排除 | ZO规划器是比较对象，所提SMC可与梯度框架结合；未给出语言模型应用。 |
| [Learning to Adapt Without Gradients: Emergence of Mental Representations via Second-Order Learning](https://openreview.net/forum?id=n9u2EkRfz5) | without gradients | 排除 | 测试时前向控制器调节GCN，但任务是迷宫和道路网络图。 |
| [Masked Diffusion Modeling for Anomaly Detection](https://openreview.net/forum?id=BD501aT6sD) | forward-only | 排除 | “forward-only”指避免reverse-time diffusion sampling；文本异常检测不等于优化语言模型。 |
| [Non-Smooth Non-Convex Stochastic Optimization: Sign-Based Methods and Beyond](https://openreview.net/forum?id=ZpeZKr5jon) | zeroth-order | 排除 | 真实ZO/压缩优化理论，但没有语言模型实验或应用。 |
| [Orthogonalization Separates Sharpness Exploration from Perturbed Gradient Updates](https://openreview.net/forum?id=cUSWy17TNR) | parameter perturbation | 排除 | MuonSAM明确依赖clean与perturbed gradients；仅称“language tasks”，不足以证明LLM/VLM优化。 |
| [Peering over the Manifold Vistas: A Unified Geometric Framework for Counterfactual XAI](https://openreview.net/forum?id=RlyUgxpm8I) | zeroth-order | 排除 | ZO Jacobian仅用于黑盒半导体计量实验；无语言模型应用。 |
| [Plasmax: Differentiable & Parallelizable Environments for Tokamak Control](https://openreview.net/forum?id=ODnc0BqTZ5) | CMA-ES; evolution strategies | 排除 | ES/CMA-ES真实用于托卡马克控制，无语言模型或语言代理。 |
| [Probability Measure Gradient Flows for Diffusion-Based Amortized Optimization](https://openreview.net/forum?id=FtpY3WzkCB) | zeroth-order | 排除 | DiFlowOpt混用一阶和ZO目标信息，但摘要未给出语言模型/VLM应用。 |
| [Regressive-Dual PINN: Faster and More Reliable Training for Long-Horizon PDEs.](https://openreview.net/forum?id=e5rlO61XDB) | finite difference | 排除 | 有限差分计算PDE二阶导数，不是模型参数DFO；纯PINN求解。 |
| [Sample Efficient World Models using Gradient Penalized Latent Dynamics](https://openreview.net/forum?id=cgGAzHaB9R) | finite difference | 排除 | 有限差分只用于推导邻域惩罚极限；方法训练DreamerV3潜动力学，非语言模型。 |
| [SGIQ: Sparse-Gradient-Informed Gradient Estimation for Variational Quantum Circuits](https://openreview.net/forum?id=RBnIugC2ZF) | SPSA | 排除 | SPSA与parameter-shift rule混合估计量子电路梯度；无语言模型关联。 |
| [SPADE-DFL: Communication-Efficient Decentralized Federated Learning via Derivative-Free Linearized ADMM](https://openreview.net/forum?id=S4bbdlhtsZ) | derivative-free | 排除 | 真实one-point DFO联邦学习，但摘要的四项分类任务未指明语言模型/VLM。 |
| [Structure-Preserving Frozen Neural Operators](https://openreview.net/forum?id=QHEILFxGty) | gradient-free | 排除 | “gradient-free core”是冻结Fourier表示上的线性代数PDE求解；无语言模型关联。 |
| [To Gate or Not to Gate? When Does an Input-Dependent Gating Pay Off in Multi-Class Dendritic Gated Networks](https://openreview.net/forum?id=BldtP95aQi) | without backpropagation | 排除 | 所提DGN确用局部凸更新；DER++等反传方法只是基线，但任务全为图像持续分类。 |
| [Wall-Clock Complexity for Zeroth-Order Optimization with Tunable Oracle Fidelity](https://openreview.net/forum?id=ReQSSCt1Eo) | zeroth-order | 排除 | 真实ZO wall-clock理论，没有语言模型应用。 |
| [Why Learn What You Can Compute? Closed-Form Operators for Periodic Time-Series Forecasting](https://openreview.net/forum?id=51E3DimEN4) | gradient-free | 排除 | CAPE是周期时间序列的闭式岭式拟合，无语言模型/VLM对象。 |

## 质量控制说明

- 没有把基线中出现的 CMA-ES、ZO 或反向传播归到所提方法。
- 没有把 `finite difference` 的验证、理论证书、PDE导数近似自动认定为参数优化。
- 没有把 `forward-only` 自动解释为无需反向传播训练。
- 对摘要未说明的训练实现写为待核实；排除依据是任务对象不属于语言模型优化，而非借未知字段作确定性推断。
