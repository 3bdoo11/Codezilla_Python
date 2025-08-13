# Project - string indexing

# id = first 3 characters of company name + - + last 2 characters of name + birth year
# get the data from the user

name = input("Enter your name: ").strip().title()

company = input("Enter your company name: ").strip().title()

birthyear = input("Enter your birth year: ")

email = input("Enter your email: ")

print("-" * 40)

# get the first name

first_name_idx = name.index(" ")
first_name = name[:first_name_idx]

# greet the user

print(f"Hello, {first_name}!\nWelcome at {company}")

print("-" * 40)

# print the id & the edited email

first_3_letters_company = company[:3]

last_2_letters_name = name[-2:]

id = first_3_letters_company + "-" + last_2_letters_name + birthyear

domin_idx = email.index("@")

new_email = email[:domin_idx] + f"@{company}.com"

print(f"Your id is: {id}\nYour email is: {new_email}")





https://www.programiz.com/online-compiler/5Yuk2fbMZtbgYhttps://www.programiz.com/online-compiler/5Yuk2fbMZtbgY