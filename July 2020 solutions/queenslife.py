def find_max(queen, grid,visited, adjacency):
    curr_x = queen[0]
    curr_y = queen[1]
    name = queen[2]
    ans = 1
    # print(visited)
    visited.add(name)
    
    if len(adjacency[name]) == 0:
        visited.remove(name)
        return ans  
 
    for q in adjacency[name]:
        if q[2] not in visited:
            path = find_max(q, grid, visited, adjacency)
            ans = max(1+path, ans)
            # print(q[2], path)
    
    visited.remove(name)
    return ans
 
 
 
def form_neighbours(adjacency, q, grid):
    curr_x = q[0]
    curr_y = q[1]
    curr_name = q[2]
    for x in range(curr_x-1,-1,-1):
        if grid[x][curr_y] != '-':
            adjacency[curr_name].append((x,curr_y,grid[x][curr_y]))
            break
    for x in range(curr_x+1, len(grid)):
        if grid[x][curr_y] != '-':
            adjacency[curr_name].append((x,curr_y,grid[x][curr_y]))
            break
    for y in range(curr_y-1, -1, -1):
        if grid[curr_x][y] != '-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x][y]))
            break
    for y in range(curr_y+1, len(grid)):
        if grid[curr_x][y] != '-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x][y]))
            break
    for i in range(1, len(grid)):
        if curr_x+i <len(grid) and curr_y+i<len(grid) and grid[curr_x+i][curr_y+i]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x+i][curr_y+i]))
            break
    for i in range(1, len(grid)):
        if curr_x+i <len(grid) and curr_y-i>=0 and grid[curr_x+i][curr_y-i]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x+i][curr_y-i]))
            break
    for i in range(1, len(grid)):
        if curr_x-i >=0 and curr_y+i<len(grid) and grid[curr_x-i][curr_y+i]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x-i][curr_y+i]))
            break
    for i in range(1, len(grid)):
        if curr_x-i >=0 and curr_y-i>=0 and grid[curr_x-i][curr_y-i]!='-':
            adjacency[curr_name].append((curr_x,y,grid[curr_x-i][curr_y-i]))
            break
        
        
    
N,M = list(map(int, input().split(',')))
 
grid = [['-' for i in range(N)] for x in range(N)]
 
queens = []
 
for _ in range(M):
    x,y,q = input().split(',')
    x = int(x)
    y = int(y)
    grid[x-1][y-1]  = q
    queens.append((x-1,y-1,q))
 
 
ans = 0
adjacency = {}
for q in queens:
    adjacency[q[2]] = []
    form_neighbours(adjacency, q, grid)
    # print(adjacency[q[2]])
 
ans = 0
 
for q in queens:
    start = q[2]
    visited = set()
    ans = max(ans, find_max(q,grid,visited, adjacency))
 
print(M-ans+1)
