# git-team-demo

> **升级提示（v0.2.0）**：本次修改后，`list` 默认只显示未完成项。
> 如果你习惯用它查看全部待办，请改用 `list --all`。
> 历史数据仍完整保存在 `data.json` 中，没有被删除。

一个极简的命令行待办清单（Todo CLI），用于练习 Git / GitHub 团队协作流程：
分支、Pull Request、代码评审与合并。

## 环境要求

- Python 3.9 及以上（已在 Python 3.11 上验证）
- 仅使用 Python 标准库，无需安装任何第三方依赖

建议先创建虚拟环境，避免污染系统 Python：

```powershell
# Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

## 功能

- `add <内容>` 添加一条待办
- `list` 列出待办，默认只显示未完成项
- `list --all` 列出全部待办（含已完成）
- `done <序号>` 把某条标记为已完成
- `remove <序号>` 删除某条
> 序号取自 `list` 输出的第一列。隐藏已完成项后序号不重排，
> 因此 `done <序号>`、`remove <序号>` 始终指向 `list --all` 视图中的位置。

## 快速开始

```powershell
python app.py add "写实验报告"
python app.py add "复习 Git 分支"

python app.py done 1        # 把第 1 条标记为已完成
python app.py list          # 只列出未完成项，所以刚 done 的第 1 条不会出现在这里
python app.py list --all    # 想看全部（含已完成）就用这个
python app.py remove 2      # 删除第 2 条
```

## 数据存储

待办数据保存在脚本同目录的 `data.json` 中，该文件已被 `.gitignore` 忽略，
不会进入版本库。想清空数据，直接删除该文件即可。

## 项目结构

```
git-team-demo/
├── .github/
│   └── pull_request_template.md   # PR 描述模板
├── .gitattributes                 # 统一换行符为 LF
├── .gitignore
├── app.py                         # 全部逻辑：参数解析、读写 JSON、四个子命令
└── README.md
```

## 协作流程

1. 从 `main` 拉出分支 `feature/<你的名字>`
2. 在分支上提交改动并推送到远程
3. 发起 Pull Request，指定另一位成员为 reviewer
4. 评审通过后合并回 `main`
