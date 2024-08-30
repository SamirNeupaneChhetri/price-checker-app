# Supermarket Application

Welcome to the Supermarket Application! This is a simple Python-based console application that allows users to view items available in a supermarket, select items to purchase, and calculate the total cost of selected items.

## Features

- **View Items**: Display all items available in the supermarket along with their prices.
- **Select Items**: Users can add items to their cart for purchase.
- **Calculate Total Cost**: The application will calculate the total cost of the items in the cart.
- **User-Friendly Interface**: Easy to navigate menu options.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Project Structure

```
--------- Welcome To Op Market ------------

Options
1 - Show Items <br>
2 - Select Items <br>
3 - Total Cost <br>
0 - Exit <br>

Select an option: 1

Apple : $0.50 <br>
Banana : $0.30 <br>
Orange : $0.80 <br>
Milk : $1.20 <br>
Bread : $1.50 <br>

Options
1 - Show Items <br>
2 - Select Items <br>
3 - Total Cost <br>
0 - Exit <br>

Select an option: 2

Enter an item you want to buy (0 for checkout): Apple
Apple added to your cart.

Enter an item you want to buy (0 for checkout): Milk
Milk added to your cart.

Enter an item you want to buy (0 for checkout): 0
Your selected items: ['Apple', 'Milk']

Options
1 - Show Items<br>
2 - Select Items<br>
3 - Total Cost<br>
0 - Exit<br>

Select an option: 3

<!-- Total cost: $1.70 -->

I am working On this

Options<br>
1 - Show Items<br>
2 - Select Items<br>
3 - Total Cost<br>
0 - Exit<br>

Select an option: 0

--------- Thanks for Shopping -----------
```

## Installation

1. **Clone the Repository**: Download or clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/supermarket-app.git
   cd supermarket-app
   ```

2. **Ensure Python3 is Installed**: The application requires Python 3.x. You can check your Python version by running:

   ```bash
   python --version
   ```

3. **Run the Application**: Execute the Python script to start the application.

   ```bash
   python supermarket.py
   ```

## CSV File Format

The `supermarket.csv` file should be structured as follows:

```csv
Item,Price
Apple,0.50
Banana,0.30
Orange,0.80
Milk,1.20
Bread,1.50
```
