import os
import subprocess

def write_file(path, content):
    """Write content to a file inside the workspace directory."""
    full_path = os.path.join("workspace", path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    return f"[File written] {full_path}"

def read_file(path):
    """Read a file from the workspace directory."""
    full_path = os.path.join("workspace", path)
    with open(full_path, "r") as f:
        return f.read()

def run_python(path):
    """Execute a Python file inside the workspace directory."""
    full_path = os.path.join("workspace", path)
    try:
        result = subprocess.run(
            ["python3", full_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)