def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(5,8,7,9))