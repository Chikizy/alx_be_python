def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice(1/2/3/4): ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item you want to add: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Select the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("You don't have this item on your list.\n")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("You have an empty shopping list.\n")
            else:
                print("\n---*YOUR SHOPPING LIST*---")
                for item in shopping_list:
                    print("{}".format(item))
                print()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()