from .base_agent import BaseAgent

architect_prompt = """
You are the Architect. Your job is to break the user's request into:
1. A file structure
2. A list of modules
3. A step-by-step plan for the Engineer

Output ONLY the plan.
"""

class Architect(BaseAgent):
    def __init__(self):
        super().__init__("Architect", architect_prompt)