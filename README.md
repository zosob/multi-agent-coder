# 🧠 Multi-Agent Coder (From Scratch)

> A minimal, fully transparent **agentic AI system** built in pure Python — no frameworks, no abstractions.

This project demonstrates how multiple specialized agents can **plan, write, review, and refine code collaboratively** using simple tools and a shared workspace.

Designed for **learning, teaching, and experimentation** with real agentic patterns.

---

## 🚀 Features

### 🧩 Architect Agent
- Breaks down user requests into:
  - File structure
  - Modules
  - Step-by-step engineering plan

### 🛠️ Engineer Agent
- Writes and updates code
- Saves files to disk
- Executes Python scripts
- Fixes errors based on feedback

### 🔍 Critic Agent
- Reviews generated code
- Checks correctness
- Suggests improvements
- Ensures consistency

---

## 🔄 Agent Workflow
Architect → Engineer → Critic → Engineer → Critic → … → Done

This loop is the **core pattern behind modern agentic systems**.

---

## 📁 Project Structure

```bash
multi-agent-coder/
│
├── agents/
│   ├── base_agent.py      # Core agent class
│   ├── architect.py       # Planning agent
│   ├── engineer.py        # Code-writing agent
│   └── critic.py          # Review agent
│
├── workspace/             # Generated code output
│
├── tools.py               # File I/O + Python execution tools
├── controller.py          # Orchestration loop
└── README.md
```
## ⚙️ How It Works

Each agent is a lightweight wrapper around an LLM with:

- A system prompt  
- Message history  
- A `send()` method for communication  

### 🧰 Built-in Tools

- 📄 File read/write  
- ▶️ Python execution  

Everything is intentionally **simple and transparent**, making it easy to understand and extend.

## 📜 License
This project is licensed under the MIT License.

## ⭐ Contributing
If you want to experiment or extend this system:
- Fork the repo
- Add your agent or tool
- Open a PR


