import json
import os

class MemoryManager:
    def __init__(self, path="workspace/memory.json"):
        self.path = path
        self.memory = {
            "project": {},
            "agents": {},
            "loop": {}
        }
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                self.memory = json.load(f)

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=2)

    def update_project(self, key, value):
        self.memory["project"][key] = value
        self.save()

    def update_agent(self, agent_name, key, value):
        if agent_name not in self.memory["agents"]:
            self.memory["agents"][agent_name] = {}
        self.memory["agents"][agent_name][key] = value
        self.save()

    def update_loop(self, key, value):
        self.memory["loop"][key] = value
        self.save()

    def get_project(self):
        return self.memory["project"]

    def get_agent(self, agent_name):
        return self.memory["agents"].get(agent_name, {})

    def get_loop(self):
        return self.memory["loop"]