import subprocess
from .base_agent import BaseAgent

test_runner_prompt = """
You are the Test Runner.

Your job:
1. Run pytest on the entire workspace directory.
2. Capture stdout and stderr.
3. Report failures clearly.
4. If everything passes, ensure the text 'All tests passed.' appears in your final output.

You do not invent results; you only report what pytest actually outputs.
"""

class TestRunner(BaseAgent):
    def __init__(self):
        super().__init__("TestRunner", test_runner_prompt)

    def run_tests(self):
        """Run pytest inside the workspace directory."""
        try:
            result = subprocess.run(
                ["pytest", "-q"],
                cwd="workspace",
                capture_output=True,
                text=True,
                timeout=30
            )
            output = (result.stdout or "") + (result.stderr or "")
            if result.returncode == 0:
                # Ensure a clear success marker for the controller loop
                if "All tests passed." not in output:
                    output = (output + "\nAll tests passed.").strip()
            return output.strip() or "All tests passed."
        except Exception as e:
            return f"Error running tests: {e}"