from plates import is_valid

def test_start():
    is_valid("111") == False

def test_length():
    is_valid("A") == False
    is_valid("AAAA234AAAA") == False

def test_is_valid_non_an():
    is_valid("AA_23") == False

def test_is_valid_middle_num():
    is_valid("AA2AA") == False

def test_is_valid_zero_start():
    is_valid("AA002") == False

def test_is_valid():
    is_valid("AA222") == True
