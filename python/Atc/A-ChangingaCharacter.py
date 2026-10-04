N, K =map(int, input().split())
S = input()
char = ""

if S[K-1] == "A":
    char = 'a'
elif S[K-1] == "B":
    char = "b"
else:
    char = "c"

S[:K-1]
S[K:]
print(S[:K-1]+char+S[K:])
