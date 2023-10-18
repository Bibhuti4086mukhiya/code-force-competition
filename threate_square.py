# import math
# n=set(input().split())
# for i in n:
#     j=int(math.sqrt(int(i)))
#     if j**2==int(i):
#         print(i)

import math
# Round a number upward to its nearest integer
# print(math.ceil(1.4))
def theatreSquare(lst):
    m,n,a = lst[0],lst[1],lst[2]
    return math.ceil(m/a)*math.ceil(n/a) 
        
 
lst = (input().split())
lst = [int(a) for a in lst]
print(theatreSquare(lst))

n,m,a=map(int,input().split())
print(-n//a*(-m//a))
