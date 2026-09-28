# 1. Ask the user for the price of one item and quantity
price_input = input("Enter the price of one item: ")
quantity_input = input("Enter the quantity: ")

# 2. Convert price to float and quantity to int
price = float(price_input)
quantity = int(quantity_input)

# 3. Calculate the total cost
total = price * quantity

# 4. Print a friendly summary using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")