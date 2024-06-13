# TODO Program written in Python
import os
import pickle
from datetime import datetime

todo_items = []     # Initialize any empty list to store todo items

TODO_FILE = 'todo.pkl'      # Define the filename for storing todos

class TodoItem:
    def __init__(self, title, created_at, is_completed=False, completed_at=None):
        self.title = title
        self.created_at = created_at
        self.is_completed = is_completed
        self.completed_at = completed_at

# Define a function to save todos to our pickle file
def save_todos():       # Define a function to save todos to the pickle file
    with open(TODO_FILE, 'wb') as file:      # Open the pickle file in write mode
        pickle.dump(todo_items, file)       # Write the list of todo items to the pickle file

# Define a function to read todos from the pickle file
def read_todos():       # Define a function to read todos from the pickle file
    global todo_items      # Declare the todo_items list as a global variable
    if os.path.exists(TODO_FILE):       # Check if the pickle file exists
        with open(TODO_FILE, 'rb') as file:      # Open the pickle file in read mode
            todo_items = pickle.load(file)      # Load the list of todo items from the pickle file

def add_todo():     # Define a function to add a new todo item
    title = input('Enter the title of the todo item (up to 50 characters): ')[:50]     # Get the title of the todo item from the user, truncating to 50 characters
    created_at = datetime.now().strftime('%d/%m %H:%M')     # Get the created_at date of the todo item and format the date and time
    todo_item = TodoItem(title, created_at)     # Create a new todo item with the title and created_at date  
    todo_items.append(todo_item)        # Add the todo item to the list of todo items
    save_todos()        # Save the todo items to the pickle file

  
def print_all_todos():
    print("+----+----------------------------------------------------+----------------------+---------------+----------------------+")
    print("| ID |                        Title                       |     Created At       |   Completed   |    Completed At      |")
    print("+----+----------------------------------------------------+----------------------+---------------+----------------------+")

    for i, todo_item in enumerate(todo_items):
        completed_at = todo_item.completed_at.strftime('%d/%m %H:%M') if todo_item.completed_at else ''
        print(f"| {i:<2} | {todo_item.title:<50} | {todo_item.created_at:<20} | {'✅' if todo_item.is_completed else '❌':^12} | {completed_at:<20} |")
    print("+----+----------------------------------------------------+----------------------+---------------+----------------------+")

def mark_todo_as_completed():        # Define a function to mark a todo item as completed   
    try:
        print_all_todos()       # Print all the todo items
        todo_id = int(input('Enter the ID of the todo item: '))    # Mark the todo item as completed
        todo_items[todo_id].is_completed = True     # Set the is_completed flag of the todo item to True
        todo_items[todo_id].completed_at = datetime.now()
        # Save todos to the pickle file
        save_todos()        # Save the todo items to the pickle file
    except IndexError:      # Handle the case where the user enters an invalid todo ID
        print('Invalid todo ID')        # Print an error message
    except ValueError:      # Handle the case where the user enters a non-integer todo ID
        print('Invalid todo ID')       # Print an error message
        
# Define a function that deletes a specific todo item
def delete_todo():      # Define a function to delete a todo item
    try:
        print_all_todos()       # Print all the todo items
        todo_id = int(input('Enter the ID of the todo item: '))   # Get the ID of the todo item to delete
        del todo_items[todo_id]     # Delete the todo item with the specified ID
        # Save todos to the pickle file
        save_todos()        # Save the todo items to the pickle file
    except IndexError:      # Handle the case where the user enters an invalid todo ID
        print('Invalid todo ID')        # Print an error message
    except ValueError:      # Handle the case where the user enters a non-integer todo ID
        print('Invalid todo ID')       # Print an error message

# Define function to show options to the user
def show_options():     # Define a function to show the options to the user
    while True:
        print('Welcome to TaskMaster!')      # Print a welcome message
        user_choice = input('Type "a" to add a new todo, "p" to print all todos, "c" to mark a todo as completed, "d" to delete a todo, or "q" to quit: ').upper()       # Get the user choice
        if user_choice == 'A':
            add_todo()
        elif user_choice == 'P':
            print_all_todos()
        elif user_choice == 'C':
            mark_todo_as_completed()
        elif user_choice == 'D':
            delete_todo()
        elif user_choice == 'Q':
            print('Thank you for using TaskMaster!')       # Print a goodbye message
            break
        else:
            print('Invalid choice! Please try again.')

# Define function to check if this is the first time you are using the app or not
def first_time():       # Define a function to check if this is the first time the user is using the app
    if os.path.exists(TODO_FILE):       # Check if the pickle file exists
        read_todos()        # Read the todos from the pickle file
    else:
        print('Welcome to TaskMaster!')
        add_todo()
        

if __name__ == '__main__':      # Check if the script is being run directly
    os.system('cls' if os.name == "nt" else "clear")      # Clear the terminal screen
    print("\033[32;1m]")
    first_time()        # Check if this is the first time the user is using the app
    show_options()      # Show the options to the user