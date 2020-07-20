import pytest
from programs import string_gen

def test_string_basic():
    assert string_gen.string_gen(basic) == True

def test_string_false():
    assert string_gen.string_gen(fAlse) == False

def test_string_length():
    assert string_gen.string_gen != len(5) == False

def test_string_case():
    assert string_gen.string_gen if any(x.isupper for x in string_gen) == False