import argparse

from tasks import add_task, update_task, delete_task, mark_in_progress, mark_done , list_tasks


def main():
    parser = argparse.ArgumentParser(prog="task_cli", description="A simple task manager CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add subcommand
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="The task description")

    # Add subcommand
    add_parser = subparsers.add_parser("update", help="Update a task")
    add_parser.add_argument("task_id", type=int, help="The task Id")
    add_parser.add_argument("task", type=str, help="The task description")

    # Add subcommand
    add_parser = subparsers.add_parser("list", help="List all tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "update":
        update_task(args.task_id, args.task)
    elif args.command == "list":
        list_tasks()        

if __name__ == "__main__":
    main()
