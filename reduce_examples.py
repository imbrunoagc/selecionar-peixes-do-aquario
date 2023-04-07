from functools import reduce

numbers = [1,2,3,4,5]

def sum(a,b):
    print("a = ", a)
    print("b = ", b)
    print("ab = ", a+b)
    return a+b

print(reduce(sum, numbers, 10))


def reducer(acc,val):
    return acc+val

print(reduce(sum, numbers))