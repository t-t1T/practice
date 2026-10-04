import sys
import bisect

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    W = [float(x) for x in input_data[3 : 3+N]]
    U = [float(x) for x in input_data[3+N : 3+N+K]]

    u1 = U[0]
    u_rest = U[1:] 

    cost1 = [0.0] * (N + 1)
    for i in range(1, N + 1):
        diff = W[i-1] - u1
        cost1[i] = cost1[i-1] + diff * diff

    sufW = [0.0] * (N + 1)
    sufW2 = [0.0] * (N + 1)
    for i in range(N - 1, -1, -1):
        sufW[i] = sufW[i+1] + W[i]
        sufW2[i] = sufW2[i+1] + W[i] * W[i]

    min_error = float('inf')
    best_t = -1
    best_x = -1

    for i in range(1, N):
        L = N - i
        actual_mean = sufW[i] / L
        
        idx = bisect.bisect_left(u_rest, actual_mean)
        
        candidates = set()
        if idx < len(u_rest):
            candidates.add(idx)
        if idx > 0:
            candidates.add(idx - 1)
            
        for c_idx in candidates:
            ux = u_rest[c_idx]
            
            error_after = sufW2[i] - 2 * ux * sufW[i] + L * (ux * ux)
            total_error = cost1[i] + error_after
            
            if total_error < min_error:
                min_error = total_error
                best_t = i + 1
                best_x = c_idx + 2

    print(f"{best_t} {best_x}")

if __name__ == '__main__':
    main()