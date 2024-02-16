import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Case-insensitive search for the word "um" as a whole word
    pattern = r'\bum\b'
    return len(re.findall(pattern, s, re.IGNORECASE))


if __name__ == "__main__":
    main()
