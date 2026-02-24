#!/usr/bin/env python3
"""
EZone (简单云) API 工具
用于自动化在简单云项目管理系统中创建卡片

使用方法:
    from ezone_api import EZoneAPI

    api = EZoneAPI(token="your_token")

    # 获取项目列表
    projects = api.list_projects()

    # 创建卡片
    card = api.create_card(
        project_id="844795161124806656",
        card_type="task",
        title="任务标题",
        content="任务描述"
    )
"""

import os
import requests
import json
from typing import Optional, List, Dict, Any
from pathlib import Path


class EZoneAPI:
    """EZone API 客户端"""

    BASE_URL = "https://ezone.matrixback.com"

    # 卡片类型映射
    CARD_TYPES = {
        "project": "项目",
        "epic": "Epic",
        "feature": "Feature",
        "story": "Story",
        "task": "Task",
        "bug": "Bug",
        "custom_3": "前端task",
        "custom_4": "后端task",
        "custom_1": "线上bug",
        "custom_2": "线下bug",
        "transaction": "子任务"
    }

    # 卡片状态
    CARD_STATUS = {
        "open": "待处理",
        "processing": "进行中",
        "closed": "已完成"
    }

    def __init__(self, token: str, company_name: str = "moji",
                 default_owner: str = None):
        """
        初始化 EZone API 客户端

        Args:
            token: 访问令牌 (从个人设置页面获取)
            company_name: 公司名称，默认 "moji"
            default_owner: 默认负责人用户名（可选，不设置则使用系统用户名）
        """
        self.token = token
        self.company_name = company_name
        self.default_owner = default_owner
        self.headers = {
            "access_token": token,
            "x-company-name": company_name,
            "Content-Type": "application/json"
        }

    def _request(self, method: str, endpoint: str, params: Dict = None,
                 json_data: Dict = None) -> Dict:
        """发送 API 请求"""
        url = f"{self.BASE_URL}{endpoint}"

        try:
            resp = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                params=params,
                json=json_data,
                timeout=30
            )

            if resp.status_code in [200, 201]:
                return resp.json()
            else:
                return {
                    "code": resp.status_code,
                    "message": f"HTTP {resp.status_code}: {resp.text}"
                }
        except Exception as e:
            return {"code": -1, "message": str(e)}

    def get_current_user(self) -> str:
        """
        获取当前用户名

        优先级：
        1. 初始化时设置的 default_owner
        2. 操作系统用户名（通过 getpass.getuser()）

        Returns:
            当前用户名
        """
        # 如果设置了默认负责人，直接返回
        if self.default_owner:
            return self.default_owner

        # 使用操作系统用户名
        import getpass
        return getpass.getuser()

    def list_projects(self, page: int = 1, page_size: int = 50,
                      scope: str = "ROLE") -> Dict:
        """
        获取项目列表

        Args:
            page: 页码
            page_size: 每页数量
            scope: 范围，ROLE 表示有角色的项目

        Returns:
            项目列表响应
        """
        return self._request(
            "POST",
            "/v1/project/project/project/search",
            params={"pageNumber": page, "pageSize": page_size, "scope": scope},
            json_data={}
        )

    def get_project_by_key(self, project_key: str) -> Optional[Dict]:
        """
        根据项目 Key 获取项目信息

        Args:
            project_key: 项目 Key (如 "MojiWeather")

        Returns:
            项目信息或 None
        """
        result = self.list_projects(page_size=100)
        if result.get("code") == 0:
            # data 可能是列表或字典
            project_list = result.get("data", [])
            if isinstance(project_list, dict):
                project_list = project_list.get("list", [])
            for project in project_list:
                if project.get("key") == project_key:
                    return project
        return None

    def search_cards(self, project_id: str, page: int = 1,
                     page_size: int = 20, sort_by: str = "last_modify_time",
                     sort_order: str = "desc", fields: List[str] = None) -> Dict:
        """
        搜索项目中的卡片

        Args:
            project_id: 项目 ID
            page: 页码
            page_size: 每页数量
            sort_by: 排序字段 (last_modify_time, create_time, seq_num 等)
            sort_order: 排序方向 (desc 降序, asc 升序)
            fields: 返回字段列表

        Returns:
            卡片列表响应
        """
        if fields is None:
            fields = ["title", "type", "status", "last_modify_time",
                      "last_modify_user", "create_time", "create_user",
                      "owner_users", "content", "seq_num"]

        return self._request(
            "POST",
            "/v1/project/project/card/searchByProject",
            params={"projectId": project_id},
            json_data={
                "pageNumber": page,
                "pageSize": page_size,
                "fields": fields,
                "sorts": [{"field": sort_by, "order": sort_order}]
            }
        )

    def create_card(self, project_id: str, card_type: str, title: str,
                    content: str = "", status: str = "open",
                    parent_id: str = None, owner_users: List[str] = None,
                    start_date: str = None, end_date: str = None,
                    estimate_workload: int = None,
                    auto_fill_owner: bool = True,
                    custom_fields: Dict[str, Any] = None,
                    biz_owner_users: List[str] = None) -> Dict:
        """
        创建卡片

        Args:
            project_id: 项目 ID
            card_type: 卡片类型 (task, story, bug, feature, epic 等)
            title: 卡片标题
            content: 卡片内容/描述
            status: 状态 (open, processing, closed)
            parent_id: 父卡片 ID (用于创建子任务)
            owner_users: 负责人用户名列表
            start_date: 开始日期 (毫秒时间戳字符串)
            end_date: 结束日期 (毫秒时间戳字符串)
            estimate_workload: 预估工时 (小时)
            auto_fill_owner: 是否自动填充负责人（默认 True）
            custom_fields: 自定义字段字典，如 {"custom_4_keyword": ["username"]}
            biz_owner_users: 业务负责人用户名列表（快捷方式，等同于 custom_fields["custom_4_keyword"]）

        Returns:
            创建结果响应
        """
        card_data = {
            "type": card_type,
            "title": title,
            "content": content,
            "project_id": project_id,
            "status": status
        }

        # 自动填充负责人
        if auto_fill_owner and not owner_users:
            current_user = self.get_current_user()
            if current_user:
                owner_users = [current_user]

        if parent_id:
            card_data["parent_id"] = parent_id
        if owner_users:
            card_data["owner_users"] = owner_users
        if start_date:
            card_data["start_date"] = start_date
        if end_date:
            card_data["end_date"] = end_date
        if estimate_workload is not None:
            card_data["estimate_workload"] = estimate_workload

        # 处理业务负责人（快捷方式）
        if biz_owner_users:
            card_data["custom_4_keyword"] = biz_owner_users
        elif auto_fill_owner and "custom_4_keyword" not in (custom_fields or {}):
            # 自动填充业务负责人（如果没有指定且开启了自动填充）
            current_user = self.get_current_user()
            if current_user:
                card_data["custom_4_keyword"] = [current_user]

        # 处理其他自定义字段
        if custom_fields:
            for key, value in custom_fields.items():
                card_data[key] = value

        return self._request(
            "POST",
            "/v1/project/project/card",
            params={"projectId": project_id},
            json_data=card_data
        )

    def create_story(self, project_id: str, title: str, content: str = "",
                     **kwargs) -> Dict:
        """创建 Story 卡片"""
        return self.create_card(project_id, "story", title, content, **kwargs)

    def create_task(self, project_id: str, title: str, content: str = "",
                    parent_id: str = None, **kwargs) -> Dict:
        """创建 Task 卡片"""
        return self.create_card(project_id, "task", title, content,
                                parent_id=parent_id, **kwargs)

    def create_bug(self, project_id: str, title: str, content: str = "",
                   **kwargs) -> Dict:
        """创建 Bug 卡片"""
        return self.create_card(project_id, "bug", title, content, **kwargs)

    def create_feature(self, project_id: str, title: str, content: str = "",
                       **kwargs) -> Dict:
        """创建 Feature 卡片"""
        return self.create_card(project_id, "feature", title, content, **kwargs)

    def batch_create_cards(self, project_id: str,
                           cards: List[Dict]) -> List[Dict]:
        """
        批量创建卡片

        Args:
            project_id: 项目 ID
            cards: 卡片列表，每个卡片是一个字典，包含 type, title, content 等字段

        Returns:
            创建结果列表
        """
        results = []
        for card in cards:
            card_type = card.pop("type", "task")
            title = card.pop("title", "")
            content = card.pop("content", "")

            result = self.create_card(
                project_id=project_id,
                card_type=card_type,
                title=title,
                content=content,
                **card
            )
            results.append({
                "title": title,
                "result": result
            })

        return results

    def get_card_events(self, card_id: str) -> Dict:
        """
        获取卡片的事件历史记录（包含状态变更、创建、更新等）

        Args:
            card_id: 卡片 ID

        Returns:
            事件历史列表响应，包含：
            - id: 事件ID
            - cardId: 卡片ID
            - date: 事件时间戳（毫秒）
            - user: 操作用户名
            - eventType: 事件类型 (CREATE, UPDATE, ADD_ATTACHMENT 等)
            - eventMsg: 事件描述
            - fieldDetailMsgs: 字段变更详情（状态变更时包含 fromMsg, toMsg, fromValue, toValue）
        """
        return self._request(
            "GET",
            f"/v1/project/project/card/{card_id}/event"
        )

    def get_project_schema(self, project_id: str) -> Dict:
        """
        获取项目的 schema 配置（包含状态映射等）

        Args:
            project_id: 项目 ID

        Returns:
            项目 schema 响应，包含状态码到状态名称的映射
        """
        return self._request(
            "GET",
            f"/v1/project/project/project/{project_id}/schema"
        )

    def get_card_status_history(self, card_id: str, project_id: str = None) -> List[Dict]:
        """
        获取卡片的状态变更历史（便捷方法）

        Args:
            card_id: 卡片 ID
            project_id: 项目 ID（可选，如果提供则会解析状态名称）

        Returns:
            状态变更历史列表，每项包含：
            - date: 变更时间（ISO格式）
            - user: 操作用户
            - from_status: 原状态码
            - to_status: 新状态码
            - from_name: 原状态名称（如果提供了project_id）
            - to_name: 新状态名称（如果提供了project_id）
        """
        from datetime import datetime

        # 获取事件历史
        events_resp = self.get_card_events(card_id)
        if events_resp.get("code") != 0:
            return []

        # 获取状态映射（如果提供了project_id）
        status_map = {}
        if project_id:
            schema_resp = self.get_project_schema(project_id)
            if schema_resp.get("code") == 0:
                schema_data = schema_resp.get("data", {})
                statuses = schema_data.get("statuses", [])
                for s in statuses:
                    status_map[s.get("key")] = s.get("name")

        # 解析状态变更
        history = []
        events = events_resp.get("data", [])

        for event in events:
            event_type = event.get("eventType")
            timestamp = event.get("date", 0)
            user = event.get("user", "")

            # 转换时间戳
            try:
                dt = datetime.fromtimestamp(timestamp / 1000)
                date_str = dt.strftime("%Y-%m-%d %H:%M:%S")
            except:
                date_str = str(timestamp)

            if event_type == "CREATE":
                # 创建事件
                history.append({
                    "date": date_str,
                    "user": user,
                    "action": "创建卡片",
                    "from_status": None,
                    "to_status": "open",
                    "from_name": None,
                    "to_name": status_map.get("open", "新建")
                })
            elif event_type == "UPDATE":
                # 更新事件，检查是否有状态变更
                field_details = event.get("fieldDetailMsgs", [])
                for field in field_details:
                    if field.get("fieldKey") == "status":
                        from_val = field.get("fromValue")
                        to_val = field.get("toValue")
                        history.append({
                            "date": date_str,
                            "user": user,
                            "action": "状态变更",
                            "from_status": from_val,
                            "to_status": to_val,
                            "from_name": status_map.get(from_val, field.get("fromMsg", from_val)),
                            "to_name": status_map.get(to_val, field.get("toMsg", to_val))
                        })

        return history

    def get_card_approval(self, card_id: str) -> Dict:
        """
        获取卡片的审核记录（BPM审批流程）

        Args:
            card_id: 卡片 ID

        Returns:
            审核记录响应，包含：
            - flows: 审批流程概要列表
            - details: 审批流程详情列表，每项包含 approval（审批信息）和 approvalStages（审批阶段）
        """
        return self._request(
            "GET",
            f"/v1/project/project/card/{card_id}/approval"
        )

    def get_card_approval_summary(self, card_id: str) -> List[Dict]:
        """
        获取卡片审核记录的格式化摘要（便捷方法）

        Args:
            card_id: 卡片 ID

        Returns:
            审核流程摘要列表，每项包含：
            - flow_name: 审批流程名称
            - flow_status: 审批流程状态 (FINISHED/PROCESSING/REJECTED等)
            - applicant: 发起人
            - create_time: 发起时间
            - from_status_name: 原状态名称
            - to_status_name: 目标状态名称
            - stages: 各审批阶段列表
        """
        from datetime import datetime

        resp = self.get_card_approval(card_id)
        if resp.get("code") != 0:
            return []

        results = []
        for detail in resp.get("data", {}).get("details", []):
            approval = detail.get("approval", {})

            # 解析 content 中的状态名称
            content = {}
            try:
                import json as _json
                content = _json.loads(approval.get("content", "{}"))
            except:
                pass

            create_ts = int(approval.get("gmtCreate", 0))
            try:
                create_time = datetime.fromtimestamp(create_ts / 1000).strftime("%Y-%m-%d %H:%M:%S")
            except:
                create_time = str(create_ts)

            stages = []
            for stage in detail.get("approvalStages", []):
                stage_info = {
                    "name": stage.get("approvalFlowStageName", ""),
                    "status": stage.get("status", ""),
                    "records": []
                }
                for rec in stage.get("records", []):
                    rec_ts = int(rec.get("gmtCreate", 0))
                    try:
                        rec_time = datetime.fromtimestamp(rec_ts / 1000).strftime("%Y-%m-%d %H:%M:%S")
                    except:
                        rec_time = str(rec_ts)
                    stage_info["records"].append({
                        "user": rec.get("username", ""),
                        "result": rec.get("result", ""),
                        "reason": rec.get("reason", ""),
                        "type": rec.get("recordType", ""),
                        "time": rec_time
                    })
                # 待审核人
                approvers = stage.get("approvers", [])
                if approvers:
                    stage_info["pending_approvers"] = [a.get("name", "") for a in approvers]
                stages.append(stage_info)

            results.append({
                "flow_name": approval.get("approvalFlowName", ""),
                "flow_status": approval.get("status", ""),
                "applicant": approval.get("username", ""),
                "create_time": create_time,
                "from_status_name": content.get("fromStatusName", ""),
                "to_status_name": content.get("toStatusName", ""),
                "stages": stages
            })

        return results

    def get_card_by_key(self, project_key: str, seq_num: int) -> Dict:
        """
        根据项目Key和卡片序号获取卡片详情

        Args:
            project_key: 项目 Key (如 "MojiWeather")
            seq_num: 卡片序号

        Returns:
            卡片详情响应
        """
        return self._request(
            "GET",
            f"/v1/project/project/card/{project_key}-{seq_num}"
        )

    def delete_cards(self, card_ids: List[int]) -> Dict:
        """
        批量删除卡片（逻辑删除）

        Args:
            card_ids: 卡片 ID 列表（int64 格式）

        Returns:
            删除结果响应
            {
                "code": 0,  # 0 表示成功
                "data": null
            }

        Example:
            >>> api.delete_cards([1157325358376181760, 1157325358376181761])
        """
        # 确保 card_ids 是整数列表
        int_ids = [int(cid) for cid in card_ids]

        return self._request(
            "POST",
            "/v1/project/project/card/batch/delete",
            json_data=int_ids
        )

    def search_cards_by_parent(self, project_id: str, parent_id: str,
                               page: int = 1, page_size: int = 50) -> Dict:
        """
        搜索指定父卡片下的子卡片

        Args:
            project_id: 项目 ID
            parent_id: 父卡片 ID
            page: 页码
            page_size: 每页数量

        Returns:
            卡片列表响应
        """
        return self._request(
            "POST",
            "/v1/project/project/card/searchByProject",
            params={"projectId": project_id},
            json_data={
                "pageNumber": page,
                "pageSize": page_size,
                "fields": ["title", "type", "status", "seq_num", "parent_id"],
                "filters": [
                    {"field": "parent_id", "operator": "=", "value": parent_id}
                ],
                "sorts": [{"field": "create_time", "order": "desc"}]
            }
        )

    def upload_attachment(
        self,
        card_id: str,
        file_path: str,
        description: str = ""
    ) -> Dict:
        """
        上传附件到卡片

        Args:
            card_id: 卡片ID
            file_path: 本地文件路径
            description: 附件描述/备注

        Returns:
            {
                "code": 0,
                "data": {
                    "id": 附件ID,
                    "fileName": "文件名",
                    "contentType": "文件类型",
                    "uploadTime": "上传时间",
                    "uploadUser": "上传人",
                    ...
                }
            }

        Example:
            >>> api.upload_attachment(
            ...     card_id="1157325358376181760",
            ...     file_path="/path/to/file.docx",
            ...     description="PRD需求文档"
            ... )
        """
        from pathlib import Path

        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        url = f"{self.BASE_URL}/v1/project/project/card/{card_id}/attachment"

        # 准备文件上传
        with open(file_path, 'rb') as f:
            files = {
                'file': (file_path.name, f, self._get_content_type(file_path.name))
            }

            params = {}
            if description:
                params['description'] = description

            # 文件上传时不能设置 Content-Type，让 requests 自动设置为 multipart/form-data
            upload_headers = {
                'access_token': self.headers['access_token'],
                'x-company-name': self.headers['x-company-name']
            }

            response = requests.post(
                url,
                headers=upload_headers,
                files=files,
                params=params,
                timeout=60  # 上传文件可能需要更长时间
            )

        return response.json()

    def _get_content_type(self, filename: str) -> str:
        """根据文件名推测 Content-Type"""
        import mimetypes
        content_type, _ = mimetypes.guess_type(filename)

        if content_type:
            return content_type

        # 常见文件类型映射
        ext_map = {
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.doc': 'application/msword',
            '.pdf': 'application/pdf',
            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            '.xls': 'application/vnd.ms-excel',
            '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            '.ppt': 'application/vnd.ms-powerpoint',
            '.zip': 'application/zip',
            '.txt': 'text/plain',
            '.md': 'text/markdown',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
        }

        ext = Path(filename).suffix.lower()
        return ext_map.get(ext, 'application/octet-stream')


def get_token() -> str:
    """
    获取 EZone Token，按优先级：
    1. 环境变量 EZONE_TOKEN
    2. 配置文件 ~/.ezone_token
    3. 项目配置文件 .ezone_token

    Returns:
        Token 字符串

    Raises:
        ValueError: 未找到 Token
    """
    # 1. 环境变量
    token = os.environ.get("EZONE_TOKEN")
    if token:
        return token.strip()

    # 2. 用户主目录配置文件
    home_config = Path.home() / ".ezone_token"
    if home_config.exists():
        token = home_config.read_text().strip()
        if token:
            return token

    # 3. 当前项目配置文件
    local_config = Path(".ezone_token")
    if local_config.exists():
        token = local_config.read_text().strip()
        if token:
            return token

    raise ValueError(
        "未找到 EZone Token！请通过以下方式之一配置：\n"
        "1. 设置环境变量: export EZONE_TOKEN=your_token\n"
        "2. 创建配置文件: echo 'your_token' > ~/.ezone_token\n"
        "3. 项目配置文件: echo 'your_token' > .ezone_token\n"
        "\n获取 Token: EZone 个人设置 > 访问令牌"
    )


def main():
    """示例用法"""
    # 从环境变量或配置文件获取 token
    try:
        TOKEN = get_token()
        print(f"Token 已加载 (来源: 环境变量/配置文件)")
    except ValueError as e:
        print(f"错误: {e}")
        return

    api = EZoneAPI(token=TOKEN)

    # 1. 获取项目列表
    print("=== 项目列表 ===")
    projects = api.list_projects()
    if projects.get("code") == 0:
        # 注意: data 直接是列表，不是 {"list": [...]}
        project_list = projects["data"]
        if isinstance(project_list, dict):
            project_list = project_list.get("list", [])
        for p in project_list[:5]:
            print(f"  - {p['key']}: {p['name']} (ID: {p['id']})")

    # 2. 获取 MojiWeather 项目
    print("\n=== MojiWeather 项目 ===")
    moji = api.get_project_by_key("MojiWeather")
    if moji:
        print(f"  ID: {moji['id']}")
        print(f"  名称: {moji['name']}")

        # 3. 搜索现有卡片
        print("\n=== 最新卡片 ===")
        cards = api.search_cards(moji["id"], page_size=3)
        if cards.get("code") == 0:
            for item in cards["data"]["list"]:
                card = item["card"]
                print(f"  - [{card['type']}] {card['title'][:40]}...")


if __name__ == "__main__":
    main()
