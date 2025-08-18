number =[1, -2, 3, -4, 5, 6, -7, 8, 9]
def count_positive_numbers(numbers):
    positive_numbers = 0
    for number in numbers:
        if number > 0:
            positive_numbers += 1
    return positive_numbers
print("The number of positive numbers in the list is:", count_positive_numbers(number))
def count_even_numbers(numbers):
    even_numbers = 0
    for number in numbers:
        if number % 2 == 0:
            even_numbers += 1
    return even_numbers
print("The number of even numbers in the list is:", count_even_numbers(number))