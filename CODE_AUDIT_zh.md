# 代码可用性审查

[简体中文](CODE_AUDIT_zh.md) | [**English**](CODE_AUDIT.md)

最后检查：**2026-09-01**

本次审查覆盖检查前所有标注为“未找到代码”的条目。每篇论文均通过两条独立路径检索：

1. 检查论文落地页和 PDF，包括脚注、附录以及明确给出的仓库链接；
2. 在 GitHub 中按完整论文标题、方法名和作者或机构进行搜索。

只有当仓库由论文直接链接，或仓库通过标题、作者/引用信息和官方实现声明与论文明确对应时，才会被收录。第三方复现、阅读笔记和通用工具库不会被标记为论文官方代码。

## 摘要

- 审查条目：**32**
- 找到并添加的官方或作者相关仓库：**16**
- 未找到官方仓库：**15**
- 论文给出但当前不可访问的仓库：**1**（PIZOO / MeZO-GV）

## 已添加的仓库

| 论文/方法 | 论文端证据 | GitHub 端证据 | 决定 |
|---|---|---|---|
| Quantized Evolution Strategies（QES） | PDF 直接给出仓库地址。 | 仓库标题和引用信息与论文一致。 | 添加 [`dibbla/Quantized-Evolution-Strategies`](https://github.com/dibbla/Quantized-Evolution-Strategies)。 |
| ESSAM | arXiv 落地页直接给出仓库地址。 | 仓库标明同一篇论文并提供可运行源码。 | 添加 [`szs777/ESSAM`](https://github.com/szs777/ESSAM)。 |
| Fine-Tuning Language Models to Know What They Know（ESMA） | PDF 直接给出仓库地址。 | 仓库标题、方法名和引用信息与论文一致。 | 添加 [`cosmoquester/ESMA`](https://github.com/cosmoquester/ESMA)。 |
| Evolutionary System 2 Reasoning（ERO） | DOI 落地页直接链接仓库。 | 仓库标题和引用信息与论文一致。 | 添加 [`MetaEvo/ERO`](https://github.com/MetaEvo/ERO)。 |
| Understanding Evolution Strategies for LLM Reasoning | PDF 直接给出仓库地址。 | 仓库标题和作者与论文一致。 | 添加 [`yunpengba7/understanding-es`](https://github.com/yunpengba7/understanding-es)。 |
| Matching Accuracy, Different Geometry | arXiv 落地页直接给出仓库地址。 | 仓库包含 ES 与 GRPO 对比实验代码。 | 添加 [`Bhoy1/ESvsGRPO`](https://github.com/Bhoy1/ESvsGRPO)。 |
| MeZO-SVRG | 会议论文页未展示仓库链接。 | Amazon Science 仓库标明 ICML 论文，并提供实现和引用信息。 | 添加 [`amazon-science/mezo_svrg`](https://github.com/amazon-science/mezo_svrg)。 |
| ConMeZO | 会议论文页未展示仓库链接。 | 仓库明确标注为官方代码，标题和作者与论文一致。 | 添加 [`LejsDeen/ConMeZO`](https://github.com/LejsDeen/ConMeZO)。 |
| ZO-LDSD | arXiv 页面和 PDF 直接给出仓库地址。 | 仓库名称和内容与 ZO-LDSD 一致。 | 添加 [`brain-lab-research/zo_ldsd`](https://github.com/brain-lab-research/zo_ldsd)。 |
| ZO-Muon | PDF 直接给出仓库地址。 | OPTML Group 仓库标明并引用该论文。 | 添加 [`OPTML-Group/ZO-Muon`](https://github.com/OPTML-Group/ZO-Muon)。 |
| HiZOO | 会议论文页未展示仓库链接。 | 仓库的标题、作者、引用信息和训练说明与 ICLR 论文一致。 | 添加 [`Yanjun-Zhao/HiZOO`](https://github.com/Yanjun-Zhao/HiZOO)。 |
| DistZO2 | 论文记录明确表示 DistZO2 已在原 ZO2 仓库开源。 | 链接指向作者的 ZO2/DistZO2 实现。 | 添加 [`liangyuwang/zo2`](https://github.com/liangyuwang/zo2)。 |
| QuZO | ACL Anthology 页面未展示仓库链接。 | 仓库标注为官方实现，并与论文引用信息一致。 | 添加 [`lloo099/QuZO`](https://github.com/lloo099/QuZO)。 |
| AdaMeZO | OpenReview 页面未展示仓库链接。 | 仓库标注为官方实现，标题和作者与论文一致。 | 添加 [`shawnnn3di/AdaMeZO`](https://github.com/shawnnn3di/AdaMeZO)。 |
| Zeroth-Order Optimization Finds Flat Minima（FlatZero） | 会议论文页未展示仓库链接。 | 仓库标明 NeurIPS 论文，并声明可复现论文实验。 | 添加 [`Liang137/FlatZero`](https://github.com/Liang137/FlatZero)。 |
| LLM Zeroth-Order Fine-Tuning is an Inference Workload | arXiv 落地页未展示仓库链接。 | 仓库标题、论文引用、作者和实现内容与该工作一致。 | 添加 [`playeriv65/zo-vllm`](https://github.com/playeriv65/zo-vllm)。 |

## 仍无可访问官方代码的条目

| 论文/方法 | 论文与项目页检查 | GitHub 检查 | 决定 |
|---|---|---|---|
| EA4LLM | 论文和 arXiv 记录中未找到代码链接。 | 按完整标题、方法和作者搜索，未找到可归属的官方仓库。 | 保留“未找到代码”。 |
| ESSA | 论文和 arXiv 记录中未找到代码链接。 | 未找到能与论文作者或项目对应的仓库。 | 保留“未找到代码”。 |
| The Blessing of Dimensionality in LLM Fine-tuning | 论文和 arXiv 记录中未找到代码链接。 | 按完整标题和作者搜索，未找到官方仓库。 | 保留“未找到代码”。 |
| Evolutionary Strategies Lead to Catastrophic Forgetting in LLMs | 论文和 arXiv 记录中未找到代码链接。 | 按完整标题和作者搜索，未找到官方仓库。 | 保留“未找到代码”。 |
| Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies | 论文和 arXiv 记录中未找到代码链接。 | 按完整标题和作者搜索，未找到官方仓库。 | 保留“未找到代码”。 |
| TeZO | 论文未链接官方仓库。 | [`junaidaliop/zij`](https://github.com/junaidaliop/zij) 中有社区实现，但未发现其与论文作者或官方项目的关联。 | 保留“未找到代码”，不以第三方代码替代。 |
| RoZO | ACL Anthology 页面和论文中未找到代码链接。 | 按完整标题、缩写和作者搜索，未找到官方仓库。 | 保留“未找到代码”。 |
| ZO-Act | 论文和 arXiv 记录中未找到代码链接。 | 按完整标题、缩写和作者搜索，未找到官方仓库。 | 保留“未找到代码”。 |
| SubZero+ | 论文未链接 SubZero+ 仓库。 | 作者的 [`zimingyy/SubZero`](https://github.com/zimingyy/SubZero) 仓库只说明了早期 SubZero 论文；没有证据表明其包含 SubZero+ 发布。 | 对 SubZero+ 保留“未找到代码”。 |
| KerZOO | 论文和 arXiv 记录中未找到代码链接。 | 按完整标题、缩写和作者搜索，未找到官方仓库。 | 保留“未找到代码”。 |
| P-GAP | 论文和 arXiv 记录中未找到代码链接。 | 按完整标题、缩写和作者搜索，未找到官方仓库。 | 保留“未找到代码”。 |
| ABSO | 论文和 arXiv 记录中未找到代码链接。 | 按完整标题、缩写和作者搜索，未找到官方仓库。 | 保留“未找到代码”。 |
| PIZOO / MeZO-GV | 论文 PDF 给出 `github.com/stananony/MeZO-GV`。 | 论文给出的地址当前返回 404，且未搜索到可访问的替代地址或改名仓库。 | 保留“未找到代码”；记录该失效链接，但不将其发布为可用代码。 |
| CurvZO | OpenReview 页面和论文中未找到代码链接。 | 按完整标题、缩写和作者搜索，未找到官方仓库。 | 保留“未找到代码”。 |
| HELENE | 预印本表示代码将在评审后发布，但最终出版页仍未展示仓库。 | 按完整标题、缩写和作者搜索，未找到官方发布。 | 保留“未找到代码”。 |
| Hi-ZFO | 论文未链接官方仓库。 | [`DKmiyan/zookit`](https://github.com/DKmiyan/zookit) 中有社区实现，但未发现其与论文作者或官方项目的关联。 | 保留“未找到代码”，不以第三方代码替代。 |

“未找到代码”表示本次审查期间未找到可访问且能明确归属的官方仓库；它不代表私有代码、已改名仓库或审查后新发布的代码不存在。
