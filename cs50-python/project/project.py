### This is the "(de)chordifyer".
### It allows the user to break down chords and keys into their corresponding notes.
### You can also find chords by typing in notes using the "Chord Finder" function.
### To use the program properly, the "keys_chords.py" file has to be in the same directory as this script.
### (Please note: There are about 4000 unique chords that you can make using more than 3 notes and over 100 Million different chord names - I was not able to implement all of them yet.)
### ENJOY!

from keys_chords import key_notes, chord_notes ### Importing the dictionaries containing the chords and keys (and their corresponding notes).

def main(): # This is the main function - all the loops, questions asked and available choices.

    print("Hey there, I am the (De)chordifyer! Type 'Chordify', 'Dechordify' or 'Dekeyify'.\nIf you need help with how to use this program, type 'Help'.")

    while True: # The main loop after the greeting.
        try:
            choice = input("What can I help you with? ").strip().lower() # User input prompt.

            if choice == "help": # If the user chooses "Help".
                print(f"I can either help you 'chordify' some notes you want to use, 'dechordify' a chord into notes\nor even 'dekeyify' a key into notes.")
                print("To see the notes of a chord, type 'Dechordify'.\nTo see the notes of a key, type 'Dekeyify'.\nTo get chords from typing in notes, type 'Chordify'.\nOtherwise you can exit the program by pressing CTRL + C.")

            if choice == "dechordify": # If the user chooses to "dechordify".
                while True:
                    chord = input("What chord do you want to dechordify? (e.g. Am or C#) ")
                    notes = dechordify(chord)
                    if notes:
                        print(f"The notes in the chord of {chord} are:", ", ".join(notes))
                        break
                    else:
                        print("Oops. I don't knot that chord. Try again. (e.g. Am or C#) ")

            elif choice == "chordify": # If the User chooses to "chordify".
                while True:
                    notes_input = input("Enter the notes (comma-separated) you want to find chords for: (Press CTRL+C to exit) ")
                    notes_list = [note.strip() for note in notes_input.split(",")]
                    chords = chordify(notes_list)
                    if chords:
                        print(f"The provided notes fit into the following chords: {', '.join(chords)}")
                        break
                    else:
                        print("I didn't find any chords with those notes. Try again. (Press CTRL+C to exit) ")

            elif choice == "dekeyify": # If the user chooses to "deykeyify".
                while True:
                    key = input("What key do you want to see the notes of? (e.g. Fm or C) ")
                    notes = dekeyify(key)
                    if notes:
                        print(f"The notes in the key of {key} are:", ", ".join(notes))
                        break
                    else:
                        print("Oops. I don't know that key. Try again. (e.g. Fm or C) ")



            else: # If the user types in something invalid.
                print("Enter 'Help', 'Chordify', 'Dechordify', or 'Key'. (Press CTRL+C to exit) ")

        except KeyboardInterrupt: # If the user exits by pressing CTRL + C.
            print("\nYou exited the program using CTRL + C.\nC'ya later!")
            break

def dechordify(chord): # Defining the function for breaking down a chord into notes.
    try:
        return chord_notes[chord]
    except KeyError:
        return None


def dekeyify(key): # Defining the function for breaking down a key into notes.
    try:
        return key_notes[key]
    except KeyError:
        return None


def chordify(notes_list):
    chords = []
    for chord, notes in chord_notes.items():
        if all(note in notes for note in notes_list):
            chords.append(chord)
    return chords

if __name__ == "__main__":
    main()