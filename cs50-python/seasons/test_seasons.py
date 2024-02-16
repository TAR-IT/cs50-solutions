from datetime import date
from seasons import age_in_minutes

def test_age_in_minutes():
    # Test age in minutes for a few different ages
    dob1 = date(2000, 1, 1)
    assert age_in_minutes(dob1) == 12402720  # 2000-01-01 to today

    dob2 = date(1990, 5, 15)
    assert age_in_minutes(dob2) == 17468640  # 1990-05-15 to today

    dob3 = date(1985, 9, 30)
    assert age_in_minutes(dob3) == 19899360  # 1985-09-30 to today

if __name__ == "__main__":
    test_age_in_minutes()
    print("All tests passed!")
