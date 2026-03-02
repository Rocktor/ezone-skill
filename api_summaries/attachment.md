# 附件管理 API (card-attachment-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 8 个
- **已实现**: 1 个
- **待扩展**: 7 个
- **分类**: 卡片管理

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| PUT | `/project/card/{cardId}/attachment/{attachmentId...` | 更新附件描述 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/card/{cardId}/attachment` | 附件列表 | ⬜ 待实现 |
| GET | `/project/card/{cardId}/attachment/preview/{file...` | 预览附件 | ⬜ 待实现 |
| GET | `/project/card/{cardId}/attachment/{attachmentId}` | 下载附件 | ⬜ 待实现 |
| GET | `/project/card/{cardId}/attachment/{attachmentId...` | 预览附件 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/card/{cardId}/attachment/{attachmentId}` | 移除附件 | ⬜ 待实现 |

### 批量操作

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/card/{cardId}/attachment/batch` | 上传多个附件 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/card/{cardId}/attachment` | 上传单个附件 | ✅ 已实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| cardId | integer | 卡片ID |
| attachmentId | integer | 附件ID |
| description | string | 附件描述/备注 |
| fileName | string | 附件文件名 |

## 使用示例

```python
from ezone_api import EZoneAPI, get_token

api = EZoneAPI(token=get_token())

# 上传附件
result = api.upload_attachment(
    card_id="1157325358376181760",
    file_path="/path/to/file.docx",
    description="PRD需求文档"
)
```
