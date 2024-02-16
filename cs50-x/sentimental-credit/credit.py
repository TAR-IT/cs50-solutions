import re


# Function to check if a credit card number is valid
def is_valid_credit_card(card_number):
    # Implement Luhn’s algorithm to check the validity of the card number
    # Double every second digit from right to left
    card_number = list(map(int, card_number))
    for i in range(len(card_number) - 2, -1, -2):
        card_number[i] *= 2
        if card_number[i] > 9:
            card_number[i] -= 9

    # Sum all the digits
    total = sum(card_number)

    # Check if the total sum modulo 10 equals 0
    return total % 10 == 0


# Prompt the user for a credit card number
def main():
    card_number = input("Number: ")

    # Check if the input is entirely numeric and of the correct length
    if re.match("^\d{13,16}$", card_number):
        if is_valid_credit_card(card_number):
            if card_number[0] == "4" and (
                len(card_number) == 13 or len(card_number) == 16
            ):
                print("VISA")
            elif card_number[:2] in ["34", "37"] and len(card_number) == 15:
                print("AMEX")
            elif 51 <= int(card_number[:2]) <= 55 and len(card_number) == 16:
                print("MASTERCARD")
            else:
                print("INVALID")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
