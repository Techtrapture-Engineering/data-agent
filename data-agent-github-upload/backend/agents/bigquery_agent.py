from google.adk.agents import LlmAgent

from backend.tools.bigquery_dynamic_tools import (
    list_bigquery_datasets,
    list_bigquery_tables,
    get_bigquery_table_schema,
    execute_bigquery_sql,
)

bigquery_agent = LlmAgent(
    name="bigquery_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a BigQuery specialist.

    If the user provides a project ID in chat, use it.
    If no project ID is known, ask the user for the BigQuery project ID.

    Use dynamic BigQuery tools.
    Do not use hardcoded project IDs.

    Do not transfer back to orchestrator_agent.
    """,
    tools=[
        list_bigquery_datasets,
        list_bigquery_tables,
        get_bigquery_table_schema,
        execute_bigquery_sql,
    ],
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)