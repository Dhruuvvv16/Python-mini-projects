import argparse
import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(args):
    tasks = load_tasks()
    task = {
        "id": (tasks[-1]["id"] + 1) if tasks else 1,
        "title": args.title,
        "priority": args.priority,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{task['id']}: {task['title']} [{task['priority']}]")


def list_tasks(args):
    tasks = load_tasks()
    if not tasks:
        print('No tasks yet. Add one with: python todo_list.py add "Task title"')
        return

    if not args.all:
        tasks = [t for t in tasks if not t["done"]]
        if not tasks:
            print("Nothing pending. Nice work! Use --all to see completed tasks.")
            return

    priority_order = {"high": 0, "medium": 1, "low": 2}
    tasks.sort(key=lambda t: (t["done"], priority_order.get(t["priority"], 1)))

    print(f"\n{'ID':<4}{'Status':<8}{'Priority':<10}{'Title'}")
    print("-" * 50)
    for t in tasks:
        status = "[x]" if t["done"] else "[ ]"
        print(f"{t['id']:<4}{status:<8}{t['priority']:<10}{t['title']}")
    print()


def complete_task(args):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == args.id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Marked task #{args.id} as done.")
            return
    print(f"No task with id {args.id} found.")


def remove_task(args):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != args.id]
    if len(new_tasks) == len(tasks):
        print(f"No task with id {args.id} found.")
        return
    save_tasks(new_tasks)
    print(f"Removed task #{args.id}.")


def clear_tasks(args):
    confirm = input("This will delete ALL tasks. Type 'yes' to confirm: ")
    if confirm.lower() == "yes":
        save_tasks([])
        print("All tasks cleared.")
    else:
        print("Cancelled.")


def build_parser():
    parser = argparse.ArgumentParser(description="A simple CLI to-do list manager.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument(
        "-p", "--priority", choices=["high", "medium", "low"], default="medium"
    )
    add_parser.set_defaults(func=add_task)

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--all", action="store_true", help="Include completed tasks"
    )
    list_parser.set_defaults(func=list_tasks)

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int)
    done_parser.set_defaults(func=complete_task)

    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("id", type=int)
    remove_parser.set_defaults(func=remove_task)

    clear_parser = subparsers.add_parser("clear", help="Remove all tasks")
    clear_parser.set_defaults(func=clear_tasks)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()