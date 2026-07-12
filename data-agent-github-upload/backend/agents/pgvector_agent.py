from google.adk.agents import LlmAgent

from backend.toolsets.pgvector_toolset import get_pgvector_toolset

pgvector_agent = LlmAgent(
    name="pgvector_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a PostgreSQL pgvector specialist.

    Use pgvector tools for:
    - listing vector documents
    - inserting vector documents
    - similarity search

    For similarity search, use vector_similarity_search.
    For listing documents, use vector_list_documents.
    For inserting documents, use vector_insert_document.

    Explain results clearly.
    Do not transfer back to orchestrator_agent.
    """,
    tools=[get_pgvector_toolset()],
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)