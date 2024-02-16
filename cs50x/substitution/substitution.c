#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int is_valid_key(string key);
string encrypt(string plaintext, string key);

int main(int argc, string argv[])
{
    // Check for correct command-line usage
    if (argc != 2 || !is_valid_key(argv[1]))
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Get the key from the command-line argument
    string key = argv[1];

    // Prompt the user for plaintext input
    string plaintext = get_string("plaintext: ");

    // Encrypt and print the ciphertext
    string ciphertext = encrypt(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

// Check if the key is valid
int is_valid_key(string key)
{
    int key_length = strlen(key);
    if (key_length != 26)
    {
        return 0; // Key length must be 26 characters
    }

    int freq[26] = {0}; // Initialize an array to track character frequencies

    for (int i = 0; i < key_length; i++)
    {
        if (!isalpha(key[i]))
        {
            return 0; // Key contains non-alphabetic characters
        }

        int index = tolower(key[i]) - 'a';

        if (freq[index] > 0)
        {
            return 0; // Key contains duplicate characters
        }

        freq[index]++;
    }

    return 1;
}

// Encrypt plaintext using the provided key
string encrypt(string plaintext, string key)
{
    int length = strlen(plaintext);
    for (int i = 0; i < length; i++)
    {
        if (isalpha(plaintext[i]))
        {
            char shift = isupper(plaintext[i]) ? 'A' : 'a';
            char substitute = key[tolower(plaintext[i]) - 'a'];

            if (isupper(plaintext[i]))
            {
                plaintext[i] = toupper(substitute);
            }
            else
            {
                plaintext[i] = tolower(substitute);
            }
        }
    }
    return plaintext;
}
