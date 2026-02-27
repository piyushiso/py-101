# num = 10
# bin_num = format(num, 'b')
# byte_num = format(num, '08b')
# oct_num = format(num, 'o')
# dec_num = format(num, 'd')
# hex_num = format(num, 'x')
# print('In Binary: ', bin_num, type(bin_num))
# print('In Bytes: ', byte_num, type(byte_num))
# print('In Octal: ', oct_num, type(oct_num))
# print('In Decimal: ', dec_num, type(dec_num))
# print('In Hexa-Decimal: ', hex_num, type(hex_num))

# in_bin = '1001'
# dec_num = format(int(in_bin), 'd')
# print(dec_num)

# binary_string = "1101"
# decimal_number = int(binary_string, 2)

def get_binary(num: int) -> str:
    return format(int(num), 'b')

def get_decimal(b_str: str) -> int:
    return int(b_str, 2)

def is_even(num: int) -> bool:
    return num%2 == 0

def num_steps(b_str: str) -> int:
    print(f"Evaluating for {b_str} ({get_decimal(b_str)})")
    c = 0
    while b_str != '1':
        c += 1
        dec = get_decimal(b_str)
        if is_even(dec):
            # Divide by 2.
            dec //= 2
        else:
            # Add 1.
            dec += 1
        b_str = get_binary(dec)
    return c

print(num_steps('1'))
print(num_steps('10'))
print(num_steps('1001'))
print(num_steps('1101'))
