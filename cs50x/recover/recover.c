#include <stdint.h>
#include <stdio.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for correct usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s IMAGE\n", argv[0]);
        return 1;
    }

    // Open the forensic image
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open file %s\n", argv[1]);
        return 1;
    }

    // Create variables to track the current JPEG file
    FILE *output = NULL;
    int jpeg_count = 0;
    BYTE buffer[512];

    while (fread(buffer, 1, 512, file) == 512)
    {
        // Check for the start of a JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous JPEG (if any)
            if (output != NULL)
            {
                fclose(output);
            }

            // Create a new JPEG file
            char filename[8];
            sprintf(filename, "%03i.jpg", jpeg_count++);
            output = fopen(filename, "w");
            if (output == NULL)
            {
                fprintf(stderr, "Could not create output file\n");
                return 1;
            }
        }

        // Write the current block to the JPEG file
        if (output != NULL)
        {
            fwrite(buffer, 1, 512, output);
        }
    }

    // Close the last JPEG
    if (output != NULL)
    {
        fclose(output);
    }

    // Close the forensic image
    fclose(file);

    return 0;
}
