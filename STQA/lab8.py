# --------------------------------------------
# Software Defect Manager with Severity Categories
# --------------------------------------------

# Step 1: Dictionary to store categorized defects
defects = {
    "Critical": [],
    "Major": [],
    "Minor": []
}

# Step 2: Function to add a defect
def add_defect():
    title = input("Enter defect title: ").strip()
    description = input("Enter defect description: ").strip()
    severity = input("Enter severity (Critical/Major/Minor): ").capitalize()

    if severity not in defects:
        print("Invalid severity. Please choose Critical, Major, or Minor.")
        return

    defect = (title, description)  # Tuple used for immutability
    defects[severity].append(defect)
    print(f"✅ Defect added to '{severity}' category.")

# Step 3: Function to display all defects
def view_defects():
    print("\n--- All Defects Categorized by Severity ---")
    for severity, defect_list in defects.items():
        print(f"\n{severity} Defects:")
        if defect_list:
            for i, (title, description) in enumerate(defect_list, start=1):
                print(f" {i}. Title: {title} | Description: {description}")
        else:
            print(" None")

# Step 4: Function to count and summarize defects
def defect_summary():
    print("\n--- Defect Summary Report ---")
    total = 0
    for severity, defect_list in defects.items():
        count = len(defect_list)
        total += count
        print(f"{severity}: {count} defects")
    print(f"Total Defects: {total}")

# Step 5: Menu interface
def main():
    while True:
        print("\n--- Software Defect Manager ---")
        print("1. Add Defect")
        print("2. View All Defects")
        print("3. Show Defect Summary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_defect()
        elif choice == '2':
            view_defects()
        elif choice == '3':
            defect_summary()
        elif choice == '4':
            print("Exiting Defect Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select from 1 to 4.")

# Step 6: Run the program
if __name__ == "__main__":
    main() 
