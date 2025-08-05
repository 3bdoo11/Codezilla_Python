#Project - Parity
#second project*(compare btween 3 numbers and print the greatest)
#1- ask the user to enter the 3 numbers 
print("Please, Enter the Numbers you want to compare")
print("-"*15)

First_num = float(input("Enter The First Number: "))
Second_num = float(input("Enter The Second Number: "))
Third_num = float(input("Enter The Third Number: "))

print("-"*15)

#2-compare btween them and print the greatest
if First_num > Second_num and First_num > Third_num:
    print(f"{First_num} is the greatest number")
elif Second_num > First_num and Second_num > Third_num:
    print(f"{Second_num} is the greatest number")
else:
    print(f"{Third_num} is the greatest number")

    
    

https://www.programiz.com/online-compiler/4SqBrtXrt6Oxj