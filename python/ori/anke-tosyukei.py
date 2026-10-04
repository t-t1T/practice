N = int(input())
G = input().split()

count ={}
for g in G:
    if g in count:
        count[g] += 1
    else:
        count[g] = 1


for key in count:          
    value = count[key]       
    print(f"{key}: {value}") 