n=int(input())

output_value=int()

for i in range(n):
    val=input()
    if val=='x++' or val=='++x' or val=='X++' or val=='++X':
        output_value+=1
    if val=='--x' or val=='x--' or val=='--X' or val=='X--':
        output_value-=1
print(output_value)