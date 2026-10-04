P,Q,R = map(int,input().split())

A = P + Q
B = Q + R
C = P + R

if A >= B:
    if B >= C:
        print(C)
    else:
        print(B)
else:
    if A <= C:
        print(A)
    else:
        print(C)