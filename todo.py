import argparse
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE = os.path.join(BASE_DIR, "todo.txt")

parser=argparse.ArgumentParser()
parser.add_argument('--action', choices=['add', 'remove', 'list'], required=True)
parser.add_argument('--task', help='Task description')


args = parser.parse_args()

lists=[]
def add_list(lists):
    with open(TODO_FILE,"a") as file:
        file.write(lists+"\n")
def show_tasks():
    try:
        with open(TODO_FILE,"r") as file:
            for line in file:
                print(line.strip())
   
    except FileNotFoundError:
        print("No saved tasks yet")

def remove_task(task):
    try:
        with open(TODO_FILE, "r") as file:
            lines = file.readlines()

        original_count = len(lines)

        # filter out the task
        new_lines = [line for line in lines if line.strip() != task]

        if len(new_lines) == original_count:
            print("Task not found.")
            return

        # rewrite file only if something changed
        with open("todo.txt", "w") as file:
            file.writelines(new_lines)

        print("Task removed:", task)

    except FileNotFoundError:
        print("No todo list exists yet.")

if args.action == 'add':
    add_list(args.task)
elif args.action == 'remove':
    remove_task(args.task)
elif args.action == 'list':
    show_tasks()      
        
