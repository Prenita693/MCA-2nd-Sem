# --------------------------------------------
# WHITE BOX TESTING + MCCABE'S CYCLOMATIC COMPLEXITY
# --------------------------------------------

# Step 1: Define the original simple function
def sample_function(x):
    if x > 0:
        print("Positive number")
    elif x < 0:
        print("Negative number")
    else:
        print("Zero")

# Step 2: Define the modified version with more control flow
def sample_function_modified(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                print(i, "is even")
            else:
                print(i, "is odd")
    elif x < 0:
        print("Negative number")
    else:
        print("Zero")

# Step 3: Function to calculate Cyclomatic Complexity
def calculate_cyclomatic_complexity(function_code):
    """
    Cyclomatic Complexity (CC) = D + 1
    where D = Number of decisions (if, elif, for, while, etc.)
    """
    decision_keywords = ['if', 'elif', 'for', 'while', 'case', 'except']  # Decision-making constructs
    lines = function_code.split('\n')

    decisions = 0

    for line in lines:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue  # Skip empty lines and comments
        for keyword in decision_keywords:
            if line.startswith(keyword):
                decisions += 1

    complexity = decisions + 1  # McCabe’s simpler formula
    return complexity

# Step 4: Function to display simple control flow diagram
def display_control_flow_diagram_simple():
    print("\nSimple Control Flow Diagram for 'sample_function':\n")
    print("        [Start]")
    print("           |")
    print("        [Check x > 0]")
    print("         /     \\")
    print("    Yes /       \\ No")
    print("     [Print Positive]   [Check x < 0]")
    print("                         /     \\")
    print("                    Yes /       \\ No")
    print("                  [Print Negative] [Print Zero]")
    print("                         \\     /")
    print("                          [End]")

# Step 5: Control flow demonstration function
def control_flow_demo(x):
    print("\nControl Flow Execution for input:", x)
    print("Start")
    if x > 0:
        print("Decision: x > 0 → True path")
    elif x < 0:
        print("Decision: x < 0 → True path")
    else:
        print("Else path (Zero)")
    print("End")

# Step 6: Importing inspect to fetch function source code
import inspect

# Analyze original function
print("---- Analyzing Original 'sample_function' ----")
function_source = inspect.getsource(sample_function)
complexity = calculate_cyclomatic_complexity(function_source)
print("Cyclomatic Complexity of 'sample_function' is:", complexity)
control_flow_demo(5)
control_flow_demo(-3)
control_flow_demo(0)
display_control_flow_diagram_simple()

# Analyze modified function
print("\n---- Analyzing Modified 'sample_function_modified' ----")
function_source_modified = inspect.getsource(sample_function_modified)
complexity_modified = calculate_cyclomatic_complexity(function_source_modified)
print("Cyclomatic Complexity of 'sample_function_modified' is:", complexity_modified)
]
