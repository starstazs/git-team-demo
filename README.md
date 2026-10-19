# git-team-demo

一个极简的命令行待办清单（Todo CLI），用于练习 Git / GitHub 团队协作流程：
分支、Pull Request、代码评审与合并。

## 功能

- 添加待办
- 列出待办

## 快速开始

```bash
python app.py add "写实验报告"
python app.py list
```

数据保存在脚本同目录的 `data.json` 中，该文件已被 `.gitignore` 忽略。

## 项目结构

```
git-team-demo/
├── app.py        # 全部逻辑：参数解析、读写 JSON、四个子命令
├── README.md
└── .gitignore
```

## 协作流程

1. 从 `main` 拉出分支 `feature/<你的名字>`
2. 在分支上提交改动并推送到远程
3. 发起 Pull Request，指定另一位成员为 reviewer
4. 评审通过后合并回 `main`
