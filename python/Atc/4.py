N = int(input())
t ,x , y = 0
for i in range(N):
    ti,xi,yi = int(input())
    if ti == t:
        if x == xi and y == yi:
            continue