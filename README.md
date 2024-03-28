# python_challenge_1

# Python Challenge 1 program overview:
This program is created for use in ordering food from a food truck menu using their interactive ordering system.
It allows the user to choose a menu category from available options. 
Once user selects a menu category, it then provides a list of available menu items for that category.
It will display menu item and menu item price. 

# Technical Details:
Below are few technical highlights
- Menu items are stored in nested dictionary
- Program makes use of following commands
```python
    WHILE loop
    FOR loop 
    MATCH 
        CASE 
    List comprehension
```

## Use:
When this program is executed it will display following menu options: 

![alt text](image.png)

User will need to input one of the available options. If user inputs a negative number,
alpha characters then it will prompt the user to choose again.
Once user inputs a valid menu category number, then it will display a submenu something
like following: 

![alt text](image-1.png)

Once user makes a item selection and quantity, it will ask the user if they would 
like to order any more items(s). User can make additional menu category selection and individual food items in a 
submenu. 
Once user completes ordering all required items, it will display following 
order list and total cost.

![alt text](image-2.png)
