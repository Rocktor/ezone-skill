# 迭代目标 API (plan-goal-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 5 个
- **已实现**: 0 个
- **待扩展**: 5 个
- **分类**: 迭代计划

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/plan/{planId}/goal` | 新建计划目标 | ⬜ 待实现 |
| PUT | `/project/plan/{planId}/goal/{goalId}` | 更新计划目标 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/plan/{planId}/goal` | 查询计划目标 | ⬜ 待实现 |
| GET | `/project/plan/{planId}/goal/descendant` | 查询计划目标：使用场景是查子计划的目标 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/plan/{planId}/goal/{goalId}` | 删除计划目标 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| planId | integer | 计划ID |
| request |  | 计划目标详情 |
| goalId | integer | 计划目标ID |
