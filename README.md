# EZone Card Creator Skill

Claude Code skill for managing cards in [EZone](https://ezone.matrixback.com) (简单云) project management system.

## Features

- Create cards (Task/Story/Bug/Feature/Epic)
- Batch create cards
- Query card status history & event timeline
- Query card approval/review records (BPM workflow)
- Delete cards (single & batch)

## File Structure

```
ezone-card-creator/
├── SKILL.md                    # Skill 定义与使用说明
├── ezone_api.py                # API 客户端
├── ezone_api_doc.json          # EZone Swagger/OpenAPI 完整文档 (341 APIs)
├── generate_api_summaries.py   # API 文档摘要生成脚本
└── api_summaries/              # 按模块生成的 API 摘要 (27 files)
    ├── README.md
    ├── card.md
    ├── project.md
    └── ...
```

## Installation

Copy the entire directory to your Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills/ezone-card-creator
cp -r . ~/.claude/skills/ezone-card-creator/
```

## Token Configuration

```bash
# Option 1: Environment variable (recommended)
export EZONE_TOKEN=your_token_here

# Option 2: User config file
echo 'your_token_here' > ~/.ezone_token
chmod 600 ~/.ezone_token
```

Get your token at: EZone → 个人设置 → 访问令牌
