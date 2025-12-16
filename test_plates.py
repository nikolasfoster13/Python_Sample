from plates import is_valid

def test_start():
    assert is_valid("11") == False


def test_length():
    assert is_valid("A") == False
    assert is_valid("AAAAAAAA") == False
    assert is_valid("AA") == True

def test_is_valid_non_an():
    assert is_valid("_A") == False
    assert is_valid("AA") == True

def test_is_valid_middle_num():
    assert is_valid("A2A") == False
    assert is_valid("AA") == True

def test_is_valid_zero_start():
    assert is_valid("A0") == False
    assert is_valid("A2") == True

def test_is_valid():
    assert is_valid("AA") == True
