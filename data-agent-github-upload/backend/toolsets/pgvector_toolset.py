from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

PGVECTOR_MCP_URL = "https://pgvector-toolbox-539049793214.us-central1.run.app/mcp"

def get_pgvector_toolset():
    return McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=PGVECTOR_MCP_URL,
            timeout=60,
        )
    )