# 评论 API (card-comment-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 5 个
- **已实现**: 0 个
- **待扩展**: 5 个
- **分类**: 卡片管理

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/card/{cardId}/comment` | 新建卡片评论 | ⬜ 待实现 |
| POST | `/project/card/{cardId}/comment/{commentId}/reply` | 新建卡片评论回复 | ⬜ 待实现 |
| PUT | `/project/card/{cardId}/comment/{commentId}` | 更新卡片评论 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/card/{cardId}/comment` | 查询卡片评论 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/card/{cardId}/comment/{commentId}` | 删除卡片评论 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| cardId | integer | 卡片ID |
| request |  | 评论内容 |
| commentId | integer | 评论ID |
