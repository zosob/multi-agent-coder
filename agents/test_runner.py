from .base_agent import BaseAgent
from tools import run_python

test_runner_prompt = """
You are the Test Runner. Your job is to:
1. Run the user's Python project.
2. Capture stdout and stderr.
3. Report failures clearly.
4. If everything passes, say: 'All tests passed.'
"""

class TestRunner(BaseAgent):
    def __init__(self):
        super().__init__("TestRunner", test_runner_prompt)

    def run(self, path):
        """Execute a Python file inside workspace and return output."""
        result = run_python(path)
        return result