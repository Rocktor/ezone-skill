# EZone Card Creator Skill

Kiro CLI skill for managing cards in [EZone](https://ezone.matrixback.com) (简单云) project management system.

## Features

- Create cards (Task/Story/Bug/Feature/Epic)
- Batch create cards
- Query card status history & event timeline
- Query card approval/review records (BPM workflow)
- Delete cards (single & batch)

## Installation

Copy `SKILL.md` and `ezone_api.py` to your Kiro skills directory:

```bash
mkdir -p ~/.kiro/skills/ezone-card-creator
cp SKILL.md ezone_api.py ~/.kiro/skills/ezone-card-creator/
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
