import random

def montecarlo(n):
    a = 0
    b = 0
    for i in range(n):
        x = 10 * (random.random())
        y = 10 * (random.random())
        if (x ** 2 + y ** 2 < 1):
            b += 1
        elif (x ** 2 + y ** 2 >= 4) and (x ** 2 + y ** 2 < 9):
            a += 1

    print(a)
    print(b)
    print(a / b)

montecarlo(1000000)