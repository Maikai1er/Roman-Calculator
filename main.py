symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


# to start with, just refactor roman num to arabian


input_number = str(input('Enter a roman number: '))


def convert_roman_to_arabian(num):
    list_num = list(num)
    temp_symbol = symbols[list_num[-1]]
    current_sum = 0
    for symbol in reversed(list_num):
        if temp_symbol > symbols[symbol]:
            current_sum -= symbols[symbol]
        else:
            current_sum += symbols[symbol]
        temp_symbol = symbols[symbol]
    return current_sum

# def convert_arabian_to_roman(num):


result = convert_roman_to_arabian(input_number)

print(result)
