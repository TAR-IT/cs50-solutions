import pytest
from working import convert


# Test cases
def test_convert_format1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:30 AM to 2:45 PM") == "00:30 to 14:45"
    assert convert("6:15 PM to 1:30 AM") == "18:15 to 01:30"
    assert convert("11:45 AM to 8:30 PM") == "11:45 to 20:30"


def test_convert_format2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 2 PM") == "00:00 to 14:00"
    assert convert("6 PM to 1 AM") == "18:00 to 01:00"
    assert convert("11 AM to 8 PM") == "11:00 to 20:00"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")  # Missing AM/PM
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Incorrect separator
    with pytest.raises(ValueError):
        convert("12:60 AM to 2 PM")  # Invalid time (60 minutes)


def test_invalid_time():
    with pytest.raises(ValueError):
        convert("13:00 AM to 2:00 PM")  # Invalid hour (13)
    with pytest.raises(ValueError):
        convert("12:00 PM to 13:00 PM")  # Invalid time (13 PM)


# Run the tests
if __name__ == "__main__":
    pytest.main(["test_working.py"])
