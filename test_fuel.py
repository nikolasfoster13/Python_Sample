import pytest
from fuel import convert, gauge

def test_convert():
    with pytest.raises(ValueError):
        convert("3")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("4/1")
    with pytest.raises(ValueError):
        convert("-3/1")
    with pytest.raises(ValueError):
        convert("1/-3")
    with pytest.raises(ValueError):
        convert("2.5/4")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    assert convert("1/4") == 25
def test_gague():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(5) == "5%"
    assert gauge(10) == "10%"
