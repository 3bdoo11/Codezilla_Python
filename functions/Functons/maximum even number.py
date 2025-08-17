numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
neg_numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
def maximum_even_number(numbers):
    maximum = 0
    for number in numbers:
        if number % 2 == 0 and number > maximum:
            maximum = number
    return maximum
def maximum_negative_even_number(neg_numbers):
    maximum = -4 
    for number in neg_numbers:
        if number % 2 == 0 and number > maximum:
            maximum = number
    return maximum

print(maximum_even_number(numbers))
print(maximum_negative_even_number(neg_numbers))                
