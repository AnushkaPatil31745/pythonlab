def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        if digit == '1':
            decimal += 2 ** power
        power += 1
    return decimal

def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    binary = ''
    is_negative = decimal < 0
    decimal = abs(decimal)
    
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

    if is_negative:
        return '-' + binary
    return binary

def binary_sub(a, b):
    # Convert binary inputs to decimal
    decimal_a = binary_to_decimal(a)
    decimal_b = binary_to_decimal(b)
    
    # Subtract the decimal values
    result_decimal = decimal_a - decimal_b
    
    # Convert the result back to binary
    result_binary = decimal_to_binary(result_decimal)
    
    return result_binary

# Test the function
print(binary_sub('1101', '101'))  # Example: 13 - 5 = 8 in decimal, result should be '1000' in binary

