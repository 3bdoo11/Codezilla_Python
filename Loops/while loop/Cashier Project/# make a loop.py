# make a loop
total_cost = []
while True:
    product_name = input("Enter product name: ")
    
    if product_name.lower() == "exit" or len(product_name) < 1:
        break
    
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))
    
    total_product_price = quantity * price
    total_cost.append(total_product_price)
    print("-" * 15)
    print(f"Product: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    
    print("-" * 15)
    print(f"Total item cost: {total_product_price}")
    print("-" * 30)
i = 0
total_cost.sort(reverse=True)

print("Thank you for shoppoing with 3naab store. Have a geart day!")
print("prices in descending order: ")

while len(total_cost) > i:
    print(f"price{i+1}: {total_cost[i]}")
    i += 1 
print("-" * 30)
sum_total = sum(total_cost)
print(f"Total cost: {sum_total}")


https://www.programiz.com/online-compiler/3kNjW7wxUAtT1