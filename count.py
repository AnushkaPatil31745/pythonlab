def count(iterable, value):
    count = 0
    for item in iterable:
        if item == value:
            count += 1
    return count

print(count([2,3,4,2,2],2))
