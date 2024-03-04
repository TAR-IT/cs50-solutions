from fuel import convert, gauge
import pytest

def test_valid_input():
    assert convert("1/3") == 33
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_invalid_input():
    try:
        convert("150/100")
        assert False
    except ValueError:
        pass

    try:
        convert("50/0")
        assert False
    except ZeroDivisionError:
        pass

    try:
        convert("cat")
        assert False
    except ValueError:
        pass
    try:
        convert(",.?!")
        assert False
    except ValueError:
        pass


def test_gauge():

    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(45) == "45%"

