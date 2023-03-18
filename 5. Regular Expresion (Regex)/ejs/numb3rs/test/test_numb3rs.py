import pytest
from validate import validate

def test_normal():
    assert validate("1.4.5.6")
    assert validate("1.55.200.1")

def test_cornerCases():
    assert validate("0.4.255.2")
    assert validate("0.0.0.0")
    assert validate("0.255.0.255")
    assert validate("255.255.255.255")
    assert not validate("0.256.23.11")
    assert not validate("512.512.512.512")
    assert not validate("1.2.3.1000")
    assert not validate("cat")

def test_negatives():
    assert not validate("43.22.-5.3")
    assert not validate("55.34.-1.-2")