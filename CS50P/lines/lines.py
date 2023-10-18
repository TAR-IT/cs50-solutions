import sys

def count_lines_of_code(file_name):
    line_count = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    line_count += 1
    except FileNotFoundError:
        sys.exit("Invalid file name or file does not exist.")
    return line_count

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <file_name.py>")

    file_name = sys.argv[1]
    if not file_name.endswith('.py'):
        sys.exit("Invalid file name.")

    line_count = count_lines_of_code(file_name)
    print(f"Number of lines of code (excluding comments and blanks): {line_count}")

if __name__ == "__main__":
    main()