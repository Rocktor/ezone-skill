# 成员管理 API (project-member-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 5 个
- **已实现**: 0 个
- **待扩展**: 5 个
- **分类**: 项目管理

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| PUT | `/project/project/{id}/member` | 设置项目成员 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/project/{id}/member` | 查询项目成员 | ⬜ 待实现 |
| GET | `/project/project/{id}/member/memberUsers` | 查询项目成员-用户组会转换成用户 | ⬜ 待实现 |
| GET | `/project/project/{id}/member/role` | 查询当前用户在项目中最大角色 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/project/{id}/member/rolesUsers` | 查询指定角色的用户 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| id | integer | 项目ID |
