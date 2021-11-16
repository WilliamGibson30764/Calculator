import math
def code():
    q = (b*b)
    e = (4*a*c)
    while True:
    if a == 0:
        print("a cannot be 0")
    elif q > e:
        quadratic_function(a,b,c)
        print(f'The x intercepts are {x1} and {x2}')
    elif e > q:
        imaginary(a,b,c)
        print(f'The x  are {x1}i and {x2}i')
    elif q == e:
        print(-b/2*a)
    else:
        print("This quadratic equation cannot be done")
    a = input()
def quadratic_function(a,b,c):
    d = q - e
    sqrtd = math.sqrt(int(d))
    global x1
    x1 = (-b-sqrtd)/(2*a)
    global x2
    x2 = (-b+sqrtd)/(2*a)
def imaginary(a,b,c):
    f = e - q
    sqrtd = math.sqrt(int(f))
    global x1
    x1 = (-b-sqrtd)/(2*a)
    global x2
    x2 = (-b+sqrtd)/(2*a)

