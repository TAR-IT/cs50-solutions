import emoji

def main():
    english_text = input("Enter the text in English: ")
    emojized_text = emoji.emojize(english_text)
    print(emojized_text)

if __name__ == "__main__":
    main()