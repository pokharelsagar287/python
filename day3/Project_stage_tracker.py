stages = [
    {"name": "Excavation", "completed": False},
    {"name": "Foundation", "completed": True},
]

#function to add a new stage
def add_stage(stages):
    stage = input(f"Enter the name of the new stage:")
    stages.append({"name": stage, "completed": False})
    print(f"Stage '{stage}' added successfully.")

#function to mark a stage as completed
def mark_stage_completed(stages, stage_name):
    if not stages:
        print("No stages available to mark as completed.")
        return
    print("Available stages:")
    for i, stage in enumerate(stages):
        status = "Completed" if stage["completed"] else "Not Completed"
        print(f"{i + 1}. {stage['name']} - {status}")

    try:
        choice = int(input(f"Enter the number of the stage to mark as completed (1-{len(stages)}): "))
        if 1 <= choice <= len(stages):
            stages[choice - 1]["completed"] = True
            print(f"Stage '{stages[choice - 1]['name']}' marked as completed.")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#function to display all stages
def display_stages(stages):
    if not stages:
        print("No stages available.")
        return
    completed = sum(stage["completed"] for stage in stages)
    total = len(stages)
    print(f"\nTotal Stages: {total}, Completed: {completed}")
    for i, stage in enumerate(stages):
        status = "Completed" if stage["completed"] else "Not Completed"
        print(f"{i + 1}. {stage['name']} - {status}")


def main():
    while True:
        print("\nProject Stage Tracker")
        print("1. Add Stage")
        print("2. Mark Stage as Completed")
        print("3. Display Stages")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_stage(stages)
        elif choice == '2':
            mark_stage_completed(stages, "Mark Completed")
        elif choice == '3':
            display_stages(stages)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


