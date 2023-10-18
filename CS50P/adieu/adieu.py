def adieu(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        comma_separated = ", ".join(names[:-1])
        return f"Adieu, adieu, to {comma_separated}, and {names[-1]}"

def main():
    names = []
    try:
        while True:
            name = input("Enter a name: ")
            names.append(name)
    except EOFError:
        if names:
            for i in range(1, len(names) + 1):
                print(adieu(names[:i]))

if __name__ == "__main__":
    main()
