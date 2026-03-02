# 版本管理 API (product-version-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 17 个
- **已实现**: 0 个
- **待扩展**: 17 个
- **分类**: 其他

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| PUT | `/project/version` | 创建产品版本 | ⬜ 待实现 |
| PUT | `/project/version/{id}` | 编辑产品版本信息(全量更新版本关联) | ⬜ 待实现 |
| PUT | `/project/version/{id}/active` | 还原产品版本 | ⬜ 待实现 |
| PUT | `/project/version/{id}/description` | 编辑版本的描述信息 | ⬜ 待实现 |
| PUT | `/project/version/{id}/inactive` | 归档产品版本 | ⬜ 待实现 |
| PUT | `/project/version/{id}/release` | 发布产品版本 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/version/hasTitle` | 检查标题是否被占用 | ⬜ 待实现 |
| GET | `/project/version/listVersion` | 查询项目下产品版本列表 | ⬜ 待实现 |
| GET | `/project/version/listVersionDifference` | 比较产品版本差异 | ⬜ 待实现 |
| GET | `/project/version/project/relateRepoTags` | 根据代码库ID查询tag | ⬜ 待实现 |
| GET | `/project/version/project/relateRepos` | 查询当前项目关联的代码库 | ⬜ 待实现 |
| GET | `/project/version/reposTagCanUseRange` | 获取指定产品版本前后版本绑定的最大及最小tagId | ⬜ 待实现 |
| GET | `/project/version/{id}` | 获取产品版本详情及tag关联关系 | ⬜ 待实现 |
| GET | `/project/version/{id}/cards` | 获取产品版本中关联所有tag的卡片信息 | ⬜ 待实现 |
| GET | `/project/version/{id}/codeVersionsDetail` | 获取单个关联代码tag的详细信息 | ⬜ 待实现 |
| GET | `/project/version/{id}/tagsSummary` | 获取产品版本关联代码库所有tag的概要信息(除卡片外的其他信息) | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/version/{id}` | 删除产品版本 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| id | integer | 产品版本ID |
| projectId | integer | projectId |
| request |  | request |
| cardFields | array | cardFields |
| versionId | integer | 产品版本ID |
| repoId | integer | repoId |
