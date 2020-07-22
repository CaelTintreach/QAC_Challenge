import pytest
from programs import string_gen

def test_string_basic():
    assert string_gen.string_gen(basic) == True

def test_string_false():
    assert string_gen.string_gen(fAlse) == False

def test_string_length():
    assert string_gen.string_gen != len(5) == False

def test_string():
    assert isinstance(string_gen.string_gen(), str) == True

def test_length():
    assert len(string_gen.string_gen()) == 5

def test_lower_case():
    assert string_gen.string_gen().islower() == True

def test_upper_case():
    assert string_gen.string_gen().isupper() == False