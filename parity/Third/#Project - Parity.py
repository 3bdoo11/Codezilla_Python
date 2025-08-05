#Project - Parity
#Third project(you don't have enough balance)
#1- ask the user abourt the amont of money
Balance = float(input("Enter The amount of money you have: "))

print("-" * 20)

#2-ask about the price of the items
First_item = float(input("Enter The price of The first item: "))
Second_item = float(input("Enter The price of The second item: "))
Third_item = float(input("Enter The price of The thrid item: "))

print("-" * 20)

#3-calculate the items and subetract from the balance 
Total = First_item + Second_item + Third_item

#4- see if te balance bigger than the purchased items confirm the process and print the remaning money

#5-and if the balance smaller than the purchased items stop the process and print the extra the user need to add

if Total <= Balance:
    print("Items have been purchased successfully ")
    print(f"The remaining amount is {Balance - Total}$")
else:
    print("Sorry, You don't have enough balance")
    print(f"You need to add extra {Total - Balance}$")
    


https://www.programiz.com/online-compiler/1c2qA2wLsgJIM