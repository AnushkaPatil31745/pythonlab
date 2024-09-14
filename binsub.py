def convert_to_binary(num_str):
    if num_str.startswith('0x') or num_str.startswith('0X'):
        num = int(num_str, 16)
    elif num_str.startswith('0o') or num_str.startswith('0O'):
        num = int(num_str, 8)
    else:
        num = int(num_str, 10)
    
    return bin(num)[2:], num

def binary_subtraction(a, b):
    bin_a, dec_a = convert_to_binary(a)
    bin_b, dec_b = convert_to_binary(b)
    
    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)
    
    print(f"Binary of {a} (Decimal: {dec_a}): {bin_a}")
    print(f"Binary of {b} (Decimal: {dec_b}): {bin_b}")
    
    result = ''
    borrow = 0
    
    for i in range(max_len - 1, -1, -1):
        bit_a = int(bin_a[i])
        bit_b = int(bin_b[i])
        
        sub = bit_a - bit_b - borrow
        
        if sub == -1:
            result = '1' + result
            borrow = 1
        elif sub == -2:
            result = '0' + result
            borrow = 1
        else:
            result = str(sub) + result
            borrow = 0
        
        print(f"Step {max_len - i}: {bit_a} - {bit_b} (borrow {borrow}) -> result bit: {result[0]}")
    
    result = result.lstrip('0')
    if not result:
        result = '0'
    
    result_decimal = int(result, 2)
    
    print(f"\nFinal Binary Subtraction Result: {result}")
    print(f"Decimal result: {result_decimal}")
    print(f"Hexadecimal result: {hex(result_decimal)}")
    print(f"Octal result: {oct(result_decimal)}")

binary_subtraction('10', '6')
binary_subtraction('0xA', '0x4')
binary_subtraction('0o12', '0o4')

 
 
 
 
