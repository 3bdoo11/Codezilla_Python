2# Project - conditionals 2
# grades2
#lists containing the code of items with sales
sales_70 = ['070', '170', '270', '370', '470']
sales_50 = ['050', '150', '250', '350', '450']
sales_30 = ['030', '130', '230', '330', '430']
#get the code and price of the item
code = input("Enter The Code of the item: ")
price = float(input("Enter The Price of the item: "))
#check for sales
if code in sales_70:
    price = price - (price * (70/100))
    discount = "70%"
elif code in sales_50:
    price = price - (price * (50/100))
    discount = "50%"
elif code in sales_30:
    price = price - (price * (30/100))
    discount = "30%"
else:
    discount = "0%"

print(F"The Final Price of Item code-{code} After {discount} sale is {price:,.2f} EGP")



https://www.programiz.com/online-compiler/0oVi1k9NmEzy6