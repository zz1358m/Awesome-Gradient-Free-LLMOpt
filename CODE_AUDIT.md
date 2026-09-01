# Code availability audit

[**English**](CODE_AUDIT.md) | [简体中文](CODE_AUDIT_zh.md)

Last checked: **2026-09-01**

This audit covers every entry that was marked `code not located` before the check. Each paper was checked through two independent routes:

1. the paper landing page and PDF, including footnotes, appendices, and explicit repository URLs;
2. GitHub searches by exact paper title, method name, and author or organization.

A repository is accepted only when it is linked by the paper or when the repository itself unambiguously matches the paper through its title, authors/citation, and official-implementation statement. Community reimplementations, reading notes, and general-purpose libraries are not labeled as the paper's code.

## Summary

- Audited: **32** entries
- Official or author-linked repositories found and added: **16**
- No official repository located: **15**
- Paper-linked repository currently unavailable: **1** (PIZOO / MeZO-GV)

## Repositories added

| Paper / method | Evidence from the paper | Evidence from GitHub | Decision |
|---|---|---|---|
| Quantized Evolution Strategies (QES) | The PDF gives the repository URL. | Repository title and citation match the paper. | Added [`dibbla/Quantized-Evolution-Strategies`](https://github.com/dibbla/Quantized-Evolution-Strategies). |
| ESSAM | The arXiv landing page gives the repository URL. | Repository identifies the same paper and provides runnable source files. | Added [`szs777/ESSAM`](https://github.com/szs777/ESSAM). |
| Fine-Tuning Language Models to Know What They Know (ESMA) | The PDF gives the repository URL. | Repository title, method name, and citation match the paper. | Added [`cosmoquester/ESMA`](https://github.com/cosmoquester/ESMA). |
| Evolutionary System 2 Reasoning (ERO) | The DOI landing page links the repository. | Repository title and citation match the paper. | Added [`MetaEvo/ERO`](https://github.com/MetaEvo/ERO). |
| Understanding Evolution Strategies for LLM Reasoning | The PDF gives the repository URL. | Repository title and authors match the paper. | Added [`yunpengba7/understanding-es`](https://github.com/yunpengba7/understanding-es). |
| Matching Accuracy, Different Geometry | The arXiv landing page gives the repository URL. | Repository contains the ES-versus-GRPO experimental code. | Added [`Bhoy1/ESvsGRPO`](https://github.com/Bhoy1/ESvsGRPO). |
| MeZO-SVRG | No repository link was exposed on the proceedings page. | The Amazon Science repository names the ICML paper and provides its implementation and citation. | Added [`amazon-science/mezo_svrg`](https://github.com/amazon-science/mezo_svrg). |
| ConMeZO | No repository link was exposed on the proceedings page. | Repository explicitly identifies itself as the official code and matches the paper title and authors. | Added [`LejsDeen/ConMeZO`](https://github.com/LejsDeen/ConMeZO). |
| ZO-LDSD | The arXiv page and PDF give the repository URL. | Repository name and contents match ZO-LDSD. | Added [`brain-lab-research/zo_ldsd`](https://github.com/brain-lab-research/zo_ldsd). |
| ZO-Muon | The PDF gives the repository URL. | The OPTML Group repository names and cites the paper. | Added [`OPTML-Group/ZO-Muon`](https://github.com/OPTML-Group/ZO-Muon). |
| HiZOO | No repository link was exposed on the proceedings page. | Repository title, authors, citation, and training instructions match the ICLR paper. | Added [`Yanjun-Zhao/HiZOO`](https://github.com/Yanjun-Zhao/HiZOO). |
| DistZO2 | The paper record explicitly states that DistZO2 is open-sourced in the existing ZO2 repository. | The linked repository is the authors' ZO2/DistZO2 implementation. | Added [`liangyuwang/zo2`](https://github.com/liangyuwang/zo2). |
| QuZO | No repository link was exposed on the ACL Anthology page. | Repository identifies itself as the official implementation and matches the paper citation. | Added [`lloo099/QuZO`](https://github.com/lloo099/QuZO). |
| AdaMeZO | No repository link was exposed on the OpenReview page. | Repository identifies itself as the official implementation and matches the paper title and authors. | Added [`shawnnn3di/AdaMeZO`](https://github.com/shawnnn3di/AdaMeZO). |
| Zeroth-Order Optimization Finds Flat Minima (FlatZero) | No repository link was exposed on the proceedings page. | Repository names the NeurIPS paper and states that it reproduces its experiments. | Added [`Liang137/FlatZero`](https://github.com/Liang137/FlatZero). |
| LLM Zeroth-Order Fine-Tuning is an Inference Workload | No repository link was exposed on the arXiv landing page. | Repository title, paper citation, authors, and implementation match the work. | Added [`playeriv65/zo-vllm`](https://github.com/playeriv65/zo-vllm). |

## Entries still without accessible official code

| Paper / method | Paper and project-page check | GitHub check | Decision |
|---|---|---|---|
| EA4LLM | No code URL found in the paper or arXiv record. | Exact-title, method, and author searches found no attributable official repository. | Keep `code not located`. |
| ESSA | No code URL found in the paper or arXiv record. | No repository could be tied to the paper authors or project. | Keep `code not located`. |
| The Blessing of Dimensionality in LLM Fine-tuning | No code URL found in the paper or arXiv record. | Exact-title and author searches found no official repository. | Keep `code not located`. |
| Evolutionary Strategies Lead to Catastrophic Forgetting in LLMs | No code URL found in the paper or arXiv record. | Exact-title and author searches found no official repository. | Keep `code not located`. |
| Overcoming Forgetting in LLM Fine-Tuning with Evolution Strategies | No code URL found in the paper or arXiv record. | Exact-title and author searches found no official repository. | Keep `code not located`. |
| TeZO | No official repository is linked by the paper. | A community implementation exists in [`junaidaliop/zij`](https://github.com/junaidaliop/zij), but no paper-author or official-project relationship was found. | Keep `code not located`; do not substitute third-party code. |
| RoZO | No code URL found on the ACL Anthology page or in the paper. | Exact-title, acronym, and author searches found no official repository. | Keep `code not located`. |
| ZO-Act | No code URL found in the paper or arXiv record. | Exact-title, acronym, and author searches found no official repository. | Keep `code not located`. |
| SubZero+ | No SubZero+ repository is linked by the paper. | The authors' [`zimingyy/SubZero`](https://github.com/zimingyy/SubZero) repository documents the earlier SubZero paper only; no evidence shows that it contains the SubZero+ release. | Keep `code not located` for SubZero+ specifically. |
| KerZOO | No code URL found in the paper or arXiv record. | Exact-title, acronym, and author searches found no official repository. | Keep `code not located`. |
| P-GAP | No code URL found in the paper or arXiv record. | Exact-title, acronym, and author searches found no official repository. | Keep `code not located`. |
| ABSO | No code URL found in the paper or arXiv record. | Exact-title, acronym, and author searches found no official repository. | Keep `code not located`. |
| PIZOO / MeZO-GV | The paper PDF gives `github.com/stananony/MeZO-GV`. | The paper-linked URL currently returns 404, and searches found no accessible replacement or rename. | Keep `code not located`; record the broken paper link rather than publishing it as working code. |
| CurvZO | No code URL found on the OpenReview page or in the paper. | Exact-title, acronym, and author searches found no official repository. | Keep `code not located`. |
| HELENE | The preprint stated that code would be released after review, but the final publication page still exposes no repository. | Exact-title, acronym, and author searches found no official release. | Keep `code not located`. |
| Hi-ZFO | No official repository is linked by the paper. | [`DKmiyan/zookit`](https://github.com/DKmiyan/zookit) contains a community implementation, but no paper-author or official-project relationship was found. | Keep `code not located`; do not substitute third-party code. |

`code not located` means that no accessible, attributable official repository was found during this audit; it does not assert that private, renamed, or subsequently released code does not exist.
