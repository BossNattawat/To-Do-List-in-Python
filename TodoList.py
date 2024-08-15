def add_todo():
    with open("TodoList.txt", "a") as file:  # Append mode
        new_todo = input("Enter some task: ")
        file.write(new_todo + '\n')


def todo_list():
    with open("TodoList.txt", "r") as file:  # Read mode
        for i, todo in enumerate(file):
            print(f"{i + 1}. {todo}", end="")
    print()


def remove_todo():
    with open("TodoList.txt", "r") as file:  # Read mode
        lines = file.readlines()

    # '-1': Subtracts 1 from the user's input. Python are zero-indexed.
    todo_to_remove = int(input("Enter the number of the task to remove: ")) - 1

    if 0 <= todo_to_remove < len(lines):
        del lines[todo_to_remove]
        print(f"Task {todo_to_remove + 1} has been removed.")

        # Write the updated list back to the file
        with open("TodoList.txt", "w") as file:
            file.writelines(lines)
    else:
        print("Invalid task number.")


def main():
    while True:
        print("________Todo-List________")
        todo_list()

        print("________Todo Menu________")
        print("1. Add \n2. Delete \n3. Close")
        menu = input("Select a menu option: ")

        if menu == "1":
            add_todo()
        elif menu == "2":
            remove_todo()
        elif menu == "3":
            add_more = input("Are you sure you want to close? (yes/no): ").strip().lower()
            if add_more == "yes":
                break


if __name__ == "__main__":
    main()