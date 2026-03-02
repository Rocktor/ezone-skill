# 卡片管理 API (card-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 73 个
- **已实现**: 6 个
- **待扩展**: 67 个
- **分类**: 卡片管理

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/card` | 新建卡片 | ✅ 已实现 |
| POST | `/project/card/createAndBind` | 新建卡片并绑定wiki、doc等 | ⬜ 待实现 |
| POST | `/project/card/draft` | 新建草稿 | ⬜ 待实现 |
| POST | `/project/card/quick` | 快速新建卡片 | ⬜ 待实现 |
| POST | `/project/card/{id}/planId/approval` | 发起修改卡片所属计划审批：错误码5042:未绑定审批流;错误码5013:审批中 | ⬜ 待实现 |
| PUT | `/project/card/changeType` | 改变卡片类型 | ⬜ 待实现 |
| PUT | `/project/card/rankByCardRank` | 更新卡片排序位置 | ⬜ 待实现 |
| PUT | `/project/card/rankByPlanDeliverLineRank` | 更新卡片排序位置 | ⬜ 待实现 |
| PUT | `/project/card/{id}` | 更新卡片 | ⬜ 待实现 |
| PUT | `/project/card/{id}/changeStoryMapLocation` | 更新卡片在故事地图中的位置 | ⬜ 待实现 |
| PUT | `/project/card/{id}/changeStoryMapLocation/approval` | 更新卡片在故事地图中的位置-发起审批 | ⬜ 待实现 |
| PUT | `/project/card/{id}/fields` | 更新卡片 | ⬜ 待实现 |
| PUT | `/project/card/{id}/fields/{field}` | 更新卡片属性: 不支持直接修改卡片类型/编号/父卡片/是否删除等特殊字段 | ⬜ 待实现 |
| PUT | `/project/card/{id}/incrWorkload/{workloadId}` | 直接修改登记工时;错误码5012:未绑定审批流; | ⬜ 待实现 |
| PUT | `/project/card/{id}/incrWorkload/{workloadId}/ap...` | 发审批类修改被拒绝的登记工时 | ⬜ 待实现 |
| PUT | `/project/card/{id}/parentId` | 修改卡片的父卡片 | ⬜ 待实现 |
| PUT | `/project/card/{id}/recovery` | 还原 | ⬜ 待实现 |
| PUT | `/project/card/{id}/remind` | 催办 | ⬜ 待实现 |
| PUT | `/project/card/{id}/status` | 更新卡片流程状态;错误码5010:需要同时设置其它必填字段;错误码5011:需要发起审批流;错误码5013:审批中 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/card/countByAncestorPlan` | 查询计划下卡片数量；用于归档或删除计划前检查相关卡片 | ⬜ 待实现 |
| GET | `/project/card/import/excel` | 下载导入卡片模版 | ⬜ 待实现 |
| GET | `/project/card/import/fail/excel` | 下载导入失败卡片的详细原因excel | ⬜ 待实现 |
| GET | `/project/card/incrWorkload/my` | 获取当前用户卡片登记工时记录 | ⬜ 待实现 |
| GET | `/project/card/searchQueryExamples` | Query子类示例 | ⬜ 待实现 |
| GET | `/project/card/searchRelateCards` | 查询关联卡片 | ⬜ 待实现 |
| GET | `/project/card/searchUpDownCards` | 查询卡片及其上下游层级卡片 | ⬜ 待实现 |
| GET | `/project/card/{id}` | 获取卡片详情 | ✅ 已实现 |
| GET | `/project/card/{id}/approval` | 获取卡片审批记录 | ⬜ 待实现 |
| GET | `/project/card/{id}/approval/byFlowIds` | 根据ID获取卡片审批记录 | ⬜ 待实现 |
| GET | `/project/card/{id}/approval/{flowId}` | 获取卡片审批记录 | ⬜ 待实现 |
| GET | `/project/card/{id}/incrWorkload` | 获取卡片登记工时审批记录 | ⬜ 待实现 |
| GET | `/project/card/{id}/incrWorkload/approvalTemplate` | 获取卡片登记工时审批模版 | ⬜ 待实现 |
| GET | `/project/card/{id}/incrWorkload/revert/approval...` | 获取卡片登记工时审批模版 | ⬜ 待实现 |
| GET | `/project/card/{id}/incrWorkload/{workloadId}` | 获取卡片登记工时记录 | ⬜ 待实现 |
| GET | `/project/card/{id}/status/approvalTemplate` | 获取卡片流程状态审批模版 | ⬜ 待实现 |
| GET | `/project/card/{projectKey}-{seqNum}` | 获取卡片详情 | ✅ 已实现 |
| GET | `/project/card/{projectKey}-{seqNum}/accessToken` | 获取卡片accessToken | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/card/{id}` | 逻辑删除 | ✅ 已实现 |
| DELETE | `/project/card/{id}/incrWorkload/{workloadId}` | 直接取消登记工时;错误码5011:需要发起审批流; | ⬜ 待实现 |
| DELETE | `/project/card/{id}/incrWorkload/{workloadId}/ap...` | 取消登记工时流程审批 | ⬜ 待实现 |
| DELETE | `/project/card/{id}/incrWorkload/{workloadId}/re...` | 取消取消登记工时流程审批 | ⬜ 待实现 |
| DELETE | `/project/card/{id}/planId/approval` | 解绑卡片流程当前的计划变更审批 | ⬜ 待实现 |
| DELETE | `/project/card/{id}/status/approval` | 解绑卡片流程当前的状态审批 | ⬜ 待实现 |

### 批量操作

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/card/batch/delete` | 批量逻辑删除 | ✅ 已实现 |
| POST | `/project/card/batch/delete/approval` | 批量逻辑删除(提交审批） | ⬜ 待实现 |
| POST | `/project/card/batch/recovery` | 批量还原 | ⬜ 待实现 |
| POST | `/project/card/batchCreateChildrenCard` | 批量新建子卡片 | ⬜ 待实现 |
| POST | `/project/card/batchCreateChildrenCard/approval` | 批量新建子卡片-并提交审批（目前只支持计划变更审批） | ⬜ 待实现 |
| POST | `/project/card/planId/approvals` | 批量发起修改卡片所属计划审批：错误码5042:未绑定审批流;错误码5013:审批中 | ⬜ 待实现 |
| PUT | `/project/card/batchUpdateFields` | 更新卡片 | ⬜ 待实现 |
| PUT | `/project/card/cardType/status/batch` | 更新卡片流程状态;若返回5010错误码说明目标状态合法但需要同时设置其它必选字段 | ⬜ 待实现 |
| PUT | `/project/card/copy` | 批量复制卡片到另一个计划 | ⬜ 待实现 |
| PUT | `/project/card/copy/approval` | 批量复制卡片到另一个计划(提交审批） | ⬜ 待实现 |
| PUT | `/project/card/fields/batch/parent_id` | 批量修改卡片字段 | ⬜ 待实现 |
| PUT | `/project/card/migrate` | 批量迁移卡片到同项目下的另一个计划 | ⬜ 待实现 |
| PUT | `/project/card/migrate/approval` | 批量迁移卡片到同项目下的另一个计划 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/card/export/byPortfolio/excel` | 导出卡片 | ⬜ 待实现 |
| POST | `/project/card/export/excel` | 导出卡片 | ⬜ 待实现 |
| POST | `/project/card/import/excel` | 导入卡片 | ⬜ 待实现 |
| POST | `/project/card/listCardType` | 获取查询范围内用到的卡片类型列表 | ⬜ 待实现 |
| POST | `/project/card/searchBpmProcessingByAncestorPlan` | 查询审批中的卡片且目标计划为指定计划的卡片 | ⬜ 待实现 |
| POST | `/project/card/searchByActiveAndNoPlan` | 查询项目计划下卡片 | ⬜ 待实现 |
| POST | `/project/card/searchByIds` | 查询卡片 | ⬜ 待实现 |
| POST | `/project/card/searchByMemberProject` | 查询当前公司下当前用户有权限的项目中的卡片（企业管理员查询整个企业） | ⬜ 待实现 |
| POST | `/project/card/searchByPlan` | 查询项目计划下卡片 | ⬜ 待实现 |
| POST | `/project/card/searchByPortfolio` | 查询项目集下卡片 | ⬜ 待实现 |
| POST | `/project/card/searchByProject` | 查询项目下卡片 | ✅ 已实现 |
| POST | `/project/card/searchCardsByAccessToken` | 查询卡片 | ⬜ 待实现 |
| POST | `/project/card/{id}/delete/approval` | 逻辑删除-提交审批 | ⬜ 待实现 |
| POST | `/project/card/{id}/incrWorkload` | 登记工时;错误码5012:需要发起审批流; | ⬜ 待实现 |
| POST | `/project/card/{id}/incrWorkload/approval` | 发起登记工时审批流 | ⬜ 待实现 |
| POST | `/project/card/{id}/incrWorkload/{workloadId}/re...` | 发起审批来取消已登记工时 | ⬜ 待实现 |
| POST | `/project/card/{id}/status/approval` | 发起卡片流程状态审批;错误码5012:未绑定审批流;错误码5013:审批中 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| id | integer | 卡片ID |
| projectId | integer | 项目ID |
| request |  | 卡片ID |
| ids | array | 卡片ID |
| workloadId | integer | workloadId |
| location | string | 复制到新计划后的排序策略 |
| targetPlanId | integer | 目标计划ID |
| sendEmail | boolean | 创建卡片时是否发送邮件 |
| pageNumber | integer | pageNumber |
| pageSize | integer | pageSize |
| searchCardRequest |  | searchCardRequest |
| targetProjectId | integer | 目标项目ID |
| fields | array | 卡片字段 |
| planId | integer | 计划ID |
| bpmUserChoosesRequest |  | bpmUserChoosesRequest |

## 使用示例

```python
from ezone_api import EZoneAPI, get_token

api = EZoneAPI(token=get_token())

# 搜索卡片
cards = api.search_cards(project_id="844795161124806656")

# 创建卡片
result = api.create_card(
    project_id="844795161124806656",
    card_type="task",
    title="任务标题",
    content="任务描述"
)
```
