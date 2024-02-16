import fuel


def test_convert_valid_input():
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/2") == 50
    assert fuel.convert("3/4") == 75
    assert fuel.convert("2/3") == 67


def test_convert_invalid_input():
    try:
        fuel.convert("3/0")
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

    try:
        fuel.convert("3/a")
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        fuel.convert("4/3")  # X is greater than Y
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(98) == "98%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"


if __name__ == "__main__":
    test_convert_valid_input()
    test_convert_invalid_input()
    test_gauge()
    print("All tests passed.")
