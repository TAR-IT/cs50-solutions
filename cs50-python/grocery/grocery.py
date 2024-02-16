def main():
    grocery_list = {}
    try:
        while True:
            item = input().strip().lower()
            if item == '':
                continue
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass

    sorted_items = sorted(grocery_list.items())
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()
