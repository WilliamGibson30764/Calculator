import math
a = int(input("enter a:"))
b = int(input('Enter b:'))
c = int(input("enter c:"))
def code(a,b,c):
    a != 0
    q = (b*b)
    e = (4*a*c)

    if a == 0:
        return "a cannot be 0"
    elif q > e:
        return quadratic_function(a,b,c,q,e)
        #print(f'The x intercepts are {x1} and {x2}')
    elif e > q:
        return imaginary(a,b,c,e,q)
        #print(f'The x  are {x1}i and {x2}i')
    elif q == e:
        return -b/2*a
    else:
        return "This quadratic equation cannot be done"
def quadratic_function(a,b,c,q,e):
    d = q - e
    sqrtd = math.sqrt(int(d))
    x1 = (-b-sqrtd)/(2*a)
    x2 = (-b+sqrtd)/(2*a)
    return f"{x1},{x2}"
def imaginary(a,b,c,e,q):
    f = e - q
    sqrtd = math.sqrt(int(f))
    x1 = (-b-sqrtd)/(2*a)
    x2 = (-b+sqrtd)/(2*a)
    return f"{x1}i,{x2}i"
