from numb3rs import validate

def test_valid_ipv4_addresses():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("10.20.30.40") == True
    assert validate("172.16.0.1") == True

def test_invalid_ipv4_addresses():
    assert validate("256.256.256.256") == False
    assert validate("1.2.3.4.5") == False
    assert validate("300.12.34.56") == False
    assert validate("hello.world") == False
    assert validate("192.168.1") == False
    assert validate("172.16.0.256") == False
    assert validate("10.10.10.") == False

if __name__ == "__main__":
    test_valid_ipv4_addresses()
    test_invalid_ipv4_addresses()
    print("All tests passed!")
