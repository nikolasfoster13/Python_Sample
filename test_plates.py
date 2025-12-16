from plates import is_valid

def test_start():
    is_valid("11") == False

def test_length():
    is_valid(" A") == False
    is_valid("AAAA234AAAA") == False

def test_is_valid_non_an():
    is_valid("_A") == False

def test_is_valid_middle_num():
    is_valid("A2A") == False

def test_is_valid_zero_start():
    is_valid("AA002") == False

def test_is_valid():
    is_valid("AA222") == True
