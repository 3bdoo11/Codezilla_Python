# students = { 
#     "Mohamed Hassan": {"grades": { 
#         "math": 100, 
#         "english": 90, 
#         "science": 80, 
#         "arabic": 100,  
#         "history": 97}, 
#         "school": "Codezilla" 
#     }, 
#     "Ahmed Kamal": {"grades": { 
#         "math": 100, 
#         "english": 95, 
#         "science": 93, 
#         "arabic": 100, 
#         "history": 94}, 
#         "school": "Codezilla" 
#     }, 
#     "Ali Adel": {"grades": { 
#         "math": 85, 
#         "english": 83, 
#         "science": 87, 
#         "arabic": 100, 
#         "history": 90}, 
#         "school": "Al-Azhar" 
#     }, 
#     "Hossam Yehia": {"grades": { 
#         "math": 100, 
#         "english": 94, 
#         "science": 98, 
#         "arabic": 100, 
#         "history": 100}, 
#         "school": "Al-Azhar" 
#     } 
# } 

# highest_score = sum(students["Mohamed Hassan"]["grades"].values())
# for student in students:
#     grades = students[student]["grades"]
#     degree = grades.values()
#     total = sum(degree)
#     if total >= highest_score:
#         highest_score = total
#         frist_place = student
#         percentage = highest_score / len(degree)
# print(f"{frist_place} has the highest total percentage which is {percentage:.2f}%")
# for subject, score in students[frist_place]["grades"].items():
#     print(f"{subject}: {score}")
    
    
    
    
    



inventory = {"Paracetamol": {"price":25, "quantity":10}, 
            "Aspirin": {"price":15, "quantity":20}, 
            "Ibuprofen": {"price":20, "quantity":15}, 
            "Cough Syrup": {"price":30, "quantity":5}, 
            "Augmentin": {"price":100, "quantity":7}, 
            "Amoxicillin": {"price":80, "quantity":8}, 
            "Panadol": {"price":25, "quantity":10}, 
            "Zinc": {"price":15, "quantity":20}, 
            "Vitamin C": {"price":20, "quantity":15}, 
            "Fucidin": {"price":30, "quantity":5}, 
            "Kolanog": {"price":100, "quantity":2}, 
            } 
            
message = """1. Add new items
2. Remove items
3. Update items
4. Check Available quantity
5. Print treatment information
6. Exit
"""
while True:
    print(message)
    choice = input("Enter your choice: ")
    if choice == "1":
        while True:
            print("---Entering vew item---")
            new_item = input("Enter item name (Press Enter to Exit): ").title()
            if new_item == "":
                break
            price = int(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            inventory[new_item]={"price":price,"quantity":quantity}
            
    elif choice == "2":
        while True:
            print("---Deleting item---")
            del_item = input("Enter item name (Press Enter to Exit): ").title() 
            if del_item == "":
                break
            if del_item in inventory:
                duble_check = input(f"Are you sure you want to delete {del_item}? (y/n): ").lower()
                if duble_check == "y":
                    del inventory[del_item]
                    print(f"{del_item} has been deleted")
            else:
                print("item not found")
    elif choice == "3":
        while True:
            print("---Updating item---")
            item_update = input("Enter item name to be updated (press Enter to Exit): ").title()
            if item_update == "":
                break
            if item_update in inventory:
                price_update = int(input("Enter the new price: "))
                quantity_update = int(input("Enter the new quantity: "))
                inventory[item_update]["price"]= price_update
                inventory[item_update]["quantity"]= quantity_update
                print(f"{item_update} has been updated")
            else:
                print("item not found")
    elif choice == "4":
        while True:
            print("---Checking item quantity---")
            item_check = input("Enter item name to be checked (press Enter to Exit): ").title()
            if item_check == "":
                break
            if item_check in inventory:
                avilable_quantity = inventory[item_check]["quantity"]
                print(f"We have {avilable_quantity} {item_check} units")
            else:
                print("item not found")
    elif choice == "5":
        while True:
            print("---Printing treatment information---")
            item_info = input("Enter item name (press Enter to Exit): ").title()
            if item_info == "":
                break
            if item_info in inventory:
                print(f"Item: {item_info}")
                print(f"Price: {inventory[item_info]["price"]} EGP")
                print(f"Quantity: {inventory[item_info]["quantity"]} units")
            else:    
                print("item not found")
    elif choice == "6":
        print("Have a nice day!")
        break
    else:
        print("invaled choice")






https://www.programiz.com/online-compiler/8eY5nFF9I88Lm