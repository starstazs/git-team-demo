#!/usr/bin/env python3
"""待办清单（Todo CLI）—— Git 团队协作实践 demo 项目。

只用 Python 标准库，数据保存在脚本同目录的 data.json 中。

用法示例：
    python app.py add "写实验报告"
    python app.py list
    python app.py done 1
    python app.py remove 1
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.json")


def load_items() -> list[dict]:
    """读取待办列表；文件不存在或内容损坏时返回空列表。"""
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []


def save_items(items: list[dict]) -> None:
    DATA_FILE.write_text(
        json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def cmd_add(text: str) -> None:
    items = load_items()
    items.append({"text": text, "done": False})
    save_items(items)
    print(f"已添加：{text}")


def cmd_list(show_all: bool = False) -> None:
    """列出待办事项。show_all 为 False 时只显示未完成项。"""
    items = load_items()
    if not items:
        print("暂无待办事项，用 add 添加一条吧。")
        return
    for index, item in enumerate(items, start=1):
        if not show_all and item["done"]:
            continue
        mark = "x" if item["done"] else " "
        print(f"{index:>2}. [{mark}] {item['text']}")


def cmd_done(index: int) -> None:
    items = load_items()
    if not 1 <= index <= len(items):
        print(f"序号 {index} 不存在")
        return
    items[index - 1]["done"] = True
    save_items(items)
    print(f"已完成：{items[index - 1]['text']}")


def cmd_remove(index: int) -> None:
    items = load_items()
    if not 1 <= index <= len(items):
        print(f"序号 {index} 不存在")
        return
    removed = items.pop(index - 1)
    save_items(items)
    print(f"已删除：{removed['text']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="一个极简的命令行待办清单")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="添加一条待办")
    p_add.add_argument("text", help="待办内容")

    p_list = sub.add_parser("list", help="列出待办")
    p_list.add_argument("--all", action="store_true", help="同时显示已完成项")

    p_done = sub.add_parser("done", help="把某条标记为已完成")
    p_done.add_argument("index", type=int, help="待办序号，从 1 开始")

    p_remove = sub.add_parser("remove", help="删除某条待办")
    p_remove.add_argument("index", type=int, help="待办序号，从 1 开始")

    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "add":
        cmd_add(args.text)
    elif args.command == "list":
        cmd_list(show_all=args.all)
    elif args.command == "done":
        cmd_done(args.index)
    elif args.command == "remove":
        cmd_remove(args.index)


if __name__ == "__main__":
    main()
