# put a desired balance
balance = 1000

while True:
    print("""Welcome to the ATM. Please select an option:
1. Check balance
2. Withdraw
3. Deposit
4. Exit
        """)
    num = input("Enter option number: ")
    if num == "1":
       print(f"Your balance is: ${balance}")
       
    elif num == "2":
        W_amount = int(input("Enter Withdraw amount: "))
        if W_amount > balance:
            print("Insufficient balance.")
        else:
            balance -= W_amount
            print(f"Withdrawal successful. Your new balance is: ${balance}")
            
    elif num == "3":
        D_amount = int(input("Enter deposit amount: "))
        balance += D_amount
        print(f"Deposit successful. Your new balance is: ${balance}")
        
    elif num == "4":
        print("Thank you for using the ATM. Have a great day!")
        break
    
    else:
        print("plese select an option")




https://www.programiz.com/online-compiler/9YushlpHOt1qd