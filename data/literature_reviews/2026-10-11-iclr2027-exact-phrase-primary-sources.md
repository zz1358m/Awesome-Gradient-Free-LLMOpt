# ICLR 2027 精确短语候选主来源审查（2026-10-11）

## 范围与证据边界

本审查只读取两组已缓存的官方 OpenReview note 和查询 manifest，没有重新下载页面，也没有使用搜索引擎摘要。来源为：

- `/tmp/iclr2027-parent-get-exact/manifest.txt` 与 `additional-candidates.txt`
- `/tmp/iclr2027-parent-exact-methods/manifest.txt`、`00.json`—`17.json` 与 `additional-candidates.txt`

第一组 manifest 含 3 个会议限定精确查询：标题 `Sample the Order, Not the Token` 返回 1/1，摘要 `without backpropagation` 返回 20/20，摘要 `without gradients` 返回 11/11。标题查询只证明该标题在这个查询中唯一，不能证明全会场标题已检索完整。

第二组 manifest 恰有 18 个摘要精确短语查询，依次为 `zeroth-order`、`zero-order`、`gradient-free`、`derivative-free`、`evolution strategies`、`evolutionary optimization`、`weight perturbation`、`parameter perturbation`、`finite difference`、`SPSA`、`MeZO`、`CMA-ES`、`forward-only`、`backpropagation-free`、`black-box optimization`、`without backward`、`without gradient`、`no backpropagation`。每项均有 `complete=true`，`returned=count`，且最大返回数为 92，低于 `limit=1000`，所以这 18 个特定短语查询没有分页截断。它们不构成 ICLR 2027 全部公开投稿的完整枚举证明。

两份候选文件为 6 + 29 条，共 35 个互异 OpenReview ID；这些 ID 均未出现在审查时的 `data/literature_reviews/2026-10-11-iclr2027.json`、`data/papers.json` 或 `papers.bib`。审查建议为：21 条边界收录，14 条排除，0 条已记录。所有作者均按官方匿名投稿 BibTeX 记为 `Anonymous`。下列 `openreview_created_at` 只表示 OpenReview `cdate`，不是已核实的首次公开日期；缓存 manifest 没有独立抓取时间字段，因此不补造抓取时间。

## 逐条审查

### 1. SCAMP: Black-Box Knowledge Poisoning Attack on Multimodal Retrieval-Augmented Generation

- **ID / 作者 / OpenReview 创建时间 / 原文：** `O26AmnGkFD`；Anonymous；`2026-09-17T06:02:33.687Z`；https://openreview.net/forum?id=O26AmnGkFD
- **贡献与对象：** 据官方摘要，SCAMP 用 Visual Attacker、Text Attacker、Competing Agents 和三个评估器组成自竞争循环，迭代构造同时绕过多模态 RAG 检索与重排的图文投毒文档；优化对象是外部图文对和类别级视觉原型，不是 VLM 权重。
- **机制、反传与持久性：** 摘要明确黑盒、无需梯度访问，类别级原型由 agent 驱动、without gradients；未说明各 attacker/评估器是否另经梯度训练。模型权重更新未报告；投毒文档和原型是可持久外部工件。
- **决定：** 边界收录，建议 `related_prompt_agent`。与仓库的具体关联是针对 VLM/RAG 的反馈驱动黑盒外部工件搜索。待核实完整算法是否使用显式搜索算子、各 agent 是否训练以及代码是否公开。

### 2. QK-Wanda: Coupling Queries and Keys for Unstructured Pruning

- **ID / 作者 / OpenReview 创建时间 / 原文：** `HXmRkbSJCb`；Anonymous；`2026-09-16T17:39:24.001Z`；https://openreview.net/forum?id=HXmRkbSJCb
- **贡献与对象：** 从因果掩码后的 query-key 乘积重建损失推导单权重删除的闭式重要性分数，把对侧投影项加入 Wanda，对 Llama 3 的 Q/K 权重做一次性非结构化剪枝。
- **机制、反传与持久性：** 校准集上闭式打分，摘要明确无梯度、无再训练；被删除的权重形成持久稀疏模型结构。
- **决定：** 边界收录，建议 `related_closed_form`。这是 LLM 权重的闭式、训练后结构更新，不应称为 ZO/ES。待核实剪枝掩码的导出和部署格式。

### 3. RAZOR: Pruning Replaceable Experts in LLMs

- **ID / 作者 / OpenReview 创建时间 / 原文：** `OLS3NKUhWz`；Anonymous；`2026-09-19T05:29:32.869Z`；https://openreview.net/forum?id=OLS3NKUhWz
- **贡献与对象：** 用 expert 输出相对原加权混合的 consensus residual 衡量功能可替代性，并由包含 survivor renormalization 和 router refill 的精确单删除恒等式汇总校准 token 分数，按预算剪除 MoE experts。
- **机制、反传与持久性：** 摘要明确 training-free、without gradients or recovery training；专家删除会持久改变模型结构，未报告额外学习模块。
- **决定：** 边界收录，建议 `related_closed_form`。关联在于无需反传的 LLM MoE 参数/结构压缩，而非随机 ZO 优化。待核实评分计算的实现和路由器是否完全不修改。

### 4. HarnessNet: From Engineered Harnesses to a Unified Neural Controller for Self-Evolving Agents

- **ID / 作者 / OpenReview 创建时间 / 原文：** `cFcaAi8dtG`；Anonymous；`2026-09-17T14:34:11.218Z`；https://openreview.net/forum?id=cFcaAi8dtG
- **贡献与对象：** 训练一个神经反馈控制器，根据交互历史决定请求 LLM、执行已有命令、读取环境输出或结束；先模仿 engineered harness，再用同任务多次尝试的成功差异改进控制器，LLM 保持冻结。
- **机制、反传与持久性：** 摘要只明确不通过 LLM 或环境求梯度，没有说明 controller 自身更新是否反传；controller 权重显然是持久学习对象，LLM 权重冻结。不能把 “self-evolving” 扩写为 evolutionary search。
- **决定：** 边界收录，建议 `related_hybrid`。关联在于 LLM agent harness 的外部控制器学习且不对 LLM/环境反传；待核实模仿与 reward-driven update 的优化器和梯度路径。

### 5. Written as a Record, Read as an Address: What a Forward Pass Leaves in an Operation's KV Cache

- **ID / 作者 / OpenReview 创建时间 / 原文：** `jYLlpt0DOn`；Anonymous；`2026-09-17T13:54:54.830Z`；https://openreview.net/forum?id=jYLlpt0DOn
- **贡献与对象：** 把前向过程分为冻结 writer 和单独训练的 reader，研究 operation-span KV cache 中 routing record 与 payload 的可恢复性，并用 transplant 做因果验证。
- **机制、反传与持久性：** writer cache 的重算无需梯度，但 reader 明确“trained in isolation”；摘要没有梯度无关优化 LLM、提示词或 agent 工件的方法。reader 是否用反传未明说，但不能因 writer forward-only 就称全方法无反传。
- **决定：** 排除。它是机制解释/探针研究，`without gradients` 描述缓存重算的实验控制，不是优化机制。

### 6. RC-VQ: Recovering What Calibration Discards with Vector-Quantized Residual Correction

- **ID / 作者 / OpenReview 创建时间 / 原文：** `HXmiKD1kS0`；Anonymous；`2026-09-16T02:17:01.893Z`；https://openreview.net/forum?id=HXmiKD1kS0
- **贡献与对象：** 论证压缩残差谱平坦、低秩修正结构上不匹配，并以 full-rank vector-quantized corrector 恢复 LLM 因 SVD/INT4/叠加压缩丢失的残差；提出 direction-then-refinement 的 PolarVQ 目标。
- **机制、反传与持久性：** 摘要明确 corrector 在无梯度、无 recovery data 下拟合；corrector 与压缩权重共同构成持久 checkpoint。具体 VQ 拟合算法未在摘要给出，不能硬称闭式解或 ZO。
- **决定：** 边界收录，建议 `related_closed_form`（按该类包含的非反传统计/局部适配边界）。待核实 codebook 拟合步骤及是否迭代优化。

### 7. GENO: Diversity-Preserving Green Optimization for Multi-Objective AI Service Orchestration

- **ID / 作者 / OpenReview 创建时间 / 原文：** `DYddkBo6u2`；Anonymous；`2026-09-18T15:38:51.467Z`；https://openreview.net/forum?id=DYddkBo6u2
- **贡献与对象：** DDC 同步 dominance archive 与 decomposition population，以能耗优先去重和 reassociation 改善 AI 服务编排的能耗、碳、延迟和可靠性 Pareto 前沿。
- **机制、反传与持久性：** 被优化的是服务部署/编排变量。local language model 仅提供有界 preference-channel weight perturbation 接口，摘要消融也称主要收益来自 DDC；没有优化 LLM 参数、提示词、agent 工件或推理状态的证据。
- **决定：** 排除。虽是多目标优化且用了语言接口，但与语言模型优化没有具体方法关联。

### 8. Learnable Difference-Aware Embedding: A Lightweight Plug-and-Play Module for Multivariate Time Series Forecasting

- **ID / 作者 / OpenReview 创建时间 / 原文：** `D9uldDQrKv`；Anonymous；`2026-09-09T10:54:56.079Z`；https://openreview.net/forum?id=D9uldDQrKv
- **贡献与对象：** LDAE 用以有限差分 stencil 初始化的可学习卷积构造时序变化率和曲率特征，服务多变量时间序列预测。
- **机制、反传与持久性：** finite difference 是特征初始化/信号差分，不是无梯度优化；卷积明确 learnable，训练方式未在摘要展开。无 LLM/VLM 应用。
- **决定：** 排除。纯时间序列任务，关键词不构成 ZO 机制。

### 9. Towards Shared Flat Regions: Boosting Adversarial Transferability by Exponentially Tilting Curvature-Regularized Gradients

- **ID / 作者 / OpenReview 创建时间 / 原文：** `IcsDtyQXgw`；Anonymous；`2026-09-02T13:20:57.559Z`；https://openreview.net/forum?id=IcsDtyQXgw
- **贡献与对象：** TCRA 以 response-guided finite-difference probe、梯度平行/正交分解和 exponential tilting 构造图像对抗攻击方向。
- **机制、反传与持久性：** 它依赖可访问 surrogate 的梯度并明确扩展 gradient-based attacks；finite difference 只探测局部梯度变化。没有语言模型应用，模型权重不更新，优化的是图像扰动。
- **决定：** 排除。纯图像攻击，且不是梯度无关训练。

### 10. RGB-ACD: RGB-Inspired Topology Generation for LLM-Guided Analog Circuit Design

- **ID / 作者 / OpenReview 创建时间 / 原文：** `50wgNc7yUX`；Anonymous；`2026-09-04T07:42:01.965Z`；https://openreview.net/forum?id=50wgNc7yUX
- **贡献与对象：** 用 RGB 图像编码电路拓扑，训练 text-to-connectivity generator；外层 LLM 依据仿真残差修订拓扑生成指令，内层有限差分估计更新器件参数。
- **机制、反传与持久性：** finite-difference 优化对象是模拟电路器件参数，不是 LLM；generator 已经训练且训练梯度信息未说明。LLM 只是设计 agent 的拓扑指导组件。
- **决定：** 排除。存在 LLM-guided 电路设计，但没有梯度无关语言模型优化证据，不能把电路参数优化归入本目录。

### 11. CalibCache: Cache-to-Full Feature Dynamics Calibration for Diffusion Transformers

- **ID / 作者 / OpenReview 创建时间 / 原文：** `HteiUnhO1T`；Anonymous；`2026-08-20T09:15:42.289Z`；https://openreview.net/forum?id=HteiUnhO1T
- **贡献与对象：** 对 cached/full-compute 图像扩散轨迹的二阶时间差分做 centered least-squares 标量 acceleration map 校准，以减少短采样日程的缓存误差。
- **机制、反传与持久性：** 离线最小二乘映射持久保存，推理时不在线优化；finite difference 是扩散采样步的时间差分。Qwen-Image 只是图像生成 backbone，未涉及语言模型优化。
- **决定：** 排除。纯图像 diffusion feature cache 校准，不能因模型名含 Qwen 或采用解析校准而纳入。

### 12. Scalar Smoothness Is One Point on a Besov Spectrum

- **ID / 作者 / OpenReview 创建时间 / 原文：** `osd72MlzL5`；Anonymous；`2026-09-14T08:04:25.160Z`；https://openreview.net/forum?id=osd72MlzL5
- **贡献与对象：** 提出跨扰动尺度、方向和位置的 finite-difference roughness spectrum；在 LLM PTQ 中按每个 block 的量化误差尺度/方向探测 task-loss 增量，据此给脆弱 block 分配更高精度。
- **机制、反传与持久性：** LLM 分支的机制是前向有限差分损失探针和 mixed-precision bit allocation；摘要没有报告对模型反传，GPTQ 权重已固定。持久变化是位宽分配与量化 checkpoint，而非浮点权重的梯度更新；图像 RSC 分支是否训练不影响该边界描述。
- **决定：** 边界收录，建议 `related_closed_form`。关联是有限差分探针直接驱动 LLM 压缩配置优化，但它不是标准 ZO 梯度估计器。待核实 bit allocation 求解算法及是否需要任何梯度统计。

### 13. TE-VLM: Transfer Entropy-Inspired Distillation for Vision-Language Models

- **ID / 作者 / OpenReview 创建时间 / 原文：** `a9gC9t9Zvc`；Anonymous；`2026-09-17T19:33:47.703Z`；https://openreview.net/forum?id=a9gC9t9Zvc
- **贡献与对象：** 从 optimization-step transfer entropy 推导 TE1/TE2 正则项，在 CLIP 式 teacher-student distillation 中匹配 batch 内表示变化方向。
- **机制、反传与持久性：** finite-difference directions 是相邻优化步的表示差分/正则目标，不是 finite-difference 梯度估计；student 仍通过蒸馏目标训练并持久更新权重。摘要的 “no extra teacher passes” 也不表示无反传。
- **决定：** 排除。实际主体是一阶 VLM 蒸馏，精确短语命中不是梯度无关机制。

### 14. DV-Lens: Revealing the Functional Organization of Language Model Parameters

- **ID / 作者 / OpenReview 创建时间 / 原文：** `fNrQjgb4Ch`；Anonymous；`2026-08-20T03:53:47.624Z`；https://openreview.net/forum?id=fNrQjgb4Ch
- **贡献与对象：** 估计模块级 downstream Jacobian，把原生参数列投影到词表响应空间，并以 DV-Complexity 衡量分组参数结构；readout 可指导 ablation、steering 和 swapping。
- **机制、反传与持久性：** finite-difference tests 仅验证 readout 对局部 logit 变化的预测，不是优化器；Jacobian 的求法及是否需反向模式未在摘要说明。干预会临时/持久修改参数取决于实验，但没有提出梯度无关 LLM 优化流程。
- **决定：** 排除。它是参数解释框架，有限差分只承担验证作用。

### 15. When Can First-Order Models of Fine-Tuning Bound Forgetting?

- **ID / 作者 / OpenReview 创建时间 / 原文：** `pOcuwMjDc0`；Anonymous；`2026-09-19T03:28:55.380Z`；https://openreview.net/forum?id=pOcuwMjDc0
- **贡献与对象：** 用有限差分 probe 在 LoRA 微调起点估计逐事实 margin 的一阶响应模型，推导 Freedman/Azuma first-passage bounds，并识别响应系数漂移超过安全边距时界会失效。
- **机制、反传与持久性：** finite difference 是诊断/认证机制，不负责更新模型；被分析的 LoRA fine-tuning 明确使用 SGD，会反传并持久更新 LoRA 参数。
- **决定：** 边界收录，建议 `related_hybrid`。关联是用前向有限差分探针分析真实 LLM 微调遗忘，但不能列入纯 ZO 主分类。待核实 probe 的扰动维度、查询成本与代码。

### 16. Frozen in a Frame: The Velocity Blind Spot in JEPA World Models

- **ID / 作者 / OpenReview 创建时间 / 原文：** `XgB7jpGAnn`；Anonymous；`2026-09-19T11:01:51.520Z`；https://openreview.net/forum?id=XgB7jpGAnn
- **贡献与对象：** 证明单帧 JEPA target 不可辨识速度，提出显式拆分 pose code 与 finite-difference motion code 的 TI-JEPA，用于视觉世界模型规划。
- **机制、反传与持久性：** finite difference 构造运动表示，不是无梯度参数优化；模型从头训练，摘要没有无反传声明。没有 LLM/VLM 语言优化对象。
- **决定：** 排除。纯视觉动态/机器人世界模型。

### 17. Multi-Peptide Prompting Enables In-Context Learning in Protein Language Models

- **ID / 作者 / OpenReview 创建时间 / 原文：** `HleG3nAO5S`；Anonymous；`2026-09-19T02:47:46.666Z`；https://openreview.net/forum?id=HleG3nAO5S
- **贡献与对象：** 把带标签示例肽用 glycine spacer 拼接成 MPEP，并以正/负 MPEP 概率差分数对 query peptide 分类。
- **机制、反传与持久性：** 摘要明确推理时无梯度更新、无任务再训练、无结构修改；但没有搜索或优化 prompt/模型，只评估预定义示例拼接与打分规则，也不属于通用 LLM/VLM。
- **决定：** 排除。它是蛋白语言模型的固定 ICL 构造，缺少与本仓库语言模型优化范围的具体机制联系。

### 18. RESCOM: ACTIVATION RESIDUAL COMPENSATION FOR LARGE LANGUAGE MODEL QUANTIZATION

- **ID / 作者 / OpenReview 创建时间 / 原文：** `KzeQR3Rqgi`；Anonymous；`2026-09-18T16:36:23.825Z`；https://openreview.net/forum?id=KzeQR3Rqgi
- **贡献与对象：** ResCom 以 activation rounding residual 补偿低比特 LLM 层输出误差，经 output-aware calibration 选择 residual directions 并闭式计算低秩 attention correction。
- **机制、反传与持久性：** 摘要明确无 gradient training，且不更新 calibrated weights；低秩 correction 是持久部署模块/参数。
- **决定：** 边界收录，建议 `related_closed_form`。这是解析校准和 adapter 安装，不是 ZO 梯度估计。待核实 correction 的合并/存储形式。

### 19. Sharp Horizon Scaling of Gradient Variance in On-Policy Distillation

- **ID / 作者 / OpenReview 创建时间 / 原文：** `7bsXysvipt`；Anonymous；`2026-09-17T13:43:53.160Z`；https://openreview.net/forum?id=7bsXysvipt
- **贡献与对象：** 给出 LLM on-policy distillation 中 token-local、full-return 和 reward-to-go 梯度方差随 horizon 的紧界，并在 GPT-2 训练中比较优化效果。
- **机制、反传与持久性：** 主体是基于 score/梯度的学生训练；“without gradient clipping”只表示实验未裁剪梯度，绝不表示无梯度。学生权重持久更新。
- **决定：** 排除。纯一阶蒸馏方差理论，不含梯度无关优化机制。

### 20. Beyond Parameter Space: Closed-Form Cross-Trajectory Repair After Harmful Fine-Tuning

- **ID / 作者 / OpenReview 创建时间 / 原文：** `bLQ22POBgo`；Anonymous；`2026-08-20T13:27:40.509Z`；https://openreview.net/forum?id=bLQ22POBgo
- **贡献与对象：** CCTR 在 attacked-model representations 上拟合 aligned/attacked 跨轨迹输出残差，同时约束 utility activation 漂移；每个目标线性模块求正则最小二乘闭式解，修复 harmful fine-tuning 后的安全性。
- **机制、反传与持久性：** 修复阶段明确无 gradient-based optimization、无下游任务监督；修复参数/目标线性模块形成持久模型更新。此前 harmful fine-tuning 的训练方式不属于修复算法本身。
- **决定：** 边界收录，建议 `related_closed_form`。关联是 LLM 安全模型的闭式 post-hoc 参数修复。待核实闭式 delta 是原位合并还是外挂模块。

### 21. SHIFT-LLM: Distribution Shift Correction in Depth-Pruned LLMs

- **ID / 作者 / OpenReview 创建时间 / 原文：** `rfbv29Wa3V`；Anonymous；`2026-09-18T00:26:22.323Z`；https://openreview.net/forum?id=rfbv29Wa3V
- **贡献与对象：** 在被剪 block 位置插入 Linear Residual Adapter，以小型校准集的闭式最小二乘逼近缺失 residual update，并支持低秩分解和连续剪枝点精确合并。
- **机制、反传与持久性：** 基础校准明确 training-free、无 gradient computation；LRA 是持久模型 adapter。摘要另说可与 PEFT 组合获得额外恢复，该可选阶段会训练，不能与基础方法混同。
- **决定：** 边界收录，建议 `related_closed_form`；若目录描述组合实验，应单独注明 PEFT 是一阶可选扩展。

### 22. Layer-Specialized Model Merging for Training-Free Cross-Modal Reasoning Transfer

- **ID / 作者 / OpenReview 创建时间 / 原文：** `AYwu267x63`；Anonymous；`2026-09-18T09:18:16.412Z`；https://openreview.net/forum?id=AYwu267x63
- **贡献与对象：** ANO 以共享 base 的 task vector salience 闭式计算逐层融合权重，再用 MLLM 层级视觉注意力衰减校准，将文本 reasoning decoder 融入同源 MLLM decoder，保留 visual encoder/projector。
- **机制、反传与持久性：** 合并阶段无梯度更新、无多模态 reasoning 标签；输出是持久 merged decoder。源 LLM/MLLM 的原始训练不属于合并阶段。
- **决定：** 边界收录，建议 `related_closed_form`。这是闭式模型合并而非 ZO/ES。待核实论文占位方法名 `\method{}` 的最终公开名称。

### 23. Diagnosing Failure Regimes in LLM Agent Memory with Extraction-Pass Disagreement

- **ID / 作者 / OpenReview 创建时间 / 原文：** `vpahOt8lBU`；Anonymous；`2026-09-18T08:14:10.635Z`；https://openreview.net/forum?id=vpahOt8lBU
- **贡献与对象：** RRC 重复执行 memory consolidation，以 extraction-pass disagreement 和 backbone capability 判断随机遗漏还是表示能力偏差，据此路由投票预算、检索深度和回答策略。
- **机制、反传与持久性：** 摘要明确 training-free、无 gradient updates；模型权重不更新，持久对象是结构化 agent memory，路由配置/投票结果是否跨会话保存未说明。
- **决定：** 边界收录，建议 `related_inference`。关联是对 LLM agent memory pipeline 的统计诊断和推理时配置适配，并非 ZO 优化。待核实阈值是否校准训练、memory 的持久化策略。

### 24. AgentFrontier: Stabilizing Learning Frontiers in Reinforcement Learning for Active Reasoning Agents

- **ID / 作者 / OpenReview 创建时间 / 原文：** `XetdVGr0yh`；Anonymous；`2026-09-18T01:14:21.220Z`；https://openreview.net/forum?id=XetdVGr0yh
- **贡献与对象：** 解释二值 outcome reward 下仅成功/失败混合 rollout group 提供有效梯度导致 learning frontier 收缩，并以行为正则和 difficulty-aware batches 稳定 RL。
- **机制、反传与持久性：** 方法明确围绕 gradient signals 和 RL policy training，持久更新 LLM agent policy；没有 ZO/ES 或不反传组件。
- **决定：** 排除。属于一阶 RL 训练稳定化，短语命中来自梯度讨论。

### 25. Do Shared VLM Coordinates Imply Shared Calibration? A Study through Few-Shot Class-Incremental Learning

- **ID / 作者 / OpenReview 创建时间 / 原文：** `9gVp0VCEPN`；Anonymous；`2026-09-14T07:08:02.552Z`；https://openreview.net/forum?id=9gVp0VCEPN
- **贡献与对象：** 识别 VLM 视觉/文本 reference 对几何校准的角色不对称，提出 DS-PoE：校准 empirical visual estimate、保持原生 textual anchor，再固定相加两侧 logits。
- **机制、反传与持久性：** 摘要明确 training-free、无梯度更新、无 replay 和数据集特定模态权重；backbone 权重不改，持久对象是 base-derived diagonal calibration statistics/transform 与类参考。
- **决定：** 边界收录，建议 `related_closed_form`。关联是 VLM 的统计/解析校准，不应称为 ZO。待核实统计量是否随增量 session 持久更新。

### 26. Don't Retrain, Remix: Adaptation of Web Agents using Mixture Hypernetworks

- **ID / 作者 / OpenReview 创建时间 / 原文：** `Eq74LwgkjR`；Anonymous；`2026-09-19T00:33:20.250Z`；https://openreview.net/forum?id=Eq74LwgkjR
- **贡献与对象：** WebMix 先维护源界面的 LoRA adapter bank；部署时 scout agent 总结目标界面为 manual，轻量 router 一次前向预测 mixing coefficients，组合成目标界面的 adapter。
- **机制、反传与持久性：** 目标域适配无需梯度，产生可持久新 adapter；但源 adapter 和 router 是预训练组件，摘要没有说明它们的训练梯度，不能声称全流程 gradient-free。
- **决定：** 边界收录，建议 `related_hybrid`。关联是 LLM web-agent adapter 的前向组合式适配。待核实 router/adapter 的训练方法和混合 adapter 是否保存到 checkpoint。

### 27. Breaking the Refusal Barrier: Stochastic Discovery of Residual Unsafe Behaviors in Aligned Language Models

- **ID / 作者 / OpenReview 创建时间 / 原文：** `T8c8NM6FT4`；Anonymous；`2026-09-18T10:02:55.859Z`；https://openreview.net/forum?id=T8c8NM6FT4
- **贡献与对象：** SEEK 对输入做随机扰动并反复采样响应，把发现残余 unsafe behavior 建模为 coverage objective，用于生成 safety-training data。
- **机制、反传与持久性：** 发现阶段 inference-only，明确无 gradient optimization、语义 prompt engineering 或辅助 attacker LLM；模型权重不改，发现的数据集持久保存。后续在这些 failure 上 fine-tune 会更新模型权重，但摘要未说明训练优化器，应与发现算法分开记录。
- **决定：** 边界收录，建议 `related_prompt_agent`。关联是对安全 LLM 输入/响应空间的随机、无梯度行为搜索；待核实随机扰动分布和后续 fine-tuning 实现。

### 28. In-Context Robot Learning with VLM Agents

- **ID / 作者 / OpenReview 创建时间 / 原文：** `LIa6SeOhH9`；Anonymous；`2026-09-18T04:33:49.725Z`；https://openreview.net/forum?id=LIa6SeOhH9
- **贡献与对象：** GPT-Policy 以 context compiler 组织 demonstration/反馈，以 execution harness 实现几何 grounding、action chunking 和闭环决策，让通用 VLM agent 在部署时适配机器人任务。
- **机制、反传与持久性：** 摘要明确无 gradient updates 或 task-specific 参数持久变化；VLM 权重不改，运行期 context 和交互历史为外部状态，但是否跨任务持久保存未说明。摘要没有显式数值搜索器。
- **决定：** 边界收录，建议 `related_prompt_agent`。关联是 VLM agent 的反馈驱动 context/harness 适配；应标为 ICL/运行时工作流，而非 ZO/ES。待核实 context compiler 是否包含学习组件。

### 29. Code-Probe-Adapt: Interactive Heuristic Learning for Self-Evolving Agents

- **ID / 作者 / OpenReview 创建时间 / 原文：** `zeF8echOqR`；Anonymous；`2026-09-11T17:52:39.031Z`；https://openreview.net/forum?id=zeF8echOqR
- **贡献与对象：** COPA 在 persistent REPL 中让 LLM agent 以事件触发中断和 live diagnostic probing 迭代修改 code-as-policy heuristic，适配长时游戏环境。
- **机制、反传与持久性：** 摘要明确 entire method 无 gradient updates；模型权重不改，生成/修订的策略代码和 REPL 状态是持久外部工件。没有证据表明采用遗传算法，不能由 “self-evolving” 推出 evolutionary optimization。
- **决定：** 边界收录，建议 `related_prompt_agent`。这是反馈驱动的脚本/策略搜索。待核实代码候选选择规则和跨 episode 保存范围。

### 30. GRAFT: A Lightweight Shared Generative Backbone for Efficient Cross-Schema Tabular Synthesis

- **ID / 作者 / OpenReview 创建时间 / 原文：** `hJEySPVkkv`；Anonymous；`2026-09-16T20:02:56.210Z`；https://openreview.net/forum?id=hJEySPVkkv
- **贡献与对象：** 以共享小型 GAN generator 和 schema-specific mapping/discriminator 做跨 schema 表格合成，预训练后冻结 generator，再训练新 head/discriminator。
- **机制、反传与持久性：** “without gradient interference”描述不同 discriminator 间无梯度干扰，不表示无梯度训练；新 mapping 和 discriminator 明确训练并持久保存。语言模型只作为被比较的 tabular generator backbone 类型。
- **决定：** 排除。纯表格生成训练，不是 LLM/VLM 优化。

### 31. Wired to Reason: Connectome Reservoirs Align with Vision-Language Models on Raven's Matrices

- **ID / 作者 / OpenReview 创建时间 / 原文：** `z4IXYD4vKw`；Anonymous；`2026-09-07T14:12:55.393Z`；https://openreview.net/forum?id=z4IXYD4vKw
- **贡献与对象：** 用经验脑连接矩阵固定 reservoir recurrent dynamics，分析其 Raven 视觉推理状态与已训练 VLM 各层表示的对齐。
- **机制、反传与持久性：** recurrent operators 不训练，分析也无 gradient-based optimization；但论文既不优化 VLM，也不优化语言相关外部工件，只测表示对应关系。
- **决定：** 排除。无学习 reservoir 与 VLM 的对齐研究不等于梯度无关 VLM 优化。

### 32. CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention

- **ID / 作者 / OpenReview 创建时间 / 原文：** `UpR5uTu7JV`；Anonymous；`2026-09-18T17:43:17.641Z`；https://openreview.net/forum?id=UpR5uTu7JV
- **贡献与对象：** CISA 用既有 key 的紧凑摘要选择固定大小 KV chunks，以每 KV group 单 query 建索引，并用 QShare 在相邻 prefill query 复用 chunk selection，retrofit 预训练 dense-attention LLM。
- **机制、反传与持久性：** 摘要明确无需 gradient updates 或 sparse training；模型权重不改，持久变化是 attention serving 实现和 chunk-budget 配置，KV 选择状态仅在推理时存在。
- **决定：** 边界收录，建议 `related_inference`。关联是训练自由的 LLM 推理结构/系统改造，不是 ZO 参数优化。待核实是否需要离线层级校准或模型特定 profile。

### 33. scCoLLM: An LLM-Based Model Using Context-Space Adaptation for Single-Cell Analysis under Domain Shift

- **ID / 作者 / OpenReview 创建时间 / 原文：** `ICtYd1vctM`；Anonymous；`2026-09-04T06:22:57.098Z`；https://openreview.net/forum?id=ICtYd1vctM
- **贡献与对象：** scCoLLM 从未标注目标域单细胞数据中按局部相关性与全局代表性检索 cell-profile pairs，构造 Bio-Context，让通用 GPT 在 context space 适配域偏移。
- **机制、反传与持久性：** 摘要明确 training-free、无梯度更新、无标签、无参数访问；模型权重不改，Bio-Context 是外部运行时状态，是否缓存持久化未说明。检索/平衡规则的求解细节摘要未给出。
- **决定：** 边界收录，建议 `related_inference`（也可在说明中交叉标记 prompt/context）。关联是 LLM 的训练自由上下文适配，而非参数 ZO。待核实检索选择是否执行显式优化。

### 34. Eliciting Model Behaviors by Optimizing the Latent Posterior

- **ID / 作者 / OpenReview 创建时间 / 原文：** `hw82nCsx4L`；Anonymous；`2026-09-15T18:37:46.117Z`；https://openreview.net/forum?id=hw82nCsx4L
- **贡献与对象：** Posterior Prefix Tuning 在 Bayes-filtered transformer 的 latent posterior 上优化 hard-prompt 分布，以 prior predictive Monte Carlo 一次采样、importance sampling 计算 tilted surrogate 的梯度并摊销到不同 utility。
- **机制、反传与持久性：** inner loop 不做 transformer forward，也不通过模型反传，但仍显式计算并使用 prompt-distribution 参数梯度；transformer 权重冻结，持久对象是优化后的 prompt 分布/硬提示词。
- **决定：** 边界收录，建议 `related_hybrid`。它是一阶外部提示分布优化而非纯 gradient-free 方法，但与冻结语言模型的低成本提示优化直接相关。待核实外层梯度估计器实现与最终 prompt 选择规则。

### 35. Suppressing a Rejected Action Costs a KL: Closed-Form Test-Time Updates for LLM Agents

- **ID / 作者 / OpenReview 创建时间 / 原文：** `e4pspmOVIV`；Anonymous；`2026-09-17T06:26:05.687Z`；https://openreview.net/forum?id=e4pspmOVIV
- **贡献与对象：** TALE 把环境拒绝转成精确 likelihood-suppression target，在模型输出侧施加低秩 representation edit；方向解析确定，强度由一维单调 root finding 求得，使 agent 后续尝试离开失败邻域。
- **机制、反传与持久性：** 摘要明确无 backpropagation；低秩 edit 会改变当前测试时行为，但摘要未说明是直接改权重、安装临时 adapter，还是仅在会话内保留，因此“持久模型参数更新”待核实。
- **决定：** 边界收录，建议 `related_closed_form`。关联是 LLM agent 的解析式测试时更新，不应称为 ZO。待核实 edit 的参数载体、生命周期及 root finding 查询成本。

## 汇总结论

- **建议边界收录 21 条：** SCAMP、QK-Wanda、RAZOR、HarnessNet、RC-VQ、Scalar Smoothness、When Can First-Order Models of Fine-Tuning Bound Forgetting?、RESCOM、CCTR、SHIFT-LLM、ANO（投稿标题中方法名仍为占位符）、RRC、DS-PoE、WebMix、SEEK、GPT-Policy、COPA、CISA、scCoLLM、PPT、TALE。
- **排除 14 条：** Written as a Record…、GENO、LDAE、TCRA、RGB-ACD、CalibCache、TE-VLM、DV-Lens、TI-JEPA、Multi-Peptide Prompting、Sharp Horizon Scaling…、AgentFrontier、GRAFT、Wired to Reason。
- **分类边界：** 解析解、统计校准、训练自由剪枝/合并没有被改写为 ZO/ES；仅诊断或验证用的有限差分没有被当作优化器；`without BPTT`、`without gradient clipping`、不训练某个子模块也没有被改写为整条 pipeline 无反传。
- **未完成的全量边界：** 本轮只增加精确短语查询的可验证覆盖。缺乏 ICLR 2027 全部公开投稿的无截断、无空洞枚举，因而总任务覆盖状态仍应为 `partial`。
