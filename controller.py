import re
from agents.architect import Architect
from agents.engineer import Engineer
from agents.critic import Critic
from agents.test_runner import TestRunner
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

    # Step 1: Architect creates the plan
    plan = architect.send(user_request)
    print("\n--- Architect Plan ---")
    print(plan)

    # Step 2: Engineer writes code based on the plan
    code_output = engineer.send(plan)
    print("\n--- Engineer Output ---")
    print(code_output)

    # Write all files produced by the Engineer
    files = extract_files_from_output(code_output)
    for filename, code in files:
        print(write_file(filename, code))

    # Step 3: Run tests with pytest
    print("\n--- Test Runner Output ---")
    test_output = test_runner.run_tests()
    print(test_output)

    # Step 4: Critic reviews code + test results
    review = critic.send(code_output + "\n\nTest Output:\n" + test_output)
    print("\n--- Critic Review ---")
    print(review)

    # Loop until Critic approves AND tests pass
    while "Looks good" not in review or "All tests passed" not in test_output:
        code_output = engineer.send(review)
        print("\n--- Engineer Revision ---")
        print(code_output)

        # Write updated files
        files = extract_files_from_output(code_output)
        for filename, code in files:
            print(write_file(filename, code))

        # Run tests again
        print("\n--- Test Runner Output ---")
        test_output = test_runner.run_tests()
        print(test_output)

        # Critic reviews again
        review = critic.send(code_output + "\n\nTest Output:\n" + test_output)
        print("\n--- Critic Review ---")
        print(review)

    print("\n🎉 All agents agree. Code generation complete.")

if __name__ == "__main__":
    main()