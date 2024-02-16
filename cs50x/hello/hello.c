#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for their name
    string name = get_string("What's your name? ");

    // Greet the user
    printf("Hello, %s!\n", name);
}
