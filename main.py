from collections import deque

def display_menu():
    print("\nData Structure Task App")
    print("1. Stack Operations")
    print("2. Queue Operations")
    print("3. Dictionary Operations")
    print("4. Exit")

def stack_operations():
    stack = []
    print("\n-- Stack Operations --")
    while True:
        print("1. Push\n2. Pop\n3. Display\n4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to push: ")
            stack.append(item)
        elif choice == "2":
            if stack:
                print("Popped item:", stack.pop())
            else:
                print("Stack is empty.")
        elif choice == "3":
            print("Stack content:", stack)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def queue_operations():
    queue = deque()
    print("\n-- Queue Operations --")
    while True:
        print("1. Enqueue\n2. Dequeue\n3. Display\n4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to enqueue: ")
            queue.append(item)
        elif choice == "2":
            if queue:
                print("Dequeued item:", queue.popleft())
            else:
                print("Queue is empty.")
        elif choice == "3":
            print("Queue content:", list(queue))
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def dictionary_operations():
    data = {}
    print("\n-- Dictionary Operations --")
    while True:
        print("1. Insert\n2. Delete\n3. Search\n4. Display\n5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            data[key] = value
        elif choice == "2":
            key = input("Enter key to delete: ")
            if key in data:
                del data[key]
                print("Deleted successfully.")
            else:
                print("Key not found.")
        elif choice == "3":
            key = input("Enter key to search: ")
            if key in data:
                print(f"Found: {key} → {data[key]}")
            else:
                print("Key not found.")
        elif choice == "4":
            print("Current Dictionary:", data)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            stack_operations()
        elif choice == "2":
            queue_operations()
        elif choice == "3":
            dictionary_operations()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
