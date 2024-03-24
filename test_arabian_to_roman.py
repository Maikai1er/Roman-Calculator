reversed_symbols = {
    1000: 'M',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I'
}

test_num = 697
result = []


# def inner(num):
#     for value, symbol in reversed_symbols.items():
#         while num >= value:
#             result.append(symbol)
#             num -= value
#             if num == 0:
#                 return
#

# inner(test_num)

print(''.join(result))


def split_to_divisions(num):
    digits = [int(d) for d in str(num)]
    increaser = 1
    i = len(digits) - 1
    while i >= 0:
        digits[i] *= increaser
        increaser *= 10
        i -= 1
    return digits


print(split_to_divisions(test_num))

