def get_fuel_percentage(fraction_str):
    try:
        x, y = map(int, fraction_str.split('/'))
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        fuel_percentage = (x / y) * 100
        return round(fuel_percentage)
    except (ValueError, ZeroDivisionError):
        return None


def main():
    while True:
        fraction_str = input("Enter the fuel fraction (X/Y): ")
        percentage = get_fuel_percentage(fraction_str)
        if percentage is not None:
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
