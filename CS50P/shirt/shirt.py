import sys
import os
from PIL import Image, ImageOps

def resize_and_crop(input_path, output_path, shirt_path):
    try:
        # Open the input image
        input_image = Image.open(input_path)

        # Open the shirt image
        shirt = Image.open(shirt_path)

        # Resize and crop the input image to match the size of the shirt
        resized_input = ImageOps.fit(input_image, shirt.size)

        # Overlay the shirt on the resized input image
        resized_input.paste(shirt, (0, 0), shirt)

        # Save the output image
        resized_input.save(output_path)

        print("Virtual shirt applied successfully!")

    except FileNotFoundError:
        print("Error: The specified input image does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python shirt.py <input_image> <output_image>")
        sys.exit(1)

    # Get the input and output file paths from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the file extensions are valid (jpeg, jpg, or png)
    valid_extensions = ['.jpg', '.jpeg', '.png']
    input_extension = os.path.splitext(input_file)[1].lower()
    output_extension = os.path.splitext(output_file)[1].lower()

    if input_extension not in valid_extensions or output_extension not in valid_extensions:
        print("Error: Invalid file extension. The input and output files must be JPEG or PNG images.")
        sys.exit(1)

    # Check if the input and output file extensions match
    if input_extension != output_extension:
        print("Error: The input and output file extensions must be the same.")
        sys.exit(1)

    # Check if the input image exists
    if not os.path.exists(input_file):
        print("Error: The specified input image does not exist.")
        sys.exit(1)

    # The path to the shirt image (Assuming it's called "shirt.png" and in the same directory as the script)
    shirt_path = "shirt.png"

    # Call the function to resize, crop, and overlay the shirt on the input image
    resize_and_crop(input_file, output_file, shirt_path)
