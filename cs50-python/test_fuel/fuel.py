def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0 or x > y:
            raise ValueError
        fuel_percentage = (x / y) * 100
        return round(fuel_percentage)
    except (ValueError, ZeroDivisionError):
        raise ValueError("Invalid input format. Fraction should be in X/Y format with X and Y integers.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    while True:
        fraction_str = input("Enter the fuel fraction (X/Y): ")
        try:
            percentage = convert(fraction_str)
            result = gauge(percentage)
            print(result)
            break
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
