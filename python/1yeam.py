def generate_k_steps_maze(k: int) -> list:

    MAX_SIZE = 50
    maze = [["#" for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]

    path = []
    x, y = 0, 0
    direction = 'RIGHT'
    
    for _ in range(k + 1):
        path.append((x, y))
        
        if direction == 'RIGHT':
            if x + 1 < MAX_SIZE:
                x += 1
            else:
                y += 1
                direction = 'DOWN_FROM_RIGHT'
        elif direction == 'DOWN_FROM_RIGHT':
            y += 1
            direction = 'LEFT'
        elif direction == 'LEFT':
            if x - 1 >= 0:
                x -= 1
            else:
                y += 1
                direction = 'DOWN_FROM_LEFT'
        elif direction == 'DOWN_FROM_LEFT':
            y += 1  
            direction = 'RIGHT'
            
    for px, py in path:
        maze[py][px] = "."
        
    start_x, start_y = path[0]
    goal_x, goal_y = path[-1]
    maze[start_y][start_x] = "S"
    maze[goal_y][goal_x] = "G"
    
    min_x = min(px for px, py in path)
    max_x = max(px for px, py in path)
    min_y = min(py for px, py in path)
    max_y = max(py for px, py in path)
    
    if max_x - min_x == 0:
        if max_x < MAX_SIZE - 1:
            max_x += 1
        else:
            min_x -= 1
            
    if max_y - min_y == 0:  
        if max_y < MAX_SIZE - 1:
            max_y += 1
        else:
            min_y -= 1
            
    cropped_maze = []
    for py in range(min_y, max_y + 1):
        row_string = "".join(maze[py][min_x:max_x + 1])
        cropped_maze.append(row_string)
        
    return cropped_maze


def print_maze(maze_lines: list):
    for line in maze_lines:
        print(line)


if __name__ == "__main__":
    k_steps = int(input())
    result_maze = generate_k_steps_maze(k=k_steps)
    print_maze(result_maze)
