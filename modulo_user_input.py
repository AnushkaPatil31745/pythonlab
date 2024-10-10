def modulo(a, b):
    if b == 0:
        raise ValueError("The divisor cannot be zero.")
    return a - (a // b) * b


try:
    a = int(input("Enter the dividend (a): "))
    b = int(input("Enter the divisor (b): "))
    
    result = modulo(a, b)
    print(f"The result of {a} % {b} is: {result}")
except ValueError as e:
    print(f"Error: {e}")

