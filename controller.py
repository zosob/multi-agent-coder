import re
import json
from agents.architect import Architect
from agents.engineer import Engineer
from agents.critic import Critic
from agents.test_runner import TestRunner
from agents.refactorer import Refactorer
from memory_manager import MemoryManager
from agents.planner import Planner


from tools import write_file

def extract_files_from_output(output):
    """Extract ```filename\ncode``` blocks from LLM output."""
    pattern = r"```(.*?)\n(.*?)```"
    matches = re.findall(pattern, output, re.DOTALL)
    return [(filename.strip(), code) for filename, code in matches]

def main():
    print("Multi-Agent Coder")
    print("------------------")
    user_request = input("What would you like to build? ")

    architect = Architect()
    engineer = Engineer()
    critic = Critic()
    test_runner = TestRunner()
    refactorer = Refactorer()
    memory = MemoryManager()
    planner = Planner()

    # Initial state
    state = {
        "user_request": user_request,
        "project_memory": memory.get_project(),
        "loop_memory": memory.get_loop(),
        "architect_memory": memory.get_agent("Architect"),
        "engineer_memory": memory.get_agent("Engineer"),
        "critic_memory": memory.get_agent("Critic"),
        "refactorer_memory": memory.get_agent("Refactorer"),
    }

    # Main planner driven loop
    while True:
        planner_input = json.dumps(state, indent=2)
        planner_output = planner.send(planner_input, memory.get_agent("Planner"))
        
        try:
            decision = json.loads(planner_output)
        except json.JSONDecodeError:
            print("\n⚠ Planner returned invalid JSON. Retrying...\n")
            continue
        
        next_agent = decision.get("next_agent")
        message = decision.get("message", "")
        reason = decision.get("reason", "")
        
        print(f"\n🤖 Planner Decision: {next_agent}")
        print(f"Reason: {reason}\n")
        
        # Stop Condition
        if next_agent == "Stop":
            print("\n🎉 Planner decided the project is complete.")
            break
        
        # Step 1: Architect creates the plan
        if next_agent == "Architect":
            plan = architect.send(message, memory.get_agent("Architect"))
            memory.update_agent("Architect", "last_plan", plan)
            print("\n--- Architect Plan ---")
            print(plan)

        # Step 2: Engineer writes code based on the plan
        if next_agent == "Engineer":
            code_output = engineer.send(message, memory.get_agent("Engineer"))
            memory.update_agent("Engineer", "last_code_output", code_output)
            print("\n--- Engineer Output ---")
            print(code_output)

            # Write all files produced by the Engineer
            files = extract_files_from_output(code_output)
            for filename, code in files:
                print(write_file(filename, code))
            memory.update_project("files", [f for f, _ in files])
            
            state["engineer_memory"] = memory.get_agent("Engineer")
            state["project_memory"] = memory.get_project()
            continue

        if next_agent == "TestRunner":    # Step 3: Run tests with pytest
            print("\n--- Test Runner Output ---")
            test_output = test_runner.run_tests()
            memory.update_loop("last_test_output", test_output)
            print(test_output)
            
            state["loop_memory"] = memory.get_loop()
            continue

        # Step 4: Critic reviews code + test results
        if next_agent == "Critic":
            review = critic.send(message, memory.get_agent("Critic"))
            memory.update_agent("Critic", "last_review", review)
            memory.update_loop("last_review", review)
            print("\n--- Critic Review ---")
            print(review)
            
            state["critic_memory"] = memory.get_agent("Critic")
            state["loop_memory"] = memory.get_loop()
            continue
        
        # Step 5: Refactorer improves code quality
        if next_agent == "Refactorer":
            refactor_output = refactorer.send(message, memory.get_agent("Refactorer"))
            memory.update_agent("Refactorer", "last_refactor", refactor_output)
            print("\n--- Refactorer Output ---")
            print(refactor_output)

            # Write refactored files
            files = extract_files_from_output(refactor_output)
            for filename, code in files:
                print(write_file(filename, code))
                
            state["refactorer_memory"] = memory.get_agent("Refactorer")
            continue

    # # Loop until Critic approves AND tests pass
    # while "Looks good" not in review or "All tests passed" not in test_output:
    #     code_output = engineer.send(review, memory.get_agent("Engineer"))
    #     memory.update_agent("Engineer", "last_code_output", code_output)
    #     print("\n--- Engineer Revision ---")
    #     print(code_output)

    #     # Write updated files
    #     files = extract_files_from_output(code_output)
    #     for filename, code in files:
    #         print(write_file(filename, code))
    #     memory.update_project("files", [f for f, _ in files])
        
    #     # Run tests again
    #     print("\n--- Test Runner Output ---")
    #     test_output = test_runner.run_tests()
    #     memory.update_loop("last_test_output", test_output)
    #     print(test_output)

    #     # Critic reviews again
    #     review = critic.send(code_output + "\n\nTest Output:\n" + test_output, memory.get_agent("Critic"))
    #     memory.update_agent("Critic", "last_review", review)
    #     memory.update_loop("last_review", review)
    #     print("\n--- Critic Review ---")
    #     print(review)

    # print("\n✔ All tests passed and Critic approved.")
    # print("→ Beginning refactoring pass...")

    

    # Step 6: Ensure refactoring didn't break anything
    # print("\n--- Test Runner Output (Post-Refactor) ---")
    # test_output = test_runner.run_tests()
    # print(test_output)

    # if "All tests passed" in test_output:
    #     print("\n🎉 Final result: Clean, correct, production-quality code.")
    # else:
    #     print("\n⚠ Refactoring introduced issues. Returning to Engineer loop.")
    print("\n🎉 Final result: Clean, correct, production-quality code.")
    
if __name__ == "__main__":
    main()