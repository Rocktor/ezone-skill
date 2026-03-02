# 事件历史 API (card-event-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 3 个
- **已实现**: 1 个
- **待扩展**: 2 个
- **分类**: 卡片管理

## 接口列表

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/card/{cardId}/event` | 查询卡片事件: 返回各种类型事件请参看接口'event/example' | ✅ 已实现 |
| GET | `/project/card/{cardId}/event/example` | 卡片事件Example | ⬜ 待实现 |
| GET | `/project/card/{cardId}/event/{eventId}` | 查询卡片事件: 返回各种类型事件请参看接口'event/example' | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| cardId | integer | 卡片ID |

## 使用示例

```python
from ezone_api import EZoneAPI, get_token

api = EZoneAPI(token=get_token())

# 获取卡片事件历史
events = api.get_card_events(card_id="1054283723845951488")

# 获取状态变更历史
history = api.get_card_status_history(
    card_id="1054283723845951488",
    project_id="844795161124806656"
)
```
