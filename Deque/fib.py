cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    elif n == 0:
        value =  0
    elif n == 1:
        value = 1
    else:
        value = fib(n-1) + fib(n-2)
    cache[n] = value
    return cache[n]


num = input("Number: ")

result = fib(int(num))

print("Fib(%s) = %d" %(num, result))
