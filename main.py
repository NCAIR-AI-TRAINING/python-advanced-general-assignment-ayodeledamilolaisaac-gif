from datetime import datetime, timedelta
import os

# Custom Exceptions
class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"

def ensure_file():
    """Ensure the visitors file exists."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            pass

def get_last_visitor():
    """Return last visitor's name and timestamp."""
    ensure_file()

    if os.path.getsize(FILENAME) == 0:
        return None, None

    with open(FILENAME, "r") as f:
        lines = f.readlines()
        if not lines:
            return None, None

        last_line = lines[-1].strip()
        name, timestamp_str = last_line.split(",")
        timestamp = datetime.fromisoformat(timestamp_str)
        return name, timestamp

def add_visitor(visitor_name):
    """Add visitor following rules."""
    ensure_file()  # VERY IMPORTANT

    last_name, last_time = get_last_visitor()
    now = datetime.now()

    # Rule 1: Duplicate visitor check
    if last_name == visitor_name:
        raise DuplicateVisitorError("Duplicate visitor.")

    # Rule 2: Enforce 2-minute wait time
    if last_time and (now - last_time) < timedelta(minutes=2):
        raise EarlyEntryError("Wait time not elapsed.")

    # Append visitor
    with open(FILENAME, "a") as f:
        f.write(f"{visitor_name},{now.isoformat()}\n")

def main():
    ensure_file()
    name = input("Enter visitor's name: ")
    try:
        add_visitor(name)
        print("Visitor added successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
