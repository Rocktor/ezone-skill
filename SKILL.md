---
name: ezone-skill
version: 2.0.0
description: 在简单云(EZone)项目管理系统中管理卡片。支持创建、状态扭转、查询等操作。
---

# EZone 卡片管理 Skill

> 版本：v2.0.0

## 触发条件

当用户提到以下内容时自动使用此技能：
- **扭转简单云状态 / 改简单云状态 / 扭转ezone状态 / 改ezone状态 / 卡片状态改为 / 转为待开发 / 转为开发中**
- 在简单云建卡 / 创建 EZone 卡片 / 建卡片 / 创建任务/Story/Bug / 批量建卡
- 查询卡片状态历史 / 卡片流转历史 / 查询审核记录 / 审批流程
- 删除卡片 / 批量删除卡片
- **搜索卡片 / 查找PRD / 统计卡片 / 跨项目搜索 / 按创建者搜索 / 按时间范围搜索**

## 功能特性

### 1. 支持的卡片类型

| 类型 | 代码 | 说明 |
|------|------|------|
| Task | `task` | 任务卡片 |
| Story | `story` | 用户故事 |
| Bug | `bug` | 缺陷 |
| Feature | `feature` | 功能特性 |
| Epic | `epic` | 史诗 |
| 前端Task | `custom_3` | 前端任务 |
| 后端Task | `custom_4` | 后端任务 |
| 线上Bug | `custom_1` | 线上缺陷 |
| 线下Bug | `custom_2` | 线下缺陷 |
| 子任务 | `transaction` | 子任务 |

### 2. 支持的状态

| 状态 | 代码 | 说明 |
|------|------|------|
| 待处理 | `open` | 新建状态 |
| 进行中 | `processing` | 正在处理 |
| 已完成 | `closed` | 已关闭 |

### 3. 完整状态列表（国际化项目为例）

不同项目的状态列表不同，可通过 `get_project_schema(project_id)` 获取。

| 状态码 | 状态名 |
|--------|--------|
| `open` | 新建 |
| `custom_1` | MRD立项 |
| `custom_20` | MRD评审通过 |
| `custom_2` | 需求分析 |
| `custom_21` | 需求评审通过 |
| `custom_5` | 待开发 |
| `custom_6` | 技术分析 |
| `custom_7` | 技术评审通过 |
| `custom_8` | 开发中 |
| `custom_11` | 待测试 |
| `custom_13` | 测试中 |
| `custom_14` | 测试完成 |
| `custom_23` | 已完成 |

### 4. 常用项目

| 项目Key | 项目名称 | 项目ID |
|---------|---------|--------|
| MojiWeather | 墨迹天气主版 | 844795161124806656 |
| MojiWeatherLite | 墨迹天气极速版 | 844794697939509248 |
| MojiHM | 鸿蒙原生APP | 909688715303010304 |
| IPD | IPD | 1136898811098112000 |
| VIP | 墨迹会员业务 | 860012503123472384 |
| TobProject | TOB项目管理 | 991954924693643264 |

## 首次使用配置（Token 引导）

每个用户需要使用**自己的 Token**，不能共用他人 Token。

### 检查 Token 是否已配置

执行任何操作前，先检查用户是否有 Token：

```python
from ezone_api import get_token
try:
    token = get_token()
    # Token 已配置，继续操作
except ValueError:
    # Token 未配置，引导用户设置
    pass
```

Token 按以下优先级读取：
1. 环境变量 `EZONE_TOKEN`
2. 用户配置文件 `~/.ezone_token`
3. 项目配置文件 `.ezone_token`

### 引导用户配置 Token

如果 Token 未配置，告知用户以下步骤：

1. 打开 EZone：https://ezone.matrixback.com
2. 进入：**个人设置 > 访问令牌**
3. 创建新令牌，权限勾选：**项目管理 → 读写**（其他权限不需要）
4. 复制令牌，发给我即可

收到用户的 Token 后，保存到 `~/.ezone_token`：

```bash
echo 'TOKEN_VALUE' > ~/.ezone_token
chmod 600 ~/.ezone_token
```

然后继续后续操作。

## 状态扭转工作流程（核心功能）

当用户要求扭转简单云卡片状态时，按以下流程执行：

### 第一步：检查 Token

检查 `~/.ezone_token` 是否存在。如果不存在，按「首次使用配置」引导用户设置。

### 第二步：获取卡片信息

用户需提供卡片标识（如 `mojiMainInternationalization-807`），解析出 projectKey 和 seqNum：

```python
import sys
sys.path.insert(0, '{skill_dir}')
from ezone_api import EZoneAPI, get_token

api = EZoneAPI(token=get_token())
card_resp = api.get_card_by_key('mojiMainInternationalization', 807)
card = card_resp['data']['card']
card_id = card_resp['data']['id']
```

### 第三步：列出确认项（必须等用户确认后再执行）

将以下信息**连同默认值**展示给用户，等用户确认或修改后再执行：

| 项目 | 默认值 | 说明 |
|------|--------|------|
| **卡片** | `{projectKey}-{seqNum}: {title}` | 从 API 获取，展示给用户确认 |
| **当前状态** | 从卡片信息读取 | 展示当前状态 |
| **目标状态** | `custom_5`（待开发） | 用户可改为其他状态 |
| **开始时间** | 今天（当天日期） | 用户可修改 |
| **结束时间** | **无默认值，用户必填** | 必须由用户提供 |
| **审批人** | `tongkai.zhao`（Kevin） | 用户可修改 |
| **产品负责人** | 当前卡片的 owner_users | 用户可修改 |
| **技术负责人** | 待用户确认 | 用户可修改 |

展示格式示例：

```
请确认以下信息，有需要修改的直接说：

- 卡片：mojiMainInternationalization-807「国际化-新用户注册品牌宣传+隐私页面修改」
- 当前状态：新建
- 目标状态：待开发
- 开始时间：2026-03-13（今天）
- 结束时间：❓ 请提供
- 审批人：tongkai.zhao（Kevin）
- 产品负责人：yizhuo.liu
- 技术负责人：❓ 请提供

确认无误后我来执行。
```

**重要：必须等用户确认后再执行，不要自动执行。**

### 第四步：执行状态扭转

用户确认后，按以下顺序执行：

```python
from datetime import date

# 1. 先填充必填字段
api.update_card_fields(card_id, {
    "start_date": EZoneAPI.date_to_timestamp("2026-03-13"),
    "end_date": EZoneAPI.date_to_timestamp("2026-03-19"),
    "custom_1_keyword": ["yizhuo.liu"],      # 产品负责人
    "custom_2_keyword": ["tech.lead"],       # 技术负责人
})

# 2. 再扭转状态（自动处理审批流）
result = api.change_card_status(
    card_id=card_id,
    status="custom_5",                        # 待开发
    approver_usernames=["tongkai.zhao"]       # 审批人 Kevin
)
```

### 第五步：返回结果并提醒

```
操作完成：
- 字段更新：开始时间 2026-03-13，结束时间 2026-03-19 ✅
- 状态扭转：新建 → 待开发，审批已提交（审批人：tongkai.zhao）✅
- 卡片链接：https://ezone.matrixback.com/project/{projectKey}/cardDetail/{cardId}

我已经完成状态扭转，记得在简单云评论区上传评审截图哦~
```

**重要：每次状态扭转完成后，必须附带提醒用户上传评审截图。**

### 状态扭转注意事项

- 错误码 `5010`：缺少必填字段 → 先补充字段再扭转
- 错误码 `5011`：需要走审批流 → `change_card_status()` 会自动处理
- 错误码 `5013`：审批中 → 卡片已有进行中的审批，需等待或取消
- 不同项目的状态列表不同，可通过 `get_project_schema(project_id)` 获取

## 卡片创建工作流程

### 第一步：确认项目

询问用户要在哪个项目下创建卡片，或根据上下文自动识别。

### 第二步：收集卡片信息

确认以下信息：
1. **卡片类型**：Task/Story/Bug/Feature 等
2. **标题**：卡片标题
3. **描述**：卡片内容（支持 Markdown）
4. **负责人**：可选，用户名列表
5. **父卡片**：可选，用于创建子任务

### 第三步：创建卡片

```python
result = api.create_card(
    project_id="844795161124806656",
    card_type="task",
    title="任务标题",
    content="任务描述",
    status="open"
)
```

### 第四步：返回结果

返回创建成功的卡片信息和链接：
- 卡片ID、卡片序号
- 卡片链接：`https://ezone.matrixback.com/project/{projectKey}/cardDetail/{cardId}`

## 核心代码模块

### API 客户端

使用 `./ezone_api.py`

```python
from ezone_api import EZoneAPI

# 初始化
api = EZoneAPI(token="YOUR_TOKEN", company_name="moji")

# 获取项目列表
projects = api.list_projects()

# 根据 Key 查找项目
project = api.get_project_by_key("MojiWeather")

# 搜索卡片（默认按最后修改时间降序排列）
cards = api.search_cards(project_id="xxx", page=1, page_size=20)

# 按创建时间排序
cards = api.search_cards(project_id="xxx", sort_by="create_time", sort_order="desc")

# 按序号排序
cards = api.search_cards(project_id="xxx", sort_by="seq_num", sort_order="asc")

# ========== 高级搜索（Query Builder） ==========

# 带过滤条件搜索（queries 数组为隐式 AND）
cards = api.search_cards(
    project_id="xxx",
    queries=[
        EZoneAPI.query_eq("type", "story"),                    # 类型=story
        EZoneAPI.query_in("create_user", ["user1", "user2"]),  # 创建者
        EZoneAPI.query_between("create_time", start_ts, end_ts),  # 时间范围
    ]
)

# 跨项目搜索（搜索用户有权限的所有项目）
cards = api.search_cards_cross_project(
    queries=[EZoneAPI.query_eq("type", "story")],
    page_size=100
)

# 自动翻页获取全部卡片
all_cards = api.search_all_cards(
    project_id="xxx",          # cross_project=False 时必填
    queries=[EZoneAPI.query_eq("type", "story")],
    cross_project=False,       # True=跨项目, False=单项目
    page_size=100,             # 每页条数
    max_pages=50,              # 安全上限
    filter_deleted=True        # 自动过滤幽灵记录
)

# 一站式便捷方法：按创建者+时间范围搜索
cards = api.search_cards_by_creators_and_time(
    creators=["yi.chen", "yanshuang.liu", "yizhuo.liu"],
    date_from="2026-01-31",
    date_to="2026-02-28",
    card_type="story",
    cross_project=True,
    time_field="create_time"   # 可选 "start_date"、"end_date"
)

# 创建卡片
result = api.create_card(
    project_id="xxx",
    card_type="task",
    title="标题",
    content="内容",
    status="open",
    parent_id=None,  # 父卡片ID（可选）
    owner_users=["username"],  # 负责人（可选）
    estimate_workload=8  # 预估工时（可选）
)

# 快捷方法
api.create_story(project_id, title, content)
api.create_task(project_id, title, content, parent_id=None)
api.create_bug(project_id, title, content)
api.create_feature(project_id, title, content)

# 批量创建
api.batch_create_cards(project_id, cards_list)

# 上传附件到卡片
api.upload_attachment(
    card_id="1157325358376181760",
    file_path="/path/to/file.docx",
    description="PRD需求文档"
)

# ========== 卡片编辑 ==========

# 更新卡片字段（时间、负责人等）
api.update_card_fields(card_id="xxx", fields={
    "start_date": api.date_to_timestamp("2026-03-13"),
    "end_date": api.date_to_timestamp("2026-03-19"),
    "custom_1_keyword": ["yizhuo.liu"],   # 产品负责人
    "custom_2_keyword": ["kevin.wei"],    # 技术负责人
})

# 更新单个字段
api.update_card_field(card_id="xxx", field="start_date",
                      value=api.date_to_timestamp("2026-03-13"))

# 更新状态（直接方式，可能返回 5011 需要审批）
api.update_card_status(card_id="xxx", status="custom_5")

# 更新状态（智能方式，自动处理审批流，推荐）
api.change_card_status(
    card_id="xxx",
    status="custom_5",                       # 目标状态码
    approver_usernames=["chaoju.liu"]         # 审批人（当需要审批时）
)
# 注意：部分状态扭转需要先填充必填字段（如开始/结束时间），再扭转状态

# 日期工具方法
ts = EZoneAPI.date_to_timestamp("2026-03-13")        # -> "1773331200000"
ts = EZoneAPI.date_to_timestamp("2026-03-13 10:00:00") # 支持带时间
```

## 使用示例

### 在 Claude Code 中使用

直接告诉 Claude：
- "在 MojiWeather 项目创建一个 Task"
- "帮我在简单云建一个 Bug 卡片"
- "批量创建以下任务到 IPD 项目"

### 对话示例

```
用户: 在 MojiWeather 项目创建一个 Task，标题是"优化首页加载速度"

助手: 好的，我来在 MojiWeather 项目创建这个 Task...

创建成功！
- 卡片ID: 1154353601293869056
- 序号: 1617
- 链接: https://ezone.matrixback.com/project/MojiWeather/cardDetail/1154353601293869056
```

### 扭转卡片状态

```
用户: 帮我扭转简单云状态 mojiMainInternationalization-807

助手: 好的，我查到这张卡片的信息了。请确认以下内容：

- 卡片：mojiMainInternationalization-807「国际化-新用户注册品牌宣传+隐私页面修改」
- 当前状态：新建
- 目标状态：待开发
- 开始时间：2026-03-13（今天）
- 结束时间：❓ 请提供
- 审批人：tongkai.zhao（Kevin）
- 产品负责人：yizhuo.liu
- 技术负责人：❓ 请提供

确认无误后我来执行~

用户: 结束时间3月19号，技术负责人 chaoju.liu，其他没问题

助手: 收到，开始执行...

操作完成：
- 字段更新：开始 2026-03-13，结束 2026-03-19 ✅
- 状态扭转：新建 → 待开发，审批已提交（审批人：tongkai.zhao）✅
- 链接：https://ezone.matrixback.com/project/mojiMainInternationalization/cardDetail/xxx
```

### 从 PRD 批量创建卡片

```
用户: 根据这个 PRD 在 MojiWeather 项目批量建卡

助手: 我来分析 PRD 并创建卡片...

1. 创建 Feature: AI Agent 智能助手
2. 创建 Story: 用户查询天气
3. 创建 Task: 实现意图识别接口
4. 创建 Task: 实现知识库检索
...
```

## API 端点参考

| 功能 | 方法 | 端点 |
|------|------|------|
| 项目列表 | POST | `/v1/project/project/project/search?pageNumber=1&pageSize=50&scope=ROLE` |
| 搜索卡片(单项目) | POST | `/v1/project/project/card/searchByProject?projectId={id}&pageNumber=1&pageSize=100` |
| **搜索卡片(跨项目)** | POST | `/v1/project/project/card/searchByMemberProject?pageNumber=1&pageSize=100` |
| **搜索Query示例** | GET | `/v1/project/project/card/searchQueryExamples` |
| 卡片详情 | GET | `/v1/project/project/card/{cardId}?projectId={id}` |
| 按序号获取卡片 | GET | `/v1/project/project/card/{projectKey}-{seqNum}` |
| 创建卡片 | POST | `/v1/project/project/card?projectId={id}` |
| **卡片事件历史** | GET | `/v1/project/project/card/{cardId}/event` |
| **项目Schema** | GET | `/v1/project/project/project/{projectId}/schema` |
| **卡片审核记录** | GET | `/v1/project/project/card/{cardId}/approval` |
| **更新卡片状态** | PUT | `/v1/project/project/card/{cardId}/status?status={statusCode}` |
| **更新卡片字段** | PUT | `/v1/project/project/card/{cardId}/fields` |
| **更新单个字段** | PUT | `/v1/project/project/card/{cardId}/fields/{field}` |
| **发起状态审批** | POST | `/v1/project/project/card/{cardId}/status/approval?status={statusCode}` |
| **获取审批模版** | GET | `/v1/project/project/card/{cardId}/status/approvalTemplate?targetStatus={statusCode}` |
| **删除单卡片** | DELETE | `/v1/project/project/card/{cardId}?projectId={projectId}` |
| **批量删除卡片** | POST | `/v1/project/project/card/batch/delete?projectId={projectId}` |

## 高级搜索功能

### Query Builder（搜索过滤条件构造器）

所有 `query_*` 方法返回一个字典，放入 `queries` 列表中传给搜索方法。`queries` 列表中多个条件为**隐式 AND**（API 不支持显式 And/Or 嵌套）。

| 方法 | 说明 | 示例 |
|------|------|------|
| `query_eq(field, value)` | 精确匹配 | `query_eq("type", "story")` |
| `query_not_eq(field, value)` | 不等于 | `query_not_eq("status", "closed")` |
| `query_in(field, values)` | 多值匹配 | `query_in("create_user", ["a", "b"])` |
| `query_not_in(field, values)` | 多值排除 | `query_not_in("type", ["bug", "task"])` |
| `query_between(field, start, end)` | 范围 | `query_between("create_time", ts1, ts2)` |
| `query_gt/gte/lt/lte(field, value)` | 比较 | `query_gte("create_time", ts)` |
| `query_exist/not_exist(field)` | 存在性 | `query_exist("start_date")` |
| `query_contains(field, values)` | 包含文本 | `query_contains("title", "PRD 需求")` |
| `query_not_contains(field, values)` | 不包含 | `query_not_contains("title", "test")` |
| `query_keyword(values, fields)` | 关键词搜索 | `query_keyword("登录 注册", ["title"])` |

> **注意**：type 值全部是 **lowercase**（`eq`, `in`, `between` 等），不是 PascalCase。

### 搜索方法对比

| 方法 | 用途 | 分页 |
|------|------|------|
| `search_cards(project_id, queries=)` | 单项目搜索 | 手动翻页 |
| `search_cards_cross_project(queries=)` | 跨项目搜索 | 手动翻页 |
| `search_all_cards(queries=, cross_project=)` | 自动翻页（最多5000条） | 自动 |
| `search_cards_by_creators_and_time(...)` | 按创建者+时间一站式搜索 | 自动 |

### 搜索重要注意事项

1. **分页参数必须放在 query params 中**，不能放在请求体中（否则不生效，始终返回10条）
2. `searchByMemberProject` 无需 projectId，搜索用户有权限的所有项目
3. `search_all_cards` 自动过滤已删除的幽灵记录（`seq_num is None`）
4. 常用字段名：`type`, `status`, `create_user`, `create_time`, `owner_users`, `start_date`, `end_date`, `title`, `content`, `project_id`

### 搜索对话示例

```
用户: 统计2月份各产品经理创建的PRD数量

助手: 我来搜索2月份9位产品经理在所有项目中创建的Story...

搜索结果（2026-01-31 ~ 02-28）:
| 创建者 | PRD数量 |
|--------|---------|
| yizhuo.liu | 8 |
| yi.chen | 4 |
| fangchao.zhang | 2 |
| 合计 | 14 |
```

## 卡片删除功能

### 重要提醒：软删除机制

EZone 使用**软删除**机制，删除后需要注意：

1. **幽灵记录问题**：删除后 API 仍会返回这些记录，但数据字段（如 `seq_num`、`title`）会变为 `None` 或空
2. **过滤有效卡片**：查询卡片时必须过滤掉 `seq_num` 为 `None` 的记录，只处理有效卡片
3. **总数不准确**：API 返回的 `total` 可能包含已删除的记录数

### 查询有效卡片的正确方式

```python
# 查询卡片后，必须过滤掉已删除的"幽灵"记录
result = api.search_cards(project_id="xxx", page=1, page_size=50)
items = result.get('data', {}).get('list', [])

# 只处理有 seq_num 的有效卡片
valid_cards = []
for item in items:
    card = item.get('card', {})
    seq_num = card.get('seq_num')
    if seq_num is not None:  # 关键：过滤掉已删除的卡片
        valid_cards.append({
            'id': item.get('id'),
            'seq_num': seq_num,
            'title': card.get('title'),
            'type': card.get('type'),
            'status': card.get('status')
        })

print(f"有效卡片数: {len(valid_cards)}")
```

### 删除卡片的 API 使用

```python
from ezone_api import EZoneAPI

api = EZoneAPI(token="YOUR_TOKEN")

# 方法1：使用 DELETE 方法删除单个卡片（推荐）
# 直接使用 requests，因为 ezone_api.py 暂未封装 DELETE 方法
import requests

card_id = "1157325358376181760"
project_id = "1136898811098112000"

headers = {
    "access_token": "YOUR_TOKEN",
    "x-company-name": "moji",
    "Content-Type": "application/json"
}

url = f"https://ezone.matrixback.com/v1/project/project/card/{card_id}?projectId={project_id}"
resp = requests.delete(url, headers=headers)

if resp.json().get('code') == 0:
    print("删除成功")

# 方法2：批量删除（注意：此接口在某些情况下可能返回 data:0）
card_ids = [1157325358376181760, 1137277716262887424]
result = api.delete_cards(card_ids)  # 使用 ezone_api.py 的方法
```

### 删除注意事项

| 注意点 | 说明 |
|--------|------|
| 使用 DELETE 方法 | 单卡片删除推荐使用 `DELETE /v1/project/project/card/{cardId}?projectId={projectId}` |
| 批量删除限制 | `batch/delete` 接口在某些情况下可能不生效（返回 `data: 0`） |
| 必须带 projectId | 删除时必须在 URL 参数中携带 `projectId` |
| 软删除特性 | 删除后记录仍存在，只是数据被清空 |
| 网页界面同步 | 软删除后，网页界面应该不再显示该卡片 |

### 批量清理项目卡片示例

```python
import requests
import time

def cleanup_project_cards(project_id, token):
    """清理项目中的所有卡片"""
    headers = {
        "access_token": token,
        "x-company-name": "moji",
        "Content-Type": "application/json"
    }

    deleted_count = 0

    while True:
        # 查询卡片
        url = f"https://ezone.matrixback.com/v1/project/project/card/searchByProject?projectId={project_id}"
        resp = requests.post(url, headers=headers, json={
            "pageNumber": 1,
            "pageSize": 50,
            "fields": ["title", "seq_num"],
            "sorts": [{"field": "seq_num", "order": "desc"}]
        })

        items = resp.json().get('data', {}).get('list', [])

        # 过滤有效卡片（seq_num 不为 None）
        valid_cards = [item for item in items
                       if item.get('card', {}).get('seq_num') is not None]

        if not valid_cards:
            break

        # 逐个删除
        for item in valid_cards:
            card_id = item.get('id')
            delete_url = f"https://ezone.matrixback.com/v1/project/project/card/{card_id}?projectId={project_id}"
            del_resp = requests.delete(delete_url, headers=headers)

            if del_resp.json().get('code') == 0:
                deleted_count += 1

            time.sleep(0.2)  # 避免请求过快

    return deleted_count
```

## 卡片审核记录（BPM审批流程）

### 功能说明

查询卡片的审批流程记录，包括：
- 审批流程名称和状态（FINISHED/PROCESSING/REJECTED）
- 各审批阶段的审核人、审核结果、审核意见
- 待审核人信息
- 抄送记录

### API 使用

```python
from ezone_api import EZoneAPI

api = EZoneAPI(token="YOUR_TOKEN")

# 方法1：获取原始审核记录
approval_resp = api.get_card_approval(card_id="1180788304141967360")

# 方法2：获取格式化的审核摘要（推荐）
summary = api.get_card_approval_summary(card_id="1180788304141967360")
```

### 审核记录响应结构

```json
{
  "code": 0,
  "data": {
    "flows": [
      {
        "date": 1770686889285,
        "user": "kaiwen.wei",
        "cardId": "1180788304141967360",
        "flowId": "5721",
        "approvalType": "CARD_STATUS",
        "flowDetail": {
          "fromStatus": "open",
          "toStatus": "processing",
          "fromStatusName": "新建",
          "toStatusName": "概念期"
        }
      }
    ],
    "details": [
      {
        "approval": {
          "id": "5721",
          "approvalFlowName": "MM转IPD",
          "status": "FINISHED",
          "username": "kaiwen.wei",
          "gmtCreate": "1770686889000"
        },
        "approvalStages": [
          {
            "approvalFlowStageName": "创建",
            "status": "CREATE",
            "records": [{"username": "kaiwen.wei", "result": "CREATE", "recordType": "APPROVAL"}]
          },
          {
            "approvalFlowStageName": "申请进概念期",
            "status": "FINISHED",
            "records": [
              {"username": "xiaoxiao.liu", "result": "APPROVAL", "reason": "已评审通过", "recordType": "APPROVAL"},
              {"username": "kaiwen.wei", "recordType": "COPY"}
            ]
          }
        ],
        "pendingApproval": false
      }
    ]
  }
}
```

### 格式化摘要返回结构

`get_card_approval_summary()` 返回：

```python
[
    {
        "flow_name": "MM转IPD",
        "flow_status": "FINISHED",        # FINISHED/PROCESSING/REJECTED
        "applicant": "kaiwen.wei",
        "create_time": "2026-02-10 09:28:09",
        "from_status_name": "新建",
        "to_status_name": "概念期",
        "stages": [
            {
                "name": "创建",
                "status": "CREATE",
                "records": [{"user": "kaiwen.wei", "result": "CREATE", "reason": "", "type": "APPROVAL", "time": "..."}]
            },
            {
                "name": "申请进概念期",
                "status": "FINISHED",
                "records": [{"user": "xiaoxiao.liu", "result": "APPROVAL", "reason": "已评审通过", "type": "APPROVAL", "time": "..."}]
            }
        ]
    },
    {
        "flow_name": "IPD转开发验证",
        "flow_status": "PROCESSING",
        "applicant": "rongtao.wang",
        "create_time": "2026-02-24 16:06:10",
        "from_status_name": "计划期",
        "to_status_name": "开发验证期",
        "stages": [
            {"name": "计划转开发", "status": "PROCESSING", "records": [], "pending_approvers": ["jia.ma"]}
        ]
    }
]
```

### 审批状态说明

| status | 说明 |
|--------|------|
| FINISHED | 审批已完成（通过） |
| PROCESSING | 审批进行中（等待审核） |
| REJECTED | 审批被拒绝 |
| CREATE | 创建阶段 |

### 审批记录类型说明

| recordType | result | 说明 |
|------------|--------|------|
| APPROVAL | CREATE | 发起审批 |
| APPROVAL | APPROVAL | 审批通过 |
| APPROVAL | REJECT | 审批拒绝 |
| COPY | - | 抄送通知 |

### 对话示例

```
用户: 查一下 IPD-114 的审核记录

助手: 我来查询这张卡片的审核记录...

审核流程 1：MM转IPD（新建 → 概念期）— ✅ 已完成
  - 发起人: kaiwen.wei (2026-02-10 09:28)
  - 申请进概念期: xiaoxiao.liu 审批通过 (2026-02-10 09:42)
    理由: "2月6日需求管理委员会已评审通过"

审核流程 2：IPD转开发验证（计划期 → 开发验证期）— ⏳ 审批中
  - 发起人: rongtao.wang (2026-02-24 16:06)
  - 计划转开发: 等待 jia.ma 审批
```

## 卡片事件历史（状态变更追踪）

### 功能说明

查询卡片的完整事件历史，包括：
- 创建时间和创建人
- 状态变更记录（谁在什么时间将状态从A改为B）
- 附件添加记录
- 其他字段修改记录

### API 使用

```python
from ezone_api import EZoneAPI

api = EZoneAPI(token="YOUR_TOKEN")

# 方法1：获取原始事件历史
events = api.get_card_events(card_id="1054283723845951488")

# 方法2：获取格式化的状态变更历史（推荐）
history = api.get_card_status_history(
    card_id="1054283723845951488",
    project_id="844795161124806656"  # 可选，提供后会解析状态名称
)

# 方法3：获取项目的状态映射
schema = api.get_project_schema(project_id="844795161124806656")

# 方法4：根据项目Key和卡片序号获取卡片
card = api.get_card_by_key(project_key="MojiWeather", seq_num=236)

# 方法5：获取卡片审核记录（BPM审批流程）
approval = api.get_card_approval(card_id="1180788304141967360")

# 方法6：获取格式化的审核摘要（推荐）
summary = api.get_card_approval_summary(card_id="1180788304141967360")
```

### 事件历史响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": "1115563957303918592",
      "cardId": "1054283723845951488",
      "date": 1711764892000,
      "user": "lingling.zhu",
      "eventType": "CREATE",
      "eventMsg": "创建了卡片"
    },
    {
      "id": "1115563957303918593",
      "cardId": "1054283723845951488",
      "date": 1712635892000,
      "user": "lingling.zhu",
      "eventType": "UPDATE",
      "eventMsg": "将 状态 从 新建 改为 待开发",
      "fieldDetailMsgs": [
        {
          "fieldKey": "status",
          "fromValue": "open",
          "toValue": "custom_5",
          "fromMsg": "新建",
          "toMsg": "待开发"
        }
      ]
    }
  ]
}
```

### 事件类型说明

| eventType | 说明 |
|-----------|------|
| CREATE | 卡片创建 |
| UPDATE | 卡片更新（包含状态变更） |
| ADD_ATTACHMENT | 添加附件 |

### 状态变更历史便捷方法

`get_card_status_history()` 返回格式化的状态变更列表：

```python
[
    {
        "date": "2025-03-30 10:15:00",
        "user": "lingling.zhu",
        "action": "创建卡片",
        "from_status": None,
        "to_status": "open",
        "from_name": None,
        "to_name": "新建"
    },
    {
        "date": "2025-04-09 14:30:00",
        "user": "lingling.zhu",
        "action": "状态变更",
        "from_status": "open",
        "to_status": "custom_5",
        "from_name": "新建",
        "to_name": "待开发"
    }
]
```

### 对话示例

```
用户: 查一下卡片 MojiWeather-236 的状态变更历史

助手: 我来查询这张卡片的状态变更历史...

状态变更时间线：
1. 2025-03-30 10:15:00 - lingling.zhu 创建卡片（新建）
2. 2025-04-09 14:30:00 - lingling.zhu 将状态从 新建 改为 待开发
3. 2025-04-27 09:00:00 - chaoju.liu 将状态从 待开发 改为 开发中
4. 2025-04-27 15:30:00 - shunxing.zuo 将状态从 开发中 改为 待测试
5. 2025-04-27 17:00:00 - chaoju.liu 将状态从 待测试 改为 测试完成
```

## 卡片字段说明

### 创建卡片请求体

```json
{
  "type": "task",           // 必填：卡片类型
  "title": "任务标题",       // 必填：标题
  "content": "任务描述",     // 可选：内容（支持 Markdown）
  "status": "open",         // 必填：状态
  "project_id": "xxx",      // 必填：项目ID
  "parent_id": "xxx",       // 可选：父卡片ID
  "owner_users": ["user1"], // 可选：负责人列表
  "start_date": "1700000000000",  // 可选：开始日期（毫秒时间戳）
  "end_date": "1700000000000",    // 可选：结束日期
  "estimate_workload": 8    // 可选：预估工时（小时）
}
```

### 创建成功响应

```json
{
  "code": 0,
  "data": {
    "id": "1154353601293869056",
    "projectId": "844795161124806656",
    "projectKey": "MojiWeather",
    "seqNum": "1617"
  }
}
```

## 依赖项

### Python 包

```bash
pip install requests
```

### 文件

- API 客户端：`./ezone_api.py`

## 质量检查清单

创建卡片后自检：

- [ ] 卡片类型正确？
- [ ] 标题清晰明确？
- [ ] 描述包含必要信息？
- [ ] 状态设置正确？
- [ ] 父卡片关联正确（如适用）？
- [ ] 返回了卡片链接？

## 参考文件

| 文件 | 用途 |
|------|------|
| `./ezone_api.py` | API 客户端 |
| 本 Skill | EZone 建卡逻辑说明 |
| https://ezone.matrixback.com/v1/project/doc.html | API 文档 |
