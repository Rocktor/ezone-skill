# 卡片外部接口 API (card-api-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 25 个
- **已实现**: 0 个
- **待扩展**: 25 个
- **分类**: 卡片管理

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| PUT | `/project/api/card/query/byKeys` | 获取卡片信息 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/api/card/check` | 检查卡片:权限&存在&在项目下 | ⬜ 待实现 |
| GET | `/project/api/card/filter` | 过滤返回合法&有权限的卡片列表 | ⬜ 待实现 |
| GET | `/project/api/card/getCardIdsByKeys` | 获取卡片ID | ⬜ 待实现 |
| GET | `/project/api/card/list` | 获取卡片信息 | ⬜ 待实现 |
| GET | `/project/api/card/list/byKeys` | 获取卡片信息 | ⬜ 待实现 |
| GET | `/project/api/card/searchByProject` | 查询项目下卡片-搜索标题与编号 | ⬜ 待实现 |
| GET | `/project/api/card/{projectKey}-{seqNum}/check` | 判断合法&有权限&关联代码库 | ⬜ 待实现 |

### 批量操作

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/api/card/plan/flow/results` | 计划锁定卡片审批单结果回调-批量 | ⬜ 待实现 |
| POST | `/project/api/card/status/flow/results` | 审批单结果回调-批量 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/api/card/check` | 检查卡片:权限&存在&在项目下 | ⬜ 待实现 |
| POST | `/project/api/card/checkTypeProjectAndExist` | 检查卡片:存在&在项目下&卡片内置类型 | ⬜ 待实现 |
| POST | `/project/api/card/checkTypeProjectAndExistAndBi...` | 测试记录下的case绑定卡片 | ⬜ 待实现 |
| POST | `/project/api/card/countBugEnd` | 通过bug分组，计算每组bug中已经完成的bug数。 | ⬜ 待实现 |
| POST | `/project/api/card/filter` | 过滤返回合法&有权限的卡片列表 | ⬜ 待实现 |
| POST | `/project/api/card/filterByRelRepo` | 过滤返回拼写合法&关联了对应代码库的卡片列表 | ⬜ 待实现 |
| POST | `/project/api/card/getCardIdsByKeys` | 获取卡片ID | ⬜ 待实现 |
| POST | `/project/api/card/list` | 获取卡片信息 | ⬜ 待实现 |
| POST | `/project/api/card/list/byKeys` | 获取卡片信息 | ⬜ 待实现 |
| POST | `/project/api/card/query/byKeys` | 获取卡片信息 | ⬜ 待实现 |
| POST | `/project/api/card/query/byProject` | 查询项目下卡片-组合字段搜索 | ⬜ 待实现 |
| POST | `/project/api/card/unBindCardPlanCase` | 测试记录下的case解绑卡片 | ⬜ 待实现 |
| POST | `/project/api/card/{cardId}/plan/flow/result` | 审批单结果回调 | ⬜ 待实现 |
| POST | `/project/api/card/{cardId}/status/flow/result` | 审批单结果回调 | ⬜ 待实现 |
| POST | `/project/api/card/{cardId}/workload/flow/result` | 审批单结果回调 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| X-INTERNAL-AUTH-MD5 | string | md5(拼接约定token+timestamp) |
| X-INTERNAL-AUTH-TIMESTAMP | integer | milliseconds |
| request |  | request |
| companyId | integer | 公司ID |
| projectId | integer | 项目ID |
| cardKeys | array | 卡片keys |
| pageNumber | integer | pageNumber |
| pageSize | integer | pageSize |
| user | string | 用户名 |
| fields | array | 卡片字段 |
| approved | boolean | 审批流结果是否通过 |
| cardId | integer | 卡片ID |
| flowId | integer | 审批流ID |
| cardIds | array | 卡片ids |
| flowResults | array | flowResults |
