from datetime import datetime, timedelta
import os

# Custom Exceptions
class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"
WAIT_MINUTES = 5  # wait time between visitors in minutes

def ensure_file():
    """Create the visitors file if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            pass  # just create empty file

def get_last_visitor():
    """Return the last visitor's name and timestamp as a tuple, or None if file is empty."""
    ensure_file()
    with open(FILENAME, "r") as f:
        lines = f.readlines()
        if not lines:
            return None
        last_line = lines[-1].strip()
        name, timestamp = last_line.split('|')
        return name.strip(), datetime.fromisoformat(timestamp.strip())

def add_visitor(visitor_name):
    """Add a visitor to the file, enforcing no duplicates and wait time."""
    ensure_file()
    now = datetime.now()

    # Check for duplicates and wait time
    with open(FILENAME, "r") as f:
        for line in f:
            name, timestamp = line.strip().split('|')
            name = name.strip()
            timestamp = datetime.fromisoformat(timestamp.strip())
            if name == visitor_name:
                raise DuplicateVisitorError(f"{visitor_name} already exists")
            if (now - timestamp).total_seconds() < WAIT_MINUTES * 60:
                raise EarlyEntryError(f"Visitors must wait at least {WAIT_MINUTES} minutes")

    # Append new visitor
    with open(FILENAME, "a") as f:
        f.write(f"{visitor_name} | {now.isoformat()}\n")

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
