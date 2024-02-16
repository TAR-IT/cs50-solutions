def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

def main():
    sentence = input("Input a Sentence: ")
    sentence = convert(sentence)
    print(sentence)

main ()