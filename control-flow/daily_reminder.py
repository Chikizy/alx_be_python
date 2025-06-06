task_description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time == "yes":
            print(f"{task_description} is a {priority} priority task that requires immediate attention today!")
        elif time == "no":
            print(f"{task_description} is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("time not specified!")
    case "medium":
        if time == "yes":
            print(f"{task_description} is a {priority} priority task that requires immediate attention today!")
        elif time == "no":
            print(f"{task_description} is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("time not specified!")
    case "low":
        if time == "yes":
            print(f"{task_description} is a {priority} priority task that requires immediate attention today!")
        elif time == "no":
            print(f"{task_description} is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("time not specified!")
    case _:
        print("priority is not specified!")
            


