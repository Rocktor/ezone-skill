# 报表图表 API (chart-controller)

> 来源: ezone_api_doc.json | 生成时间: 2026-01-31

## 概览

- **接口总数**: 22 个
- **已实现**: 0 个
- **待扩展**: 22 个
- **分类**: 其他

## 接口列表

### 创建/更新

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/chart` | 新建 | ⬜ 待实现 |
| POST | `/project/chart/group` | 新建报表组 | ⬜ 待实现 |
| PUT | `/project/chart/group/{id}` | 更新 | ⬜ 待实现 |
| PUT | `/project/chart/{id}` | 更新 | ⬜ 待实现 |
| PUT | `/project/chart/{id}/move` | 移动调整顺序 | ⬜ 待实现 |

### 查询/搜索

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| GET | `/project/chart` | 获取报表列表 | ⬜ 待实现 |
| GET | `/project/chart/gantt/data` | 甘特图数据 | ⬜ 待实现 |
| GET | `/project/chart/group` | 获取报表分组列表 | ⬜ 待实现 |
| GET | `/project/chart/group/{groupId}/chart` | 获取报表列表 | ⬜ 待实现 |
| GET | `/project/chart/types` | 获取已支持的报表类型列表 | ⬜ 待实现 |
| GET | `/project/chart/{id}/detail` | 获取报表详细配置 | ⬜ 待实现 |

### 删除

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| DELETE | `/project/chart/group/{id}` | 删除 | ⬜ 待实现 |
| DELETE | `/project/chart/{id}` | 删除 | ⬜ 待实现 |

### 其他

| 方法 | 路径 | 说明 | 状态 |
|------|------|------|------|
| POST | `/project/chart/burn/data` | 计划燃烧进度数据 | ⬜ 待实现 |
| POST | `/project/chart/group/{id}/copy` | 复制报表组及组中报表 | ⬜ 待实现 |
| POST | `/project/chart/insight/queryChartCard` | 根据自定义报表中卡片数获取卡片列表（用于效能度量中报表） | ⬜ 待实现 |
| POST | `/project/chart/userBug` | 查询用户新增bug数据 | ⬜ 待实现 |
| POST | `/project/chart/userEndCard` | 查询用户完成卡片数据 | ⬜ 待实现 |
| POST | `/project/chart/userIncrWorkloadDayDetail` | 查询用户某日工时登录明细（登录状态SUCCESS的） | ⬜ 待实现 |
| POST | `/project/chart/userWorkloadDays` | 查询时间段内用户每日工时统计 | ⬜ 待实现 |
| POST | `/project/chart/userWorkloadSummary` | 查询用户时间段内工时总量 | ⬜ 待实现 |
| POST | `/project/chart/{id}/data` | 获取报表数据，不同报表类型返回不同结果 | ⬜ 待实现 |

## 常用参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| id | integer | 报表ID |
| request |  | 报表 |
| user | string | user |
| projectId | integer | 项目ID |
| range |  | range |
| groupId | integer | 分组ID |
| searchCardRequest |  | searchCardRequest |
