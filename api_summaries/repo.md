# 代码仓库 API (project-repo-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 5 个
- **已实现**: 0 个
- **待扩展**: 5 个
- **分类**: 代码集成

## 接口列表

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/project/{projectId}/repo` | 获取关联代码库 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/project/{projectId}/repo/deleteExterRepo` | 移除外部关联代码库 | ⬜ 待实现 |
| DELETE | `/project/project/{projectId}/repo/{id}` | 移除关联代码库 | ⬜ 待实现 |

### 批量操作

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/project/{projectId}/repo/batchBindExte...` | 添加关联的外部系统代码库 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/project/{projectId}/repo` | 添加关联代码库 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| projectId | integer | 项目ID |
