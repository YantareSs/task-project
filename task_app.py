import argparse
import json
import sys

DEFAULT_PRIORITY = "normal"
PRIORITIES = ("low", "normal", "high")

def load_tasks(path="tasks.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks, path="tasks.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(title, path="tasks.json"):
    tasks = load_tasks(path)
    new_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})
    save_tasks(tasks, path)
    return new_id

def mark_done(task_id, path="tasks.json"):
    tasks = load_tasks(path)
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
    save_tasks(tasks, path)

def filter_by_status(done, path="tasks.json"):
    tasks = load_tasks(path)
    return [t for t in tasks if t["done"] == done]

def validate_priority(priority):
    if priority not in PRIORITIES:
        raise ValueError(f"Invalid priority: {priority}")
    return priority

def sort_by_priority(tasks):
    order = {"high": 0, "normal": 1, "low": 2}
    return sorted(tasks, key=lambda t: order.get(t.get("priority", "normal"), 1))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--priority",
        choices=PRIORITIES,
        default=DEFAULT_PRIORITY,
        help="Приоритет по умолчанию",
    )
    args = parser.parse_args()
    tasks = load_tasks()
    print(f"Загружено задач: {len(tasks)}")
    print(f"Приоритет по умолчанию: {args.priority}")

if __name__ == "__main__":
    main()
