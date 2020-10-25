n = int(input())
x = 1
y = 1
print(x, y, end=" ")
for i in range(3,n+1):
    print(x+y, end=" ")
    b = x
    x = y
    y = b+y
print()
