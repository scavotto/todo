import os
import pickle
from datetime import datetime

todo_items = []
TODO_FILE = 'todo.pkl'
CHANGELOG_FILE = 'changelog.txt'

class TodoItem:
    def __init__(self, title, created_at, is_completed=False, completed_at=None):
        self.title = title
        self.created_at = created_at
        self.is_completed = is_completed
        self.completed_at = completed_at

def save_todos():
    with open(TODO_FILE, 'wb') as file:
        pickle.dump(todo_items, file)
    
    with open(CHANGELOG_FILE, 'a') as file:
        for todo_item in todo_items:
            if not hasattr(todo_item, 'logged'):
                action = 'Added' if not todo_item.is_completed else 'Completed'
                log_message = f"{action} todo item: {todo_item.title} | Created at: {todo_item.created_at}"
                if todo_item.is_completed:
                    log_message += f" | Completed at: {todo_item.completed_at}"
                file.write(log_message + '\n')
                todo_item.logged = True

def read_todos():
    global todo_items
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'rb') as file:
            todo_items = pickle.load(file)

def add_todo():
    title = input('Enter the title of the todo item (up to 50 characters): ')[:50]
    created_at = datetime.now().strftime('%d/%m %H:%M')
    todo_item = TodoItem(title, created_at)
    todo_items.append(todo_item)
    save_todos()

def print_all_todos():
    print("+----+----------------------------------------------------+----------------------+---------------+----------------------+")
    print("| ID |                        Title                       |     Created At       |   Completed   |    Completed At      |")
    print("+----+----------------------------------------------------+----------------------+---------------+----------------------+")

    for i, todo_item in enumerate(todo_items):
        completed_at = todo_item.completed_at.strftime('%d/%m %H:%M') if todo_item.completed_at else ''
        print(f"| {i:<2} | {todo_item.title:<50} | {todo_item.created_at:<20} | {'✅' if todo_item.is_completed else '❌':^12} | {completed_at:<20} |")
    print("+----+----------------------------------------------------+----------------------+---------------+----------------------+")

def mark_todo_as_completed():
    try:
        print_all_todos()
        todo_id = int(input('Enter the ID of the todo item: '))
        todo_item = todo_items[todo_id]
        todo_item.is_completed = True
        todo_item.completed_at = datetime.now()
        save_todos()
        
        with open(CHANGELOG_FILE, 'a') as file:
            log_message = f"Completed todo item: {todo_item.title} | Created at: {todo_item.created_at} | Completed at: {todo_item.completed_at}"
            file.write(log_message + '\n')
    except IndexError:
        print('Invalid todo ID')
    except ValueError:
        print('Invalid todo ID')

def delete_todo():
    try:
        print_all_todos()
        todo_id = int(input('Enter the ID of the todo item: '))
        deleted_todo = todo_items.pop(todo_id)
        save_todos()
        
        with open(CHANGELOG_FILE, 'a') as file:
            log_message = f"Deleted todo item: {deleted_todo.title} | Created at: {deleted_todo.created_at}"
            file.write(log_message + '\n')
    except IndexError:
        print('Invalid todo ID')
    except ValueError:
        print('Invalid todo ID')

def show_options():
    while True:
        print('Welcome to TaskMaster!')
        user_choice = input('Type "a" to add a new todo, "p" to print all todos, "c" to mark a todo as completed, "d" to delete a todo, or "q" to quit: ').upper()
        if user_choice == 'A':
            add_todo()
        elif user_choice == 'P':
            print_all_todos()
        elif user_choice == 'C':
            mark_todo_as_completed()
        elif user_choice == 'D':
            delete_todo()
        elif user_choice == 'Q':
            print('Thank you for using TaskMaster!')
            break
        else:
            print('Invalid choice! Please try again.')

def first_time():
    if os.path.exists(TODO_FILE):
        read_todos()
    else:
        print('Welcome to TaskMaster!')
        add_todo()

if __name__ == '__main__':
    os.system('cls' if os.name == "nt" else "clear")
    print("\033[32;1m]")
    first_time()
    show_options()