def camel_to_snake(camel_case):
    snake_case = ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case])
    return snake_case.lstrip('_')


def main():
    camel_case_var = input("Enter a variable name in camel case: ")
    snake_case_var = camel_to_snake(camel_case_var)
    print("Variable name in snake case:")
    print(snake_case_var)


if __name__ == "__main__":
    main()?=?