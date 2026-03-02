# 字段/状态配置 API (project-schema-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 35 个
- **已实现**: 1 个
- **待扩展**: 34 个
- **分类**: 项目管理

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/project/{id}/schema/role` | 新建项目角色 | ⬜ 待实现 |
| POST | `/project/project/{id}/schema/statuses` | 新建项目schema状态 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema` | 设置项目卡片Schema | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/fieldFlows` | 设置项目schema的字段关联 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/fields` | 设置项目schema的字段列表 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/role/update` | 更新项目的角色设置 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/statuses` | 设置项目schema的状态列表 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/statuses/sort` | 更新项目schema的状态顺序 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/statuses/update` | 更新项目schema的状态设置 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/types` | 设置项目schema的卡片类型列表 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/types/{cardType}/a...` | 设置项目schema下具体卡片类型的状态自动流转 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/types/{cardType}/f...` | 设置项目schema下具体卡片类型的字段列表 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/types/{cardType}/s...` | 设置项目schema下具体卡片类型的状态限制值是否自动复制到后面的所有状态 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/types/{cardType}/s...` | 设置项目schema下具体卡片类型的状态列表 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/types/{cardType}/s...` | 关闭指定卡片类型的指定状态; 5001错误：缺合法目标迁移状态 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/types/{cardType}/s...` | 启用指定卡片类型的指定状态 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/workflowRule/{ruleId}` | 更新项目的工作流规则 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/workflowRule/{rule...` | 更新项目的工作流规则 | ⬜ 待实现 |
| PUT | `/project/project/{id}/schema/workloadSetting` | 更新项目的工时设置 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/project/{id}/schema` | 获取项目卡片Schema | ✅ 已实现 |
| GET | `/project/project/{id}/schema/checkSchemaForCopy` | 跨项目复制卡片校验Schema | ⬜ 待实现 |
| GET | `/project/project/{id}/schema/field/{key}/options` | 项目自定义的接口选项型字段的选项列表 | ⬜ 待实现 |
| GET | `/project/project/{id}/schema/role` | 查看项目角色 | ⬜ 待实现 |
| GET | `/project/project/{id}/schema/types/{cardType}/s...` | 获取项目schema下具体卡片类型的状态审批绑定的bpm审批流 | ⬜ 待实现 |
| GET | `/project/project/{id}/schema/workflowRule` | 获取项目的工作流规则 | ⬜ 待实现 |
| GET | `/project/project/{id}/schema/workflowRule/{rule...` | 项目的工作流规则中引用的外部项目 | ⬜ 待实现 |
| GET | `/project/project/{id}/schema/workloadSetting` | 获取项目的工时设置 | ⬜ 待实现 |
| GET | `/project/project/{id}/schema/workloadSetting/bp...` | 获取项目的工时设置绑定的bpm审批流 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/project/{id}/schema/field/{key}` | 设置项目模版的字段列表 | ⬜ 待实现 |
| DELETE | `/project/project/{id}/schema/role/{roleKey}` | 移除项目角色 | ⬜ 待实现 |
| DELETE | `/project/project/{id}/schema/statuses/{cardStatus}` | 移除项目schema状态; 5001错误：缺合法目标迁移状态 | ⬜ 待实现 |
| DELETE | `/project/project/{id}/schema/workflowRule/{ruleId}` | 删除项目的工作流规则 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/project/{id}/schema/checkSchemaForChan...` | 同项目转换卡片类型校验Schema | ⬜ 待实现 |
| POST | `/project/project/{id}/schema/role/customerRoleRank` | 移动项目自定义角色位置 | ⬜ 待实现 |
| POST | `/project/project/{id}/schema/workflowRule` | 添加项目的工作流规则 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| id | integer | 项目ID |
| cardType | string | 卡片类型 |
| cardStatus | string | cardStatus |
| ruleId | integer | 工作流规则ID |
| request |  | request |
| key | string | 字段标识 |
| fields | array | fields |
| role |  | role |

## 使用示例

```python
from ezone_api import EZoneAPI, get_token

api = EZoneAPI(token=get_token())

# 获取项目 Schema
schema = api.get_project_schema(project_id="844795161124806656")
```
