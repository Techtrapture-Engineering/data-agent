# Data Agent: Multi-Database AI Assistant

An enterprise-grade AI Data Agent built using **Google Agent Development Kit (ADK)**, **Gemini 2.5 Flash**, and **Google MCP Toolbox for Databases**. The agent enables users to interact with multiple databases using natural language, automatically routing requests to the appropriate database-specific agent.

---

## Overview

Data Agent is a modular multi-agent system that allows users to query and analyze data stored across heterogeneous databases without writing database-specific queries.

Users can simply ask questions in plain English, and the system:

- Identifies the target database
- Discovers the database schema
- Generates the appropriate query
- Executes the query using MCP Toolbox
- Returns a natural language response

The project is designed to be extensible, allowing additional database connectors to be integrated with minimal changes.

---

## Features

- Natural Language to Database Query
- Multi-Agent Architecture using Google ADK
- Google Gemini 2.5 Flash powered reasoning
- Database-specific specialized agents
- Dynamic schema discovery
- Secure database access through Google MCP Toolbox
- Modular and extensible architecture
- Cloud Run deployment support

---

# Supported Databases

| Database | Type | Status |
|----------|------|--------|
| BigQuery | Data Warehouse | ✅ Integrated |
| MongoDB | NoSQL Document Database | ✅ Integrated |
| PostgreSQL + pgvector | Vector Database | ✅ Integrated |
| Neo4j | Graph Database | ✅ Integrated |
| Cloud SQL (PostgreSQL/MySQL) | Relational Database | 🚧 In Progress |
| Elasticsearch | Search Database | Planned |

---

# Project Architecture

```
                        User
                          │
                          ▼
                Orchestrator Agent
                          │
 ┌──────────────┬───────────────┬──────────────┬──────────────┐
 │              │               │              │              │
 ▼              ▼               ▼              ▼              ▼
BigQuery     MongoDB        pgvector        Neo4j        Future Agents
  Agent        Agent          Agent          Agent
 │              │               │              │
 ▼              ▼               ▼              ▼
MCP           MCP            MCP            MCP
Toolbox      Toolbox        Toolbox        Toolbox
 │              │               │              │
 ▼              ▼               ▼              ▼
Database     Database      Database      Database
```

---

# Current Agent Workflow

Every database agent follows a common workflow:

```
User Query
      │
      ▼
Discover Database
      │
      ▼
Inspect Schema
      │
      ▼
Generate Query
      │
      ▼
Execute Query
      │
      ▼
Explain Results
```

---

# Tech Stack

## AI

- Google Gemini 2.5 Flash
- Google Agent Development Kit (ADK)

## Backend

- Python
- AsyncIO

## Database Connectivity

- Google MCP Toolbox

## Cloud

- Google Cloud Platform
- Cloud Run
- Secret Manager
- Vertex AI

## Databases

- BigQuery
- MongoDB
- PostgreSQL
- pgvector
- Neo4j

---

# Current Folder Structure

```
backend/
│
├── agents/
│   ├── orchestrator_agent.py
│   ├── bigquery_agent.py
│   ├── mongodb_agent.py
│   ├── pgvector_agent.py
│   └── neo4j_agent.py
│
├── toolsets/
│   ├── bigquery_toolset.py
│   ├── mongodb_toolset.py
│   ├── pgvector_toolset.py
│   └── neo4j_toolset.py
│
├── mcp_toolbox/
│
├── mcp_toolbox_pgvector/
│
├── mcp_toolbox_neo4j/
│
├── tools/
│
├── services/
│
├── agent.py
├── main.py
└── requirements.txt
```

---

# Database Agents

## BigQuery Agent

Capabilities

- Dataset discovery
- Table discovery
- Schema inspection
- SQL execution
- Analytical queries

---

## MongoDB Agent

Capabilities

- Collection discovery
- Document inspection
- Aggregation pipelines
- Query execution

---

## pgvector Agent

Capabilities

- List vector tables
- Discover vector columns
- Describe tables
- Similarity search
- Vector database inspection

---

## Neo4j Agent

Capabilities

- Graph schema discovery
- Node labels discovery
- Relationship type discovery
- Graph sampling
- Read-only Cypher execution

---

# MCP Toolbox

Each database is connected using an independent MCP Toolbox deployment.

Current Toolbox Services

```
BigQuery Toolbox
MongoDB Toolbox
pgvector Toolbox
Neo4j Toolbox
```

Each toolbox is deployed independently on Cloud Run.

---

# Cloud Deployment

Cloud Run hosts

- Data Agent
- MongoDB Toolbox
- pgvector Toolbox
- Neo4j Toolbox

Google Secret Manager stores

- Toolbox configuration
- Database credentials
- API keys

---

# Security

- Read-only database operations wherever possible
- Secret Manager integration
- Cloud Run IAM
- Vertex AI authentication
- No credentials stored in source code

---

# Future Roadmap

## Phase 1 (Completed)

- BigQuery Integration
- MongoDB Integration
- pgvector Integration
- Neo4j Integration

---

## Phase 2

- Cloud SQL
- Oracle
- Elasticsearch
- Redis

---

## Phase 3

Universal Database Discovery Layer

```
Discover
    ↓
Inspect
    ↓
Generate Query
    ↓
Execute
    ↓
Explain
```

Every database will implement this common workflow.

---

## Phase 4

Enterprise Features

- Authentication
- User sessions
- Query history
- Result visualization
- Multi-turn conversations
- Cross-database reasoning
- Agent memory
- SQL optimization
- Cost estimation
- Database recommendations

---

# Example Queries

### BigQuery

```
Show total sales by region.
```

### MongoDB

```
List customers who placed more than five orders.
```

### pgvector

```
Find documents similar to this embedding.
```

### Neo4j

```
Show all relationship types.

Describe the graph schema.

Find the shortest path between two nodes.

List all Person nodes connected to Company.
```

---

# Deployment

```bash
gcloud run deploy
```

Deploy each MCP Toolbox separately and connect it to the corresponding database.

---

# Built With

- Google Agent Development Kit (ADK)
- Google Gemini 2.5 Flash
- Google Cloud Platform
- Google MCP Toolbox
- Cloud Run
- Vertex AI
- Python

---

# Author

**Diya Mokal**
