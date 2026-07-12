from google.adk.agents import LlmAgent

from .bigquery_agent import bigquery_agent
from .cloudsql_agent import cloudsql_agent
from .mongodb_agent import mongodb_agent
from backend.agents.pgvector_agent import pgvector_agent
from backend.agents.neo4j_agent import neo4j_agent

orchestrator_agent = LlmAgent(
    name="orchestrator_agent",
    model="gemini-2.5-flash",
    instruction="""
    Route user requests to the correct specialist.

    Use bigquery_agent for:
    - BigQuery datasets
    - BigQuery tables
    - BigQuery schemas
    - BigQuery SQL queries

    Use cloudsql_agent for:
    - Cloud SQL instances
    - Cloud SQL databases
    - Cloud SQL users
    - Cloud SQL SQL queries

    Use mongodb_agent for MongoDB collections, documents, find queries, and aggregation.
    Use pgvector_agent for vector database, embeddings, semantic search, similarity search, or pgvector questions.
    Use neo4j_agent for Neo4j graph database, graph schema, node labels, relationship types, sample nodes, and Cypher-related graph questions.
    
    If unclear, ask one short clarification question.
    Route the request once to the correct specialist.
    Do not repeatedly transfer between agents.
    For greetings, answer directly.
    If the user message is only a greeting or casual conversation, do not route to database agents. Ask the user which database they want to work with.
    """,
    sub_agents=[
        bigquery_agent,
        cloudsql_agent,
        mongodb_agent,
        pgvector_agent,
        neo4j_agent,
    ],
)
