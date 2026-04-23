import openai

class BaseAgent:
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt
        self.messages = [{"role": "system", "content": system_prompt}]

    def send(self, message):
        self.messages.append({"role": "user", "content": message})

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages
        )

        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply