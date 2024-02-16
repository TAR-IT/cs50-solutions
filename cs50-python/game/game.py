import random

def main():
    level = get_level()
    secret_number = generate_integer(level)

    while True:
        guess = get_guess()

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_level():
    while True:
        try:
            level = int(input("Enter the level (a positive integer): "))
            if level > 0:
                return level
            else:
                print("Invalid level. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def generate_integer(level):
    return random.randint(1, level)

def get_guess():
    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess > 0:
                return guess
            else:
                print("Invalid guess. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()