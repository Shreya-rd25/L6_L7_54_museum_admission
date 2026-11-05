
import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


# Ticket category and age branches
def test_ticket_category():
    with pytest.raises(ValueError):
        ticket_price("invalid", 20, "tuesday", False)

    assert ticket_price("adult", 30, "tuesday", False) == 300


def test_age_branches():
    with pytest.raises(ValueError):
        ticket_price("adult", -1, "tuesday", False)

    assert ticket_price("adult", 4, "tuesday", False) == 0
    assert ticket_price("adult", 5, "tuesday", False) == 300


# Day branches
def test_day_branches():
    assert ticket_price("adult", 30, "monday", False) == 150
    assert ticket_price("adult", 30, "saturday", False) == 350
    assert ticket_price("adult", 30, "sunday", False) == 350
    assert ticket_price("adult", 30, "tuesday", False) == 300


# Guided tour branches
def test_guided_tour_branches():
    assert ticket_price("student", 20, "tuesday", True) == 200
    assert ticket_price("adult", 30, "tuesday", True) == 400
    assert ticket_price("student", 20, "tuesday", False) == 150


# Group discount branches
def test_group_size_validation():
    with pytest.raises(ValueError):
        group_discount(0, False)

    assert group_discount(1, False) == 0


def test_school_group_branches():
    assert group_discount(20, True) == 40
    assert group_discount(19, True) == 25


def test_regular_group_branches():
    assert group_discount(15, False) == 20
    assert group_discount(8, False) == 10
    assert group_discount(7, False) == 0


# Gallery entry branches
def test_gallery_full():
    assert gallery_entry(100, 100, False) == "wait"
    assert gallery_entry(110, 100, False) == "wait"


def test_gallery_capacity_branches():
    assert gallery_entry(80, 100, False) == "enter"
    assert gallery_entry(90, 100, False) == "queue"
    assert gallery_entry(95, 100, False) == "queue"
    assert gallery_entry(95, 100, True) == "enter"
    assert gallery_entry(50, 100, True) == "enter"
