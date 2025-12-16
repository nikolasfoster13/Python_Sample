from plates import is_valid

def test_is_valid_start():
    is_valid("23APE") == False

def test_is_valid_short():
    is_valid("A") == False

def test_is_valid_long():
    is_valid("AAAA234") == False

def test_is_valid_non_an():
    is_valid("AA!23") == False

def test_is_valid_middle_num():
    is_valid("AA2AA") == False

def test_is_valid_zero_start():
    is_valid("AA002") == False

def test_is_valid():
    is_valid("AA222") == True
