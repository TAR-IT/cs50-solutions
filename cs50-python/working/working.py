import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        print(str(e))
        sys.exit(1)


def convert(s):
    # Define regular expression for the expected format
    format_pattern = r'^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s(AM|PM)$'

    # Check for a match
    match = re.match(format_pattern, s)
    if not match:
        raise ValueError("ValueError")

    # Extract the values from the match groups
    start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = match.groups()

    # Convert the hours and minutes to integers
    start_hour = int(start_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_hour = int(end_hour)
    end_minute = int(end_minute) if end_minute else 0

    # Check for valid hours, minutes, and meridiem
    if not (1 <= start_hour <= 12 and 0 <= start_minute <= 59 and
            1 <= end_hour <= 12 and 0 <= end_minute <= 59 and
            start_meridiem in ("AM", "PM") and end_meridiem in ("AM", "PM")):
        raise ValueError("ValueError")

    # Convert to 24-hour format
    if start_meridiem == "PM" and start_hour != 12:
        start_hour += 12
    if end_meridiem == "PM" and end_hour != 12:
        end_hour += 12

    # Handle special cases of 12:00 AM and 12:00 PM
    if start_hour == 12 and start_meridiem == "AM":
        start_hour = 0
    if end_hour == 12 and end_meridiem == "AM":
        end_hour = 0

    # Format the output
    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()
