from datetime import datetime, timedelta
import os

# Custom Exceptions
class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"
WAIT_MINUTES = 5  # as per assignment requirement

def ensure_file():
    """Ensure the visitors file exists."""
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()  # safe creation of empty file

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
        if " - " not in last_line:
            return None, None
        name, timestamp_str = last_line.rsplit(" - ", 1)
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return name, timestamp

def add_visitor(visitor_name):
    """Add a visitor respecting duplicate and wait-time rules."""
    ensure_file()

    last_name, last_time = get_last_visitor()
    now = datetime.now()

    # Rule 1: No duplicate consecutive visitors
    if last_name == visitor_name:
        raise DuplicateVisitorError("Duplicate visitor.")

    # Rule 2: Enforce 5-minute wait time
    if last_time and (now - last_time) < timedelta(minutes=WAIT_MINUTES):
        raise EarlyEntryError("Wait time not elapsed.")

    # Append visitor to file
    with open(FILENAME, "a") as f:
        f.write(f"{visitor_name} - {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

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
