def todo_list_app():
    tasks = []  #List of Tasks will be kept here
    completed_tasks = [] #List of Copleted Tasks will be Appendede Here
    
    print("Welcome to the  To-Do List App!")
    print("Type 'exit' at any time to quit.\n")
    
    while True:
        print("\n   Main Menu:")
        print("-"*20)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice.lower() == "exit" or choice == "5":
            break
            
        elif choice == "1":
            # Add Task with Priority
            while True:
                task = input("\nEnter new task (or 'back' to return): ").strip()
                if task.lower() == "back":
                    break
                if task.lower() == "exit":
                    choice = "5"
                    break
                
                print("\nSelect Priority:")
                print("1. High")
                print("2. Medium")
                print("3. Low")
                
                priority_choice = input("Enter priority (1-3): ").strip()
                priorities = {1: "High", 2: "Medium", 3: "Low"}
                
                try:
                    priority = priorities.get(int(priority_choice), "Medium")
                    tasks.append({
                        "description": task,
                        "priority": priority,
                        "completed": False
                    })
                    print(f"\nAdded: '{task}' with {priority} priority") #by defaullt "medium" will be assigned
                    break
                except:
                    print("Invalid priority. Using Medium by default.")
                    tasks.append({
                        "description": task,
                        "priority": "Medium",
                        "completed": False
                    })
                    print(f"\nAdded: '{task}' with Medium priority")
                    break
                    
        elif choice == "2":
            # View Tasks -
            if not tasks:
                print("\nNo tasks in your list!")
            else:
                print("\nCurrent Tasks:")#Otherwise, it proceeds to display all tasks.
                print("-" * 40)
                print(f"{'No.':<5}{'Status':<8}{'Task':<20}{'Priority':<10}")#Task table header format (n) no. char wide
                print("-" * 40)
                for i, task in enumerate(tasks, 1):#tasks with index i starting at 1
                    status = "✓" if task["completed"] else " "
                    print(f"{i:<5}[{status:<3}]{task['description'][:18]:<20}{task['priority']:<10}")##Prevents long descriptions breaking the layout.
                print("-" * 40)
                
        elif choice == "3":
            # Delete Task
            if not tasks:
                print("\nNo tasks to delete!")
                continue
                
            print("\nCurrent Tasks:")# Show tasks first so user knows what to delete
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['description']}")
                
            try:
                task_num = input("\nEnter task number to delete (or 'back'): ").strip()
                if task_num.lower() == "back":    #it cancels deletion and returns to the previous menu.
                    continue
                if task_num.lower() == "exit":
                    choice = "5"
                    break # Breaks out of the current loop
                    
                task_num = int(task_num)
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    # Remove from completed if it was there
                    if deleted_task in completed_tasks:
                        completed_tasks.remove(deleted_task)
                    print(f"\nDeleted: '{deleted_task['description']}'")
                else:
                    print("Invalid task number!")
            except:
                print("Invalid input!") #
                
        elif choice == "4":
            # Mark Task Complete
            if not tasks:
                print("\nNo tasks to mark complete!")
                continue
                
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['description']}")
                
            try:
                task_num = input("\nEnter task number to mark complete (or 'back'): ").strip()
                if task_num.lower() == "back":
                    continue
                if task_num.lower() == "exit":
                    choice = "5"
                    break
                    
                task_num = int(task_num)
                if 1 <= task_num <= len(tasks):
                    if tasks[task_num - 1]["completed"]:
                        print("\nTask is already completed!")
                    else:
                        tasks[task_num - 1]["completed"] = True
                        completed_tasks.append(tasks[task_num - 1])
                        print(f"\nMarked as complete: '{tasks[task_num - 1]['description']}'")
                else:
                    print("Invalid task number!")
            except:
                print("Invalid input!")
                
        else:
            print("\nInvalid choice! Please enter 1-5.")
    
    # Exit Summary
    pending_tasks = [task for task in tasks if not task["completed"]]
    
    print("\n" + "=" * 40)
    print("SUMMARY REPORT".center(40))
    print("=" * 40)
    
    print(f"\nCOMPLETED TASKS ({len(completed_tasks)}):")
    print("---------------------")
    if completed_tasks:
        for i, task in enumerate(completed_tasks, 1):
            print(f"  {i}. {task['description']} (Priority: {task['priority']})")
    else:
        print("  No completed tasks")
    
    print(f"\nPENDING TASKS ({len(pending_tasks)}):")
    print("---------------------")
    if pending_tasks:
        for i, task in enumerate(pending_tasks, 1):
            print(f"  {i}. {task['description']} (Priority: {task['priority']})")
    else:
        print("  No pending tasks")
    
    print("\nThank you for using the To-Do List App!")

# Run Todo List App
todo_list_app()