#include <cs50.h>
#include <stdio.h>
#include <math.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    int cents = get_cents();
    int quarters = calculate_quarters(cents);
    int dimes = calculate_dimes(cents);
    int nickels = calculate_nickels(cents);
    int pennies = calculate_pennies(cents);

    int total_coins = quarters + dimes + nickels + pennies;
    printf("%i\n", total_coins);
}

int get_cents(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    return cents;
}

int calculate_quarters(int cents)
{
    int quarters = cents / 25;
    return quarters;
}

int calculate_dimes(int cents)
{
    int dimes = (cents % 25) / 10;
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickels = ((cents % 25) % 10) / 5;
    return nickels;
}

int calculate_pennies(int cents)
{
    int pennies = ((cents % 25) % 10) % 5;
    return pennies;
}
