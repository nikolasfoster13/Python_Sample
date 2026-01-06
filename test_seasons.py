from datetime import date, timedelta
from seasons import date_diff, num_to_word
import pytest

def test_date_diff():
    assert date_diff(str(date.today())) == 0
    assert date_diff(str(date.today() - timedelta(days=1))) == 1440
    with pytest.raises(SystemExit):
        date_diff("05-27-1998")

def test_num_to_word():
    assert num_to_word(1) == "one"
    assert num_to_word(111) == "one hundred eleven"
    assert num_to_word(1111) == "one thousand, one hundred eleven"
    assert num_to_word(1111111) == "one million, one hundred eleven thousand, one hundred eleven"
