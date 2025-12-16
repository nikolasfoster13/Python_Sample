from plates import is_valid

def test_start():
    assert is_valid("11") == False
    assert is_valid("1A") == False
    assert is_valid("AA") == True

def test_length():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAA") == True
    assert is_valid("AAAA") == True
    assert is_valid("AAAAA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAAAAA") == False

def test_is_valid_non_an():
    assert is_valid("AA!") == False
    assert is_valid("AAA") == True

def test_is_valid_middle_num():
    assert is_valid("AA2A") == False
    assert is_valid("AA2") == True

def test_is_valid_zero_start():
    assert is_valid("AA0") == False
    assert is_valid("AA2") == True

def test_is_valid():
    assert is_valid("AA") == True
