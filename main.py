from datetime import datetime
import os

# Custom Exceptions
class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

# File to store visitors
FILENAME = "visitors.txt"

# Ensure the visitors file exists
def ensure_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            pass  # create an empty file

# Get the last visitor's name and timestamp
def get_last_visitor():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        return None, None  # No visitors yet

    with open(FILENAME, "r") as f:
        lines = f.readlines()
        if not lines:
            return None, None
        last_line = lines[-1].strip()  # Last line in file
        name, timestamp_str = last_line.split(",")
        timestamp = datetime.fromisoformat(timestamp_str)
        return name, timestamp

# Add a visitor if rules are satisfied
def add_visitor(visitor_name):
    last_name, last_time = get_last_visitor()
    now = datetime.now()

    # Rule 1: No duplicate consecutive visitors
    if last_name == visitor_name:
        raise DuplicateVisitorError("Duplicate consecutive visitor!")

    # Rule 2: 5-minute wait between different visitors
    if last_time and (now - last_time).total_seconds() < 5 * 60:
        raise EarlyEntryError("Must wait 5 minutes between visitors!")

    # Append visitor to file
    with open(FILENAME, "a") as f:
        f.write(f"{visitor_name},{now.isoformat()}\n")
        #Append visitor ends

# Main function to run the program
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