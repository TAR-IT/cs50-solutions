def main():
    while True:
        fraction_str = input("Enter the fuel fraction (X/Y): ")
        percentage = convert(fraction_str)
        result = gauge(percentage)
        print(result)
        break


def convert(fraction: str) -> float:
    """
    Convert a fraction string to a fuel percentage.

    Args:
        fraction (str): The input fraction string in the format 'X/Y'.

    Returns:
        float: The fuel percentage.

    Raises:
        ValueError: If the fraction format is invalid.
        ZeroDivisionError: If the denominator is zero.
    """
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0:
            raise ZeroDivisionError("Do not divide by zero.")
        elif x > y:
            raise ValueError("Invalid input format. Fraction should be in X/Y format with X and Y integers.")
        fuel_percentage = (x / y) * 100
        return round(fuel_percentage)
    except (ValueError, ZeroDivisionError) as e:
        raise e


def gauge(percentage: float) -> str:
    """
    Determine the gauge level based on the fuel percentage.

    Args:
        percentage (float): The fuel percentage.

    Returns:
        str: The gauge level.

    Example:
        gauge(25) -> "E"
        gauge(50) -> "50%"
        gauge(99) -> "F"
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
