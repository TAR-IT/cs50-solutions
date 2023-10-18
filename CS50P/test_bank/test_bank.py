import bank


def test_value_hello():
    assert bank.value("Hello, world!") == 0
    assert bank.value("Hello") == 0
    assert bank.value("hello there") == 0


def test_value_h():
    assert bank.value("hola") == 20
    assert bank.value("Hi!") == 20
    assert bank.value("heya") == 20


def test_value_other():
    assert bank.value("Welcome") == 100
    assert bank.value("Hey") == 20
    assert bank.value("goodbye") == 100


def test_value_case_insensitive():
    assert bank.value("hEllO") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("Hello") == 0
    assert bank.value("HeYa") == 20
    assert bank.value("HEllo") == 0
    assert bank.value("welcomE") == 100


if __name__ == "__main__":
    test_value_hello()
    test_value_h()
    test_value_other()
    test_value_case_insensitive()
    print("All tests passed.")
