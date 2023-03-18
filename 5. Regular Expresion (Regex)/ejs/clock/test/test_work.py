import pytest
from working import convert

def test_simple():
    assert convert("4 AM to 1 PM") == "4 to 13"
    assert convert("1 AM to 2 PM") == "1 to 14"
    assert convert("4 PM to 1 PM") == "16 to 13"
    assert convert("4 PM to 1 AM") == "16 to 1"
    assert convert("0 AM to 0 PM") == "0 to 12"
    assert convert("10 PM to 8 AM") == "22 to 8"

def test_notSimple():
    assert convert("4:32 AM to 1:12 AM") == "4:32 to 1:12"
    assert convert("4:00 AM to 3:61 PM") == None
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 8:50"
    assert convert("9:60 AM to 5:60 PM") == None
    assert convert("9 AM - 5 PM") == None


