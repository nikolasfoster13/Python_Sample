from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert str(jar) == ""

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar._size == 6
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(1)
    assert jar._size == 5
    with pytest.raises(ValueError):
        jar.withdraw(100)
