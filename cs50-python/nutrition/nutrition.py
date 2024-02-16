def main():
    fruit = input("What fruit? ")
    if fruit.casefold() == "apple":
        print("Calories: 130")
    elif fruit.casefold() == "banana":
        print("Calories: 110")
    elif fruit.casefold() == "avocado":
        print("Calories: 50")
    elif fruit.casefold() == "kiwifruit":
        print("Calories: 90")
    elif fruit.casefold() == "pear":
        print("Calories: 100")
    elif fruit.casefold() == "sweet cherries":
        print("Calories: 100")

main()