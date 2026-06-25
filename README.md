# Data Agent

A multi-database AI-powered data assistant built with Google ADK and MCP (Model Context Protocol) that allows users to query databases using natural language.

## Overview

Data Agent enables users to interact with multiple databases such as BigQuery, Cloud SQL, Oracle, PostgreSQL, and MySQL without writing SQL manually. The system converts plain English questions into SQL queries, executes them securely, and returns structured insights and statistics.

This project is designed to simplify data analysis by providing a unified AI interface for different database systems.

## Features

* Natural language to SQL conversion
* Multi-database support
* Schema discovery and table exploration
* Analytical query execution
* Database connector management using MCP Toolbox
* Modular agent architecture using Google ADK
* Extensible support for additional databases
* Dockerized deployment support

## Supported Databases

* BigQuery
* Cloud SQL (MySQL)
* PostgreSQL
* Oracle
* MySQL

## Project Architecture

```text
User Query
   ↓
Root Agent
   ↓
--------------------------------
|                              |
Schema Agent              Query Agent
|                              |
Schema Tools              Query Tools
|                              |
MCP Toolbox / Database Connectors
|                              |
Connected Databases
```

## Tech Stack

* Python
* Google ADK
* Vertex AI (Gemini 2.5 Flash)
* MCP Toolbox
* BigQuery MCP Server
* Cloud SQL MCP Server
* FastAPI
* Docker

## Project Structure

```text
backend/
├── agents/
├── services/
├── tools/
├── toolsets/
├── mcp_toolbox/
├── agent.py
├── config.py
├── connection_manager.py
├── main.py
├── requirements.txt
Dockerfile
PROJECT_STATUS.md
```

## Working

### 1. User asks a question

Example:

"Show total sales by month"

### 2. Root Agent routes the request

The root agent decides whether the question is:

* Schema-related → Schema Agent
* Analytical → Query Agent

### 3. Query generation

The selected agent uses database schema context and Gemini to generate SQL.

### 4. SQL execution

SQL is executed through MCP connectors.

### 5. Results returned

The agent summarizes the results and provides insights.

## Setup

### Clone repository

```bash
git clone https://github.com/your-username/data-agent.git
cd data-agent
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r backend/requirements.txt
```

## Environment Variables

Create `.env` inside backend:

```env
PROJECT_ID=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=path-to-service-account.json
MODEL=gemini-2.5-flash
```

## Run the project

```bash
python backend/main.py
```

## Current Progress

✅ BigQuery MCP integration completed
✅ Schema Agent completed
✅ Query Agent completed
✅ Root Agent routing completed
⏳ Cloud SQL integration in progress
⏳ Oracle/PostgreSQL connectors pending
⏳ Frontend integration pending

## Future Scope

* Add authentication layer
* Query history tracking
* Visualization dashboard
* Export results as CSV/PDF
* Role-based database access
* Support for more enterprise databases

## Use Cases

* Business analytics
* Sales reporting
* Data exploration
* Schema understanding
* Cross-database querying
* Automated reporting

## Author

Diya

## License

MIT License
