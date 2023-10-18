import plates


def test_is_valid_valid_plates():
    assert plates.is_valid("AA1234")
    assert plates.is_valid("ABCDEF")
    assert plates.is_valid("XY123")
    assert plates.is_valid("AA9999")


def test_is_valid_invalid_plates():
    assert not plates.is_valid("A")
    assert not plates.is_valid("123")
    assert not plates.is_valid("1234567")
    assert not plates.is_valid("0A1234")
    assert not plates.is_valid("AA123A")
    assert not plates.is_valid("A!B123")
    assert not plates.is_valid("AA0A123")


def test_is_valid_edge_cases():
    assert plates.is_valid("AB")
    assert plates.is_valid("ABC")
    assert plates.is_valid("ABCDEF")
    assert plates.is_valid("XY1234")


if __name__ == "__main__":
    test_is_valid_valid_plates()
    test_is_valid_invalid_plates()
    test_is_valid_edge_cases()
    print("All tests passed.")
