#include <cs50.h>
#include <stdio.h>

// Function prototypes
bool is_valid(long long card_number);
int get_card_type(long long card_number);

int main(void)
{
    long long card_number;

    // Prompt the user for a credit card number
    do
    {
        card_number = get_long("Number: ");
    }
    while (card_number < 0);

    // Check if the credit card number is valid
    if (is_valid(card_number))
    {
        int card_type = get_card_type(card_number);

        // Print the card type
        switch (card_type)
        {
            case 1:
                printf("AMEX\n");
                break;
            case 2:
                printf("MASTERCARD\n");
                break;
            case 3:
                printf("VISA\n");
                break;
            default:
                printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

bool is_valid(long long card_number)
{
    int sum = 0;
    int digit_count = 0;

    while (card_number > 0)
    {
        int digit = card_number % 10;

        // Double every other digit, starting from the right
        if (digit_count % 2 == 1)
        {
            digit *= 2;

            // If doubling results in a two-digit number, add the digits
            if (digit > 9)
            {
                digit = digit % 10 + 1;
            }
        }

        sum += digit;
        card_number /= 10;
        digit_count++;
    }

    // Check if the sum's last digit is 0
    return (sum % 10 == 0);
}

int get_card_type(long long card_number)
{
    // Check if it's an American Express card
    if ((card_number >= 34e13 && card_number < 35e13) || (card_number >= 37e13 && card_number < 38e13))
    {
        return 1; // AMEX
    }

    // Check if it's a MasterCard
    if ((card_number >= 51e14 && card_number < 56e14))
    {
        return 2; // MASTERCARD
    }

    // Check if it's a Visa
    if (card_number >= 4e12 && card_number < 5e12)
    {
        return 3; // VISA
    }

    return 0; // Invalid
}
