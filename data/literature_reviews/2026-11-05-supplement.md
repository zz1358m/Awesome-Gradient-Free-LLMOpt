# 2026-11-05 文献补充检查

在今日已有268条的远端目录上补充4篇：ZEST为2025年零阶语言模型参数优化漏收录；FAAST为2026年5月闭式适配漏收录，须标明读出和评分模块预训练依赖AdamW；SPOD与EGDR为11月3日arXiv初版的无模型权重更新推理校准，跨平台最早公开日期待核实。目录增至272条。本轮没有新增确定本周首次公开的主线论文；今日先前已收录MobileSpec不重复计数。

UTC: 2026-10-29T14:10:50.200Z -- 2026-11-05T14:10:50.200Z.

今日早前检查已另行提交：[2026-11-05.json](2026-11-05.json)。本补充不重复统计MobileSpec或已有同题版本。

## Zeroth-Order Sharpness-Aware Learning with Exponential Tilting

作者: Xuchen Gong; Tian Li

公开日期: 2025-10-17T19:01:34Z; arXiv v1 2025-10-17T19:01:34Z; backfill

原文: [paper](https://arxiv.org/abs/2510.16157)

核心贡献: ZEST通过成对函数值扰动和种子重建更新，优化指数倾斜的锐度感知目标；无需反传即可持久更新语言模型权重，一阶SAM方法为比较基线。历史补收录；具体模块覆盖、代码和录用待核实。

方法: 指数倾斜目标；成对随机扰动的函数值加权；种子重建参数更新。

反传依赖: ZEST更新无需反传；一阶SAM、TSAM等为独立比较分支，非ZEST必需阶段。

持久参数及模块: 是，语言模型权重；实验含RoBERTa-Base与OPT-1.3B，逐模块参数集合待核实。

相关性: 高，直接语言模型函数值零阶参数优化，放入更优方向与更低方差。

实际位置: data/papers.json / zo_directions; README.md, README_zh.md, papers.bib

待人工核实: 核实原始摘要、版本历史、算法1和部分实验设置，未阅读全文或独立复现。 不能把近期会议解读或抓取日期视为首发；首次arXiv公开为2025-10-17。 未核实作者代码与正式录用；泛化与锐度结论保留为作者在其设置下的结果。

## FAAST: Forward-Only Associative Learning via Closed-Form Fast Weights for Test-Time Supervised Adaptation

作者: Guangsheng Bao; Hongbo Zhang; Han Cui; Ke Sun; Yanbin Zhao; Juncai He; Yue Zhang

公开日期: 2026-05-06T08:58:11Z; arXiv v1 2026-05-06T08:58:11Z; backfill

原文: [paper](https://arxiv.org/abs/2605.04651)

核心贡献: 在冻结语言模型表征上，将监督样本编译为闭式快权重矩阵；适配阶段无需反传，改变辅助快权重而非骨干。语言模型实验先以AdamW预训练词元评分与读出组件，全流程并非梯度无关。历史补收录；录用待核实。

方法: 基于伪逆或最小二乘的关联快权重编译与增量统计更新。

反传依赖: 测试时闭式适配不需反传；附录C.2及表7说明词元评分器和读出投影预训练采用AdamW，不能称全流程无反传。

持久参数及模块: 骨干冻结；改变可复用的任务快权重矩阵及其统计状态。另有事先训练的评分与读出参数，不计纯ES/ZO骨干训练。

相关性: 中高，非智能体的闭式语言模型适配，保留准备阶段反传边界。

实际位置: data/papers.json / related_closed_form; README.md, README_zh.md, papers.bib

待人工核实: 核实摘要、版本历史、方法及附录C.2，未阅读全文或复现。 首次提交为2026-05-06，2026-05-08是修订日期，不能混作首次公开。 代码仓库可访问但未全面审查；快权重持久保存与重置策略、全部模块实现和录用待核实。

## SPOD: Recovering Suppressed Temporal Evidence in Video-LLMs via Single-Pass Orthogonal Decomposition

作者: Yangguang Lin; Quan Fang; Xiaoyan Liu; Zefan Xu

公开日期: 最早日期待核实; arXiv v1 2026-11-03T11:46:39Z; arxiv_v1_in_window_earliest_public_unverified

原文: [paper](https://arxiv.org/abs/2611.04728)

核心贡献: 利用帧区分度与帧间隐状态差异构建时间及先验子空间，在一次前向过程中重缩放隐状态分量；所提阶段不反传、不持久更新模型权重。归入关联推理校准。arXiv初版11月3日；作者称ACM MM 2026，最早公开时间待核实。

方法: 隐状态几何、截断SVD、正交子空间分解与分量重缩放。

反传依赖: 所提推理干预不需反传；既有模型训练依赖另行存在。

持久参数及模块: 不更新持久模型权重；操作当前视频和生成过程的隐状态、分解基与缩放配置。

相关性: 中，视频语言模型无反传内部校准；非提示优化或外部智能体工件搜索，按现有范围保留。

实际位置: data/papers.json / related_inference; README.md, README_zh.md, papers.bib

待人工核实: 核实原始摘要、版本历史和部分方法及实现说明，未阅读全文或独立复现。 arXiv记载ACM MM 2026与DOI 10.1145/3767308.3835492，未独立读取正式论文集或核实更早公开时间。 代码可访问，未全面审查；不将作者的单遍效率和性能声明作为独立验证结论。

## Entropy-Gated Dynamic Rectification for Object Hallucination in Large Vision-Language Models

作者: Riasad Alvi; Md. Asaduzzaman Shuvo; Md. Ahashan Habib; Md. Faiyaz Abdullah Sayeedi

公开日期: 最早日期待核实; arXiv v1 2026-11-03T07:31:21Z; arxiv_v1_in_window_earliest_public_unverified

原文: [paper](https://arxiv.org/abs/2611.04438)

核心贡献: EGDR以前一词元熵调节已校准的隐空间干预门；用留出数据前向评估确定方向、层位及门控设置，推理时改变隐状态，无需反传且不持久更新模型权重。归入关联推理校准。arXiv初版11月3日；WACV 2027声明和最早公开时间待核实。

方法: 预测熵驱动阈值调节；固定潜在方向与留出数据前向校准。

反传依赖: 原文第4节明确不添加训练参数或梯度更新；校准依赖前向评估，非一阶模型训练。

持久参数及模块: 不更新骨干或适配器权重；保存校准向量、阈值及配置，逐词元改变隐状态。

相关性: 中，视觉语言模型无反传推理校准；不计梯度无关模型参数优化。

实际位置: data/papers.json / related_inference; README.md, README_zh.md, papers.bib

待人工核实: 核实原始摘要、版本历史、第4节与限制部分，未阅读全文或复现。 作者标注WACV 2027，未独立核实录用、正式论文集及跨平台最早日期。 正文限定两种7B LLaVA骨干和贪心解码，并报告均值而无置信区间；额外收益稳定性和校准迁移待核实。

## 候选检查记录

- Training Specialist LLMs on Your Phone: Forward-Only Optimization via Block-Spectral Coordinates: already_added_by_prior_2026_11_05_commit. 最新远端c6c3f6b已收录MobileSpec；不重复新增。
- The Evolution Strategies Paradox: Better Models from Worse Perturbations: existing_duplicate. 已有OpenReview条目，最新远端已补arXiv链接；不将11月3日预印本版本作为新工作重复收录。
- Weight-Space Software Engineering (WSSE): not_added_language_model_application_unverified. 已核实原始仓库及论文源文件；实证对象为生成器、超分辨模型等。语言模型权重编辑主要出现在相关工作与未来场景，未取得当前语言模型方法或实证依据。项目页与Zenodo DOI访问失败，不以第三方报道代替原始证据。
- Black-Box Tuning / BBTv2: excluded_prompt_scope. 以软提示优化为核心，按用户现行范围不收录。
- ReflectDrive: not_added_pending_primary_training_evidence. 命中第三方知识库，未取得原始研究的持久模型参数训练证据，不进入目录。
- AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization: not_added_pending_primary_training_evidence. 命中旧文献二手解读；未取得目标模型参数训练的原始证据，不因零阶措辞新增外部工件优化。
- Sketchpad: certified exact arithmetic with a small vision-language model: not_added. 原始检索摘要为模型与可证明运算过程，未确认梯度无关优化机制。
- Backpropagation-Free Continual Learning: A Unified Energy-Based Framework, Reproducible Benchmark, and Open Challenges: not_added_pending_primary_scope_verification. 检索命中通用无反传持续学习综述，未核实语言模型适用性与原始研究内容，不将其视作本周首发。
- Accelerating LLM Pretraining with Zeroth-Order Curvature on Idle Serving Compute: existing_duplicate. 已有题名及原始链接记录，不重复收录。
- ENGINE: Endogenous Variational MultiScale Optimization for Zeroth-Order LLM Fine-Tuning: existing_duplicate. 已有题名及原始链接记录，不重复收录。
- The Cost of Mismatch: Noise Amplification in Zeroth-Order Reinforcement Learning: existing_duplicate. 已有题名及原始链接记录，不重复收录。
- Dust: Pretraining Transformers Without Backpropagation: existing_duplicate. 已有题名及原始链接记录，不重复收录。
- Consolidating Rewarded Perturbations for LLM Post-Training: existing_duplicate. 已有题名及原始链接记录，不重复收录。
- Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM Fine-Tuning: existing_duplicate. 已有题名及原始链接记录，不重复收录。
- Delta N-gram: Forward-Only Continual Writing into a Language Model's Native N-gram Memory: existing_duplicate. 已有题名及原始链接记录，不重复收录。
- Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights: existing_duplicate. 已有题名及原始链接记录，不重复收录。

## 检索与限制

本报告补充今日已有2026-11-05.json记录，检索窗口仍为2026-10-29至2026-11-05；近期新增查询重点覆盖上次检查后的日期，并复用已提交的一周候选记录去重。只使用明确方法关键词和精确题名，未抓通用语言模型语料或会议全量投稿。论文或作者原始页面均已核实，部分方法和设置已阅读，未宣称全文核读或独立复现。未证实的会议声明、首次公开时间及代码实现均保留待核实标记。

- "zeroth-order" "LLM" after:2026-11-02 before:2026-11-06
- "gradient-free" "language model" after:2026-11-02 before:2026-11-06
- "evolution strategies" "language" after:2026-11-02 before:2026-11-06
- "backpropagation-free" "language" after:2026-11-02 before:2026-11-06
- "zeroth-order" "language model" "November 4" "2026"
- "gradient-free" "LLM" "November 5" "2026"
- "forward-only" "language model" after:2026-11-03 before:2026-11-06
- site:openreview.net "zeroth-order" "ICLR 2027"
- "Zeroth-Order Sharpness-Aware Learning with Exponential Tilting" arxiv
- "zeroth-order" "Nov 4" "2026"
- "gradient-free" "Nov 4" "2026"
- "FAAST: Forward-Only Associative Learning via Closed-Form Fast Weights for Test-Time Supervised Adaptation"
