from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

NEO4J_MCP_URL = "https://neo4j-toolbox-539049793214.us-central1.run.app/mcp"

def get_neo4j_toolset():
    return McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=NEO4J_MCP_URL,
            timeout=60,
        )
    )