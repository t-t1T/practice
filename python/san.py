def counts():
    m = int(input())
    A = input().split()
    n = int(input())
    B = input().split()

    b_count = {}
    for b in B:
        if b in b_count:
            b_count[b] += 1
        else:
            b_count[b] = 1
    
    A.sort()

    for a in A:
        count = b_count.get(a,0)
        print(f"{a}:{count}")


if __name__ == "__main__":
    counts()
