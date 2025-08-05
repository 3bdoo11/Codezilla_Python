# import random module
import random
# make a list to save the rndom numbers
random_numbers = []

for num in range(1, 1001):
    random_numbers.append(random.randint(1, 1000))
unique_numbers = set(random_numbers)   

avr_random_numbers = sum(random_numbers) / len(random_numbers)
avr_unique_numbers = sum(unique_numbers) / len(unique_numbers) 
print(f"The number of unique numbers: {len(unique_numbers)}")
print(f"The average of the list of random numbers : {avr_random_numbers:.0f}")
print(f"The average of the unique numbers : {avr_unique_numbers:.0f}")


  https://www.programiz.com/online-compiler/7I9DKiv9pbYID