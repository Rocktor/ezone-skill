# EZone API 摘要索引

> 生成时间: 2026-01-31

本目录包含 EZone 项目管理系统的 API 摘要文件，方便快速查阅和扩展功能。

## 统计

- **总接口数**: 341
- **已实现**: 10
- **覆盖率**: 2.9%
- **模块数**: 24

## 模块索引

### 卡片管理

| 模块 | 文件 | 接口数 | 已实现 |
|------|------|--------|--------|
| 卡片管理 API | [card.md](card.md) | 73 | 6 |
| 卡片外部接口 API | [card-api.md](card-api.md) | 25 | 0 |
| 附件管理 API | [attachment.md](attachment.md) | 8 | 1 |
| 评论 API | [comment.md](comment.md) | 5 | 0 |
| 事件历史 API | [event.md](event.md) | 3 | 1 |
| 卡片关联 API | [relate.md](relate.md) | 2 | 0 |
| 关注 API | [watch.md](watch.md) | 3 | 0 |
| 自定义查询视图 API | [query-view.md](query-view.md) | 8 | 0 |

### 项目管理

| 模块 | 文件 | 接口数 | 已实现 |
|------|------|--------|--------|
| 项目管理 API | [project.md](project.md) | 29 | 1 |
| 项目外部接口 API | [project-api.md](project-api.md) | 34 | 0 |
| 成员管理 API | [member.md](member.md) | 5 | 0 |
| 字段/状态配置 API | [schema.md](schema.md) | 35 | 1 |

### 迭代计划

| 模块 | 文件 | 接口数 | 已实现 |
|------|------|--------|--------|
| 迭代管理 API | [plan.md](plan.md) | 19 | 0 |
| 迭代外部接口 API | [plan-api.md](plan-api.md) | 7 | 0 |
| 迭代目标 API | [goal.md](goal.md) | 5 | 0 |

### 其他

| 模块 | 文件 | 接口数 | 已实现 |
|------|------|--------|--------|
| 报表图表 API | [chart.md](chart.md) | 22 | 0 |
| 版本管理 API | [version.md](version.md) | 17 | 0 |
| 工作台 API | [workbench.md](workbench.md) | 2 | 0 |
| 故事地图 API | [story-map.md](story-map.md) | 11 | 0 |

### 代码集成

| 模块 | 文件 | 接口数 | 已实现 |
|------|------|--------|--------|
| 代码分支关联 API | [code-branch.md](code-branch.md) | 9 | 0 |
| 代码评审 API | [code-review.md](code-review.md) | 5 | 0 |
| 代码仓库 API | [repo.md](repo.md) | 5 | 0 |

### 测试管理

| 模块 | 文件 | 接口数 | 已实现 |
|------|------|--------|--------|
| 测试用例 API | [test-case.md](test-case.md) | 5 | 0 |
| 测试计划 API | [test-plan.md](test-plan.md) | 4 | 0 |

## 快速开始

```python
from ezone_api import EZoneAPI, get_token

# 初始化
api = EZoneAPI(token=get_token())

# 搜索卡片
cards = api.search_cards(project_id="844795161124806656")

# 创建卡片
result = api.create_card(
    project_id="844795161124806656",
    card_type="task",
    title="任务标题"
)
```

## 扩展指引

需要扩展新功能时：

1. 查找对应模块的摘要文件
2. 找到需要的 API 端点
3. 在 `ezone_api.py` 中添加方法
4. 更新 `SKILL.md` 文档

## 相关文件

| 文件 | 说明 |
|------|------|
| `../ezone_api.py` | API 客户端实现 |
| `../SKILL.md` | Skill 使用说明 |
| `../ezone_api_doc.json` | 原始 Swagger JSON |
