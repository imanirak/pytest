from shopping_cart import ShoppingCart
import pytest

def test_can_add_item_to_cart():
    cart = ShoppingCart(5)
    cart.add("apple")
    cart.size() == 1
    assert cart.size() == 1
    
def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert "apple" in cart.get_items()
    
def test_when_add_more_than_max_items_should_fail():
    cart = ShoppingCart(5)
    for i in range(5):
        cart.add("apple")
        # checks after cart is filled with more than max items
    with pytest.raises(OverflowError):
            cart.add("apple")
