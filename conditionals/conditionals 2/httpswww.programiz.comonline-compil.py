#Project - conditionals(Body mass index)
#grades2

#ask the user about weight in kg and height in cm
Height = float(input("Enter Height in cm: "))/100
Weight = float(input("Enter Weight in kg: "))

print("-"*20)

#calculat the BMI

BMI = Weight / (Height**2)

if 0 <= BMI <= 15:
    condition = "Very Very Skinny"
elif 15 < BMI <= 18.5:    
    condition = "Skinny"
elif 18.5 < BMI <= 25:
    condition = "Normal"
elif 25 < BMI <= 40:
    condition = "Overwieght"
else:
    condition = "Very fat"
print(f"Your BMI is {BMI:.2f} which is considered as {condition}")    




https://www.programiz.com/online-compiler/2bivCyLn8xhvY
