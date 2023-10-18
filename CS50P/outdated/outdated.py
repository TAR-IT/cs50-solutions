def is_valid_date(date_str):
    # Check if the date string is in the format "month day, year"
    if ',' in date_str:
        try:
            month, day_year = date_str.split(" ", 1)
            day, year = day_year.split(", ")
            month_index = months.index(month.capitalize()) + 1
            year = int(year)
            day = int(day)
            if month_index < 1 or month_index > 12 or day < 1 or day > 31:
                return False
        except ValueError:
            return False
    # Check if the date string is in the format "month/day/year"
    elif '/' in date_str:
        try:
            month, day, year = date_str.split("/")
            month_index = int(month)
            year = int(year)
            day = int(day)
            if month_index < 1 or month_index > 12 or day < 1 or day > 31:
                return False
        except ValueError:
            return False
    else:
        return False

    return True


def convert_to_iso(date_str):
    # Check if the date string is in the format "month day, year"
    if ',' in date_str:
        month, day_year = date_str.split(" ", 1)
        day, year = day_year.split(", ")
        month_index = months.index(month.capitalize()) + 1
        year = int(year)
        day = int(day)
    # Check if the date string is in the format "month/day/year"
    elif '/' in date_str:
        month, day, year = date_str.split("/")
        month_index = int(month)
        year = int(year)
        day = int(day)

    return f"{year:04d}-{month_index:02d}-{day:02d}"


months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]
while True:
    user_input = input("Enter a date (in month-day-year or month day, year format): ")
    if is_valid_date(user_input):
        iso_date = convert_to_iso(user_input)
        print(iso_date)
        break
    else:
        print("Invalid date format. Please try again.")
