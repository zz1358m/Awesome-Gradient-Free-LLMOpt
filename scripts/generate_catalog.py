#!/usr/bin/env python3
"""Generate the bilingual paper tables."""

from __future__ import annotations

import argparse
import json
import re
import sys
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
                "## Evolution strategies",
            ]
        )
    else:
        lines.extend(
            [
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


def generated_files(papers: list[dict[str, str]]) -> dict[Path, str]:
    return {
        ROOT / "README.md": render_catalog(papers, "en"),
        ROOT / "README_zh.md": render_catalog(papers, "zh"),
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
    print(f"Generated bilingual tables for {len(papers)} papers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
