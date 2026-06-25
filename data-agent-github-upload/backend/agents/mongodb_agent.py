from google.adk.agents import LlmAgent

from backend.toolsets.mongodb_toolset import get_mongodb_toolset

mongodb_toolset = get_mongodb_toolset()

mongodb_agent = LlmAgent(
    name="mongodb_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a MongoDB specialist.

    Use MongoDB MCP tools for:
    - finding orders
    - finding one order
    - aggregating orders by region

    Use read-only tools only.
    Explain results clearly.
    """,
    tools=[get_mongodb_toolset()],
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)