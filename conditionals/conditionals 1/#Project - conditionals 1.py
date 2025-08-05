#Project - conditionals 1
#grades1
#1-ask about the User's name
name = input("Enter the winning name: ").lower().strip()
#2-enter the winners names
winners = ["mohamed", "ahmed", 'mahmoud', 'islam', 'hassan', 'israa', 'mariam']
#3-tell the user if he from it or no 
if name in winners:
    print(f"Congratulation {name.title()} is a winner!!!")
else:
    print(f"Sorry {name.title()} is not a winner!")




https://www.programiz.com/online-compiler/2Jec21VM87WQK