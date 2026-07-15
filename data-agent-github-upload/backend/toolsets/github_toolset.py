import os

from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StreamableHTTPConnectionParams,
)


GITHUB_MCP_URL = "https://api.githubcopilot.com/mcp/x/repos"


def get_github_toolset() -> McpToolset:
    github_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")

    if not github_token:
        raise RuntimeError(
            "GITHUB_PERSONAL_ACCESS_TOKEN is not configured."
        )

    return McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=GITHUB_MCP_URL,
            headers={
                "Authorization": f"Bearer {github_token}",
                "X-MCP-Readonly": "false",
            },
            timeout=60,
        )
    )