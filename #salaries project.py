#salaries project
#1-ask about name and remove the trail spaces from all "str" inputs and title'em  
Name = input("Name: ").strip().title()

#2-ask  about Currency 
Currency = input("Currency: ").strip().title()
#3-ask about num of hours
Num_hours = float(input("Number Of Hours: "))
#4-ask about hour rate
Hour_rate = float(input("Hourly Rate: "))
#5-culculat the salary
Salary = Num_hours * Hour_rate
#-6-print name and the salary and Currency
print("-" * 20)
print(f"The Salary of {Name} is {Salary:,} {Currency}")