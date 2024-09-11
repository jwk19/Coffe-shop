import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order():
    james = Customer("James")
    latte = Coffee("Latte")
    order = Order(james, latte, 5.0)

    assert order.customer == james
    assert order.coffee == latte
    assert order.price == 5.0

    with pytest.raises(ValueError):
        Order(james, latte, 0)  
