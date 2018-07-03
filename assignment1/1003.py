from decimal import *
from decimal import Decimal
getcontext().prec = 30
def get(n):    #fairly accurate brute force 
    if n == 0: return 0
    s=Decimal(0); i=Decimal(1);
    while s < n:
        i += 1
        s += Decimal(1.0)/i
    return i-1
    
def get2(goal): #inaccurate but faster approximation
    if goal == 0: return 0
    r = Decimal("0.57721566490153286060651209008240243104215933593992359880576723488486772677766467093694706329")
    n = Decimal(Decimal(goal) - r + 1).exp() - Decimal(0.5)
    return int(n)
    
def gen(n):
    s = Decimal(0)
    for i in range(1,n):
        s += Decimal(1.0)/i
    return s
    
def gen2(n):
    r = Decimal("0.57721566490153286060651209008240243104215933593992359880576723488486772677766467093694706329")
    return r + Decimal(n+0.5).ln() 

def check_test(goal):
    return get(goal) != get2(goal)

def get_diff(a,b):
    a = str(a)+"0000000000000000000000000000"
    b = str(b)+"0000000000000000000000000000"
    for i in range(min(len(a),len(b))):
        if a[i] != b[i]: 
            if check_test(float(a[0:i+1])):
                break
    return a[:i+1]

def print_tests(i):
    for n in range(3,i+3):
        print(n-2, get_diff(gen(n)-1, gen2(n)-1))
        
print_tests(99)

while True:
    goal = float(input())
    if goal == 0: 
        break
    print(get(goal), get2(goal))
    