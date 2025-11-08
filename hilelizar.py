import random
random.randint(1, 6)

def hilelizar(n):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    for i in range(n):
        x = random.randint(1, 6)
        if (x == 1):

            a += 1
        elif (x == 2):

            b += 1
        elif (x == 3):

            c += 1
        elif (x == 4):

            d += 1
        elif (x == 5):

            e += 1
        else:

            f += 1
    toplam = a + b + c + d + e + f
    print('a=', a / toplam)
    print('b=', b / toplam)
    print('c=', c / toplam)
    print('d=', d / toplam)
    print('e=', e / toplam)
    print('f=', f / toplam)

hilelizar(360000000)