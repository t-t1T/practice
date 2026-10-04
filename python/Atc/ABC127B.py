r,D,x2000=map(int,input().split())
xi = r*x2000-D
for num in range(10):
    print(xi)
    xi = r*xi-D
