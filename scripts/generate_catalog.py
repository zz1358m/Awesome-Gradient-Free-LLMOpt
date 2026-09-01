#!/usr/bin/env python3
"""Generate the bilingual paper tables and distribution charts."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"

START = "<!-- GENERATED CATALOG:START -->"
END = "<!-- GENERATED CATALOG:END -->"

CATEGORIES = [
    {
        "key": "es_pretraining",
        "family": "ES",
        "level": 3,
        "en": "Pretraining",
        "zh": "预训练",
    },
    {
        "key": "es_single_turn",
        "family": "ES",
        "level": 3,
        "en": "Single-turn reasoning and alignment",
        "zh": "单轮推理与对齐",
    },
    {
        "key": "es_multi_turn",
        "family": "ES",
        "level": 3,
        "en": "Multi-turn and agentic reasoning",
        "zh": "多轮与智能体推理",
    },
    {
        "key": "es_understanding",
        "family": "ES",
        "level": 3,
        "en": "Understanding ES",
        "zh": "理解 ES",
    },
    {
        "key": "zo_baselines",
        "family": "ZO",
        "level": 4,
        "en": "Baselines, sparse updates, and subspaces",
        "zh": "基线、稀疏更新与子空间",
    },
    {
        "key": "zo_directions",
        "family": "ZO",
        "level": 4,
        "en": "Better directions and lower variance",
        "zh": "更优方向与更低方差",
    },
    {
        "key": "zo_systems",
        "family": "ZO",
        "level": 4,
        "en": "Memory systems, preconditioning, and quantization",
        "zh": "内存系统、预条件与量化",
    },
    {
        "key": "zo_multi_turn",
        "family": "ZO",
        "level": 3,
        "en": "Multi-turn agent adaptation",
        "zh": "多轮智能体适配",
    },
    {
        "key": "zo_understanding",
        "family": "ZO",
        "level": 3,
        "en": "Understanding and systems",
        "zh": "机理理解与系统",
    },
]

CATEGORY_BY_KEY = {category["key"]: category for category in CATEGORIES}


def load_papers() -> list[dict[str, str]]:
    papers = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    required = {
        "title",
        "category",
        "date",
        "description_en",
        "description_zh",
        "resources_en",
        "resources_zh",
    }
    titles: set[str] = set()
    for index, paper in enumerate(papers, start=1):
        missing = required - paper.keys()
        if missing:
            raise ValueError(f"Paper {index} is missing fields: {sorted(missing)}")
        if paper["category"] not in CATEGORY_BY_KEY:
            raise ValueError(f"Unknown category for {paper['title']}: {paper['category']}")
        if not re.fullmatch(r"20\d{2}(?:-\d{2})?", paper["date"]):
            raise ValueError(f"Invalid date for {paper['title']}: {paper['date']}")
        if paper["title"] in titles:
            raise ValueError(f"Duplicate paper title: {paper['title']}")
        titles.add(paper["title"])
    return papers


def escape_table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def table_for(papers: list[dict[str, str]], language: str) -> str:
    if language == "en":
        lines = [
            "| Date | Paper | Contribution | Resources |",
            "|---|---|---|---|",
        ]
    else:
        lines = [
            "| 日期 | 论文 | 核心贡献 | 资源 |",
            "|---|---|---|---|",
        ]
    for paper in papers:
        row = [
            paper["date"],
            f"**{paper['title']}**",
            paper[f"description_{language}"],
            paper[f"resources_{language}"],
        ]
        lines.append("| " + " | ".join(escape_table_cell(cell) for cell in row) + " |")
    return "\n".join(lines)


def render_catalog(papers: list[dict[str, str]], language: str) -> str:
    grouped = {
        category["key"]: [p for p in papers if p["category"] == category["key"]]
        for category in CATEGORIES
    }
    lines = [START]
    if language == "en":
        lines.extend(
            [
                "## Literature overview",
                "",
                f"**{len(papers)} papers** are currently included. The tables and figures below are generated from [`data/papers.json`](data/papers.json).",
                "",
                '<p align="center">',
                '  <img src="assets/year-distribution.svg" width="48%" alt="Papers by year">',
                '  <img src="assets/category-distribution.svg" width="48%" alt="Papers by category">',
                "</p>",
                "",
                "## Evolution strategies",
            ]
        )
    else:
        lines.extend(
            [
                "## 文献概览",
                "",
                f"当前共收录 **{len(papers)} 篇论文**。下列表格和图表均由 [`data/papers.json`](data/papers.json) 自动生成。",
                "",
                '<p align="center">',
                '  <img src="assets/year-distribution-zh.svg" width="48%" alt="论文年度分布">',
                '  <img src="assets/category-distribution-zh.svg" width="48%" alt="论文类别分布">',
                "</p>",
                "",
                "## 进化策略",
            ]
        )

    for category in CATEGORIES:
        if category["family"] != "ES":
            continue
        lines.extend(
            [
                "",
                f"{'#' * category['level']} {category[language]}",
                "",
                table_for(grouped[category["key"]], language),
            ]
        )

    if language == "en":
        lines.extend(
            [
                "",
                "## Zeroth-order optimization",
                "",
                "Unless an entry says otherwise, these methods optimize a supervised CE/NLL-style objective with forward-only function evaluations. Their main contribution is making SFT feasible under activation-memory, optimizer-state, or black-box constraints.",
                "",
                "### Single-turn SFT and adaptation",
            ]
        )
    else:
        lines.extend(
            [
                "",
                "## 零阶优化",
                "",
                "除非条目另有说明，这些方法通常通过纯前向函数值评估优化监督式 CE/NLL 目标。其主要贡献是使监督微调能够在激活内存、优化器状态或黑盒访问受限的条件下进行。",
                "",
                "### 单轮监督微调与适配",
            ]
        )

    for category in CATEGORIES:
        if category["family"] != "ZO":
            continue
        lines.extend(
            [
                "",
                f"{'#' * category['level']} {category[language]}",
                "",
                table_for(grouped[category["key"]], language),
            ]
        )
    lines.extend([END, ""])
    return "\n".join(lines)


def replace_catalog(path: Path, language: str, catalog: str) -> None:
    content = path.read_text(encoding="utf-8")
    if START in content and END in content:
        pattern = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
        updated = pattern.sub(catalog, content, count=1)
    else:
        start_heading = "## Evolution strategies" if language == "en" else "## 进化策略"
        end_heading = "## Scope" if language == "en" else "## 收录范围"
        start_index = content.index(start_heading)
        end_index = content.index(end_heading)
        updated = content[:start_index] + catalog + "\n" + content[end_index:]
    path.write_text(updated, encoding="utf-8")


def svg_document(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
<style>
  text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; fill: #24292f; }}
  .title {{ font-size: 20px; font-weight: 700; }}
  .label {{ font-size: 13px; }}
  .value {{ font-size: 13px; font-weight: 700; }}
  @media (prefers-color-scheme: dark) {{
    text {{ fill: #e6edf3; }}
    .background {{ fill: #161b22; stroke: #30363d; }}
  }}
</style>
<rect class="background" width="100%" height="100%" rx="12" fill="#f6f8fa" stroke="#d0d7de"/>
{body}
</svg>
"""


def year_svg(papers: list[dict[str, str]], language: str) -> str:
    counts = Counter(paper["date"][:4] for paper in papers)
    years = sorted(counts)
    width, height = 620, 330
    left, right, top, bottom = 58, 24, 58, 48
    chart_width = width - left - right
    chart_height = height - top - bottom
    slot = chart_width / len(years)
    bar_width = min(72, slot * 0.58)
    maximum = max(counts.values())
    title = "Papers by year" if language == "en" else "论文年度分布"
    body = [f'<text x="24" y="34" class="title">{title}</text>']
    body.append(
        f'<line x1="{left}" y1="{top + chart_height}" x2="{width - right}" y2="{top + chart_height}" stroke="#8c959f"/>'
    )
    for index, year in enumerate(years):
        count = counts[year]
        bar_height = chart_height * count / maximum
        x = left + slot * index + (slot - bar_width) / 2
        y = top + chart_height - bar_height
        body.extend(
            [
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_width:.1f}" height="{bar_height:.1f}" rx="5" fill="#2f81f7"/>',
                f'<text x="{x + bar_width / 2:.1f}" y="{y - 8:.1f}" text-anchor="middle" class="value">{count}</text>',
                f'<text x="{x + bar_width / 2:.1f}" y="{height - 20}" text-anchor="middle" class="label">{year}</text>',
            ]
        )
    return svg_document(width, height, "\n".join(body))


def category_svg(papers: list[dict[str, str]], language: str) -> str:
    counts = Counter(paper["category"] for paper in papers)
    width = 760
    row_height = 31
    top = 58
    height = top + len(CATEGORIES) * row_height + 24
    label_width = 315 if language == "en" else 235
    chart_left = label_width + 24
    chart_width = width - chart_left - 52
    maximum = max(counts.values())
    title = "Papers by category" if language == "en" else "论文类别分布"
    body = [
        f'<text x="24" y="34" class="title">{title}</text>',
        '<rect x="625" y="18" width="12" height="12" rx="2" fill="#a371f7"/>',
        '<text x="643" y="29" class="label">ES</text>',
        '<rect x="686" y="18" width="12" height="12" rx="2" fill="#2f81f7"/>',
        '<text x="704" y="29" class="label">ZO</text>',
    ]
    colors = {"ES": "#a371f7", "ZO": "#2f81f7"}
    for index, category in enumerate(CATEGORIES):
        count = counts[category["key"]]
        y = top + index * row_height
        bar_width = chart_width * count / maximum
        label = html.escape(category[language])
        body.extend(
            [
                f'<text x="24" y="{y + 17}" class="label">{label}</text>',
                f'<rect x="{chart_left}" y="{y + 3}" width="{bar_width:.1f}" height="20" rx="4" fill="{colors[category["family"]]}"/>',
                f'<text x="{chart_left + bar_width + 8:.1f}" y="{y + 18}" class="value">{count}</text>',
            ]
        )
    return svg_document(width, height, "\n".join(body))


def generated_files(papers: list[dict[str, str]]) -> dict[Path, str]:
    return {
        ROOT / "README.md": render_catalog(papers, "en"),
        ROOT / "README_zh.md": render_catalog(papers, "zh"),
        ROOT / "assets" / "year-distribution.svg": year_svg(papers, "en"),
        ROOT / "assets" / "year-distribution-zh.svg": year_svg(papers, "zh"),
        ROOT / "assets" / "category-distribution.svg": category_svg(papers, "en"),
        ROOT / "assets" / "category-distribution-zh.svg": category_svg(papers, "zh"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="fail if generated files are stale"
    )
    args = parser.parse_args()

    if not DATA_PATH.exists():
        print(f"Missing canonical data file: {DATA_PATH.relative_to(ROOT)}", file=sys.stderr)
        return 1

    papers = load_papers()
    outputs = generated_files(papers)

    if args.check:
        stale = []
        for path, generated in outputs.items():
            if path.name.startswith("README"):
                content = path.read_text(encoding="utf-8")
                if START not in content or END not in content:
                    stale.append(path)
                    continue
                current = content.split(START, 1)[1].split(END, 1)[0]
                expected = generated.split(START, 1)[1].split(END, 1)[0]
                if current != expected:
                    stale.append(path)
            elif not path.exists() or path.read_text(encoding="utf-8") != generated:
                stale.append(path)
        if stale:
            for path in stale:
                print(f"Stale generated file: {path.relative_to(ROOT)}", file=sys.stderr)
            print("Run: python3 scripts/generate_catalog.py", file=sys.stderr)
            return 1
        print(f"Catalog is up to date ({len(papers)} papers).")
        return 0

    for path, generated in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.name.startswith("README"):
            replace_catalog(path, "zh" if path.name == "README_zh.md" else "en", generated)
        else:
            path.write_text(generated, encoding="utf-8")
    print(f"Generated bilingual tables and charts for {len(papers)} papers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
