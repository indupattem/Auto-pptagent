import asyncio
from agent.agent_ppt import run_ppt_agent

if __name__ == "__main__":
    user_input = input("Enter topic: ")
    asyncio.run(run_ppt_agent(user_input))