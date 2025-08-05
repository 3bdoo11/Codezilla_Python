<<<<<<< HEAD
#username project

#1-ask about the name
Name = input("Enter Your Name: ").strip()
len_name = len(Name)
#2-ask about the Birth Year
Birth_year = int(input("Enter Your Birth Year: "))
Birth_year = Birth_year + len_name
#3-ask about the Birth Month
Birth_month = int(input("Enter Your Birth Month: "))
#4-ask about the Birth Day
Birth_day = int(input("Enter Your Birth Day: "))
#5-make username from the name
User_name = Name.lower()
User_name = f"{User_name} {Birth_day} {Birth_month} {Birth_year}@codezilla.com".replace(" ","_")
#remove trile spaces 
#make letters small
#add the birht date to th user 
#add numbr of chracters to birth year 
#add @codezilla.com 
#greet the user 
print("-" * 20)
print(f"Hello, {Name}")
=======
#username project

#1-ask about the name
Name = input("Enter Your Name: ").strip()
len_name = len(Name)
#2-ask about the Birth Year
Birth_year = int(input("Enter Your Birth Year: "))
Birth_year = Birth_year + len_name
#3-ask about the Birth Month
Birth_month = int(input("Enter Your Birth Month: "))
#4-ask about the Birth Day
Birth_day = int(input("Enter Your Birth Day: "))
#5-make username from the name
User_name = Name.lower()
User_name = f"{User_name} {Birth_day} {Birth_month} {Birth_year}@codezilla.com".replace(" ","_")
#remove trile spaces 
#make letters small
#add the birht date to th user 
#add numbr of chracters to birth year 
#add @codezilla.com 
#greet the user 
print("-" * 20)
print(f"Hello, {Name}")
>>>>>>> ca4d8509fd9dd9e5ac83e645f32aeab8225bfecc
print(f"Your username is ....\n{User_name}")