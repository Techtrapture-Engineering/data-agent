from google.adk.tools import ToolContext
from google.cloud import bigquery


def list_bigquery_datasets(tool_context: ToolContext) -> dict:
    """List BigQuery datasets using project_id from session state."""

    project_id = tool_context.state.get("project_id")

    if not project_id:
        return {
            "error": "Project ID is missing. Please complete onboarding first."
        }

    client = bigquery.Client(project=project_id)

    datasets = list(client.list_datasets(project=project_id))

    return {
        "project_id": project_id,
        "datasets": [
            {
                "dataset_id": dataset.dataset_id,
                "full_id": dataset.full_dataset_id,
            }
            for dataset in datasets
        ],
    }


#Add list tables

def list_bigquery_tables(
    tool_context: ToolContext,
    dataset_id: str
) -> dict:
    """List tables from a dataset using project_id from session state."""

    project_id = tool_context.state.get("project_id")

    if not project_id:
        return {
            "error": "Project ID missing."
        }

    client = bigquery.Client(project=project_id)

    tables = list(
        client.list_tables(f"{project_id}.{dataset_id}")
    )

    return {
        "project_id": project_id,
        "dataset_id": dataset_id,
        "tables": [
            table.table_id for table in tables
        ]
    }


#Add get schema

def get_bigquery_table_schema(
    tool_context: ToolContext,
    dataset_id: str,
    table_id: str
) -> dict:
    """Get schema for a table."""

    project_id = tool_context.state.get("project_id")

    if not project_id:
        return {
            "error": "Project ID missing."
        }

    client = bigquery.Client(project=project_id)

    table = client.get_table(
        f"{project_id}.{dataset_id}.{table_id}"
    )

    return {
        "table": table_id,
        "schema": [
            {
                "name": field.name,
                "type": field.field_type,
                "mode": field.mode
            }
            for field in table.schema
        ]
    }


#Add readonly SQL execution

def execute_bigquery_sql(
    tool_context: ToolContext,
    query: str
) -> dict:
    """Execute read-only SQL."""

    project_id = tool_context.state.get("project_id")

    if not project_id:
        return {
            "error": "Project ID missing."
        }

    client = bigquery.Client(project=project_id)

    query_job = client.query(query)

    rows = [dict(row) for row in query_job.result()]

    return {
        "project_id": project_id,
        "query": query,
        "rows": rows
    }


