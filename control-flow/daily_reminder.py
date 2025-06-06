task_description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task_description}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("time not specified!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task_description}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("time not specified!")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task_description}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("time not specified!")
    case _:
        if time_bound == "yes" or time_bound == "no":
            print("priority is not specified!")
        else:
            print("Both priority and time bound nature are not specified.\nInput correct values!")
  
            


