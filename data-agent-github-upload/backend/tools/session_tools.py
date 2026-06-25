from google.adk.tools import ToolContext


def save_database_connection(
    tool_context: ToolContext,
    db_type: str,
    project_id: str = "",
    instance_name: str = "",
    username: str = "",
    password: str = "",
) -> dict:
    """Save database connection details into session state."""

    tool_context.state["db_type"] = db_type
    tool_context.state["project_id"] = project_id
    tool_context.state["instance_name"] = instance_name
    tool_context.state["username"] = username
    tool_context.state["password"] = password

    return {
        "status": "saved",
        "db_type": db_type,
        "project_id": project_id,
        "instance_name": instance_name,
    }