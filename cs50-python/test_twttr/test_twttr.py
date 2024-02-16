import twttr


def test_shorten_no_vowels():
    assert twttr.shorten("python") == "pythn"
    assert twttr.shorten("hello") == "hll"
    assert twttr.shorten("algorithm") == "lgrthm"


def test_shorten_with_vowels():
    assert twttr.shorten("Artificial") == "rtfcl"
    assert twttr.shorten("Intelligence") == "ntllgnc"
    assert twttr.shorten("PYTHON") == "PYTHN"


def test_shorten_empty_string():
    assert twttr.shorten("") == ""


def test_shorten_all_vowels():
    assert twttr.shorten("aeiouAEIOU") == ""
    assert twttr.shorten("AeIoU") == ""
    assert twttr.shorten("aeiOU") == ""


def test_shorten_with_numbers():
    assert twttr.shorten("hello123") == "hll123"
    assert twttr.shorten("twttr99") == "twttr99"


def test_shorten_with_punctuation():
    assert twttr.shorten("Hello, World!") == "Hll, Wrld!"
    assert twttr.shorten("Testing...") == "Tstng..."


if __name__ == "__main__":
    test_shorten_no_vowels()
    test_shorten_with_vowels()
    test_shorten_empty_string()
    test_shorten_all_vowels()
    test_shorten_with_numbers()
    test_shorten_with_punctuation()
    print("All tests passed.")
