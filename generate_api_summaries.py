#!/usr/bin/env python3
"""
EZone API 摘要文件生成器

从 Swagger JSON 解析 API 并为每个模块生成 Markdown 摘要文件。
"""

import json
import os
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# 模块配置
MODULE_CONFIG = {
    # 卡片管理（核心）
    "card-controller": {
        "output": "card.md",
        "title": "卡片管理 API",
        "description": "卡片 CRUD、批量、搜索",
        "category": "卡片管理"
    },
    "card-api-controller": {
        "output": "card-api.md",
        "title": "卡片外部接口 API",
        "description": "卡片外部接口",
        "category": "卡片管理"
    },
    "card-attachment-controller": {
        "output": "attachment.md",
        "title": "附件管理 API",
        "description": "卡片附件管理",
        "category": "卡片管理"
    },
    "card-comment-controller": {
        "output": "comment.md",
        "title": "评论 API",
        "description": "卡片评论",
        "category": "卡片管理"
    },
    "card-event-controller": {
        "output": "event.md",
        "title": "事件历史 API",
        "description": "卡片事件历史",
        "category": "卡片管理"
    },
    "card-relate-controller": {
        "output": "relate.md",
        "title": "卡片关联 API",
        "description": "卡片关联关系",
        "category": "卡片管理"
    },
    "card-watch-controller": {
        "output": "watch.md",
        "title": "关注 API",
        "description": "卡片关注",
        "category": "卡片管理"
    },
    "card-query-view-controller": {
        "output": "query-view.md",
        "title": "自定义查询视图 API",
        "description": "自定义查询视图",
        "category": "卡片管理"
    },

    # 项目管理
    "project-controller": {
        "output": "project.md",
        "title": "项目管理 API",
        "description": "项目 CRUD",
        "category": "项目管理"
    },
    "project-api-controller": {
        "output": "project-api.md",
        "title": "项目外部接口 API",
        "description": "项目外部接口",
        "category": "项目管理"
    },
    "project-member-controller": {
        "output": "member.md",
        "title": "成员管理 API",
        "description": "项目成员管理",
        "category": "项目管理"
    },
    "project-schema-controller": {
        "output": "schema.md",
        "title": "字段/状态配置 API",
        "description": "项目 Schema 配置",
        "category": "项目管理"
    },

    # 迭代计划
    "plan-controller": {
        "output": "plan.md",
        "title": "迭代管理 API",
        "description": "迭代计划管理",
        "category": "迭代计划"
    },
    "plan-api-controller": {
        "output": "plan-api.md",
        "title": "迭代外部接口 API",
        "description": "迭代外部接口",
        "category": "迭代计划"
    },
    "plan-goal-controller": {
        "output": "goal.md",
        "title": "迭代目标 API",
        "description": "迭代目标",
        "category": "迭代计划"
    },

    # 其他实用模块
    "chart-controller": {
        "output": "chart.md",
        "title": "报表图表 API",
        "description": "报表图表",
        "category": "其他"
    },
    "product-version-controller": {
        "output": "version.md",
        "title": "版本管理 API",
        "description": "产品版本管理",
        "category": "其他"
    },
    "work-bench-controller": {
        "output": "workbench.md",
        "title": "工作台 API",
        "description": "工作台/待办",
        "category": "其他"
    },
    "story-map-controller": {
        "output": "story-map.md",
        "title": "故事地图 API",
        "description": "故事地图",
        "category": "其他"
    },

    # 代码集成（可选）
    "card-code-branch-controller": {
        "output": "code-branch.md",
        "title": "代码分支关联 API",
        "description": "代码分支关联",
        "category": "代码集成"
    },
    "card-code-review-controller": {
        "output": "code-review.md",
        "title": "代码评审 API",
        "description": "代码评审",
        "category": "代码集成"
    },
    "project-repo-controller": {
        "output": "repo.md",
        "title": "代码仓库 API",
        "description": "代码仓库",
        "category": "代码集成"
    },

    # 测试管理（可选）
    "card-test-case-controller": {
        "output": "test-case.md",
        "title": "测试用例 API",
        "description": "测试用例",
        "category": "测试管理"
    },
    "card-test-plan-controller": {
        "output": "test-plan.md",
        "title": "测试计划 API",
        "description": "测试计划",
        "category": "测试管理"
    },
}

# 已实现的接口（从 ezone_api.py 中提取）
# 使用 Swagger 路径格式（无 /v1/project/project 前缀）
IMPLEMENTED_APIS = [
    # card-controller
    ("POST", "/project/card", "创建卡片"),
    ("POST", "/project/card/searchByProject", "按项目搜索卡片"),
    ("GET", "/project/card/{id}", "获取卡片详情"),
    ("GET", "/project/card/{projectKey}-{seqNum}", "按序号获取卡片"),
    ("DELETE", "/project/card/{id}", "删除卡片"),
    ("POST", "/project/card/batch/delete", "批量删除卡片"),

    # card-event-controller
    ("GET", "/project/card/{cardId}/event", "获取卡片事件历史"),

    # card-attachment-controller
    ("POST", "/project/card/{cardId}/attachment", "上传附件"),

    # project-controller
    ("POST", "/project/project/search", "搜索项目"),

    # project-schema-controller
    ("GET", "/project/project/{id}/schema", "获取项目Schema"),
]


def load_swagger(filepath):
    """加载 Swagger JSON 文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_apis_by_tag(swagger_data):
    """按 tag 提取 API"""
    apis_by_tag = defaultdict(list)

    paths = swagger_data.get("paths", {})

    for path, methods in paths.items():
        for method, details in methods.items():
            # 跳过非 HTTP 方法
            if method.upper() not in ["GET", "POST", "PUT", "DELETE", "PATCH"]:
                continue

            tags = details.get("tags", [])
            summary = details.get("summary", "")
            operation_id = details.get("operationId", "")
            parameters = details.get("parameters", [])
            deprecated = details.get("deprecated", False)

            for tag in tags:
                api_info = {
                    "method": method.upper(),
                    "path": path,
                    "summary": summary,
                    "operation_id": operation_id,
                    "parameters": parameters,
                    "deprecated": deprecated
                }
                apis_by_tag[tag].append(api_info)

    return apis_by_tag


def categorize_apis(apis):
    """将 API 按功能分类"""
    categories = {
        "创建/更新": [],
        "查询/搜索": [],
        "删除": [],
        "批量操作": [],
        "其他": []
    }

    for api in apis:
        method = api["method"]
        path = api["path"]
        summary = api["summary"].lower()

        # 判断分类
        if "batch" in path.lower() or "批量" in summary:
            categories["批量操作"].append(api)
        elif method == "DELETE" or "delete" in summary:
            categories["删除"].append(api)
        elif method == "POST" and ("create" in summary or "add" in summary or "新建" in summary):
            categories["创建/更新"].append(api)
        elif method == "PUT" or method == "PATCH" or "update" in summary or "修改" in summary:
            categories["创建/更新"].append(api)
        elif method == "GET" or "search" in summary or "list" in summary or "query" in summary or "get" in summary:
            categories["查询/搜索"].append(api)
        else:
            categories["其他"].append(api)

    return categories


def get_implementation_status(method, path):
    """获取实现状态"""
    # 检查是否已实现（精确匹配）
    for impl_method, impl_path, desc in IMPLEMENTED_APIS:
        if method == impl_method and path == impl_path:
            return "✅ 已实现", desc

    return "⬜ 待实现", ""


def extract_common_params(apis):
    """提取常用参数"""
    param_counts = defaultdict(lambda: {"count": 0, "type": "", "description": ""})

    for api in apis:
        for param in api.get("parameters", []):
            name = param.get("name", "")
            if name == "x-company-name":
                continue  # 跳过通用头

            param_type = param.get("type", param.get("schema", {}).get("type", ""))
            description = param.get("description", "")

            param_counts[name]["count"] += 1
            if not param_counts[name]["type"]:
                param_counts[name]["type"] = param_type
            if not param_counts[name]["description"]:
                param_counts[name]["description"] = description

    # 返回出现次数 > 1 的参数
    common_params = []
    for name, info in sorted(param_counts.items(), key=lambda x: -x[1]["count"]):
        if info["count"] > 1:
            common_params.append({
                "name": name,
                "type": info["type"],
                "description": info["description"]
            })

    return common_params[:15]  # 最多 15 个


def generate_summary_md(tag, config, apis):
    """生成单个模块的摘要 Markdown"""
    title = config["title"]
    description = config["description"]
    category = config["category"]

    # 统计
    total_count = len(apis)
    implemented_count = sum(1 for api in apis
                           if get_implementation_status(api["method"], api["path"])[0].startswith("✅"))

    # 分类
    categories = categorize_apis(apis)

    # 常用参数
    common_params = extract_common_params(apis)

    # 生成时间
    gen_time = datetime.now().strftime("%Y-%m-%d")

    # 构建 Markdown
    lines = [
        f"# {title} ({tag})",
        "",
        f"> 来源: ezone_api_doc.json | 生成时间: {gen_time}",
        "",
        "## 概览",
        "",
        f"- **接口总数**: {total_count} 个",
        f"- **已实现**: {implemented_count} 个",
        f"- **待扩展**: {total_count - implemented_count} 个",
        f"- **分类**: {category}",
        "",
        "## 接口列表",
        "",
    ]

    # 按分类输出
    for cat_name, cat_apis in categories.items():
        if not cat_apis:
            continue

        lines.append(f"### {cat_name}")
        lines.append("")
        lines.append("| 方法 | 路径 | 说明 | 状态 |")
        lines.append("|------|------|------|------|")

        for api in sorted(cat_apis, key=lambda x: (x["method"], x["path"])):
            method = api["method"]
            path = api["path"]
            summary = api["summary"]
            status, _ = get_implementation_status(method, path)

            # 简化路径显示
            display_path = path
            if len(display_path) > 50:
                display_path = display_path[:47] + "..."

            lines.append(f"| {method} | `{display_path}` | {summary} | {status} |")

        lines.append("")

    # 常用参数说明
    if common_params:
        lines.append("## 常用参数说明")
        lines.append("")
        lines.append("| 参数 | 类型 | 说明 |")
        lines.append("|------|------|------|")

        for param in common_params:
            lines.append(f"| {param['name']} | {param['type']} | {param['description']} |")

        lines.append("")

    # 使用示例（如果有已实现的接口）
    if implemented_count > 0:
        lines.append("## 使用示例")
        lines.append("")
        lines.append("```python")
        lines.append("from ezone_api import EZoneAPI, get_token")
        lines.append("")
        lines.append("api = EZoneAPI(token=get_token())")
        lines.append("")

        # 添加具体示例
        if tag == "card-controller":
            lines.append("# 搜索卡片")
            lines.append('cards = api.search_cards(project_id="844795161124806656")')
            lines.append("")
            lines.append("# 创建卡片")
            lines.append("result = api.create_card(")
            lines.append('    project_id="844795161124806656",')
            lines.append('    card_type="task",')
            lines.append('    title="任务标题",')
            lines.append('    content="任务描述"')
            lines.append(")")
        elif tag == "project-controller":
            lines.append("# 获取项目列表")
            lines.append("projects = api.list_projects()")
            lines.append("")
            lines.append("# 根据 Key 获取项目")
            lines.append('project = api.get_project_by_key("MojiWeather")')
        elif tag == "card-event-controller":
            lines.append("# 获取卡片事件历史")
            lines.append('events = api.get_card_events(card_id="1054283723845951488")')
            lines.append("")
            lines.append("# 获取状态变更历史")
            lines.append("history = api.get_card_status_history(")
            lines.append('    card_id="1054283723845951488",')
            lines.append('    project_id="844795161124806656"')
            lines.append(")")
        elif tag == "project-schema-controller":
            lines.append("# 获取项目 Schema")
            lines.append('schema = api.get_project_schema(project_id="844795161124806656")')
        elif tag == "card-attachment-controller":
            lines.append("# 上传附件")
            lines.append("result = api.upload_attachment(")
            lines.append('    card_id="1157325358376181760",')
            lines.append('    file_path="/path/to/file.docx",')
            lines.append('    description="PRD需求文档"')
            lines.append(")")
        else:
            lines.append("# 参考 ezone_api.py 中的实现")
            lines.append("# 或查看 SKILL.md 获取更多示例")

        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def generate_readme(module_stats, output_dir):
    """生成总索引 README.md"""
    gen_time = datetime.now().strftime("%Y-%m-%d")

    lines = [
        "# EZone API 摘要索引",
        "",
        f"> 生成时间: {gen_time}",
        "",
        "本目录包含 EZone 项目管理系统的 API 摘要文件，方便快速查阅和扩展功能。",
        "",
        "## 统计",
        "",
    ]

    # 按分类统计
    categories = defaultdict(list)
    total_apis = 0
    total_implemented = 0

    for tag, stats in module_stats.items():
        config = MODULE_CONFIG.get(tag, {})
        category = config.get("category", "其他")
        categories[category].append({
            "tag": tag,
            "output": config.get("output", ""),
            "title": config.get("title", tag),
            "total": stats["total"],
            "implemented": stats["implemented"]
        })
        total_apis += stats["total"]
        total_implemented += stats["implemented"]

    lines.append(f"- **总接口数**: {total_apis}")
    lines.append(f"- **已实现**: {total_implemented}")
    lines.append(f"- **覆盖率**: {total_implemented/total_apis*100:.1f}%")
    lines.append(f"- **模块数**: {len(module_stats)}")
    lines.append("")

    # 按分类输出
    lines.append("## 模块索引")
    lines.append("")

    category_order = ["卡片管理", "项目管理", "迭代计划", "其他", "代码集成", "测试管理"]

    for category in category_order:
        if category not in categories:
            continue

        lines.append(f"### {category}")
        lines.append("")
        lines.append("| 模块 | 文件 | 接口数 | 已实现 |")
        lines.append("|------|------|--------|--------|")

        for item in categories[category]:
            lines.append(f"| {item['title']} | [{item['output']}]({item['output']}) | {item['total']} | {item['implemented']} |")

        lines.append("")

    # 快速开始
    lines.append("## 快速开始")
    lines.append("")
    lines.append("```python")
    lines.append("from ezone_api import EZoneAPI, get_token")
    lines.append("")
    lines.append("# 初始化")
    lines.append("api = EZoneAPI(token=get_token())")
    lines.append("")
    lines.append("# 搜索卡片")
    lines.append('cards = api.search_cards(project_id="844795161124806656")')
    lines.append("")
    lines.append("# 创建卡片")
    lines.append("result = api.create_card(")
    lines.append('    project_id="844795161124806656",')
    lines.append('    card_type="task",')
    lines.append('    title="任务标题"')
    lines.append(")")
    lines.append("```")
    lines.append("")

    # 扩展指引
    lines.append("## 扩展指引")
    lines.append("")
    lines.append("需要扩展新功能时：")
    lines.append("")
    lines.append("1. 查找对应模块的摘要文件")
    lines.append("2. 找到需要的 API 端点")
    lines.append("3. 在 `ezone_api.py` 中添加方法")
    lines.append("4. 更新 `SKILL.md` 文档")
    lines.append("")
    lines.append("## 相关文件")
    lines.append("")
    lines.append("| 文件 | 说明 |")
    lines.append("|------|------|")
    lines.append("| `../ezone_api.py` | API 客户端实现 |")
    lines.append("| `../SKILL.md` | Skill 使用说明 |")
    lines.append("| `../ezone_api_doc.json` | 原始 Swagger JSON |")
    lines.append("")

    return "\n".join(lines)


def main():
    """主函数"""
    script_dir = Path(__file__).parent
    swagger_path = script_dir / "ezone_api_doc.json"
    output_dir = script_dir / "api_summaries"

    # 确保输出目录存在
    output_dir.mkdir(exist_ok=True)

    # 加载 Swagger
    print(f"加载 Swagger 文件: {swagger_path}")
    swagger_data = load_swagger(swagger_path)

    # 按 tag 提取 API
    apis_by_tag = extract_apis_by_tag(swagger_data)
    print(f"发现 {len(apis_by_tag)} 个 controller")

    # 统计信息
    module_stats = {}

    # 生成各模块摘要
    for tag, config in MODULE_CONFIG.items():
        apis = apis_by_tag.get(tag, [])

        if not apis:
            print(f"  跳过 {tag}: 无 API")
            continue

        # 生成摘要
        md_content = generate_summary_md(tag, config, apis)

        # 写入文件
        output_path = output_dir / config["output"]
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        # 统计
        implemented_count = sum(1 for api in apis
                               if get_implementation_status(api["method"], api["path"])[0].startswith("✅"))
        module_stats[tag] = {
            "total": len(apis),
            "implemented": implemented_count
        }

        print(f"  生成 {config['output']}: {len(apis)} 个接口, {implemented_count} 个已实现")

    # 生成 README
    readme_content = generate_readme(module_stats, output_dir)
    readme_path = output_dir / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"生成索引: README.md")

    print(f"\n完成! 共生成 {len(module_stats) + 1} 个文件")


if __name__ == "__main__":
    main()
