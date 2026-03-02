# 故事地图 API (story-map-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 11 个
- **已实现**: 0 个
- **待扩展**: 11 个
- **分类**: 其他

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/story-map` | 新建故事地图 | ⬜ 待实现 |
| POST | `/project/story-map/{storyMapId}/node` | 新建故事地图分类节点 | ⬜ 待实现 |
| PUT | `/project/story-map/node/{storyMapNodeId}` | 更新故事地图分类 | ⬜ 待实现 |
| PUT | `/project/story-map/node/{storyMapNodeId}/move` | 移动故事地图分类 | ⬜ 待实现 |
| PUT | `/project/story-map/{storyMapId}` | 更新故事地图 | ⬜ 待实现 |
| PUT | `/project/story-map/{storyMapId}/query` | 更新故事地图未规划卡片池的查询条件 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/story-map` | 故事地图 | ⬜ 待实现 |
| GET | `/project/story-map/{storyMapId}/node` | 故事地图分类 | ⬜ 待实现 |
| GET | `/project/story-map/{storyMapId}/query` | 查询故事地图未规划卡片池的查询条件 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/story-map/node/{storyMapNodeId}` | 删除故事地图分类 | ⬜ 待实现 |
| DELETE | `/project/story-map/{storyMapId}` | 删除故事地图 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| storyMapId | integer | 故事地图ID |
| name | string | 故事地图名称 |
| storyMapNodeId | integer | 故事地图分类ID |
| projectId | integer | 项目ID |
| afterId | integer | 位于哪个兄弟分类ID之后，开头则为0 |
