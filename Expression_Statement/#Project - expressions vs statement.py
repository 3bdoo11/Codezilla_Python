#Project - expressions vs statements
#ask about the number of hours 
Num_hours = float(input("Enter The Number of Hours Per Month: "))
#ask about  hourly rate
Hourly_rate = float(input("Enter Your Hourly Rate: "))

print("-"*20)
#if  Num_Hours  > 100 subtracte (100 - NUM_hours) 
if Num_hours > 100:
    Over_time = Num_hours - 100
    Salary = (100 * Hourly_rate) + (Over_time * (2 * Hourly_rate))
    print(f"You have worked {Num_hours} hours this month, Your salary  is {Salary:,.2f}$ ")
else:
    Salary = Num_hours * Hourly_rate
    print(f"You have worked {Num_hours} hours this month, Your salary  is {Salary:,.2f}$ ")
    

https://www.programiz.com/online-compiler/4vCn7zZlca3XK