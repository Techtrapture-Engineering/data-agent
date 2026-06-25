from google.adk.agents import LlmAgent

from backend.toolsets.cloudsql_toolset import get_cloudsql_toolset

cloudsql_toolset = get_cloudsql_toolset()

cloudsql_agent = LlmAgent(
    name="cloudsql_agent",
    model="gemini-2.5-flash",
    instruction="""
        Expert in Cloud SQL.

        Supported engines:
        - MySQL
        - PostgreSQL

        Before generating SQL:
        first identify the engine type.

        Use MySQL syntax for MySQL instances.
        Use PostgreSQL syntax for PostgreSQL instances.

        Always use execute_sql_readonly when possible.
        """,
    tools=[get_cloudsql_toolset()],
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)