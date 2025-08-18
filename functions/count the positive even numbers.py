def count_positive_even_numbers(*args):
    positive_even_nums = [num for num in args if num > 0 and num % 2 == 0]
    return len(positive_even_nums)


count_positive_even = count_positive_even_numbers(1, 2, 3, -4, -5, -6, -7, 8, 9, 10)


print(count_positive_even) 


def generate_random_even_numbers(num_even_numbers, range_start, range_end):
    import random
    even_numbers = []
    while len(even_numbers) < num_even_numbers:
        num = random.randint(range_start, reange_end)
        if num % 2 == 0 and num not in even_numbers:
            even_numbers.append(num)
    return even_numbers
random_20_even_numbers = generate_random_even_numbers(
    num_even_numbers=20, range_start=0, range_end=100)
print(random_20_even_numbers)



def convert_list_into_integers(list_of_strings):
    integers = []
    for stirng in list_of_strings:
        integers.append(int(float(stirng)))
    return integers

numbers = convert_list_into_integers(['1', '2', '3.5', '4', '5'])
print(numbers)
