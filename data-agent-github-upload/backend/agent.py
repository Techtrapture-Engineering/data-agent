import os

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
os.environ["GOOGLE_CLOUD_PROJECT"] = "tt-labs-001"
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"

os.environ.pop("GOOGLE_API_KEY", None)
os.environ.pop("GOOGLE_AI_API_KEY", None)

from google.adk.agents import LlmAgent

from .agents.orchestrator_agent import orchestrator_agent

root_agent = LlmAgent(
    name="data_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are an enterprise data platform assistant.

    If the user sends a greeting such as:
    hi, hello, hey, good morning, good evening

    Reply directly with a short greeting and ask what database task they need help with.
    Do not delegate greetings to any sub-agent.

    For all database-related requests:
    delegate to orchestrator_agent.

    Never call database tools for casual greetings.
    """,
    sub_agents=[
        orchestrator_agent
    ]
)