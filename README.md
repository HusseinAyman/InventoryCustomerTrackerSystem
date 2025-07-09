# InventoryCustomerTrackerSystem

## Description

This project is a command-line based Inventory and Customer Tracker System written in Python. It allows an admin to manage products, track customer purchases, and generate summary reports. The system uses Python data structures such as dictionaries, tuples, sets, and lists, and incorporates file handling and input validation.

## Features

### 1. Product Management

* Add new products with ID, name, price, quantity, and categories.
* Store products in a dictionary, where each product's data is a tuple.
* Categories are stored as sets to enable flexible category filtering.

### 2. View Products

* Display all available products along with their details.

### 3. Search by Category

* Search products by any category keyword entered by the user.

### 4. Customer Purchases

* Record purchases made by customers.
* Update stock levels automatically based on quantity purchased.
* Track multiple customers and their transactions.

### 5. Reports

* Generate summary report of:

  * Total number of customers
  * Unique customer names
  * Total sales amount
  * Product with the lowest stock

### 6. File Saving

* Save inventory to `inventory.txt`
* Save customer purchases to `purchases.txt`

## File Structure

* `InventoryCustomerTrackerSystem.py`: Main Python script containing all functionalities.
* `inventory.txt`: Generated file that stores product inventory.
* `purchases.txt`: Generated file that stores customer purchase records.

## How to Run

Make sure Python 3 is installed, then run the program:

```bash
python InventoryCustomerTrackerSystem.py
```

Use the interactive menu to:

* Add and view products
* Search products by category
* Record purchases
* Generate reports
* Save data and exit

## Concepts Covered

* Dictionaries and nested data structures
* Tuples and sets
* Loops and conditionals
* Functions and modular design
* Exception handling
* File I/O operations

## Author

Developed by Hussein Rookba for educational use and practical training in Python programming.
husseinayman3009@gmail.com
---

Feel free to expand this system with features like product editing, customer IDs, or loading from saved files on startup.
