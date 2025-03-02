import json
from datetime import datetime, timezone

from utils import get_records, write_data, print_header


def add_task(task):

    records = get_records()

    key = str(len(records) + 1)
    records[key] = {"description": task, 
                    "status": "todo", 
                    "createdAt": datetime.now(timezone.utc).isoformat(),
                    "updatedAt": datetime.now(timezone.utc).isoformat()
                    }
   
    write_data(records)
    
    message = f"Task successfully added: ( {key} )"

    print_header()
    print(message)


def update_task(task_id, task):

    records = get_records()
    update_record = records[str(task_id)]
    update_record["description"] = task
    update_record["updatedAt"] = datetime.now(timezone.utc).isoformat()

    records[str(task_id)] = update_record

    write_data(records)
    
    message = f"Task updated: {task}"
    print_header()
    print(message)

def list_tasks():
    records = get_records()

    print_header()
    for k, v in records.items():

        # print(f"{k}: , {v["description"].ljust(20)} {v["status"].ljust(8)} {v["createdAt"].ljust(30)} {v["updatedAt"].ljust(30)}")

        print(f"{k}: , {v["description"]} {v["status"]} {v["createdAt"]} {v["updatedAt"]}")

def delete_task(task):
    pass


def mark_in_progress(task):
    pass


def mark_done(task):
    pass


