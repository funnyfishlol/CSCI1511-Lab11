import pytest
from Lab11_funnyfishlol_1 import adjust_angle

def test_adjust_angle_with_correct_input_positive():
    assert adjust_angle(100) == 100
    assert adjust_angle(460) == 100
    assert adjust_angle(820) == 100

def test_adjust_angle_with_correct_input_negative():
    assert adjust_angle(-100) == 260
    assert adjust_angle(-460) == 260
    assert adjust_angle(-820) == 260

def test_adjust_angle_with_string_input():
    assert adjust_angle("360") == None
    assert adjust_angle("Hello") == None

def test_adjust_angle_with_large_positive_input():
    assert adjust_angle(360000) == 0
    assert adjust_angle(720090) == 90

def test_adjust_angle_with_large_negative_input():
    assert adjust_angle(-360000) == 0
    assert adjust_angle(-720090) == 270