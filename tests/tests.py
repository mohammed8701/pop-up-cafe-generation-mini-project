import pytest
import functions

mock_prod_name = "coke cherry"
def test_item_name(monkeypatch):
    monkeypatch.setattr('builtins.input',mock_prod_name)
    actual = functions.item_name("Product")
    expected = "Coke Cherry"
    assert actual == expected
    
mock_price = "2.4333333"
def test_item_second_attr(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_price)
    actual = functions.add_item_second_attr("Product","price")
    expected = 2.43
    assert actual == expected

mock_number = "073453453"
def test_item_second_attr_2(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_number)
    actual = functions.add_item_second_attr("Courier","phone number")
    expected = 73453453
    assert actual == expected

mock_address = "64 zoo lane"
def test_order_addrress(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_address)
    actual = functions.order_address()
    expected = "64 Zoo Lane"
    assert actual == expected
    
mock_name = "thomas JEFFERSON"
def test_order_name(monkeypatch):
    monkeypatch.setattr('builtins.input', mock_name)
    actual = functions.order_name()
    expected = "Thomas Jefferson"
    assert actual == expected   
    
mock_phone = "074651161"
def test_order_phone(monkeypatch):
    monkeypatch.setattr('builtins.input',mock_phone)
    actual = functions.order_phone()
    expected = "074651161"
    assert actual == expected
