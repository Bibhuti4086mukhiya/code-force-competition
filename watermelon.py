n=int(input())

if n%2==0:
    print('YES')
else:
    print('NO')
# [*open(0)] is telling python to put every line of stdin into a list.



w = int(input())
print("YES" if (w % 2 == 0 and w > 2)  else'NO')