Multi‑Agent Coder (from scratch)
A minimal, fully transparent agentic AI system built in pure Python — no frameworks, no abstractions, just the real mechanics of how agents plan, write, review, and refine code together.
This project demonstrates how to build a multi‑agent architecture where each agent has a role, communicates with others, uses tools, and iterates toward a shared goal. It’s designed for learning, experimentation, and extending into more advanced agentic systems.

What this project does
This system uses three collaborating agents:
1. Architect
Breaks a user request into:
- a file structure
- modules
- a step‑by‑step engineering plan
2. Engineer
- writes code
- saves files
- runs Python scripts
- fixes errors based on feedback
3. Critic
- reviews code
- checks correctness
- suggests improvements
- ensures consistency
The controller orchestrates the loop:
Architect → Engineer → Critic → Engineer → Critic → … → Done


This is a foundational pattern in modern agentic AI systems.

Project Structure
multi-agent-coder/
│
├── agents/
│   ├── base_agent.py      # Core agent class
│   ├── architect.py       # Planning agent
│   ├── engineer.py        # Code‑writing agent
│   └── critic.py          # Review agent
│
├── workspace/             # Where generated code is written
│
├── tools.py               # File I/O + Python execution tools
├── controller.py          # Multi‑agent orchestration loop
└── README.md              # Project documentation



How it works
Each agent is a lightweight wrapper around an LLM with:
- a system prompt
- message history
- a send() method for communication
The system uses simple Python tools to:
- write files
- read files
- execute Python code
This keeps the entire system transparent and easy to extend.

Run the system
Make sure Python 3 is installed.
Install dependencies:
pip install openai


Run the controller:
python3 controller.py


The agents will collaborate to build whatever project is requested, such as:
“Build a CLI todo app with JSON storage.”

Generated files will appear in the workspace/ folder.

Why this project exists

Most agent frameworks hide the real mechanics behind layers of abstractions.
This project does the opposite:
- exposes the agent loop
- exposes tool calling
- exposes message passing
- exposes the orchestration logic
It’s ideal for:
- learning agentic AI
- teaching agent systems
- experimenting with new agent roles
- extending into autonomous planners, memory, or multi‑tool workflows

Future direction to extend the system: 

Add new agents easily:
- TestRunner
- Refactorer
- Documentation Writer
- Performance Optimizer
- Planner (autonomous orchestration)
- Memory module
Or integrate:
- local models (Ollama)
- vector memory
- web search tools
- API‑calling tools


MIT License
Copyright (c) 2026 Bhaskar

