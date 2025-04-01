import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider

# Load environment variables from .env file
load_dotenv()
# Set the API key for Anthropic
api_key = os.getenv("ANTHROPIC_API_KEY")

model = AnthropicModel(
    'claude-3-5-sonnet-latest', provider=AnthropicProvider(api_key=api_key)
)
agent = Agent(model)
