# ICLR 2027 补充同义词检索：主来源与七条候选核验

核验时间：2026-10-11T17:20:17+08:00
核验范围：仅使用上级已缓存的官方 OpenReview 搜索响应与完整 note；没有重抓已成功页面，也没有绕过 challenge、CAPTCHA 或访问控制。

## 检索覆盖证据

官方检索均限定 `group=ICLR.cc/2027/Conference`、`source=forum`、`limit=1000`，主来源为 OpenReview API2。原始查询清单保存在 `/tmp/iclr2027-parent-synonyms/manifest.txt`，七条完整官方 note 保存在 `/tmp/iclr2027-parent-synonyms/additional-candidates.txt`。

| 检索词 | 官方 `count` | 本地缓存返回数 | 覆盖判断 | 官方查询 |
|---|---:|---:|---|---|
| `backward-free` | 0 | 0 | 完成；官方返回零条 | [OpenReview API](https://api2.openreview.net/notes/search?term=backward-free&group=ICLR.cc%2F2027%2FConference&source=forum&limit=1000&count=true) |
| `gradientless` | 0 | 0 | 完成；官方返回零条 | [OpenReview API](https://api2.openreview.net/notes/search?term=gradientless&group=ICLR.cc%2F2027%2FConference&source=forum&limit=1000&count=true) |
| `forward-forward` | 10 | 10 | 完成；本页返回数等于官方计数 | [OpenReview API](https://api2.openreview.net/notes/search?term=forward-forward&group=ICLR.cc%2F2027%2FConference&source=forum&limit=1000&count=true) |
| `gradient-independent` | 3 | 3 | 完成；本页返回数等于官方计数 | [OpenReview API](https://api2.openreview.net/notes/search?term=gradient-independent&group=ICLR.cc%2F2027%2FConference&source=forum&limit=1000&count=true) |
| `without backpropagation` | 10,000 | 1,000 | **不完整**；只缓存首个 1,000 条窗口，尚有至少 9,000 个窗口内结果未分页，且 `count=10000` 可能仍是服务端窗口上限 | [OpenReview API](https://api2.openreview.net/notes/search?term=without+backpropagation&group=ICLR.cc%2F2027%2FConference&source=forum&limit=1000&count=true) |

这五个补充查询不能证明全会覆盖，尤其不能把 `without backpropagation` 的 `count=10000` 当作会议总数或完整结果数。本文件只说明缓存中识别出的七条新增线索及其逐条决定。

## 逐条核验

七条 note 的作者字段均为双盲投稿的 `Anonymous`，venue 均为 `ICLR 2027 Conference Submission`，BibTeX note 均为 `under review`。下列 `openreview_created_at` 只由 note 的 `cdate` 换算，**不代表已核实的首次公开日期**；七条的 `first_public_date` 均待核实。

### 1. Local-Window Contrastive Forward-Forward Learning with Masked Reconstruction

- **OpenReview ID / 原文：** `03wjv3G8UP`；[官方 forum](https://openreview.net/forum?id=03wjv3G8UP)
- **作者 / 状态 / 日期：** Anonymous；ICLR 2027 投稿、审稿中；`openreview_created_at=2026-09-14T10:55:02.434+08:00`。
- **官方摘要支持的核心贡献：** CFF+MAE 在 ViT 预训练中按一块或两块 encoder block 的局部窗口联合优化 contrastive Forward-Forward 与 masked reconstruction，并把 decoder checkpoint 传到后续窗口，以降低保留全深度计算图的内存开销。
- **方法与更新对象：** 当前 encoder 局部窗口与轻量 decoder 是训练对象；前序 blocks 只做无 autograd 的前向计算；decoder checkpoint 是跨窗口携带的外部训练状态。
- **反传与持久更新：** 不是完全无反传。摘要明确说 CFF 与 MAE 分支分别 backpropagate，因而活动 encoder blocks 和 decoder 有梯度更新及持久参数更新；只是不做贯穿整个 ViT 的端到端反传。
- **LLM/VLM 关联：** 摘要、关键词和实验仅涉及 Vision Transformer、CIFAR-10、ImageNet-1K 与手部姿态数据；没有语言模型或视觉—语言模型应用。
- **决定：** **排除**。这是纯视觉的局部反传训练，既无 LLM/VLM 应用，也不是完全 gradient-free；不能因 `Forward-Forward` 或“不恢复 full-depth backward graph”而归入梯度无关 LLM 优化。
- **待核实：** 无需为当前排除决定补证；若未来公开版本加入明确 VLM/语言骨干实验，应重新审查。

### 2. TopX: Skeleton-Aware In-Context Text-to-Motion Diffusion Across Heterogeneous Topologies

- **OpenReview ID / 原文：** `KuIOR6EwIp`；[官方 forum](https://openreview.net/forum?id=KuIOR6EwIp)
- **作者 / 状态 / 日期：** Anonymous；ICLR 2027 投稿、审稿中；`openreview_created_at=2026-09-16T23:20:10.268+08:00`。
- **官方摘要支持的核心贡献：** TopX 以统一的 per-joint 表示、作为 prompt 的 skeleton rest pose/tree-distance attention bias，以及按 channel group 校准的 flow-matching objective，让单个 text-conditioned motion diffusion transformer 服务异构骨架。
- **方法与更新对象：** 训练对象是 text-to-motion diffusion transformer；骨架作为条件输入，不是被搜索或更新的语言提示词。命中 `gradient-independent` 的语义是让各 channel group 对训练 gradient 的占比不随 cell 数量变化。
- **反传与持久更新：** 摘要描述带梯度权重的 flow-matching 训练，没有无梯度优化步骤；模型权重显然是训练后的持久状态，但摘要未交代优化器和反传实现细节。
- **LLM/VLM 关联：** 有文本条件，但核心是动作生成与骨架拓扑，摘要没有 LLM、VLM 或语言骨干优化应用。
- **决定：** **排除**。`gradient-independent` 在此不是 gradient-free，而是梯度贡献对 group size 的独立性；text conditioning 本身不足以构成目标仓库所需的 LLM/VLM 优化关联。
- **待核实：** 模型所用文本编码器及其是否冻结未由摘要说明，但不影响当前方法命中为假阳性的判断。

### 3. DeltaNet-PC: Test-Time Memory Without Backpropagation Through Time

- **OpenReview ID / 原文：** `I0AW0dp7WL`；[官方 forum](https://openreview.net/forum?id=I0AW0dp7WL)
- **作者 / 状态 / 日期：** Anonymous；ICLR 2027 投稿、审稿中；`openreview_created_at=2026-09-18T10:26:27.125+08:00`。
- **官方摘要支持的核心贡献：** DeltaNet-PC 把每一步记忆增量 `ΔS_t` 当作 latent variable 而非慢权重，从 predictive-coding 概率模型的 prediction-error energy 推导顺序记忆更新，并把该局部规则联系到 DeltaNet 等 linear attention 更新。
- **方法与更新对象：** 测试时更新的是固定容量的顺序 latent memory `S_t`；它可存储单序列、多序列和 key-value 关联，不是摘要所称的 slow model weight。
- **反传与持久更新：** 测试时记忆更新按摘要为局部 predictive-coding update，不需要 BPTT。`without BPTT` 不能推出系统完全不使用梯度：基础模型如何训练、局部 energy 的具体求解是否用显式导数，摘要均未说明。
- **持久状态边界：** 未见测试时持久模型权重更新；`S_t` 在序列内持续演化且内存规模固定。是否跨样本/会话保留需看正文。
- **LLM/VLM 关联：** 论文以 LLM attention 的 test-time sequential memory 为动机，并分析 linear-attention/DeltaNet 机制；摘要没有报告在完整 LLM 上的模型权重微调。
- **决定：** **收录为边界关联**，建议放入“闭式、局部与统计适配”类（若未增该类则暂放 `related_inference`）。它提供与 LLM linear attention 直接相关、无 BPTT 的测试时局部记忆更新，但不应标作 ES/ZO 权重优化。
- **待核实：** 基础网络训练是否使用 BPTT/普通反传、局部 PC 推断是否显式求梯度、`S_t` 是否跨序列持久保存，以及完整 LLM 上的实验范围。

### 4. Block-Level Positional Reconstruction for Sparse Long-context Prefilling（RePhase）

- **OpenReview ID / 原文：** `2jfW67zbil`；[官方 forum](https://openreview.net/forum?id=2jfW67zbil)
- **作者 / 状态 / 日期：** Anonymous；ICLR 2027 投稿、审稿中；`openreview_created_at=2026-09-17T17:07:12.944+08:00`。
- **官方摘要支持的核心贡献：** RePhase 为 block-sparse long-context attention 把当前 unrotated block interactions、一次拟合的 position/distance-conditioned response profile 与精确相对 RoPE phase 组合起来，从而直接在 block level 估计相关性而无需 token-level search。
- **方法与更新对象：** 使用无标签 forward-pass statistics 一次性拟合可复用 positional-response profile；推理时读取该 profile 为 key blocks 打分。
- **反传与持久更新：** 摘要明确说 profile 拟合无需 backpropagation，也不更新模型参数；基础 LLM 权重保持不变。profile 是模型外的持久校准状态，而非模型权重。
- **LLM/VLM 关联：** primary area 明确为 foundation/frontier models including LLMs，任务为长上下文文本和视频推理。
- **决定：** **收录为边界关联**，建议放入“闭式、局部与统计适配”类（若未增该类则放 `related_inference`）。它是 forward-only 的长上下文统计校准，不应标作 ZO/ES。
- **待核实：** profile 的具体拟合公式、离线统计集构成、跨模型/上下文长度复用范围，以及视频实验所用语言/视觉骨干细节需读正文确认。

### 5. Functional Memory Compilation: Behavior-Level Migration of Aggregate LoRA Memory

- **OpenReview ID / 原文：** `fKWM0tmEOE`；[官方 forum](https://openreview.net/forum?id=fKWM0tmEOE)
- **作者 / 状态 / 日期：** Anonymous；ICLR 2027 投稿、审稿中；`openreview_created_at=2026-09-18T14:04:45.254+08:00`。
- **官方摘要支持的核心贡献：** Functional Memory Compilation（FMC）从旧语言模型在保留问题上的可观察回答构造 successor output constraints，用批量前向计算和一次 analytic low-rank fit 把 aggregate LoRA memory 迁移为目标模型原生的 output-head adapter。
- **方法与更新对象：** 输入包括 source model、successor model 和 retained questions；最终更新对象是安装到 successor 上的 low-rank output-head adapter。
- **反传与持久更新：** 摘要明确说迁移阶段没有 backpropagation 或 optimizer steps；source/successor 主干只用于前向计算。新 output-head adapter 是持久模型参数更新，不能归为“无参数更新的推理”。
- **LLM/VLM 关联：** 直接处理语言模型升级后的 LoRA memory 迁移。
- **决定：** **收录**，建议放入“闭式、局部与统计适配”类。它是 analytic fitting 的持久 adapter 安装，不应硬称为 ZO 或 ES，也不应放 `related_inference`。
- **待核实：** analytic fit 的数值求解、adapter rank/安装层范围、除 output head 外是否还有可训练部件，以及公开代码链接；摘要只支持迁移阶段无反传，不证明原 LoRA memory 的训练无反传。

### 6. ReLaDrift: Recurrent Language Generation via Drifting for Test-Time Scaling

- **OpenReview ID / 原文：** `C1HGhWNaYZ`；[官方 forum](https://openreview.net/forum?id=C1HGhWNaYZ)
- **作者 / 状态 / 日期：** Anonymous；ICLR 2027 投稿、审稿中；`openreview_created_at=2026-09-18T12:52:41.133+08:00`。
- **官方摘要支持的核心贡献：** ReLaDrift 把同一个 Drifting Model 循环用于语言生成，使后续轮次修正上一轮 draft；训练时只对随机选中的一个 round 应用 drifting loss，避免跨轮 BPTT，并在测试时用更多 function evaluations 做少步迭代改进。
- **方法与更新对象：** 训练对象是 recurrently reused Drifting Model 的持久权重；测试时更新的是生成 draft，未描述测试时参数更新或外部搜索。
- **反传与持久更新：** 明确不做 across-round BPTT，但仍有对一个选定 round 的训练 loss。摘要没有声明该 selected-round 参数训练也无 backpropagation，因此不能把 `without BPTT` 扩写成完全 gradient-free；其具体一阶更新方式待正文确认。
- **LLM/VLM 关联：** 明确是 language generation，并在 GSM8K 等任务评估 test-time scaling。
- **决定：** **收录为混合/边界关联**，建议放 `related_hybrid`。它与“避免 BPTT 的语言模型训练 + 前向迭代生成”直接相关，但不应列入纯 ES/ZO 主分类。
- **待核实：** selected-round drifting loss 的反向传播范围、是否 stop-gradient 其他轮、基础模型规模与初始化，以及测试时是否存在摘要未说明的状态缓存。

### 7. Towards Unbiased Test-Time Adaptation for Vision–Language Models（UTA）

- **OpenReview ID / 原文：** `yngr3bVtsX`；[官方 forum](https://openreview.net/forum?id=yngr3bVtsX)
- **作者 / 状态 / 日期：** Anonymous；ICLR 2027 投稿、审稿中；`openreview_created_at=2026-09-10T14:37:55.959+08:00`。
- **官方摘要支持的核心贡献：** UTA 在 statistics-based VLM test-time adaptation 中，用 historical class responses 调节样本到类别状态的分配，并按 test stream 的 coordinate activity 重加权累积 class states 来构造 classifier，以减轻 prediction-biased accumulation 与 classifier homogenization。
- **方法与更新对象：** 测试流被汇总为固定大小的 class statistics/class states；classifier 根据这些累积状态构造。摘要没有把它们描述为基础 VLM 权重。
- **反传与持久更新：** 适配阶段明确不使用 backpropagation，也不保存逐实例数据；没有基础 VLM 模型权重更新。class statistics 在测试流内持续更新，派生 classifier 是持久的运行时适配状态，其是否写回可训练参数需正文确认。
- **LLM/VLM 关联：** 直接用于 VLM，摘要报告 CLIP/ImageNet-1K 的统计适配。
- **决定：** **收录为边界关联**，建议放入“闭式、局部与统计适配”类（若未增该类则暂放 `related_inference`）。它不是 ZO/ES，而是无反传的状态统计与 classifier construction。
- **待核实：** class states 的重置/跨 domain 生命周期、classifier 是否仅即时构造还是持久缓存、VLM backbone 的冻结配置及公开代码链接。

## 决定汇总与去重

- 建议收录 5 条：DeltaNet-PC、RePhase、FMC、ReLaDrift、UTA。
- 具体排除 2 条：Local-Window CFF+MAE（纯视觉且仍有局部反传）、TopX（`gradient-independent` 仅描述梯度权重不随 group size 变化，且无 LLM/VLM 优化方法）。
- 在当前 `data/papers.json`、`papers.bib`、主审查 JSON 与双语 README 中按七个 OpenReview ID 和完整标题检索均未命中，因此这七条都是此前未记录的候选；最终目录写入时仍应运行全局标题、OpenReview ID 和原文链接重复检查。
- 分类建议以模块和更新对象为准：FMC 有持久 output-head adapter；UTA 有测试流 class statistics/派生 classifier；RePhase 有可复用 profile；DeltaNet-PC 有序列内 latent memory；ReLaDrift 有训练中的模型权重与测试时 draft。不能用统一的“无持久模型更新”或“无反传”句式覆盖这些不同机制。
