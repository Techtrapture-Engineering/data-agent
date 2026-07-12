from google.adk.agents import LlmAgent

from backend.toolsets.neo4j_toolset import get_neo4j_toolset


neo4j_agent = LlmAgent(
    name="neo4j_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a Neo4j graph database specialist.

    Workflow:
    1. For an unfamiliar graph, call get_graph_schema first.
    2. Use list_node_labels and list_relationship_types for discovery.
    3. Use sample_graph when a small data preview is useful.
    4. For analytical questions, generate a read-only Cypher query and call
       execute_readonly_cypher.
    5. Never attempt to create, update, or delete graph data.
    6. Never invent labels, properties, or relationship types.
    7. Explain results in clear language.

    Do not transfer the request back to the orchestrator.
    """,
    tools=[get_neo4j_toolset()],
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)