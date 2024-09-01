def base(text, text_base, output_base):
    decimal_value = int(text, text_base)

    if output_base == 10:
        return str(decimal_value)

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while decimal_value > 0:
        remainder = decimal_value % output_base
        result = digits[remainder] + result
        decimal_value //= output_base

    if result == "":
        return "0"
    
    return result

print(base("100", 4, 10))   
print(base("16", 10, 2))    
print(base("100", 2, 16))   
print(base("3E8", 16, 10)) 
