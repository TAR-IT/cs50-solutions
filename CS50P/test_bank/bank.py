def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


def main():
    user_greeting = input("Greeting: ").strip()
    offer = value(user_greeting)
    print(f"${offer}")


if __name__ == "__main__":
    main()
