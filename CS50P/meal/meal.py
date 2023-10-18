def convert(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours + minutes / 60.0


def main():
    user_input = input("Enter the time in 24-hour format (e.g., 07:30): ")

    try:
        time_in_hours = convert(user_input)

        if 7 <= time_in_hours < 12:
            print("breakfast time")
        elif 12 <= time_in_hours < 15:
            print("lunch time")
        elif 18 <= time_in_hours < 21:
            print("dinner time")

    except ValueError:
        print("Invalid time format. Please use the format 'HH:MM' (e.g., 07:30).")


if __name__ == "__main__":
    main()