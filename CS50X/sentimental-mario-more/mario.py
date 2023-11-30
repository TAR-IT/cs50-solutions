def main():
    height = get_valid_height()
    print_pyramids(height)

def get_valid_height():
    while True:
        try:
            height = int(input("Height: "))
            if height >= 1 and height <= 8:
                return height
            else:
                print("Height must be a positive integer between 1 and 8, inclusive.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

def print_pyramids(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        hashes_left = "#" * i
        hashes_right = "#" * i
        print(f"{spaces}{hashes_left}  {hashes_right}")

if __name__ == "__main__":
    main()