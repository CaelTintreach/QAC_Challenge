import pytest
import RectangleClass

def test_rectangle():
    ra = RectangleClass.Rectangle_(70,60)
    assert ra.returnArea() == 4200 
