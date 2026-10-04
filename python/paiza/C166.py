X = int(input())
count = int(0)

coins = [500, 100, 50, 10, 5, 1]

for BB in coins:
    count += X // BB
    
    X = X % BB
print(count)