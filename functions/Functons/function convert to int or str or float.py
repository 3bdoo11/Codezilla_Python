str_1st = ["1.5", "2", "3.5", "4", "5"]
float_1st = [1.5, 2.5, 3.5, 4.5, 5.5]

def convert_list_to_integers(args, convert_to_float=False, convert_to_string = False):
    args_list = []
    for arg in args:
        if convert_to_float:
            args_list.append(float(arg))
        elif convert_to_string:
            args_list.append(str(arg))
        else:
            args_list.append(int(float(arg)))
    return args_list    
# convert to integers
numbers_int = convert_list_to_integers(str_1st)
print(numbers_int)
# output: [1, 2, 3, 4, 5]

# convert to float
numbers_float = convert_list_to_integers(str_1st, convert_to_float=True)
print(numbers_float)


# output: [1.5, 2.0, 3.5, 4.0, 5.0]

# convert to string
numbers_str = convert_list_to_integers(float_1st, convert_to_string=True)
print(numbers_str)
# output: ['1.5', '2.5', '3.5', '4.5', '5.5']
