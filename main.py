from datetime import datetime
import os

class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"

def ensure_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            pass

def get_last_visitor():
    if not os.path.exists(FILENAME):
        return None

    with open(FILENAME, "r") as f:
        lines = f.readlines()

    if not lines:
        return None

    last_line = lines[-1].strip()
    name = last_line.split(" | ")[0]
    return name

def add_visitor(visitor_name):
    ensure_file()
    last_name = get_last_visitor()

    if visitor_name == last_name:
        raise DuplicateVisitorError("Duplicate consecutive visitor not allowed.")

    with open(FILENAME, "a") as f:
        f.write(f"{visitor_name} | {datetime.now().isoformat()}\n")

def main():
    ensure_file()
    name = input("Enter visitor's name: ")
    try:
        add_visitor(name)
        print("Visitor added successfully!")
    except Exception as e:
        print("Error:", e)

if _name_ == "_main_":
    main()
