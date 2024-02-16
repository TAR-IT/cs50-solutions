import sys
from pyfiglet import Figlet

def print_usage():
    print("Usage: python figlet.py [-f|--font font_name]")
    sys.exit(1)

def get_available_fonts():
    figlet = Figlet()
    return figlet.getFonts()

def main():
    if len(sys.argv) not in [1, 3]:
        print_usage()

    if len(sys.argv) == 1:  # Random font
        font_name = None
    elif len(sys.argv) == 3:  # Specific font
        if sys.argv[1] not in ['-f', '--font']:
            print_usage()
        font_name = sys.argv[2]
        available_fonts = get_available_fonts()
        if font_name not in available_fonts:
            print("Error: Invalid font name. Available fonts:")
            print(", ".join(available_fonts))
            sys.exit(1)

    figlet = Figlet(font=font_name) if font_name else Figlet()

    user_input = input("Enter your text: ")
    output = figlet.renderText(user_input)
    print(output)

if __name__ == "__main__":
    main()
