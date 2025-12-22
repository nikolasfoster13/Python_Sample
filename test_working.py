from working import convert
import pytest

def test_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("12 AM to 8 AM") == "00:00 to 08:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5 AM") == "21:00 to 05:00"
    assert convert("12:00 AM to 8 AM") == "00:00 to 08:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("12 AM to 8:00 AM") == "00:00 to 08:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("12:00 AM to 8:00 AM") == "00:00 to 08:00"

def test_nonint():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("cat to cat")
    with pytest.raises(ValueError):
        convert("12 AM - 8 AM")
    with pytest.raises(ValueError):
        convert("cat - cat")
    with pytest.raises(ValueError):
        convert("17 PM - 20 PM")
    with pytest.raises(ValueError):
        convert("12:60 PM - 4:60 AM")

