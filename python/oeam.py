import sys

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
    k = int(line)
    
    n, m = 50, 50
    grid = [['#' for _ in range(m)] for _ in range(n)]
    
    path = []
    for r in range(0, n, 2):
        if r % 4 == 0:
            for c in range(m):
                path.append((r, c))
            if r + 1 < n:
                path.append((r + 1, m - 1))
        else:
            for c in range(m - 1, -1, -1):
                path.append((r, c))
            if r + 1 < n:
                path.append((r + 1, 0))
                
    for i in range(k + 1):
        r, c = path[i]
        grid[r][c] = '.'
        
    sr, sc = path[0]
    gr, gc = path[k]
    grid[sr][sc] = 'S'
    grid[gr][gc] = 'G'
    
    max_r = max(path[i][0] for i in range(k + 1))
    max_c = max(path[i][1] for i in range(k + 1))
    
    out_n = max(2, max_r + 1)
    out_m = max(2, max_c + 1)
    
    print(f"{out_n} {out_m}")
    for r in range(out_n):
        print("".join(grid[r][:out_m]))

if __name__ == '__main__':
    main()