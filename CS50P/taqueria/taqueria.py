menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def get_total_cost(order_items):
    total_cost = sum(menu[item] for item in order_items)
    return total_cost

def main():
    order_items = []

    try:
        while True:
            item = input("Enter an item (Ctrl-D to finish): ").strip().title()
            if item in menu:
                order_items.append(item)
                total_cost = get_total_cost(order_items)
                print(f"Total: ${total_cost:.2f}")
            else:
                print("Invalid item. Please try again.")
    except EOFError:
        pass

if __name__ == "__main__":
    main()
