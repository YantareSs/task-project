import json
import sys

def load_tasks(path="tasks.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks, path="tasks.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def main():
    tasks = load_tasks()
    print("Загружено задач:", len(tasks))

if __name__ == "__main__":
    main()
