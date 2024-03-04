import sys

def main():
    while True:
        fraction_str = input("Input: ")
        try:
            percentage = convert(fraction_str)
            result = gauge(percentage)
            print(result)
            break
        except ValueError as e:
            print(e)

def convert(fraction):
    try:
        # Split fraction to x and y
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        # Raise exception if dividing by zero or fraction > 1
        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        # Turn fraction into decimal number
        decimal = x / y
        # Turn decimal number into rounded percentage
        percentage = "{:.0f}".format(decimal * 100)
        return int(percentage)
    except ValueError:
        raise ValueError("Invalid input format. Fraction should equal less than 1. Do not divide by zero.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
