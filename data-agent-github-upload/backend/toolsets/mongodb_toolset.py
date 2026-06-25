from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

MONGODB_MCP_URL = "https://mongodb-toolbox-539049793214.us-central1.run.app/mcp"

def get_mongodb_toolset():
    return McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=MONGODB_MCP_URL,
            timeout=60,
        )
    )