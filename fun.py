import time, pickle
from datetime import date, datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = date.today().strftime("%m/%d/%Y")

# Define a list of items and their prices
item_1 = "Bread       "
item_2 = "Candy       "
item_3 = "Water       "
item_4 = "Ice Cream   "
item_5 = "Chocolate   "
item_6 = "Soft Drink  "
item_7 = "Chips       "
item_8 = "Biscuits    "
item_9 = "Energy Drink"
item_10 = "Coffee      "

price_1 = 2.50
price_2 = 1.00
price_3 = 1.50
price_4 = 2.0
price_5 = 3.5
price_6 = 3.0
price_7 = 2.0
price_8 = 1.5
price_9 = 4.0
price_10 = 3.5

# Welcoming
print("Welcome to 7-Eleven Shop!")
print("Here are the items we offer:")
print(f"1.  {item_1} for RM{price_1:.2f}")
print(f"2.  {item_2} for RM{price_2:.2f}")
print(f"3.  {item_3} for RM{price_3:.2f}")
print(f"4.  {item_4} for RM{price_4:.2f}")
print(f"5.  {item_5} for RM{price_5:.2f}")
print(f"6.  {item_6} for RM{price_6:.2f}")
print(f"7.  {item_7} for RM{price_7:.2f}")
print(f"8.  {item_8} for RM{price_8:.2f}")
print(f"9.  {item_9} for RM{price_9:.2f}")
print(f"10. {item_10} for RM{price_10:.2f}")

def verifyInteger(input_var):
    try:
        a = int(input_var)
        return False
    except ValueError as e:
        print("Invalid, Please enter a Valid Number.")
        return True

#width
width = 53

# Function to print the receipt
def print_receipt(item, quantity, current_time):
    print("7-Eleven Shop Receipt".center(width))
    print(("Date: "+current_date).center(width))
    print(("Time: "+current_time).center(width))
    print("Item".ljust(16), "Quantity".rjust(11), "Price".rjust(11), "Total".rjust(11))
    print("-"*width)

    total_price = 0

    for i in range(len(item)):
        item_name = item[i]
        if item_name == "Bread       ":
            item_price = price_1
        elif item_name == "Candy       ":
            item_price = price_2
        elif item_name == "Water       ":
            item_price = price_3
        elif item_name == "Ice Cream   ":
            item_price = price_4
        elif item_name == "Chocolate   ":
            item_price = price_5
        elif item_name == "Soft Drink  ":
          item_price = price_6
        elif item_name == "Chips       ":
          item_price = price_7
        elif item_name == "Biscuits    ":
          item_price = price_8
        elif item_name == "Energy Drink":
          item_price = price_9
        elif item_name == "Coffee      ":
          item_price = price_10

        item_quantity = quantity[i]
        item_total = item_price * item_quantity

        print("{:2d}.{:14s} {:11d} {:11.2f} {:11.2f}".format((i+1),item_name, item_quantity, item_price, item_total))

        total_price += item_total

    print("-"*width)
    print("Total".ljust(40),"{:11.2f}".format(total_price).rjust(11))
    print("Thank you for shopping at 7-Eleven Shop!\n".center(width))


# Keep track of the items and their quantities the customer wants to purchase
item = []
quantity = []

# Allow the customer to select items
print("\n")
while True:
    item_choice = input("Enter the item code you want to purchase (0 to 10): ")

    while verifyInteger(item_choice):
        item_choice = input("Enter the item code you want to purchase (0 to 10): ")
    item_choice = int(item_choice)


    if item_choice == 1:
        item.append(item_1)
        selected_quantity = input("Enter the quantity: ")

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 2:
        item.append(item_2)
        selected_quantity = int(input("Enter the quantity: "))

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 3:
        item.append(item_3)
        selected_quantity = int(input("Enter the quantity: "))

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 4:
        item.append(item_4)
        selected_quantity = int(input("Enter the quantity: "))

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 5:
        item.append(item_5)
        selected_quantity = int(input("Enter the quantity: "))

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 6:
        item.append(item_6)
        selected_quantity = int(input("Enter the quantity: "))

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 7:
        item.append(item_7)
        selected_quantity = int(input("Enter the quantity: "))

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 8:
        item.append(item_8)
        selected_quantity = int(input("Enter the quantity: "))

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 9:
        item.append(item_9)
        selected_quantity = int(input("Enter the quantity: "))

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 10:
        item.append(item_10)
        selected_quantity = int(input("Enter the quantity: "))

        while verifyInteger(selected_quantity):
            selected_quantity = input("Enter the quantity: ")
        selected_quantity = int(selected_quantity)

        quantity.append(selected_quantity)

    elif item_choice == 0:
        break

    else:
        print("Invalid option, try again.")

# Print the receipt
print("\n")
print_receipt(item, quantity, current_time)

#Confirmation if Mistaken the number of item they bought
print("\n")
while True:
    update = input("Do you want to update the quantities of items? (y/n): ")
    if update.lower() == 'y':
        item_code = input("Enter the code of the item you want to update : ")

        while verifyInteger(item_code):
            item_code = input("Enter the code of the item you want to update : ")
        item_code = int(item_code)

        new_quantity = input("Enter the new quantity: ")

        while verifyInteger(new_quantity):
            new_quantity = input("Enter the code of the item you want to update : ")
        new_quantity = int(new_quantity)

        quantity[item_code-1] = new_quantity

    elif update.lower() == 'n':
        break

    else:
        print("Invalid option, try again.")

# Print the receipt
print("\n")
print_receipt(item, quantity, current_time)


