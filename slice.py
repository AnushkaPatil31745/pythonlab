def custom_slice(sequence, start=None, stop=None, step=1):
    if start is None:
        start = 0
    if stop is None:
        stop = len(sequence)

    if start < 0:
        start += len(sequence)
    if stop < 0:
        stop += len(sequence)
    result = []
    
    i = start
    while (step > 0 and i < stop) or (step < 0 and i > stop):
        result.append(sequence[i])
        i += step

    return result if isinstance(sequence, list) else ''.join(result)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(custom_slice(my_list, 2, 8, 2)) 

my_string = "Hello, World!"
print(custom_slice(my_string, 7, 12)) 
