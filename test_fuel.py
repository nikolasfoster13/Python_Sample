from fuel import convert, gauge

def test_convert():
    assert convert("3") == ValueError
    assert convert("cat") == ValueError
    assert convert("cat/dog") == ValueError
    assert convert("4/1") == ValueError
    assert convert("4/0") == ZeroDivisionError
def test_gague():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(5) == "5%"
    assert gauge(10) == "10%"
