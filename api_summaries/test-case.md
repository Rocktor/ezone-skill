# 测试用例 API (card-test-case-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 5 个
- **已实现**: 0 个
- **待扩展**: 5 个
- **分类**: 测试管理

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| PUT | `/project/card/{id}/updateBindCases` | 更新卡片关联的测试用例 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/card/{id}/listBindCaseIds` | 查询卡片关联的测试用例 | ⬜ 待实现 |
| GET | `/project/card/{id}/listBindCases` | 查询卡片关联的测试用例 | ⬜ 待实现 |
| GET | `/project/card/{id}/listBugBindCaseRuns` | 查询发现bug的测试用例执行记录 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/card/{id}/unBindCases` | 解绑卡片关联的测试用例 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| id | integer | 卡片ID |
| spaceId | integer | spaceId |
| caseIds | array | caseIds |
