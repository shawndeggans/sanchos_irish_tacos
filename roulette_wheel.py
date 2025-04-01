from pydantic_ai import Agent, RunContext
import os
from dotenv import load_dotenv
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.providers.anthropic import AnthropicProvider

# Load environment variables from .env file
load_dotenv()
# Set the API key for Anthropic
api_key = os.getenv("ANTHROPIC_API_KEY")

model = AnthropicModel(
    'claude-3-5-sonnet-latest', provider=AnthropicProvider(api_key=api_key)
)

roulette_agent = Agent(  
    model,
    deps_type=int,
    result_type=bool,
    system_prompt=(
        'Use the `roulette_wheel` function to see if the '
        'customer has won based on the number they provide.'
    ),
)

@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:  
    """check if the square is a winner"""
    return 'winner' if square == ctx.deps else 'loser'


# Run the agent
success_number = 18  
result = roulette_agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.data)  
#> True

result = roulette_agent.run_sync('I bet five is the winner', deps=success_number)
print(result.data)
#> False