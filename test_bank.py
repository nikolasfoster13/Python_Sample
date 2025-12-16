from bank import value

def test_bank_hello():
    assert value("Hello").lower() == "$0"

def test_bank_hi():
    assert value("Hi").lower() == "$20"

def test_bank_whats_up():
    assert value("What's up") == "$100"
    
