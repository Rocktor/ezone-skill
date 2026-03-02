# 代码评审 API (card-code-review-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 5 个
- **已实现**: 0 个
- **待扩展**: 5 个
- **分类**: 代码集成

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| PUT | `/project/card/{projectKey}-{seqNum}/bindCodeReview` | 卡片绑定评审 | ⬜ 待实现 |
| PUT | `/project/card/{projectKey}-{seqNum}/bindExterCo...` | 卡片绑定外部系统评审 | ⬜ 待实现 |
| PUT | `/project/card/{projectKey}-{seqNum}/unbindCodeR...` | 卡片解绑评审 | ⬜ 待实现 |
| PUT | `/project/card/{projectKey}-{seqNum}/unbindExter...` | 卡片解绑外部系统评审 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/card/listReviews` | 获取评审列表 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| projectKey | string | projectKey |
| seqNum | integer | 卡片编号 |
| request |  | 创建绑定请求 |
