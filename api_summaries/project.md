# 项目管理 API (project-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 29 个
- **已实现**: 1 个
- **待扩展**: 28 个
- **分类**: 项目管理

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/project` | 新建项目 | ⬜ 待实现 |
| PUT | `/project/project/{id}` | 更新项目基本信息 | ⬜ 待实现 |
| PUT | `/project/project/{id}/active` | 取消归档 | ⬜ 待实现 |
| PUT | `/project/project/{id}/cardPlanBpmFlow` | 设置锁定计划后，计划中卡片变更所属计划时是否进行审批 | ⬜ 待实现 |
| PUT | `/project/project/{id}/inactive` | 归档 | ⬜ 待实现 |
| PUT | `/project/project/{id}/isStrict` | 设置是否严谨模式--（快速新建卡片) | ⬜ 待实现 |
| PUT | `/project/project/{id}/keepDays` | 设置回收站卡片保存时长（日） | ⬜ 待实现 |
| PUT | `/project/project/{id}/planKeepDays` | 设置归档计划保存时长（日） | ⬜ 待实现 |
| PUT | `/project/project/{id}/portfolio` | 更新项目所属项目集 | ⬜ 待实现 |
| PUT | `/project/project/{id}/summaryConfig` | 项目概览设置 | ⬜ 待实现 |
| PUT | `/project/project/{id}/top` | 新增项目置顶 | ⬜ 待实现 |
| PUT | `/project/project/{key}/menus` | 设置项目菜单 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/project` | 查询当前公司下的项目列表-todo删除，因为dev环境单独加上 | ⬜ 待实现 |
| GET | `/project/project/check/key` | check | ⬜ 待实现 |
| GET | `/project/project/check/name` | check | ⬜ 待实现 |
| GET | `/project/project/key/{key}` | 通过项目KEY查询项目 | ⬜ 待实现 |
| GET | `/project/project/{id}` | 查询项目 | ⬜ 待实现 |
| GET | `/project/project/{id}/cardPlanBpmFlow` | 获取卡片计划审批设置 | ⬜ 待实现 |
| GET | `/project/project/{id}/cardPlanBpmFlow/approvalT...` | 获取卡片计划审批模板信息 | ⬜ 待实现 |
| GET | `/project/project/{id}/listBugSpaces` | 查询项目关联的测试空间 | ⬜ 待实现 |
| GET | `/project/project/{id}/listRequirementSpaces` | 查询项目关联的测试空间 | ⬜ 待实现 |
| GET | `/project/project/{id}/listSpaces` | 查询项目关联的测试空间 | ⬜ 待实现 |
| GET | `/project/project/{id}/permissions` | 查询项目操作权限 | ⬜ 待实现 |
| GET | `/project/project/{key}/menus` | 获取项目菜单配置 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/project/{id}` | 删除项目 | ⬜ 待实现 |
| DELETE | `/project/project/{id}/favourite` | 取消收藏 | ⬜ 待实现 |
| DELETE | `/project/project/{id}/top` | 取消项目置顶 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/project/search` | 查询当前公司下的项目列表 | ✅ 已实现 |
| POST | `/project/project/{id}/favourite` | 收藏 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| id | integer | 项目ID |
| key | string | key |
| pageNumber | integer | pageNumber |
| pageSize | integer | pageSize |
| scope | string | scope |
| projectId | integer | projectId |
| withRole | boolean | 是否返回当前用户角色 |

## 使用示例

```python
from ezone_api import EZoneAPI, get_token

api = EZoneAPI(token=get_token())

# 获取项目列表
projects = api.list_projects()

# 根据 Key 获取项目
project = api.get_project_by_key("MojiWeather")
```
