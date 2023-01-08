from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(5)

@pytest.fixture
def itemDB():
    return ItemDatabase()

def test_can_add_item_to_cart(cart):
    cart.add("apple")
    cart.size() == 1
    assert cart.size() == 1
    
def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()
    
def test_when_add_more_than_max_items_should_fail(cart):
    for i in range(5):
        cart.add("apple")
        # checks after cart is filled with more than max items
    with pytest.raises(OverflowError):
            cart.add("apple")

def test_can_get_total_price(cart, itemDB):
    cart.add("apple")
    cart.add("orange")
    cart.add("pear")
    
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0
        if item == "pear":
            return 3.0
        
    itemDB = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(itemDB) == 6.00
