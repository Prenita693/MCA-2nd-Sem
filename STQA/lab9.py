# --------------------------------------------
# Software Configuration Management System
# --------------------------------------------

import datetime

# Step 1: Dictionary to track current versions
version_registry = {}

# Step 2: File to log version history
LOG_FILE = "version_log.txt"

# Step 3: Add or update software version
def add_version():
    software = input("Enter software/module name: ").strip()
    version = input("Enter new version (e.g., v1.2.0): ").strip()
    description = input("Enter description of update/modification: ").strip()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update in-memory registry
    version_registry[software] = version

    # Append to log file
    with open(LOG_FILE, 'a') as log:
        log.write(f"{timestamp} | {software} updated to {version} | {description}\n")

    print(f"✅ Version for '{software}' updated to '{version}' and logged.")

# Step 4: View current version status
def view_versions():
    if not version_registry:
        print("No versions tracked yet.")
    else:
        print("\n--- Current Software Versions ---")
        for software, version in version_registry.items():
            print(f"{software}: {version}")

# Step 5: Show version history log
def view_log():
    print("\n--- Version History Log ---")
    try:
        with open(LOG_FILE, 'r') as log:
            content = log.read()
            print(content if content else "Log is empty.")
    except FileNotFoundError:
        print("No log file found yet.")

# Step 6: Main menu-driven interface
def main():
    while True:
        print("\n--- Configuration Management Menu ---")
        print("1. Add/Update Software Version")
        print("2. View Current Versions")
        print("3. View Version History Log")
        print("4. Exit")
        choice = input("Enter your choice (1–4): ").strip()

        if choice == '1':
            add_version()
        elif choice == '2':
            view_versions()
        elif choice == '3':
            view_log()
        elif choice == '4':
            print("Exiting Configuration Management System. Goodbye!")
            break
        else:
            print("Invalid input. Please choose between 1 and 4.")

# Step 7: Run the program
if __name__ == "__main__":
    main()
