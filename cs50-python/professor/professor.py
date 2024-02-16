import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y, correct_answer = generate_problem(level)
        user_answer = get_user_answer()
        attempts = 1

        while user_answer != correct_answer and attempts < 3:
            print("EEE")
            user_answer = get_user_answer()
            attempts += 1

        if user_answer == correct_answer:
            score += 1
        else:
            print(f"The correct answer is: {correct_answer}")

    print(f"Score:{score}")
    return score

def get_level():
    while True:
        try:
            level = int(input("Choose a level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            print("Invalid input. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level. Level must be 1, 2, or 3.")

def generate_problem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    correct_answer = x + y
    print(f"What is {x} + {y} = ?")
    return x, y, correct_answer

def get_user_answer():
    while True:
        try:
            user_input = input("Your answer: ")
            user_answer = int(user_input)
            return user_answer
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    while True:
        score = main()
        break
