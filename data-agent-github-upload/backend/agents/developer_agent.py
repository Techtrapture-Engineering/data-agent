from google.adk.agents import LlmAgent

from ..toolsets.developer_toolset import get_developer_toolset

developer_toolset = get_developer_toolset()

developer_agent = LlmAgent(
    name="developer_agent",
    model="gemini-2.5-flash",
    instruction="""
    Expert in Google Cloud documentation.

    Use Developer Knowledge MCP.

    Search documentation before answering.

    Cite documentation when available.
    """,
    tools=[developer_toolset],
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)