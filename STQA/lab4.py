# Step 1: Define the function to be tested
def add_numbers(a, b):
    return a + b

# Step 2: Read test cases from a file
def read_test_cases(filename):
    test_cases = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove any inline comments
            line = line.split('#')[0].strip()
            if line:  # Ensure it's not an empty line after stripping
                parts = line.split(',')
                input1 = int(parts[0].strip())
                input2 = int(parts[1].strip())
                expected_output = int(parts[2].strip())
                test_cases.append((input1, input2, expected_output))
    return test_cases


# Step 3: Execute tests and log results
def execute_tests_and_log(test_cases, result_file_path):
    with open(result_file_path, 'w') as result_file:
        for index, (input1, input2, expected) in enumerate(test_cases):
            actual = add_numbers(input1, input2)
            if actual == expected:
                result = "PASS"
            else:
                result = "FAIL"
            # Log format: Test Case ID, Inputs, Expected, Actual, Result
            result_file.write(f"Test Case {index+1}: Inputs=({input1},{input2}), Expected={expected}, Actual={actual} --> {result}\n")

    print(f"Testing complete. Results saved in '{result_file_path}'.")

# Step 4: Main Execution
if __name__ == "__main__":
    test_case_file = "test_cases.txt"
    result_file = "test_results.txt"

    # Read test cases
    test_cases = read_test_cases(test_case_file)

    # Execute tests and log results
    execute_tests_and_log(test_cases, result_file)
