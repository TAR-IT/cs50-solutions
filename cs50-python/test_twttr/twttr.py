def shorten(word):
    vowels = set("aeiouAEIOU")
    return "".join(char for char in word if char not in vowels or not char.isalpha())


def main():
    word = input("Enter a word: ")
    shortened_word = shorten(word)
    print(shortened_word)


if __name__ == "__main__":
    main()
