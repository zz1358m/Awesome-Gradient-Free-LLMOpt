# ICLR 2027 方法定向 exact/content=all 候选审查：批次 1

- 审查日期：2026-10-11
- 主来源：OpenReview 官方投稿 note 的标题、摘要、关键词和 venueid 缓存。
- 范围：用户允许的方法短语 `type=exact&content=all` 查询所得31条；词面命中不等于主题相关。
- 结果：1条建议补收录，30条排除。所有记录均保留逐篇依据。

> `openreview_online_at` 仅表示 OpenReview 平台公开日期，不等于跨平台首次公开日期。

## 1. 4D Point Splatting for mmWave Radar Micro-Doppler Differentiable Rendering

- OpenReview：[5FWBc0Cays](https://openreview.net/forum?id=5FWBc0Cays)
- 命中查询：forward-only
- 决定：`exclude`
- 核心贡献：提出可拟合真实动态人体雷达采集的4D点泼溅可微渲染器，用于合成mmWave雷达训练数据。
- 方法判断：“forward-only”仅指既有雷达模拟器；本文核心是可微逆渲染，不是梯度无关语言模型优化。
- 更新对象：雷达场景的材质、法线、速度等显式表示。
- 反向传播：摘要称其为可微渲染并执行拟合，具体反传实现未说明。
- 持久状态：拟合后场景表示是否作为持久状态保留未说明。
- 仓库关联：纯雷达感知与可微渲染，无LLM/VLM优化关联。
- 待核实：完整实现训练细节待核实，但不影响范围外判断。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 2. AdaptoFlux: A Typed Graph Representation Substrate for Stateful Symbolic Program Synthesis

- OpenReview：[bv2vITgGyH](https://openreview.net/forum?id=bv2vITgGyH)
- 命中查询：gradient-free
- 决定：`exclude`
- 核心贡献：提出带类型检查和外部状态读写的GDFG表示底座，以轻量梯度无关搜索验证程序空间可导航性。
- 方法判断：梯度无关搜索只是表示可行性的探针；论文明确不提出新优化算法。
- 更新对象：类型化可执行程序图及其隐式外部状态。
- 反向传播：摘要未说明搜索器是否涉及任何可训练神经模块。
- 持久状态：程序图和外部状态可持久保存；无语言模型权重。
- 仓库关联：一般符号程序合成，摘要没有语言模型或语言代理应用。
- 待核实：proof-of-concept搜索器的具体算法待原文核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 3. Are Neural Models Always Necessary For Irregular Time Series Forecasting?

- OpenReview：[vgJbgsHx68](https://openreview.net/forum?id=vgJbgsHx68)
- 命中查询：gradient-free
- 决定：`exclude`
- 核心贡献：构建Anchor透明诊断基线，检验不规则多变量时间序列基准是否真正需要神经模型。
- 方法判断：gradient-free指持久、平滑、稀疏重复等非神经诊断规则，并非LLM优化。
- 更新对象：时间序列预测规则及经验规则选择。
- 反向传播：Anchor规则不需反传；对照神经基线的训练不属于所提方法。
- 持久状态：经验选择的规则可保留，无模型权重更新。
- 仓库关联：纯时间序列预测诊断，与语言模型优化无关。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 4. Caffeinate: Recovering Dormant Subnetworks in Modern Convolutional Neural Networks

- OpenReview：[ibXtIxvO2e](https://openreview.net/forum?id=ibXtIxvO2e)
- 命中查询：without gradients
- 决定：`exclude`
- 核心贡献：提出Caffeinate，以闭式方式校正剪枝CNN的LayerNorm仿射参数，恢复逐通道输出矩。
- 方法判断：仅用前向和无标签数据求闭式校正；对象是现代CNN。
- 更新对象：剪枝CNN的LayerNorm仿射参数。
- 反向传播：Caffeinate据摘要无需梯度；CHITA使用二阶信息仅是比较/组合的剪枝方法。
- 持久状态：校正后的LayerNorm参数是持久模型权重。
- 仓库关联：实验全部为ImageNet CNN，无语言模型关联。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 5. CMDO: A Cognitive Memory-Driven Optimization Algorithm for Adaptive Population-Based Search

- OpenReview：[n7i8pUutpH](https://openreview.net/forum?id=n7i8pUutpH)
- 命中查询：derivative-free, CMA-ES
- 决定：`exclude`
- 核心贡献：提出带工作、情景和巩固记忆的导数无关群体优化器CMDO，按上下文检索搜索策略。
- 方法判断：群体式导数无关搜索以函数值结果调整搜索行为。
- 更新对象：通用连续黑盒变量；另验证光伏模型七参数。
- 反向传播：核心优化器不使用反传；摘要未涉及训练神经组件。
- 持久状态：搜索记忆与候选群体持久更新，不涉及语言模型参数。
- 仓库关联：通用BBOB/CEC与光伏参数估计，无语言模型应用。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 6. Continuous Search Allocation: Jointly Shaping Probes and Updates for Query-Efficient Black-Box Video Attacks

- OpenReview：[d394H1GLAg](https://openreview.net/forum?id=d394H1GLAg)
- 命中查询：zeroth-order
- 决定：`exclude`
- 核心贡献：提出CSA，按坐标连续分配视频黑盒攻击的零阶探针和更新强度，以减少查询。
- 方法判断：对视频攻击扰动执行加权零阶探针与更新。
- 更新对象：视频输入对抗扰动。
- 反向传播：攻击环路为零阶查询；受害模型训练方式不属于所提攻击。
- 持久状态：攻击扰动在迭代中持久更新，受害模型权重不更新。
- 仓库关联：纯视频识别黑盒攻击，摘要无VLM或语言模型。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 7. DECAF: Decomposition of Evidence, Contradiction, and Fragility in Perturbation Responses

- OpenReview：[oow1GzZSQm](https://openreview.net/forum?id=oow1GzZSQm)
- 命中查询：forward-only
- 决定：`exclude`
- 核心贡献：提出DECAF，将扰动响应分解为证据、矛盾与脆弱性，用于解释预测变化。
- 方法判断：forward-only指沿输入揭示路径执行前向归因，不是参数优化。
- 更新对象：解释轨迹与归因分量，不更新模型。
- 反向传播：DECAF只需前向；摘要中的梯度基线仅供比较。
- 持久状态：无持久模型更新；产生解释结果。
- 仓库关联：实验为视觉和表格模型，无语言模型应用。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 8. Divergence-Aware Flow Likelihoods for Industrial Anomaly Localization

- OpenReview：[BZlMmPacyO](https://openreview.net/forum?id=BZlMmPacyO)
- 命中查询：forward-only, finite difference
- 决定：`exclude`
- 核心贡献：提出FlowAD，在冻结视觉基础模型特征上学习流匹配密度，并以有限差分Hutchinson探针估计推理期散度。
- 方法判断：前向有限差分只用于估计流似然散度。
- 更新对象：推理期异常分数；训练对象为视觉特征上的流模型。
- 反向传播：流模型训练的反传细节未说明；散度估计为前向探针。
- 持久状态：训练后的流密度模型持久；推理探针不改参数。
- 仓库关联：工业视觉异常定位，无语言模型关联。
- 待核实：训练实现待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 9. Evolutionary One-Step Generators: Fast and Diverse Sampling for Discrete Design

- OpenReview：[ncIgYIZi4s](https://openreview.net/forum?id=ncIgYIZi4s)
- 命中查询：evolution strategies
- 决定：`exclude`
- 核心贡献：提出EGO，以低秩反向采样进化策略训练一次推理的离散图生成器。
- 方法判断：进化策略直接优化硬解码后的约束和奖励，不要求可微代理。
- 更新对象：分子图或神经架构的生成器参数。
- 反向传播：ES环路本身不反传判据；分布匹配项的训练细节需原文核实。
- 持久状态：训练后生成器权重持久更新。
- 仓库关联：面向分子与NAS离散设计，不是语言模型或语言代理优化。
- 待核实：混合损失是否含梯度步骤待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 10. Fed-MOZOO: Federated Multi-Objective Online Zeroth-Order Optimization with Intermittent Communication

- OpenReview：[PADSR4oMaD](https://openreview.net/forum?id=PADSR4oMaD)
- 命中查询：zeroth-order
- 决定：`exclude`
- 核心贡献：提出Fed-MOZOO，以两点函数值估计、偏好标量化、投影更新和周期聚合处理联邦多目标在线优化。
- 方法判断：两点零阶估计外加周期模型聚合。
- 更新对象：通用凸多目标在线模型变量。
- 反向传播：所提更新使用函数值反馈，不需目标梯度。
- 持久状态：联邦局部/全局模型随轮次持久更新。
- 仓库关联：仅合成与凸多目标任务，无语言模型应用。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 11. Gauss–Newton is Blind to Embedded Saddles: Value-Trained Surrogates as a Derivative Oracle for Amortized Inversion

- OpenReview：[ZJBy5QMwdt](https://openreview.net/forum?id=ZJBy5QMwdt)
- 命中查询：finite difference
- 决定：`exclude`
- 核心贡献：分析嵌入鞍点为何对Gauss–Newton不可见，并用值训练神经代理提供摊销逆问题所需导数。
- 方法判断：finite difference是昂贵经典逃逸方案的成本对照；主方法用代理导数。
- 更新对象：光谱线型逆问题参数与神经代理。
- 反向传播：代理以函数值训练，但训练是否反传未在摘要明确；在线LM使用代理导数。
- 持久状态：训练后的代理持久；每个逆问题参数被优化。
- 仓库关联：物理逆问题，无语言模型关联。
- 待核实：代理训练实现待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 12. Geometry-Aware Robust Denoising via Hierarchical Manifold Traversal

- OpenReview：[t26i2Tk32y](https://openreview.net/forum?id=t26i2Tk32y)
- 命中查询：zero-order
- 决定：`exclude`
- 核心贡献：提出分层流形遍历网络，以逐层初始化改善引力波和图像去噪。
- 方法判断：zero-order shortcuts是既有图遍历描述，核心为多分辨率层次遍历。
- 更新对象：流形图节点与去噪路径。
- 反向传播：摘要未说明一次性构图/训练是否使用梯度。
- 持久状态：构建后的层次图持久保留。
- 仓库关联：引力波、MNIST/CIFAR/CelebA去噪，无语言模型关联。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 13. GS-MoE: Training-Free MoE Compression via Groupwise Subspace Sharing and Pruning

- OpenReview：[mDDEcTyT5B](https://openreview.net/forum?id=mDDEcTyT5B)
- 命中查询：gradient-free
- 决定：`include_new`；分类 `related_closed_form`
- 核心贡献：提出GS-MoE，通过跨专家共享低秩子空间与Nyström神经元压缩同时削减MoE专家的秩和中间宽度，并以梯度无关层重要性分配预算。
- 方法判断：固定共享子空间下由重构目标推导专家保留能量增益，再用gradient-free层重要性分数在层、组和专家间分配秩/宽度预算；不是零阶梯度估计。
- 更新对象：DeepSeek-MoE专家的共享子空间秩、分组以及专家中间宽度，最终形成压缩模型。
- 反向传播：作者将整体框架称为training-free且重要性评分为gradient-free；摘要未逐组件说明低秩/Nyström计算是否包含自动微分，因此仅能确认没有额外训练环路的作者声明。
- 持久状态：会持久改写/生成压缩后的MoE专家参数结构；不是仅推理期临时状态。
- 仓库关联：直接压缩大规模MoE语言模型，属于闭式/评分驱动、非反传训练式的语言模型参数适配边界。
- 待核实：仅据官方摘要；代码链接、跨平台首次公开日期和各分解步骤实现细节待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 14. Informed Plastic Attractors for Adaptive Few-Shot Learning

- OpenReview：[bixmDdl5TS](https://openreview.net/forum?id=bixmDdl5TS)
- 命中查询：gradient-free, without gradients
- 决定：`exclude`
- 核心贡献：提出IPA，将信息瓶颈原则解析映射为Hebbian塑性矩阵，使冻结视觉骨干的分类头在少样本部署时无梯度适配。
- 方法判断：解析Hebbian吸引子以无梯度流式更新分类头。
- 更新对象：ResNet/DINO冻结骨干上的少样本分类头。
- 反向传播：部署适配不反传；摘要提到身体可meta-train，但其反传方式未说明。
- 持久状态：分类头权重通过Hebbian规则持久更新。
- 仓库关联：实验是图像少样本与持续学习，无VLM/语言模型关联。
- 待核实：meta-training实现待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 15. Latent Search Manifolds: Reusing Control Experience for PDE-Constrained Optimization

- OpenReview：[ubKC2O6rQo](https://openreview.net/forum?id=ubKC2O6rQo)
- 命中查询：derivative-free
- 决定：`exclude`
- 核心贡献：学习历史PDE控制解的低维连续搜索流形，再用导数无关优化器求解新控制任务。
- 方法判断：在自编码器潜在流形中执行导数无关控制搜索。
- 更新对象：PDE控制轨迹/控制变量。
- 反向传播：在线搜索不需梯度；流形自编码器训练是否反传未在摘要明确。
- 持久状态：训练后的流形模型持久；每个任务产生控制解。
- 仓库关联：PDE约束控制，无语言模型关联。
- 待核实：流形训练实现待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 16. Learning Physics from an Imperfect Ancestor

- OpenReview：[WHwzkjcW2p](https://openreview.net/forum?id=WHwzkjcW2p)
- 命中查询：finite difference
- 决定：`exclude`
- 核心贡献：用不完美神经算子给PINN提供正确解分支的初始化，再以PDE残差训练细化。
- 方法判断：finite-difference仅是参考数值解，不是所提优化机制。
- 更新对象：PINN参数及PDE场解。
- 反向传播：PINN通过PDE残差优化，通常依赖反传；摘要未逐字说明实现。
- 持久状态：训练后的PINN权重持久。
- 仓库关联：PDE科学机器学习，无语言模型关联。
- 待核实：具体优化器待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 17. Lower Bounds For Gradient-Free Convex Optimization And Convex-Concave Saddle-Point Problems

- OpenReview：[qwAOJhaINd](https://openreview.net/forum?id=qwAOJhaINd)
- 命中查询：gradient-free
- 决定：`exclude`
- 核心贡献：给出精确标量值查询下凸优化与凸凹鞍点问题的查询复杂度下界。
- 方法判断：研究通用梯度无关值查询的理论下界。
- 更新对象：抽象凸函数和双线性博弈变量。
- 反向传播：理论查询模型无训练组件。
- 持久状态：不产生模型参数或外部持久状态。
- 仓库关联：虽属零阶理论，但摘要没有大语言模型应用，未满足仓库要求。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 18. NeuroContext-TTA: Source-Anchored Context Calibration for Cross-Subject EEG Emotion Recognition

- OpenReview：[KJ0mwI2BjI](https://openreview.net/forum?id=KJ0mwI2BjI)
- 命中查询：forward-only
- 决定：`exclude`
- 核心贡献：提出NeuroContext-TTA，用上下文偏移平移源类原型，并以可靠性门控校准EEG特征和logit。
- 方法判断：部署时仅前向更新上下文统计与平移参考，校准模块冻结。
- 更新对象：EEG上下文统计、平移后的类参考与输出校正。
- 反向传播：部署无反传；源域校准模块训练的反传方式未说明。
- 持久状态：部署更新统计/参考但不更新模型参数；源训练模型持久。
- 仓库关联：EEG情绪识别，无语言模型或VLM关联。
- 待核实：源训练细节待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 19. One Gradient, Yet More Robust Policies: Momentum-Guided Policy Optimization

- OpenReview：[MP2k9NOHFo](https://openreview.net/forum?id=MP2k9NOHFo)
- 命中查询：parameter perturbation
- 决定：`exclude`
- 核心贡献：提出mSAM策略优化，用累积动量构造对抗参数扰动，使每次更新只需一次策略梯度。
- 方法判断：参数扰动由梯度动量构造，明确不是梯度无关方法。
- 更新对象：强化学习策略参数。
- 反向传播：每步明确计算一次policy gradient。
- 持久状态：策略权重持久更新。
- 仓库关联：通用鲁棒RL且依赖一阶梯度，无语言模型应用。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 20. PathSpeed: Accelerating Structural Recovery in Flow Matching

- OpenReview：[CYZbnNobTC](https://openreview.net/forum?id=CYZbnNobTC)
- 命中查询：finite difference
- 决定：`exclude`
- 核心贡献：提出PathSpeed，以相邻路径边缘样本的有限差分速度构建固定的flow-matching时间采样分布。
- 方法判断：有限差分估计的是路径边缘运动，用于采样调度，不是无梯度参数更新。
- 更新对象：flow-matching训练时间采样概率。
- 反向传播：速度测量本身无需网络前/反传；随后的生成模型训练仍进行常规更新。
- 持久状态：采样分布被缓存；训练后的生成模型权重持久。
- 仓库关联：图像生成实验，无语言模型优化关联。
- 待核实：生成模型训练细节不影响范围判断。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 21. PILOT: Probe-guided Imputation via Local Subspace Optimization for Time-Series Forecasting

- OpenReview：[P4mrdHxWu2](https://openreview.net/forum?id=P4mrdHxWu2)
- 命中查询：finite difference
- 决定：`exclude`
- 核心贡献：提出PILOT，对黑盒时间序列基础模型作前向查询，在局部子空间用有限差分优化插补值。
- 方法判断：以有限差分估计预测损失变化并修正缺失值插补。
- 更新对象：输入时间序列中的插补值，不是基础模型权重。
- 反向传播：黑盒TSFM仅前向；摘要未说明插补器是否有其他训练组件。
- 持久状态：模型权重不更新；每批次插补值是任务状态。
- 仓库关联：时间序列基础模型，不是语言模型。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 22. Probabilistic Agentic Memory: Learning Distributional Evidence for Skill Reuse

- OpenReview：[ZoTnXQHanX](https://openreview.net/forum?id=ZoTnXQHanX)
- 命中查询：without gradients
- 决定：`exclude`
- 核心贡献：提出PAM，把预测结果的对数评分写入广义Bayes记忆，以选择和复用流行病预测技能。
- 方法判断：部署时对黑盒技能无梯度，但训练PAM会穿过时间回放求导。
- 更新对象：持久技能支持记忆以及PAM的分布建模参数。
- 反向传播：训练明确对时间回放求导，但不穿过技能；部署参数冻结。
- 持久状态：训练后的PAM参数持久，部署时记忆随结果持续更新。
- 仓库关联：“agentic”指预测技能复用，任务是流行病预测且摘要无LLM代理。
- 待核实：底层技能类型待核实，但无语言模型证据。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 23. Reducing the Sample Complexity of Sampling-based Control via Horizon Splitting

- OpenReview：[R5AzsIf1CQ](https://openreview.net/forum?id=R5AzsIf1CQ)
- 命中查询：zeroth-order, CMA-ES
- 决定：`exclude`
- 核心贡献：分析采样控制对规划时域的指数样本复杂度，并以时域分割顺序求解子控制问题。
- 方法判断：MPPI/CMA-ES/CEM等零阶采样控制配合时域分割。
- 更新对象：机器人控制轨迹。
- 反向传播：在线采样优化无需反传；无可训练语言组件。
- 持久状态：规划轨迹在求解中更新，不改模型权重。
- 仓库关联：机器人控制，无VLM/语言模型优化关联。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 24. Same Target, Different Origins: Aligning Latent Rollout for Consistent PDE Emulation

- OpenReview：[NSvIJnAORy](https://openreview.net/forum?id=NSvIJnAORy)
- 命中查询：zeroth-order
- 决定：`exclude`
- 核心贡献：提出ALR，正则化神经PDE求解器，使不同起点的潜在rollout在同一目标时间保持状态和动力学一致。
- 方法判断：“zeroth-order”表示潜在状态一致性项的Taylor阶次，不是零阶优化。
- 更新对象：神经PDE求解器内部表示与权重。
- 反向传播：作为训练正则项，具体反传实现摘要未说明。
- 持久状态：训练后的求解器权重持久。
- 仓库关联：PDE仿真，无语言模型关联。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 25. Second-Order Motion Representations: Grassmannian Differential Kinematics for Unsupervised Hand-Object Interaction Segmentation

- OpenReview：[Al9NxBL54h](https://openreview.net/forum?id=Al9NxBL54h)
- 命中查询：zero-order
- 决定：`exclude`
- 核心贡献：构建Grassmann流形上的二阶运动表示，用于无监督手物交互分段。
- 方法判断：zero-order只指被比较的低阶运动描述符，不是优化方法。
- 更新对象：3D场景流的运动描述与聚类标签。
- 反向传播：所提因果training-free检测不需要模型训练；场景流估计器不属于所提方法。
- 持久状态：生成分段和聚类，不更新模型权重。
- 仓库关联：纯视觉动作分割，无语言模型关联。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 26. Slot-MPC: Goal-Conditioned Model Predictive Control with Object-Centric Representations

- OpenReview：[1aoQWfoqRQ](https://openreview.net/forum?id=1aoQWfoqRQ)
- 命中查询：gradient-free
- 决定：`exclude`
- 核心贡献：提出Slot-MPC，以物体中心世界模型和可微MPC规划未见场景中的动作。
- 方法判断：摘要明确选择gradient-based MPC，gradient-free sampling MPC仅为对比。
- 更新对象：机器人动作序列及训练出的世界模型。
- 反向传播：规划通过可微世界模型对动作求梯度；世界模型也需训练。
- 持久状态：世界模型权重持久，动作计划为任务状态。
- 仓库关联：机器人视觉控制，无语言模型关联且主方法是一阶规划。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 27. STRIDE: An Efficient SNN Training-to-Deployment Framework on Real-World Vision Tasks

- OpenReview：[OBDZfSiQXp](https://openreview.net/forum?id=OBDZfSiQXp)
- 命中查询：without backpropagation
- 决定：`exclude`
- 核心贡献：提出STRIDE，将低比特权重、Integer-LIF脉冲编码和专用SNN硬件执行结合。
- 方法判断：without backpropagation仅限定“不做时间反向传播”；仍用量化感知蒸馏训练。
- 更新对象：SNN低比特权重与硬件执行表示。
- 反向传播：不做BPTT，但摘要未排除逐时刻/替代梯度反传。
- 持久状态：训练后的SNN权重持久。
- 仓库关联：纯视觉SNN软硬件协同，无语言模型关联。
- 待核实：训练梯度路径待原文核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 28. The Normalization Landscape in Continual Learning: Resolving Moving-Average Breakdown and Subspace Interference for Buffer-Free Edge Intelligence

- OpenReview：[lB4XQBr9SX](https://openreview.net/forum?id=lB4XQBr9SX)
- 命中查询：without backpropagation
- 决定：`exclude`
- 核心贡献：提出SMR，以BatchNorm重校准、感觉/决策分区、测试时路由和正交子空间复用改善边缘持续学习。
- 方法判断：无反传仅指20个微批次的BatchNorm统计重校准，不代表整个持续学习流程无梯度。
- 更新对象：BatchNorm统计、模块化视觉子网络与路由状态。
- 反向传播：重校准无需反传；模块学习/扩展训练方式摘要未充分说明。
- 持久状态：BN统计和任务模块持久保存；另有动态通道扩展。
- 仓库关联：CIFAR视觉持续学习与边缘系统，无语言模型关联。
- 待核实：完整训练路径待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 29. ViLo-TM: Visual-Logic Mapping from Deep CNNs to Tsetlin Machines

- OpenReview：[ZsDGfzVnKt](https://openreview.net/forum?id=ZsDGfzVnKt)
- 命中查询：gradient-free
- 决定：`exclude`
- 核心贡献：提出ViLo-TM，将CNN视觉证据映射为可追踪布尔Tsetlin规则，并导出整数CNN与布尔TM。
- 方法判断：部署TM用标准离散反馈作无乘法/梯度规则学习，但前端以连续松弛和QAT端到端优化。
- 更新对象：CNN编码器、阈值与布尔子句。
- 反向传播：端到端连续松弛/QAT训练很可能使用反传；部署TM反馈不使用梯度，摘要未逐组件完全说明。
- 持久状态：编码器和布尔规则均可持久保存；部署可更新TM规则。
- 仓库关联：纯计算机视觉，无语言模型关联。
- 待核实：QAT实现细节待核实。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 30. Which features remain vulnerable in robust models?

- OpenReview：[y8bfpQh6gX](https://openreview.net/forum?id=y8bfpQh6gX)
- 命中查询：gradient-free
- 决定：`exclude`
- 核心贡献：分析鲁棒CIFAR分类器中仍可被攻击的特征，并提出与鲁棒性相关的无梯度margin spread度量。
- 方法判断：gradient-free只修饰诊断度量，不是语言模型优化。
- 更新对象：鲁棒视觉分类器的特征脆弱性统计。
- 反向传播：诊断度量不需反传；攻击和模型训练方式不属于新方法。
- 持久状态：不更新模型参数，仅输出审计统计。
- 仓库关联：纯视觉鲁棒性分析，无语言模型关联。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z

## 31. ZOFOSGDA: A Hybrid Method for Nonsmooth Nonconvex-Nonconcave Minimax Optimization

- OpenReview：[9xbgm7J1m9](https://openreview.net/forum?id=9xbgm7J1m9)
- 命中查询：zeroth-order
- 决定：`exclude`
- 核心贡献：提出ZOFOSGDA，对非光滑非凸外变量用随机两点零阶估计，对光滑内变量用随机一阶梯度和SPIDER。
- 方法判断：外层零阶、内层一阶的通用混合minimax优化。
- 更新对象：抽象minimax外/内变量；实验为分类和AUC。
- 反向传播：内变量明确依赖一阶梯度，外变量使用函数值查询。
- 持久状态：优化变量在迭代中持久更新。
- 仓库关联：通用优化理论与分类基准，没有语言模型应用。
- 待核实：无。
- OpenReview 平台公开：2026-10-03T12:42:08.286000Z
