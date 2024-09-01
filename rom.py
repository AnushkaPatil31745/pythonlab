def rom(text, text_base):
    num = int(text, text_base)
    
    roman_mapping = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman_numeral = ''
    for value, symbol in roman_mapping:
        while num >= value:
            roman_numeral += symbol
            num -= value
    
    return roman_numeral

print(rom("100", 4))  # Output: "XVI"
print(rom("101", 2))  # Output: "V"
print(rom("3E8", 16))  # Output: "M"
