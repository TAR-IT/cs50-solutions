def has_minimum_letters(s):
    return len(s) >= 2 and s[:2].isalpha()

def has_valid_length(s):
    return 2 <= len(s) <= 6

def has_numbers_at_end(s):
    if not s[-1].isdigit():
        return False
    if s[0].isdigit() or '0' in s[:-1]:
        return False
    return True

def has_no_invalid_characters(s):
    return s.isalnum()

def is_valid(s):
    return (
        has_minimum_letters(s)
        and has_valid_length(s)
        and (s.isalpha() or has_numbers_at_end(s))
        and has_no_invalid_characters(s)
    )


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
