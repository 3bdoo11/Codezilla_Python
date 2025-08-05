# Employees and their offices 
cairo = ['Islam Mahfouz', 'Mohamed Mesilhy',  
'Hatem Elmaghraby', 'Kareem Embaby'] 
 
riyadh = ['Mohamed Gouda', 'Ayman Hamed',  
'Seif Ali', 'Adham Wael'] 
 
casablanca = ['Ahmed Ashraf', 'Abd El-Rahman Mahrous',  
'Islam Sheta', 'Mohamed Medhat', 'Mahmoud Nasser'] 
 
dubai= ['Ahmed Alaa', 'Kareem Abd-Elmeged',  
'Osama Ashraf', 'Mohamed Mostafa', 'Ahmed Bedeir'] 

# converte the list into statment
cairo_str = ", ".join(cairo[:-1]) + f" and {cairo[-1]}"
riyadh_str = ", ".join(riyadh[:-1]) + f" and {riyadh[-1]}"
casablanca_str = ", ".join(casablanca[:-1]) + f" and {casablanca[-1]}"
dubai_str = ", ".join(dubai[:-1]) + f" and {dubai[-1]}"

# get the office name
office = input("Enter the name of the office: ").lower()

# check if the input matchs the offices
match office:
    case "cairo" | "egypt":
        print(f"The employees in {office.upper()} are: {cairo_str}.")
    case "riyadh"|"saudi arabia"|"ksa":
        print(f"The employees in {office.upper()} are: {riyadh_str}.")
    case "casablanca" | "morocco":
        print(f"The employees in {office.upper()} are: {casablanca_str}.")
    case "dubai" | "uae":
        print(f"The employees in {office.upper()} are: {dubai_str}.")
    case _:
        print("Not found")




https://www.programiz.com/online-compiler/6DMhwj4UG04q9