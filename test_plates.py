from plates import is_valid

def test_start():
    is_valid("11") == False
    is_valid("AA") == True

def test_length():
    is_valid("A") == False
    is_valid("AAAAAAAA") == False
    is_valid("AA") == True

def test_is_valid_non_an():
    is_valid("_A") == False
    is_valid("AA") == True

def test_is_valid_middle_num():
    is_valid("A2A") == False
    is_valid("AA") == True

def test_is_valid_zero_start():
    is_valid("A0") == False
    is_valid("A2") == True

def test_is_valid():
    is_valid("AA") == True
