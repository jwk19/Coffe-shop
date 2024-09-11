Coffee Shop
===========================

Project Overview
----------------

This project models a simple coffee shop using Object-Oriented Programming (OOP) principles in Python. The domain consists of three main entities: `Customer`, `Coffee`, and `Order`. The relationships between these entities are modeled through classes and methods that allow for creating customers, placing orders, and associating those orders with coffees.

The project also includes automated tests using `pytest` to ensure that the methods and object relationships work as expected.

Folder Structure
----------------


`coffe_shop/
│
├── customer.py        # Customer class implementation
├── coffee.py          # Coffee class implementation
├── order.py           # Order class implementation
│
├── tests/             # Test files directory
│   ├── test_customer.py  # Unit tests for Customer class
│   ├── test_coffee.py    # Unit tests for Coffee class
│   └── test_order.py     # Unit tests for Order class
│
├── README.md          # This README file
├── LICENSE            # License for the project
└── debug.py           # Optional script for quick debugging`

Classes and Relationships
-------------------------

### Customer Class (`customer.py`)

The `Customer` class models a customer in the coffee shop.

**Attributes**:

-   `name`: The name of the customer (1 to 15 characters).
-   `_orders`: A private list to store the orders placed by the customer.

**Methods**:

-   `place_order(coffee, price)`: Creates an order and associates it with the customer.
-   `orders()`: Returns a list of the customer's orders.
-   `coffees()`: Returns a unique list of coffees the customer has ordered.

### Coffee Class (`coffee.py`)

The `Coffee` class models the coffee available in the shop.

**Attributes**:

-   `name`: The name of the coffee (minimum 3 characters).
-   `_orders`: A list to store orders associated with this coffee.

**Methods**:

-   `orders()`: Returns all orders for that coffee.
-   `num_orders()`: Returns the total number of orders for that coffee.
-   `average_price()`: Returns the average price of orders for the coffee.

### Order Class (`order.py`)

The `Order` class models an individual order placed by a customer for a coffee.

**Attributes**:

-   `customer`: The `Customer` instance who placed the order.
-   `coffee`: The `Coffee` instance that was ordered.
-   `price`: The price of the order (between 1.0 and 10.0).

**Methods**:

-   `all()`: Returns all orders.

Tests
-----

### Running Tests

To run the tests, ensure you have `pytest` installed. Navigate to your project folder and run:


`pytest`

The test suite is organized in the `tests/` directory with individual test files for the `Customer`, `Coffee`, and `Order` classes.

### Test Coverage

-   **test_customer.py**: Tests customer creation, name validation, and placing orders.
-   **test_coffee.py**: Tests coffee creation and name validation.
-   **test_order.py**: Tests order creation, customer and coffee association, and price validation.

Installation
------------

1.  **Clone the repository**:



`git clone https://github.com/jwk19/Coffe-shop`

1.  **Navigate into the project directory**:


`cd coffe_shop`

1.  **Set up a virtual environment** (optional but recommended):



`pipenv install
pipenv shell`

1.  **Install pytest for testing**:


`pipenv install pytest`

Debugging
---------

For quick interactive testing, you can use the `debug.py` file. This file includes example code to create instances of `Customer`, `Coffee`, and `Order` to manually test the behavior of your classes.

License
-------

This project is open-source and available under the MIT License. See the `LICENSE` file for more details.