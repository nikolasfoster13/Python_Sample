from numb3rs import validate

# Test that length of IP address is 4 ints sep by "."
def test_len():
    assert validate("1") == False
    assert validate("1.1") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.1") == True
    assert validate("1.1.1.1.1") == False

# Test that each value of IP address is within range of 0-255
def test_int():
    assert validate("256.255.255.255") == False
    assert validate("-1.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.-1.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.-1.255") == False
    assert validate("255.255.255.256") == False
    assert validate("255.255.255.-1") == False
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

# Test that each value of the input is an int
def test_str():
    assert validate("cat") == False
    assert validate("cat.0.0.0") == False
    assert validate("0.cat.0.0") == False
    assert validate("0.0.cat.0") == False
    assert validate("0.0.0.cat") == False
