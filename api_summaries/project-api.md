# 项目外部接口 API (project-api-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 34 个
- **已实现**: 0 个
- **待扩展**: 34 个
- **分类**: 项目管理

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| PUT | `/project/api/project/artifactRepoBindProject` | 制品库关联项目 | ⬜ 待实现 |
| PUT | `/project/api/project/docSpaceBindProject` | Doc空间关联项目 | ⬜ 待实现 |
| PUT | `/project/api/project/hostGroupBindProject` | 主机组关联项目 | ⬜ 待实现 |
| PUT | `/project/api/project/k8sGroupBindProject` | k8s集群关联项目 | ⬜ 待实现 |
| PUT | `/project/api/project/repoBindProject` | 代码库关联项目 | ⬜ 待实现 |
| PUT | `/project/api/project/wikiSpaceBindProject` | Wiki空间关联项目 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/api/project` | 查询项目 | ⬜ 待实现 |
| GET | `/project/api/project/artifactRepoBindProject` | 查询制品库关联的项目 | ⬜ 待实现 |
| GET | `/project/api/project/count` | 查询项目总数 | ⬜ 待实现 |
| GET | `/project/api/project/docSpaceBindProject` | 查询Doc空间关联的项目 | ⬜ 待实现 |
| GET | `/project/api/project/hostGroupBindProject` | 查询主机组关联的项目 | ⬜ 待实现 |
| GET | `/project/api/project/k8sGroupBindProject` | 查询k8s集群关联的项目 | ⬜ 待实现 |
| GET | `/project/api/project/repoBindProject` | 查询代码库关联的项目 | ⬜ 待实现 |
| GET | `/project/api/project/repoCheckedBindProject` | 查询代码库关联的项目 | ⬜ 待实现 |
| GET | `/project/api/project/searchAdmin` | 查询公司下的项目列表 | ⬜ 待实现 |
| GET | `/project/api/project/searchMember` | 查询公司下的项目列表 | ⬜ 待实现 |
| GET | `/project/api/project/wikiSpaceBindProject` | 查询Wiki空间关联的项目 | ⬜ 待实现 |
| GET | `/project/api/project/{id}` | 查询项目 | ⬜ 待实现 |
| GET | `/project/api/project/{id}/checkRead` | 检查权限 | ⬜ 待实现 |
| GET | `/project/api/project/{id}/checkWrite` | 检查权限 | ⬜ 待实现 |
| GET | `/project/api/project/{id}/roleMembers` | 获取项目角色成员 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/api/project/artifactRepoUnbindProject` | 解除制品库关联项目 | ⬜ 待实现 |
| DELETE | `/project/api/project/docSpaceUnbindProject` | 解除Doc空间关联项目 | ⬜ 待实现 |
| DELETE | `/project/api/project/hostGroupUnbindProject` | 解除主机组关联项目 | ⬜ 待实现 |
| DELETE | `/project/api/project/k8sGroupUnbindProject` | 解除代码库关联项目 | ⬜ 待实现 |
| DELETE | `/project/api/project/repoUnbindProject` | 解除代码库关联项目 | ⬜ 待实现 |
| DELETE | `/project/api/project/wikiSpaceUnbindProject` | 解除Wiki空间关联项目 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/api/project/checkRead` | 检查权限 | ⬜ 待实现 |
| POST | `/project/api/project/checkWrite` | 检查权限 | ⬜ 待实现 |
| POST | `/project/api/project/companyBindRepoIds` | 查询企业下所有项目关联的代码库 | ⬜ 待实现 |
| POST | `/project/api/project/companyBindWikiSpaces` | 查询企业下所有项目关联的wiki空间 | ⬜ 待实现 |
| POST | `/project/api/project/filterRead` | 去掉无读权限的项目 | ⬜ 待实现 |
| POST | `/project/api/project/projectsBindRepoIds` | 查询项目关联的代码库 | ⬜ 待实现 |
| POST | `/project/api/project/projectsBindWikiSpaces` | 查询project关联的wiki空间 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| X-INTERNAL-AUTH-MD5 | string | md5(拼接约定token+timestamp) |
| X-INTERNAL-AUTH-TIMESTAMP | integer | milliseconds |
| user | string | 用户名 |
| projectId | integer | projectId |
| companyId | integer | companyId |
| repoId | integer | repoId |
| spaceId | integer | spaceId |
| projectIds | array | 项目ID |
| id | integer | 项目ID |
| groupId | integer | groupId |
| k8sGroupId | integer | k8s环境Id |
| repo | string | 代码库路径 |
| pageNumber | integer | pageNumber |
| pageSize | integer | pageSize |
| q | string | 查询项目名过滤 |
