from fuel import convert, gauge
import pytest

def test_valid_input():
    assert convert("1/3") == 33
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_invalid_input():
    with pytest.raises(ValueError):
        convert("150/100") 
    with pytest.raises(ZeroDivisionError):
        convert("50/0")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert(",.?!")


def test_gauge():

    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(45) == "45%"

