
import pytest
from museum_admission import ticket_price, group_discount, gallery_entry

def test_ticket_prices():
    assert ticket_price("adult", 30, "tuesday", False) == 300
    assert ticket_price("student", 20, "tuesday", False) == 150
    assert ticket_price("child", 10, "tuesday", False) == 100
    assert ticket_price("senior", 65, "tuesday", False) == 200

def test_ticket_errors():
    with pytest.raises(ValueError):
        ticket_price("invalid", 20, "tuesday", False)
    with pytest.raises(ValueError):
        ticket_price("adult", -1, "tuesday", False)

def test_free_ticket():
    assert ticket_price("adult", 3, "tuesday", False) == 0

def test_day_prices():
    assert ticket_price("adult", 30, "monday", False) == 150
    assert ticket_price("adult", 30, "saturday", False) == 350

def test_guided_tour():
    assert ticket_price("student", 20, "tuesday", True) == 200
    assert ticket_price("adult", 30, "tuesday", True) == 400

def test_group_discounts():
    assert group_discount(4, False) == 0
    assert group_discount(8, False) == 10
    assert group_discount(15, False) == 20
    assert group_discount(20, True) == 40
    assert group_discount(10, True) == 25

def test_group_error():
    with pytest.raises(ValueError):
        group_discount(0, False)

def test_gallery():
    assert gallery_entry(100, 100, False) == "wait"
    assert gallery_entry(95, 100, False) == "queue"
    assert gallery_entry(95, 100, True) == "enter"
    assert gallery_entry(50, 100, False) == "enter"
