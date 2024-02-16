#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    // Prompt the user for a positive integer between 1 and 8, inclusive
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Build the pyramid
    for (int i = 1; i <= height; i++)
    {
        // Print spaces for left pyramid
        for (int j = height - i; j > 0; j--)
        {
            printf(" ");
        }

        // Print hashes for left pyramid
        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }

        // Gap between pyramids
        printf("  ");

        // Print hashes for right pyramid
        for (int l = 1; l <= i; l++)
        {
            printf("#");
        }

        // Move to the next line for the next row
        printf("\n");
    }

    return 0;
}
