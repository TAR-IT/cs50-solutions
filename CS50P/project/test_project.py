from project import dechordify, dekeyify, chordify

def test_dechordify():
    # Test known chords
    assert dechordify("BbmMaj7") == ["Bb", "Db", "F", "A"]
    assert dechordify("A#9/C") == ["C", "A#", "D", "F", "G#", "C#"]
    assert dechordify("Cb6") == ["Cb", "Ebb", "Abb", "B"]

    # Test unknown chords
    assert dechordify("UnknownChord") is None

def test_chordify():
    # Test with chords that match the provided notes
    notes_list = ["C", "D", "D#", "F", "G"]
    assert chordify(notes_list) == ["Cm11", "Cm13"]

def test_dekeyify():
    # Test known keys
    assert dekeyify("Fm") == ["F", "G", "G#", "A#", "C", "C#", "D#"]
    assert dekeyify("C") == ["C", "D", "E", "F", "G", "A", "B"]
    assert dekeyify("Eb") == ["Eb", "F", "G", "Ab", "Bb", "C", "D"]

    # Test unknown keys
    assert dekeyify("UnknownKey") is None