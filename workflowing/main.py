from tools.taskbar import create_taskbar, add_workflow, delete_workflow
from tools.workflow import workflow as Workflow  # Ensure correct capitalization
from tools.subtask import Subtask
# Github Copilot was used to help with the code in this file.
taskbar = create_taskbar()
exit_program = False  # Corrected loop condition variable
tabbed_taskbar = 1
current_work = None
print("Welcome to the Workflowing Taskbar!")
while not exit_program:  # Fixed loop condition
    if tabbed_taskbar == 2:
        # Workflow management menu
        print(f"\nManaging Workflow: {current_work.name}")
        print("1. Create a new subtask")
        print("2. Delete a subtask")
        print("3. Enter a subtask")
        print("4. View workflow details")
        print("5. Back to taskbar")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Create a new subtask
            name = input("Enter the name of the subtask: ")
            description = input("Enter the description of the subtask: ")
            status = input("Enter the status of the subtask: ")
            end_date = input("Enter the end date of the subtask: ")
            new_subtask = Subtask(name, description, status, end_date, current_work)
            current_work.add_subtask(new_subtask)
            print(f"Subtask '{name}' created successfully!")

        elif choice == "2":
            # Delete a subtask
            if not current_work.get_subtasks():
                print("No subtasks available to delete.")
            else:
                print("Current subtasks:")
                for i, subtask in enumerate(current_work.get_subtasks(), start=1):
                    print(f"{i}. {subtask.name}")
                try:
                    delete_index = int(input("Enter the number of the subtask to delete: ")) - 1
                    if 0 <= delete_index < len(current_work.get_subtasks()):
                        deleted_subtask = current_work.get_subtasks()[delete_index].name
                        current_work.remove_subtask(deleted_subtask)
                        print(f"Subtask '{deleted_subtask}' deleted successfully!")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == "3":
            # Enter a subtask
            if not current_work.get_subtasks():
                print("No subtasks available to enter.")
            else:
                print("Current subtasks:")
                for i, subtask in enumerate(current_work.get_subtasks(), start=1):
                    print(f"{i}. {subtask.name}")
                try:
                    enter_index = int(input("Enter the number of the subtask to enter: ")) - 1
                    if 0 <= enter_index < len(current_work.get_subtasks()):
                        selected_subtask = current_work.get_subtasks()[enter_index]
                        print(f"Entering subtask: {selected_subtask.name}")
                        print(selected_subtask)  # Display subtask details
                        tabbed_taskbar = 3
                        current_work = selected_subtask
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == "4":
            # View workflow details
            print(f"\nWorkflow Details:")
            print(f"Name: {current_work.name}")
            print(f"Description: {current_work.description}")
            print(f"Status: {current_work.status}")
            print(f"End Date: {current_work.end_date}")
            print(f"Subtasks: {[subtask.name for subtask in current_work.get_subtasks()]}")

        elif choice == "5":
            # Back to taskbar
            current_work = None
            tabbed_taskbar = 1
            print("Returning to the taskbar.")

        elif choice == "6":
            # Exit the program
            exit_program = True
            print("Exiting the program. Goodbye!")

        else:
            print("Invalid choice. Please try again.")
    elif tabbed_taskbar == 3:
        print(f"\nManaging Subtask: {current_work.name}")
        print("1. Create a new subtask")
        print("2. Delete a subtask")
        print("3. Enter a subtask")
        print("4. View subtask details")
        print("5. Back")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Create a new subtask
            name = input("Enter the name of the subtask: ")
            description = input("Enter the description of the subtask: ")
            status = input("Enter the status of the subtask: ")
            end_date = input("Enter the end date of the subtask: ")
            new_subtask = Subtask(name, description, status, end_date, current_work)
            current_work.add_subtask(new_subtask)
            print(f"Subtask '{name}' created successfully!")

        elif choice == "2":
            # Delete a subtask
            if not current_work.get_subtasks():
                print("No subtasks available to delete.")
            else:
                print("Current subtasks:")
                for i, subtask in enumerate(current_work.get_subtasks(), start=1):
                    print(f"{i}. {subtask.name}")
                try:
                    delete_index = int(input("Enter the number of the subtask to delete: ")) - 1
                    if 0 <= delete_index < len(current_work.get_subtasks()):
                        deleted_subtask = current_work.get_subtasks()[delete_index].name
                        current_work.remove_subtask(deleted_subtask)
                        print(f"Subtask '{deleted_subtask}' deleted successfully!")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == "3":
            # Enter a subtask
            if not current_work.get_subtasks():
                print("No subtasks available to enter.")
            else:
                print("Current subtasks:")
                for i, subtask in enumerate(current_work.get_subtasks(), start=1):
                    print(f"{i}. {subtask.name}")
                try:
                    enter_index = int(input("Enter the number of the subtask to enter: ")) - 1
                    if 0 <= enter_index < len(current_work.get_subtasks()):
                        selected_subtask = current_work.get_subtasks()[enter_index]
                        print(f"Entering subtask: {selected_subtask.name}")
                        print(selected_subtask)  # Display subtask details
                        tabbed_taskbar = 3
                        current_work = selected_subtask
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == "4":
            # View subtask details
            print(f"\nSubtask Details:")
            print(f"Name: {current_work.name}")
            print(f"Description: {current_work.description}")
            print(f"Status: {current_work.status}")
            print(f"End Date: {current_work.end_date}")
            print(f"Subtasks: {[subtask.name for subtask in current_work.get_subtasks()]}")

        elif choice == "5":
            # Back to parent workflow or subtask
            parent = current_work.get_parent_workflow()
            if isinstance(parent, Subtask):
                current_work = parent
                tabbed_taskbar = 3
            else:
                current_work = parent
                tabbed_taskbar = 2
            print("Returning to the parent task.")

        elif choice == "6":
            # Exit the program
            exit_program = True
            print("Exiting the program. Goodbye!")

        else:
            print("Invalid choice. Please try again.")   
    else: 
        print("\n1. Create a new workflow")
        print("2. Delete a workflow")
        print("3. Enter a workflow")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            # Create a new workflow
            name = input("Enter the name of the workflow: ")
            description = input("Enter the description of the workflow: ")
            status = input("Enter the status of the workflow: ")
            end_date = input("Enter the end date of the workflow: ")
            new_workflow = Workflow(name, description, status, end_date)
            if add_workflow(taskbar, new_workflow):
                print(f"Workflow '{name}' created successfully!")
            else:
                print(f"Workflow '{name}' already exists.")

        elif choice == "2":
            # Delete an existing workflow
            if not taskbar:
                print("No workflows available to delete.")
            else:
                print("Current workflows:")
                for i, wf in enumerate(taskbar, start=1):
                    print(f"{i}. {wf.name}")
                try:
                    delete_index = int(input("Enter the number of the workflow to delete: ")) - 1
                    if 0 <= delete_index < len(taskbar):
                        deleted_workflow = taskbar[delete_index].name
                        taskbar.pop(delete_index)
                        print(f"Workflow '{deleted_workflow}' deleted successfully!")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == "3":
            # Enter a workflow
            if not taskbar:
                print("No workflows available to enter.")
            else:
                print("Current workflows:")
                for i, wf in enumerate(taskbar, start=1):
                    print(f"{i}. {wf.name}")
                try:
                    enter_index = int(input("Enter the number of the workflow to enter: ")) - 1
                    if 0 <= enter_index < len(taskbar):
                        selected_workflow = taskbar[enter_index]
                        print(f"Entering workflow: {selected_workflow.name}")
                        print(selected_workflow)  # Display workflow details
                        tabbed_taskbar = 2
                        current_work = selected_workflow
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == "4":
            # Exit the program
            exit_program = True
            print("Exiting the program. Goodbye!")

        else:
            print("Invalid choice. Please try again.")