// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choose the number of buckets in the hash table (e.g., 26 for the English alphabet)
const unsigned int N = 26;

// Hash table
node *table[N];

// Global variable to keep track of the total number of words in the dictionary
unsigned int word_count = 0;

// Hash function
unsigned int hash(const char *word)
{
    // Simple hash function for lowercase words
    return tolower(word[0]) - 'a';
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Convert the word to lowercase for case-insensitive checking
    char lowercase_word[LENGTH + 1];
    int i = 0;
    while (word[i] != '\0' && i < LENGTH)
    {
        lowercase_word[i] = tolower(word[i]);
        i++;
    }
    lowercase_word[i] = '\0';

    // Get the hash value for the lowercase word
    int index = hash(lowercase_word);

    // Traverse the linked list at the hash index
    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcmp(lowercase_word, cursor->word) == 0)
        {
            return true; // Word found in the dictionary
        }
        cursor = cursor->next;
    }

    return false; // Word not found
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Initialize the hash table
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Open the dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Buffer to store a word from the dictionary file
    char word[LENGTH + 1];

    // Read words from the dictionary and add them to the hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // Create a new node for the word
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            return false;
        }

        // Copy the word into the new node
        strcpy(new_node->word, word);

        // Get the hash index for the word
        int index = hash(word);

        // Insert the new node at the beginning of the linked list
        new_node->next = table[index];
        table[index] = new_node;

        // Increment the word count
        word_count++;
    }

    // Close the dictionary file
    fclose(file);

    return true;
}

// Returns the number of words in the dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        // Free the nodes in the linked list
        while (table[i] != NULL)
        {
            node *temp = table[i];
            table[i] = table[i]->next;
            free(temp);
        }
    }

    return true;
}
