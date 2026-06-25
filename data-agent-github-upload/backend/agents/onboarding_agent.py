from google.adk.agents import LlmAgent
from backend.tools.session_tools import save_database_connection

onboarding_agent = LlmAgent(
    name="onboarding_agent",
    model="gemini-2.5-flash",
    instruction="""
    You collect database connection details.

    Ask which database the user wants:
    - BigQuery
    - Cloud SQL
    - PostgreSQL
    - MySQL
    - Oracle
    - Snowflake

    For BigQuery, ask for project_id.
    After user gives it, call save_database_connection with:
    db_type="bigquery"
    project_id=<user project id>

    For Cloud SQL, ask for:
    - instance_name
    - #username
    - password

    After user gives them, call save_database_connection with:
    db_type="cloudsql"
    instance_name=<instance>
    #username=<username>
    password=<password>

    Do not answer database questions.
    Save the connection first.
    """,
    tools=[save_database_connection],
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)