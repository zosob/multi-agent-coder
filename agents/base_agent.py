import openai
import json
import subprocess

class BaseAgent:
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt
        self.messages = [{"role": "system", "content": system_prompt}]

    # Load config.json
        with open("config.json", "r") as f:
            config = json.load(f)
            
        agent_cfg = config["agents"].get(name, {})
        self.backend = agent_cfg.get("backend", config["default_backend"])
        self.model = agent_cfg.get("model", config["default_model"])
        self.temperature = agent_cfg.get("temperature", 0.2)
        self.max_tokens = agent_cfg.get("max_tokens", 2000)
    
    def _send_openai(self, messages):
        """Send request to OpenAI backend."""
        response = openai.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        return response.choices[0].message.content
    
    def _send_ollama(self, messages):
        """Send request to Ollama backend."""
        prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])

        result = subprocess.run(
            ["ollama", "run", self.model],
            input=prompt,
            text=True,
            capture_output=True
        )

        return result.stdout.strip()
    
        
    def send(self, user_message, memory=None):
        """Unified send method for OpenAI + Ollama."""
        if memory:
            self.messages.append({"role": "system", "content": f"Memory:\n{memory}"})

        self.messages.append({"role": "user", "content": user_message})

        # Route to correct backend
        if self.backend == "openai":
            reply = self._send_openai(self.messages)
        elif self.backend == "ollama":
            reply = self._send_ollama(self.messages)
        else:
            raise ValueError(f"Unknown backend: {self.backend}")
        
        self.messages.append({"role": "assistant", "content": reply})
        return reply