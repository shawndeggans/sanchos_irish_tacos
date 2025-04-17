import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
# logfire.configure(send_to_logfire='if-token-present')


class MyModel(BaseModel):
    city: str
    country: str

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

model = AnthropicModel(
    'claude-3-5-sonnet-latest', provider=AnthropicProvider(api_key=api_key)
)

print(f'Using model: {model}')
agent = Agent(model, result_type=MyModel, instrument=True)

if __name__ == '__main__':
    result = agent.run_sync('The windy city in the US of A.')
    print(result.data)
    print(result.usage())