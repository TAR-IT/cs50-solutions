from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    assert jar.size == 0

    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(3)
    assert jar.size == 8

    try:
        jar.deposit(3)  # Exceeds the capacity
    except ValueError as e:
        assert str(e) == "Exceeds the cookie jar's capacity."
    else:
        assert False, "Should have raised ValueError."

def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)
    assert jar.size == 7

    jar.withdraw(3)
    assert jar.size == 4

    jar.withdraw(2)
    assert jar.size == 2

    try:
        jar.withdraw(3)  # Not enough cookies in the jar
    except ValueError as e:
        assert str(e) == "Not enough cookies in the cookie jar."
    else:
        assert False, "Should have raised ValueError."

if __name__ == "__main__":
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
    print("All tests passed!")
