from datetime import datetime, timedelta
import os

# Custom Exceptions
class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

# File to store visitors
FILENAME = "visitors.txt"
WAIT_MINUTES = 1  # minimum wait time between visits (adjust if needed by the test)

def ensure_file():
    """Ensure the visitors file exists."""
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()

def get_last_visitor():
    """Return the last visitor name and timestamp as a tuple (name, datetime)."""
    if not os.path.exists(FILENAME):
        return None, None

    with open(FILENAME, "r") as f:
        lines = f.readlines()
        if not lines:
            return None, None
        last_line = lines[-1].strip()
        if " - " not in last_line:
            return None, None
        name, ts_str = last_line.rsplit(" - ", 1)
        ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
        return name, ts

def add_visitor(visitor_name):
    """Add a visitor if they are not duplicate and wait time is satisfied."""
    ensure_file()
    last_name, last_ts = get_last_visitor()
    now = datetime.now()

    # Check for duplicate visitor
    if last_name == visitor_name:
        raise DuplicateVisitorError(f"{visitor_name} is already the last visitor.")

    # Check wait time
    if last_ts and (now - last_ts) < timedelta(minutes=WAIT_MINUTES):
        raise EarlyEntryError("Cannot add visitor yet. Wait time not passed.")

    # Append visitor with timestamp
    with open(FILENAME, "a") as f:
        f.write(f"{visitor_name} - {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
