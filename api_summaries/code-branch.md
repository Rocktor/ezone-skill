# 代码分支关联 API (card-code-branch-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 9 个
- **已实现**: 0 个
- **待扩展**: 9 个
- **分类**: 代码集成

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| PUT | `/project/card/{projectKey}-{seqNum}/bindCodeBranch` | 卡片绑定分支 | ⬜ 待实现 |
| PUT | `/project/card/{projectKey}-{seqNum}/bindExterCo...` | 卡片绑定外部系统分支 | ⬜ 待实现 |
| PUT | `/project/card/{projectKey}-{seqNum}/creadAndBin...` | 新建分支并绑定卡片 | ⬜ 待实现 |
| PUT | `/project/card/{projectKey}-{seqNum}/creadAndBin...` | 新建除ezcode的外部分支并绑定卡片 | ⬜ 待实现 |
| PUT | `/project/card/{projectKey}-{seqNum}/unbindCodeB...` | 卡片解绑分支 | ⬜ 待实现 |
| PUT | `/project/card/{projectKey}-{seqNum}/unbindExter...` | 卡片解绑外部系统分支 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/card/{projectKey}-{seqNum}/commitBuilds` | 卡片提交点对应的流水线记录 | ⬜ 待实现 |
| GET | `/project/card/{projectKey}-{seqNum}/relateCodeMsg` | 查询卡片关联的代码信息 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/card/listBranches` | 获取卡片能绑定的分支列表 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| projectKey | string | projectKey |
| seqNum | integer | 卡片编号 |
| request |  | 创建分支请求 |
