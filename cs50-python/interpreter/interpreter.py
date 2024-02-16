def calculate_expression(expression):
    x, operator, z = expression.split()

    x = float(x)
    z = float(z)

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z
    else:
        raise ValueError("Invalid operator. Please use one of +, -, *, or /.")

    return round(result, 1)


def main():
    user_input = input("Enter an arithmetic expression (e.g., 1 + 1): ")
    try:
        result = calculate_expression(user_input)
        print(f"{result}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()