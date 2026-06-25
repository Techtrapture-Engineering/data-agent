import google.auth
import google.auth.transport.requests

from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StreamableHTTPConnectionParams
)

CLOUDSQL_MCP_URL = "https://sqladmin.googleapis.com/mcp"


def get_cloudsql_toolset():

    credentials, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )

    auth_request = google.auth.transport.requests.Request()

    credentials.refresh(auth_request)

    return McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=CLOUDSQL_MCP_URL,
            headers={
                "Authorization": f"Bearer {credentials.token}",
                "x-goog-user-project": project_id,
            },
        )
    )