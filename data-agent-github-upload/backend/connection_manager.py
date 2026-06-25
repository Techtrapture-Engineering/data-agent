from toolsets.bigquery_toolset import get_bigquery_toolset
from toolsets.cloudsql_toolset import get_cloudsql_toolset


def get_toolset(db_type):

    if db_type == "bigquery":
        return get_bigquery_toolset()

    elif db_type == "cloudsql":
        return get_cloudsql_toolset()

    else:
        raise ValueError("Unsupported database")