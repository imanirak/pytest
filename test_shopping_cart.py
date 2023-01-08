from shopping_cart import ShoppingCart

def test_can_add_item_to_cart():
    cart = ShoppingCart()
    cart.add("apple")
    cart.size() == 1
    assert cart.size() == 1