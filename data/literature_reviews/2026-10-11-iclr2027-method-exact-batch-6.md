# ICLR 2027 方法定向检索候选审查：Batch 6

- 范围：`review-batch-6.json` 的 30 条官方 OpenReview 投稿摘要。
- 来源限定：明确方法词/精确短语查询；未使用裸 `LLM`、`language model` 或全会场枚举发现候选。
- 结论：新增收录 0，具体排除 30。排除的共同充分条件是官方摘要未同时给出语言模型/VLM 优化关联与所提方法的梯度无关机制；各条理由如下，不将基线、有限差分标签或普通语义命中当作所提方法。
- 日期：全部记录的 OpenReview `odate` 元数据为 2026-10-03T12:42:08.286Z；这只表示平台在线日期，不等于跨平台首次公开日期。

## 1. Adaptive Stepsizes Meet Momentum: An Improved Zeroth-Order Method

- OpenReview：[gK96j8p3Vx](https://openreview.net/forum?id=gK96j8p3Vx)
- 命中查询：zeroth-order, gradient-free
- 实际机制：ZO-AdaNesterov 用随机零阶 oracle 估计、自适应步长和 Nesterov 动量优化一般凸与非凸目标。
- 优化对象：一般数值实验中的深度网络参数。
- 反传/梯度依赖：所提优化器采用零阶 oracle；按摘要所述的 oracle 模型，无需反向模式梯度。
- 持久状态：持续更新被优化参数。
- 决定：排除。摘要未涉及语言模型、VLM、提示词或智能体应用，属于通用零阶优化理论。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 2. An Energy-Aware Sampling Method for Physics-Informed Neural Networks

- OpenReview：[b26gPbGN9O](https://openreview.net/forum?id=b26gPbGN9O)
- 命中查询：derivative-free
- 实际机制：PAS 根据无导数的双稳势信号分配 PINN 配点，并结合全局探索与局部细化。
- 优化对象：相场 PDE 训练的采样位置。
- 反传/梯度依赖：采样评分无导数；摘要未将下游 PINN 训练描述为无需反向传播。
- 持久状态：持续改变配点集合；是否持久更新模型权重未说明。
- 决定：排除。属于科学 PDE/PINN 工作，未体现语言模型或 VLM 关联。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 3. CABM: Efficient Concept Augmentation for Interpretable Deep Models

- OpenReview：[FZAUWsJD3m](https://openreview.net/forum?id=FZAUWsJD3m)
- 命中查询：parameter perturbation
- 实际机制：CABM 通过受影响函数启发的局部参数更新、EK-FAC 近似曲率和信赖域，在训练后添加概念。
- 优化对象：概念瓶颈模型中新追加的概念模块。
- 反传/梯度依赖：这是近似二阶/影响函数更新，并非梯度无关搜索；摘要没有证明无需反向传播。
- 持久状态：安装持久的概念模块/模型更新。
- 决定：排除。未涉及语言模型应用；“parameter perturbation”指问题表述，不是零阶扰动估计。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 4. Closing the Train-Test Gap in World Models for Gradient-Based Planning

- OpenReview：[PgUvaCo2j4](https://openreview.net/forum?id=PgUvaCo2j4)
- 命中查询：gradient-free
- 实际机制：该论文用合成数据训练世界模型，以改进基于梯度的测试时规划。
- 优化对象：机器人规划中的世界模型训练数据与动作序列。
- 反传/梯度依赖：所提规划器明确依赖梯度；梯度无关的 CEM 仅作为比较基线。
- 持久状态：世界模型权重经训练后持久保存；测试时动作是临时状态。
- 决定：排除。属于机器人/导航工作，未关联语言模型；仅提及基线不能使所提方法符合收录条件。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 5. Continual Reinforcement Learning with Neuroevolution

- OpenReview：[UxsGk4on0e](https://openreview.net/forum?id=UxsGk4on0e)
- 命中查询：evolution strategies, neuroevolution
- 实际机制：该研究比较在持续任务变化下对策略网络权重进行变异与选择的 ES 和遗传算法。
- 优化对象：强化学习策略的权重。
- 反传/梯度依赖：ES/GA 分支是梯度无关的权重空间搜索；被比较的 RL 方法可能使用梯度。
- 持久状态：演化所得策略权重跨任务保留。
- 决定：排除。摘要未说明 LLM、VLM、语言智能体或语言策略应用。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 6. Data Selection for Conditional Flow Matching via State–Velocity Geometry

- OpenReview：[NqKMGp6N98](https://openreview.net/forum?id=NqKMGp6N98)
- 命中查询：zero-order
- 实际机制：State-Jac 根据端点覆盖和代理局部响应 sketch 选择 flow matching 训练样本。
- 优化对象：用于 conditional flow matching 的核心数据子集。
- 反传/梯度依赖：“Zero-order”描述预先给定的监督几何，而非零阶优化器。
- 持久状态：所选数据集用于后续训练而持久保留；模型权重随后以摘要未说明的标准流程训练。
- 决定：排除。实验仅涉及图像 flow matching，未涉及语言模型优化。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 7. Distilling Diffusion Score Discrepancy for Efficient Training Data Attribution

- OpenReview：[ZzJWMU6dUI](https://openreview.net/forum?id=ZzJWMU6dUI)
- 命中查询：forward-only
- 实际机制：TID 以曲率/预条件梯度相似度估计扩散模型训练数据影响，TIDE 再把排序蒸馏到只需前向查询的学生模型。
- 优化对象：扩散生成图像的归因排序。
- 反传/梯度依赖：TID 使用梯度相似度和曲率；TIDE 推理仅需前向，但其学生模型经过明确训练。
- 持久状态：学生模型参数训练后持久保存；单次查询的排序不持久。
- 决定：排除。研究对象是扩散图像归因，而非语言模型优化。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 8. Epistemic Forward Models: Learning Predictive States for Action-Conditioned Future Distinguishability

- OpenReview：[qY8l677bHH](https://openreview.net/forum?id=qY8l677bHH)
- 命中查询：finite difference
- 实际机制：EFO 学习预测动作条件下的可辨识子空间，其监督信号由固定 RGB-D 编码器的有限差分 Jacobian 构造。
- 优化对象：机器人预测状态模型与动作选择。
- 反传/梯度依赖：有限差分用于构造离线标签，不是优化规则；摘要未说明训练是否使用反向传播。
- 持久状态：学习所得 EFO 模型持久保存；动作选择是临时状态。
- 决定：排除。属于纯 RGB-D 机器人/主动感知研究，没有 LLM 或 VLM 语言骨干。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 9. Fast-Weight Memory for Adaptive Recommendation

- OpenReview：[phwjDb6goi](https://openreview.net/forum?id=phwjDb6goi)
- 命中查询：gradient-free
- 实际机制：FWPRec 根据正负反馈更新用户专属的快速联想记忆，同时在推理时保持全局推荐器参数不变。
- 优化对象：推荐系统的用户级 fast-weight 记忆。
- 反传/梯度依赖：推理期记忆更新被描述为梯度无关；学习更新规则/模型的训练未被说明为梯度无关。
- 持久状态：用户记忆跨请求保留；推理时全局参数不变。
- 决定：排除。属于推荐系统适配机制，未涉及语言模型或 VLM 应用。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 10. From Decoder Backward to Encoder Forward: Antisymmetric Latent Updates for Diffusion Inverse Solvers

- OpenReview：[6kwgPuiq8R](https://openreview.net/forum?id=6kwgPuiq8R)
- 命中查询：forward-only
- 实际机制：ASLU 通过两次编码器前向计算的反对称差分，把像素校正映射为扩散潜变量更新。
- 优化对象：图像/视频逆问题采样过程中的潜变量。
- 反传/梯度依赖：ASLU 转换避开解码器和测量算子的梯度；其他产生校正量的求解器组件可能不同。
- 持久状态：采样潜变量是临时状态；摘要未描述模型权重更新。
- 决定：排除。用于图像、视频和 CT 逆问题求解，与语言模型无关。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 11. Geometric Regularization of Learned Behavior Spaces in Unsupervised Quality-Diversity Optimization

- OpenReview：[rtIp1pxlSG](https://openreview.net/forum?id=rtIp1pxlSG)
- 命中查询：neuroevolution
- 实际机制：AURORA-VC 在质量多样性搜索中，用方差和协方差惩罚正则化自动编码器学习到的机器人行为描述符。
- 优化对象：机器人策略库及其行为描述符自动编码器。
- 反传/梯度依赖：质量多样性搜索采用演化方法；描述符自动编码器经过训练，摘要未声称该组件无需反向传播。
- 持久状态：策略库和学习所得描述符参数持久保存。
- 决定：排除。属于机器人质量多样性优化，未使用语言模型或 VLM。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 12. Grow or Prune? Constructive Neuroevolution of Kolmogorov–Arnold Networks

- OpenReview：[pYpybkF5Yi](https://openreview.net/forum?id=pYpybkF5Yi)
- 命中查询：neuroevolution
- 实际机制：C-KAN 通过 Safe Mutation、行为物种形成和短程 Lamarckian 适配，演化用于符号回归的类型化样条边图。
- 优化对象：KAN 图结构与边参数。
- 反传/梯度依赖：演化阶段梯度无关；短程 Lamarckian 适配机制未说明，可能使用梯度。
- 持久状态：演化所得图结构与拟合参数持久保存。
- 决定：排除。属于符号回归/KAN 架构搜索，并非语言模型优化。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 13. Hq-Recycle: Efficient Bilevel Optimization through Adjoint Recycling

- OpenReview：[per4W4wDLF](https://openreview.net/forum?id=per4W4wDLF)
- 命中查询：finite difference
- 实际机制：Hq-Recycle 复用拟牛顿下层估计与伴随估计，并用方向有限差分曲率探针初始化隐式超梯度细化。
- 优化对象：一般双层优化中的伴随量与优化变量。
- 反传/梯度依赖：方法仍是隐式超梯度/拟牛顿方法；有限差分只是曲率探针，不是梯度无关的外层优化器。
- 持久状态：下层/外层变量与复用的伴随状态跨迭代保留。
- 决定：排除。摘要仅涉及线性分类和岭回归，没有语言模型应用。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 14. LaDiM: Layered Diagnosis for Multi-Agent Code Migration

- OpenReview：[qixS3l1Wsf](https://openreview.net/forum?id=qixS3l1Wsf)
- 命中查询：forward gradient
- 实际机制：LaDiM 协调 Translator、Verifier 和 Repair 三类 LLM 智能体，利用执行阶段差异与修复历史诊断和修复跨框架代码迁移。
- 优化对象：迁移后的代码与持久修复历史。
- 反传/梯度依赖：查询命中来自“forward, gradient computation, update”这一连续表述；摘要未提出梯度无关搜索或模型适配。
- 持久状态：修复历史和代码修订持久保存；未描述 LLM 权重更新。
- 决定：排除。虽然使用 LLM，但不存在符合范围的梯度无关优化机制。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 15. Learning Invariant Spike Representations For Robust Remote Sensing Detection

- OpenReview：[JqlxDi0k8a](https://openreview.net/forum?id=JqlxDi0k8a)
- 命中查询：without backpropagation
- 实际机制：SIP 联合训练不变脉冲表示，并在推理时聚合时间脉冲响应且不更新参数。
- 优化对象：脉冲遥感检测器表示与临时推理响应。
- 反传/梯度依赖：TSCI 推理不执行反向传播；PCT 是训练阶段，摘要并未否定其使用梯度。
- 持久状态：PCT 模型参数持久保存；TSCI 不更新参数。
- 决定：排除。属于遥感视觉/SNN 工作，不涉及语言模型。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 16. LESS: Lightweight Evolutionary Supernet Search in Minutes

- OpenReview：[ORAHHcnXVe](https://openreview.net/forum?id=ORAHHcnXVe)
- 命中查询：CMA-ES, evolutionary optimization
- 实际机制：LESS 先短暂预热 supernet，再对离散神经架构运行 CMA-ES，并执行候选条件化的 supernet 更新。
- 优化对象：CNN/NAS 架构与 supernet 权重。
- 反传/梯度依赖：CMA-ES 架构搜索梯度无关，但每个候选都会获得学习式 supernet 更新。
- 持久状态：选定架构/配置与 supernet 训练状态持久保存。
- 决定：排除。属于 NAS-Bench/CIFAR/ImageNet 架构搜索，未涉及语言模型应用。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 17. Neighbor Averaging as Perturbation: Risk-Aware Decentralized Federated Learning via Noise-Probed Sensitivity

- OpenReview：[zl4U97GZ9L](https://openreview.net/forum?id=zl4U97GZ9L)
- 命中查询：parameter perturbation
- 实际机制：NoRA 根据噪声探测敏感度和模型位移评估去中心化邻居模型平均的风险，并削弱高风险交互。
- 优化对象：联邦模型平均权重与本地客户端模型。
- 反传/梯度依赖：噪声探针用于估计敏感度；本地模型训练仍是 DFL 的一部分，摘要未声称其梯度无关。
- 持久状态：客户端模型和平均状态持久保存。
- 决定：排除。属于通用/CIFAR 联邦学习，未涉及 LLM 或 VLM 优化。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 18. Observable Geometry for Derivative-Free Optimization of Dynamical Systems

- OpenReview：[C69ql69qP4](https://openreview.net/forum?id=C69ql69qP4)
- 命中查询：derivative-free
- 实际机制：OM-EKI 构造响应感知坐标，并对结构化动力系统输出应用 ensemble Kalman inversion。
- 优化对象：Neural ODE、刚性 UDE 与脉冲递归模型的参数。
- 反传/梯度依赖：OM-EKI 无需导数；精确梯度和代理梯度只是比较设置。
- 持久状态：优化后的动力系统模型参数持久保存。
- 决定：排除。仅涉及科学动力系统与脉冲数字实验，没有语言模型应用。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 19. Past2Next: Past Action Conditioning Policy with Data-Augmented Tokenization

- OpenReview：[R8obaNz0uu](https://openreview.net/forum?id=R8obaNz0uu)
- 命中查询：finite difference
- 实际机制：Past2Next 用历史动作及其一阶、二阶时间有限差分作为机器人自回归策略的条件。
- 优化对象：机器人动作 token 与几何感知 tokenizer/策略。
- 反传/梯度依赖：有限差分是输入运动特征，不是函数值梯度估计或优化器。
- 持久状态：tokenizer 和策略参数经标准训练后持久保存；推理动作是临时状态。
- 决定：排除。属于机器人模仿学习，没有语言模型或符合范围的 VLM 优化。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 20. Physics-Informed Stochastic Configuration Machine: A Backpropagation-Free Neural Network with Fast Training involving Nonlinear Differential Equations

- OpenReview：[9TVnxhsWUC](https://openreview.net/forum?id=9TVnxhsWUC)
- 命中查询：backpropagation-free
- 实际机制：PI-SCM 对非线性物理算子作解析线性化，并连续求解最小二乘问题来获得网络权重。
- 优化对象：用于微分方程的物理信息网络权重。
- 反传/梯度依赖：所提训练明确无需反向传播，使用解析 Jacobian 与最小二乘，而不是零阶估计器。
- 持久状态：求解所得网络权重持久保存。
- 决定：排除。属于科学 PDE 学习，未使用语言模型或 VLM。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 21. Principled Backpropagation-Free Training via Layerwise Fenchel-Young Lifting

- OpenReview：[L6QLnBFEml](https://openreview.net/forum?id=L6QLnBFEml)
- 命中查询：backpropagation-free
- 实际机制：Lifty 将激活提升为优化变量，并使用逐层闭式 Fenchel–Young/近端更新。
- 优化对象：一般神经网络的激活与层参数。
- 反传/梯度依赖：明确无需反向传播，但摘要未展示语言模型应用。
- 持久状态：训练所得网络参数持久保存。
- 决定：排除。属于通用神经网络训练理论，摘要未说明 LLM/VLM 应用。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 22. Query Efficient Black-box Adversarial Attack via Dataset Distillation

- OpenReview：[hRc0sauHSE](https://openreview.net/forum?id=hRc0sauHSE)
- 命中查询：gradient-free
- 实际机制：DDAttack 使用蒸馏样本初始化并引导基于分数的黑盒对抗扰动搜索。
- 优化对象：输入空间的对抗扰动。
- 反传/梯度依赖：攻击搜索梯度无关；数据集蒸馏可能有自身训练流程，摘要未说明该流程。
- 持久状态：攻击扰动针对单个样本；蒸馏样本可能持久保存。
- 决定：排除。摘要只说明通用/对抗训练模型评估，没有语言模型或 VLM 目标。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 23. Rollback: Experience Backtracking in World Models for Policy Improvement

- OpenReview：[k7VrTpZ9RJ](https://openreview.net/forum?id=k7VrTpZ9RJ)
- 命中查询：forward-only
- 实际机制：Rollback 回退机器人世界模型、分支探索替代动作，并把反事实结果蒸馏成策略监督。
- 优化对象：机器人策略与世界模型经验。
- 反传/梯度依赖：“Forward-only”用于描述既有世界模型是被动代理，并非所提方法的梯度属性；训练细节未说明。
- 持久状态：世界模型和策略的改进持久保存。
- 决定：排除。属于真实机器人策略改进，不涉及语言模型优化。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 24. Second-Order Geometry of Generative Paths: Fragility and Targeted Refinement

- OpenReview：[JruDtQUl8A](https://openreview.net/forum?id=JruDtQUl8A)
- 命中查询：finite difference
- 实际机制：该工作度量生成路径的二阶弯曲/加速度风险，并据此分配细化预算。
- 优化对象：视觉生成路径中的评估/细化位置与扰动。
- 反传/梯度依赖：有限差分估计 material acceleration，用于诊断和分配；未提出零阶参数优化。
- 持久状态：未描述持久模型权重更新；细化分配仅用于当前运行。
- 决定：排除。属于视觉 flow/图像编辑分析，未关联语言模型。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 25. Simulator-Refined Diffusion for Radio-Frequency Inverse Design

- OpenReview：[IJWhEOL1pT](https://openreview.net/forum?id=IJWhEOL1pT)
- 命中查询：zeroth-order
- 实际机制：SRD 在扩散采样期间结合可微代理梯度和由不可微电磁模拟器评估的搜索。
- 优化对象：推理时生成的 PCB 布局。
- 反传/梯度依赖：这是混合方法：代理梯度提出方向，模拟器评估选择更新。
- 持久状态：生成布局作为输出持久保存；未描述扩散模型权重更新。
- 决定：排除。用于 RF 电路逆向设计，并非语言模型/VLM 优化。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 26. Stein Guidance without Gradients: Discretization Uniform Diffusion Inference Time Scaling beyond Particle SMC

- OpenReview：[JOo32CtWHH](https://openreview.net/forum?id=JOo32CtWHH)
- 命中查询：derivative-free, without gradients
- 实际机制：该方法使用 Gaussian-Stein 值加权候选选择，并以无导数的全路径 independence-MH 校正扩散推理。
- 优化对象：扩散推理过程中的提议轨迹。
- 反传/梯度依赖：引导和 MH 校正使用函数值而非目标梯度；摘要未说明价值函数如何获得。
- 持久状态：轨迹状态是临时的；未说明模型权重更新。
- 决定：排除。属于通用扩散采样理论，摘要未涉及文本/LLM 应用。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 27. The Multi-Query Paradox in Zeroth-Order Optimization

- OpenReview：[7Yl2JKKec1](https://openreview.net/forum?id=7Yl2JKKec1)
- 命中查询：zeroth-order
- 实际机制：该论文分析 ZO-Avg 与基于投影的 ZO-Align 在标准目标类别上的查询分配。
- 优化对象：一般优化变量。
- 反传/梯度依赖：两种被分析算法均使用函数值查询，而非显式梯度。
- 持久状态：优化变量持续更新，但未指定模型或应用。
- 决定：排除。属于通用零阶理论，没有语言模型实验或分析。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 28. Value-Twisted Sequential Monte Carlo for Task-Aware Missing-Modality Connectome Completion

- OpenReview：[zndZYf5lWa](https://openreview.net/forum?id=zndZYf5lWa)
- 命中查询：gradient-free
- 实际机制：VT-SMC 使用冻结的、具不确定性感知的任务反馈与校正粒子，从效用倾斜分布采样扩散生成脑连接组。
- 优化对象：缺失模态的脑连接组与粒子状态。
- 反传/梯度依赖：框架允许梯度无关变体；摘要未完整区分主要/最终变体及其训练依赖。
- 持久状态：生成的连接组是输出；推理时任务反馈/模型参数冻结。
- 决定：排除。属于医学影像/连接组补全，与语言模型无关。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 29. When Does Derivative Supervision Help? A Study of Label Construction and Noise

- OpenReview：[ayiQSugiuW](https://openreview.net/forum?id=ayiQSugiuW)
- 命中查询：finite difference
- 实际机制：该研究在同一神经网络训练流程下，比较导数标签的构造方式与噪声水平。
- 优化对象：导数监督标签与一般科学预测器。
- 反传/梯度依赖：有限差分用于构造标签，并非无导数优化方法；训练仍是常规流程。
- 持久状态：预测器权重训练后持久保存。
- 决定：排除。属于科学导数监督研究，未涉及语言模型应用。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。

## 30. ZOBA: An Efficient Single-loop Zeroth-order Bilevel Optimization Algorithm

- OpenReview：[4tp5TPhaoL](https://openreview.net/forum?id=4tp5TPhaoL)
- 命中查询：zeroth-order, finite difference
- 实际机制：ZOBA/HF-ZOBA 复用延迟函数值，以有限差分近似超梯度来进行单循环双层优化。
- 优化对象：一般双层问题的内层与外层变量。
- 反传/梯度依赖：外层超梯度由函数值近似；摘要未解决内层求解器是否需要梯度。
- 持久状态：内层/外层优化变量持续更新。
- 决定：排除。属于通用理论和未具体说明的对抗机器学习任务，没有 LLM/VLM 应用。
- 待核实：仅审阅了官方投稿摘要；实现、补充材料、代码、作者身份披露及跨平台首次公开日期均未独立核实。
