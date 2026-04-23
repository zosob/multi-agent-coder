import os
import subprocess

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def run_python(path):
    try:
        result = subprocess.run(
            ["python3", path],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)