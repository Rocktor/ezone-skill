# 迭代管理 API (plan-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 19 个
- **已实现**: 0 个
- **待扩展**: 19 个
- **分类**: 迭代计划

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/plan` | 新建计划 | ⬜ 待实现 |
| POST | `/project/plan/tree` | 新建计划 | ⬜ 待实现 |
| PUT | `/project/plan/{id}` | 更新计划 | ⬜ 待实现 |
| PUT | `/project/plan/{id}/active` | 取消归档 | ⬜ 待实现 |
| PUT | `/project/plan/{id}/inactive` | 归档 | ⬜ 待实现 |
| PUT | `/project/plan/{id}/inactive/approval` | 归档-审批 | ⬜ 待实现 |
| PUT | `/project/plan/{id}/lock` | 锁定 | ⬜ 待实现 |
| PUT | `/project/plan/{id}/unlock` | 取消锁定 | ⬜ 待实现 |
| PUT | `/project/plan/{id}/updateDeliverLineRank` | 更新卡片交付线 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/plan/active` | 查询活跃的项目计划 | ⬜ 待实现 |
| GET | `/project/plan/activeWithProgress` | 查询活跃的项目计划 | ⬜ 待实现 |
| GET | `/project/plan/countBpmProcessingByAncestorPlan` | 查询指定计划相关的待审批的卡片数（包含出与入的两种审批） | ⬜ 待实现 |
| GET | `/project/plan/inactive` | 查询已归档项目计划 | ⬜ 待实现 |
| GET | `/project/plan/milestone` | 查询项目计划里程碑，按结束时间倒序 | ⬜ 待实现 |
| GET | `/project/plan/searchAll` | 查询项目计划 | ⬜ 待实现 |
| GET | `/project/plan/{id}` | 查询计划 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/plan/{id}` | 删除 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/plan/plansProgress` | 查询指定的项目计划 | ⬜ 待实现 |
| POST | `/project/plan/selectPlans` | 查询指定的项目计划 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| id | integer | id |
| projectId | integer | projectId |
| pageNumber | integer | pageNumber |
| pageSize | integer | pageSize |
| targetPlanId | integer | 计划内卡片迁移到哪个计划下 |
| q | string | q |
| planIds | array | planIds |
| userChoosesRequest |  | userChoosesRequest |
| containsDescendant | boolean | containsDescendant |
