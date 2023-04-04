import math
a = set([0, 2, 3])
def pr(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 2
    if(n == 2):
        return 3
    if(n in a):

        a.add(3 * i)
        return 3 * i
    
    b = a.pop()
    a.add(b)
    a.add(b + 1)   
    return b + 1




def f(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 2
    for i in range(int(n / 2), n):

        if(f(i) == n):
            return 3 * i
    
    return f(n - 1) + 1



for i in range(0, 10):
    print(pr(i))
    
