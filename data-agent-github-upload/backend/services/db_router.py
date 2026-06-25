DATABASES = {
    "bigquery": {
        "agent": "bigquery_agent",
        "capabilities": [
            "datasets",
            "tables",
            "analytics",
            "sql"
        ]
    },

    "cloudsql": {
        "agent": "cloudsql_agent",
        "capabilities": [
            "instances",
            "users",
            "backups"
        ]
    }
}