from cs50 import get_string


def main():
    # Get user input
    text = get_string("Text: ")

    # Count letters, words, and sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate Coleman-Liau index
    index = coleman_liau_index(letters, words, sentences)

    # Print the grade level
    print_grade(index)


def count_letters(text):
    return sum(c.isalpha() for c in text)


def count_words(text):
    return len(text.split())


def count_sentences(text):
    sentence_endings = [".", "!", "?"]
    return sum(text.count(end) for end in sentence_endings)


def coleman_liau_index(letters, words, sentences):
    L = (letters / words) * 100
    S = (sentences / words) * 100
    return round(0.0588 * L - 0.296 * S - 15.8)


def print_grade(index):
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


if __name__ == "__main__":
    main()
