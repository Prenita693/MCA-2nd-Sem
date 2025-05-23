# --------------------------------------------
# McCall’s Quality Model Simulation in Python
# --------------------------------------------

def get_score(question):
    while True:
        try:
            score = int(input(f"{question} (Rate from 1 to 5): "))
            if 1 <= score <= 5:
                return score
            else:
                print("Please enter a score between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter an integer from 1 to 5.")

# Step 1: Define evaluation criteria under each attribute
reliability_questions = [
    "Does the software handle unexpected input gracefully?",
    "Does it recover from crashes or errors automatically?",
    "Is the software available and responsive under load?",
    "Does it produce consistent results every time?",
    "Are bugs rarely encountered during usage?"
]

maintainability_questions = [
    "Is the code modular and easy to modify?",
    "Is the documentation sufficient and updated?",
    "Can new developers understand the code easily?",
    "Are changes easy to implement without breaking existing code?",
    "Is version control and CI/CD integrated?"
]

usability_questions = [
    "Is the user interface intuitive and user-friendly?",
    "Is navigation within the application smooth?",
    "Are error messages clear and helpful?",
    "Can the user perform key tasks with minimal guidance?",
    "Is there proper help and support documentation?"
]

# Step 2: Calculate average scores for each attribute
def evaluate_category(name, questions):
    print(f"\n--- Evaluating {name} ---")
    total = 0
    for q in questions:
        total += get_score(q)
    avg_score = total / len(questions)
    return avg_score

# Step 3: Main evaluation function
def mccall_quality_evaluation():
    print("Welcome to McCall’s Quality Model Evaluation\n")
    print("Please answer the following questions to evaluate the software.\n")

    reliability_score = evaluate_category("Reliability", reliability_questions)
    maintainability_score = evaluate_category("Maintainability", maintainability_questions)
    usability_score = evaluate_category("Usability", usability_questions)

    # Step 4: Summary Report
    print("\n--- Quality Assessment Summary ---")
    print(f"Reliability Score: {reliability_score:.2f} / 5")
    print(f"Maintainability Score: {maintainability_score:.2f} / 5")
    print(f"Usability Score: {usability_score:.2f} / 5")

    overall = (reliability_score + maintainability_score + usability_score) / 3
    print(f"\nOverall Quality Score: {overall:.2f} / 5")

    # Step 5: Interpretation
    if overall >= 4:
        level = "Excellent"
    elif overall >= 3:
        level = "Good"
    elif overall >= 2:
        level = "Fair"
    else:
        level = "Poor"

    print(f"Quality Level: {level}")

# Step 6: Run program
if __name__ == "__main__":
    mccall_quality_evaluation() 
