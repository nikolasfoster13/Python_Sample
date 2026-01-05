from um import count
import pytest

# Test case sensitivity and white space
def test_um():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("um um") == 2
    assert count("   um") == 1
    assert count("um   ") == 1
    assert count("um, um") == 2

# Test count of nested "um"
def test_nested():
    assert count("yummy") == 0
    assert count("yummy um") == 1

# Test absence of "um"
def test_null():
    assert count("   ") == 0
