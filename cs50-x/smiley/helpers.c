#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE pixels[height][width])
{
    // Iterate through each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Check if the pixel is black (0, 0, 0)
            if (pixels[i][j].rgbtRed == 0 && pixels[i][j].rgbtGreen == 0 && pixels[i][j].rgbtBlue == 0)
            {
                // Change the color of the black pixel
                pixels[i][j].rgbtRed = 255;
                pixels[i][j].rgbtGreen = 0;
                pixels[i][j].rgbtBlue = 0;
            }
        }
    }
}
