# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = {}
ordered_item_num = 1

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
    
    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit() > 0:
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            selected_item = input("Choose an Item Number: ")

            # 3. Check if the customer typed a number
            if selected_item.isdigit():
                # Convert the menu selection to an integer
                selected_item = int(selected_item)

                # 4. Check if the menu selection is in the menu items
                if int(selected_item) in menu_items.keys():
                    
                    # Store the item name as a variable
                    selected_item_name = menu_items[selected_item]
                    #print(selected_item_name) #<<<<<

                    # Ask the customer for the quantity of the menu item
                    order_qty = input("Please enter quantity: ")
                    selected_item_name['Quantity'] = int(order_qty)
                    #print(selected_item_name)  #<<<<<<

                    # Check if the quantity is a number, default to 1 if not
                    if order_qty.isdigit:
                        order_qty = int(order_qty)
                    else:
                        order_qty = 1

                    # Add the item name, price, and quantity to the order list
                    # price
                    price = menu_items[(selected_item)]["Price"]
                    
                    #order_list[ordered_item_num] = selected_item_name #<<<<<<<
                    order_list[ordered_item_num] = { #selected_item_name # <<<<<
                                  'Item Name': selected_item_name["Item name"],  #<<<<
                                  'Price':  selected_item_name["Price"],   #<<<<<<
                                  'Quantity': order_qty  }  # <<<<
                                  
                    ordered_item_num += 1
                    print(order_list)  #<<<<<<

                    # Tell the customer that their input isn't valid
                else:
                    print("Please select a valid option from the menu list")

                # Tell the customer they didn't select a menu option
            else:
                print("Please select a valid menu option ")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a valid number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.lower():
            case 'y':
                keep_ordering.upper() == 'Y'
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break
                # Complete the order
            case 'n': 
                keep_ordering.upper() == 'N'
                place_order = False
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order")
                # Exit the keep ordering question loop
                place_order = False
                break
            case _:
                # Tell the customer to try again
                print("Invalid response. Please make a valid selection ")
            


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

#i = 1

#print(order_list)
for key, value in order_list.items():

#for item_num, item_details in order_list.items():
    #print(value)  <<<<<<
    
    # 7. Store the dictionary items as variables
    item_name = value["Item Name"]
    #(i, item_name)
    num_item_spaces = 25 - len(item_name)
    item_spaces = " " * num_item_spaces  

    item_price = value["Price"]
    #print(i, item_price)
    num_price_spaces = 8 - len(str(item_price))  #<<<<<
    price_spaces = " " * num_price_spaces

    item_quantity = value["Quantity"]
    #print(i, item_quantity)

    #print(f"{item_name:<25}) | {item_price:<8} | {item_quantity}")

    #if type(value) is dict:

    # if key == "Item name":
    #     #ord_item_name = value
    #     num_item_spaces = 25 - len(item_name)  # <<<<<
    #     print(num_item_spaces)
    # elif key == "Price":
    #     #ord_item_price = value
    #     num_price_spaces = 8 - len(item_price)  #<<<<<
    #     print(num_price_spaces)
    # elif key == "Quantity":
    #     ord_item_qty = value  
    #     i += 1.  

    # 8. Calculate the number of spaces for formatted printing
    # num_item_spaces = 26 - len(value)  # <<<<<
    # num_price_spaces = 9 - len(value)  #<<<<<
    #print(num_item_spaces, num_price_spaces) #<<<<<

    # 9. Create space strings
    #item_spaces = " " * num_item_spaces  #<<<<<
    #price_spaces = " " * num_price_spaces #<<<<<


    # 10. Print the item name, price, and quantity
    # if key == "Quantity":
    #     item_spaces = " " * num_item_spaces  
    #     price_spaces = " " * num_price_spaces

        # print(ord_item_name, item_spaces, ord_item_price, 
        #       price_spaces, ord_item_qty)  #<<<<<<
        # print(i)  #<<<<<
    
    print(f"{item_name} {item_spaces}| ",
          f"{item_price}  | ", #{price_spaces}| ",
          f"{item_quantity}")
    #print(f"{item_name:<25}) | {item_price:<8} | {item_quantity}")
#    i += 1

print("----------------------------------------------")
#print("\n")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
tot_oder_amt = sum([item["Price"] * item["Quantity"] for item in order_list.values()])
#sum(tot_oder_amt)
print(f"Order Total Amount: ${tot_oder_amt:.2f}")
print("----------------------------------------------")
print("\n")
# print(f"\nTotal: ${tot_order_amt:.2f}")
