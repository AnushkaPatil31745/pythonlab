def change_case(input_str, style):
    def to_upper(char):
        return chr(ord(char) - 32) if 'a' <= char <= 'z' else char

    def to_lower(char):
        return chr(ord(char) + 32) if 'A' <= char <= 'Z' else char

    def reverse_case(char):
        if 'a' <= char <= 'z':
            return to_upper(char)
        elif 'A' <= char <= 'Z':
            return to_lower(char)
        else:
            return char

    def alternate_case(input_str):
        result = []
        is_upper = input_str[0].isupper()
        for i, char in enumerate(input_str):
            if char.isalpha():
                if is_upper:
                    result.append(to_upper(char))
                else:
                    result.append(to_lower(char))
                is_upper = not is_upper
            else:
                result.append(char)
        return ''.join(result)

    style = style.lower()  
    
    if style == 'c':
        return ''.join(to_upper(char) for char in input_str)
    elif style == 's':
        return ''.join(to_lower(char) for char in input_str)
    elif style == 'r':
        return ''.join(reverse_case(char) for char in input_str)
    elif style == 'u':
        return alternate_case(input_str)
    else:
        raise ValueError("Invalid style argument")

if __name__ == "__main__":
    input_str = input("Enter the string: ")
    style = input("Enter the style (c, s, r, u): ")
    result = change_case(input_str, style)
    print("Result:", result)

