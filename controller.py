from agents.architect import Architect
from agents.engineer import Engineer
from agents.critic import Critic
from tools import write_file, read_file, run_python

def main():
    print("Multi-Agent Coder")
    print("------------------")
    user_request = input("What would you like to build? ")

    architect = Architect()
    engineer = Engineer()
    critic = Critic()

    # Step 1: Architect creates the plan
    plan = architect.send(user_request)
    print("\n--- Architect Plan ---")
    print(plan)

    # Step 2: Engineer writes code based on the plan
    code_output = engineer.send(plan)
    print("\n--- Engineer Output ---")
    print(code_output)

    # Step 3: Critic reviews the code
    review = critic.send(code_output)
    print("\n--- Critic Review ---")
    print(review)

    # Loop until Critic approves
    while "Looks good" not in review:
        code_output = engineer.send(review)
        print("\n--- Engineer Revision ---")
        print(code_output)

        review = critic.send(code_output)
        print("\n--- Critic Review ---")
        print(review)

    print("\n🎉 All agents agree. Code generation complete.")

if __name__ == "__main__":
    main()