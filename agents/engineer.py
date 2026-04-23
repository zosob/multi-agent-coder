from .base_agent import BaseAgent

engineer_prompt = """
You are the Engineer. You write code for each file in the plan.
When you output code, wrap it in triple backticks with the filename.
If tests fail or the Critic finds issues, revise the code and try again.
"""

class Engineer(BaseAgent):
    def __init__(self):
        super().__init__("Engineer", engineer_prompt)