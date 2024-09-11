# Coffee Shop Domain 

## Overview

This project models a simple coffee shop domain using Python classes. The domain consists of three primary classes: `Customer`, `Coffee`, and `Order`. The relationships between these classes are:

- A `Customer` can have many `Order`s.
- A `Coffee` can have many `Order`s.
- An `Order` belongs to both a `Customer` and a `Coffee`

### Classes

1. **Customer**
   - Represents a customer of the coffee shop.
   - Each customer is initialized with a name.
   - Can create orders, view their past orders, and see the coffees they've ordered.

2. **Coffee**
   - Represents a type of coffee offered by the shop.
   - Each coffee is initialized with a name.
   - Can track orders for that specific coffee and view the customers who have ordered it.
   - Provides methods to count the total number of orders and calculate the average price of the orders.

3. **Order**
   - Represents an order placed by a customer for a specific coffee.
   - Each order is initialized with a customer, a coffee, and a price.
   - Keeps track of all orders placed across all customers and coffees.

## Implementation Details

### Customer Class

#### Attributes

- **`name`**: The name of the customer (string). The name must be between 1 and 15 characters long. The name can be updated after instantiation.

#### Methods

- **`orders()`**: Returns a list of all orders placed by the customer.
- **`coffees()`**: Returns a unique list of all the coffees the customer has ordered.
- **`create_order(coffee, price)`**: Creates a new order for the given coffee at the specified price.

### Coffee Class

#### Attributes

- **`name`**: The name of the coffee (string). The name must be at least 3 characters long and cannot be changed after instantiation.

#### Methods

- **`orders()`**: Returns a list of all orders that include this coffee.
- **`customers()`**: Returns a unique list of all customers who have ordered this coffee.
- **`num_orders()`**: Returns the total number of orders for this coffee.
- **`average_price()`**: Returns the average price of this coffee based on the orders. Returns 0 if there are no orders.

### Order Class

#### Attributes

- **`customer`**: The customer who placed the order (instance of `Customer`).
- **`coffee`**: The coffee being ordered (instance of `Coffee`).
- **`price`**: The price of the order (float). The price must be between 1.0 and 10.0 and cannot be changed after instantiation.

#### Class Variables

- **`all_orders`**: A list of all orders placed.

### Notes on Variable Scope

- Instance variables (e.g., `self.name`, `self.customer`) are used to store the attributes specific to each instance of a class.
- Class variables (e.g., `Order.all_orders`) are used to maintain a shared state across all instances of a class.

## Known Issues

- **Recursive calls**: In the current implementation, attempting to access the `name`, `customer`, or `coffee` attributes within the getter methods leads to recursion errors. This is because the methods are calling themselves instead of accessing the instance variable directly.


