# Make a function that prints the items and their prices
pizzas = {
"Margherita": 120,
"Pepperoni": 200,
"Hawaiian": 150,
"Meat Lovers": 250,
"Mushroom": 140,
}

def print_items_and_prices(items):
    for item, price in items.items():
        print(f"{item} Pizza: {price}EGP")

print_items_and_prices(pizzas)