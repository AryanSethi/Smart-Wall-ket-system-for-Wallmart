import pygame

categories = {
    "Meat and Poultry": "A",
    "Soft Drinks": "B",
    "Alcohol and spirits": "C",
    "Home Items": "D",
    "Stationary": "E",
    "Sea Food": "F",
    "Bakery": "G",
    "Frozen": "H",
    "Grocery": "I",
    "Florist": "J"
}

sub_categories = {
    "Eggs": "Meat and Poultry",
    "Fresh Cut Chicken": "Meat and Poultry",
    "Fresh Cut Chicken Legs": "Meat and Poultry",
    "Frozen Nuggets": "Frozen",
    "Tide Detergent 2kg": "Home Items",
    "Coka cola 1L bottle": "Soft Drinks",
    "Red bull Energy Drink": "Soft Drinks",
    "Britania eggless cakes": "Bakery",
    "Large size cello tape": "Stationary",
    "Classmate 200 pages register": "Stationary",
    "Reynolds blue gel pens": "Stationary",
}

# 3 hardcoded orders for simplicity, containing 2, 4 and 3 products respectively
all_orders = [
    # order 1 with 2 products
    {
        "products": [
            {
                "description": "Eggs",
                "quantity": 5
            },
            {
                "description": "Tide Detergent 2kg",
                "quantity": 2
            }
        ]
    },

    # order 2 with 4 products
    {
        "products": [
            {
                "description": "Coka cola 1L bottle",
                "quantity": 2
            },
            {
                "description": "Britania eggless cakes",
                "quantity": 10
            },            {
                "description": "Eggs",
                "quantity": 15
            },
            {
                "description": "Red bull Energy Drink",
                "quantity": 10
            }
        ]
    },

    # order 3 with 3 products
    {
        "products": [
            {
                "description": "Large size cello tape",
                "quantity": 1
            },
            {
                "description": "Classmate 200 pages register",
                "quantity": 5
            },
            {
                "description": "Reynolds blue gel pens",
                "quantity": 10
            }
        ]
    },
]

batched_orders =[]
destinations=[]


for order in all_orders:
    for products in order["products"]:
        batched_orders.append(products["description"])

for product in batched_orders:
    if categories[sub_categories[product]] not in destinations:
        destinations.append(categories[sub_categories[product]])

print(destinations)