# 迭代外部接口 API (plan-api-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 7 个
- **已实现**: 0 个
- **待扩展**: 7 个
- **分类**: 迭代计划

## 接口列表

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/api/plan/active` | 查询活跃的项目计划 | ⬜ 待实现 |
| GET | `/project/api/plan/{id}` | 查询计划 | ⬜ 待实现 |
| GET | `/project/api/plan/{id}/checkExist` | 检查权限 | ⬜ 待实现 |
| GET | `/project/api/plan/{id}/checkRead` | 检查权限 | ⬜ 待实现 |
| GET | `/project/api/plan/{id}/checkWrite` | 检查权限 | ⬜ 待实现 |

### 批量操作

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/api/plan/select` | 查询计划-批量 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/api/plan/{id}/checkExistAndInProjects` | 检查权限 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| X-INTERNAL-AUTH-MD5 | string | md5(拼接约定token+timestamp) |
| X-INTERNAL-AUTH-TIMESTAMP | integer | milliseconds |
| id | integer | 计划ID |
| projectId | integer | projectId |
| user | string | 用户名 |
