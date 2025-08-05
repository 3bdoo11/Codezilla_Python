# Project - conditionals 3
#grades3
#isalpha(),  isalnum
text = input("Enter an Input: ")
if text.isalnum() == True:
    if text.isnumeric()== True:
        print("your input is all numbers")
    elif text.isalpha()==True:
        if text.isupper() == True:
            print("your input is all the characters are in upper case")
        elif text.islower() == True:
            print("your input is all the characters are in lower case")
        else:
            print("your input is alphabet")
    else:
     print("there is a mix between letters and numbers")
else: 
    print('Your string did not contain alphabet and Numbers only!!')





https://www.programiz.com/online-compiler/6nSs8udpZmaKr