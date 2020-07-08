


1. Ones Groups
In a square gird, two cells are connected if they share an edge and share the same value. Sharing an edge is up, down, left and right, but not diagonal. Given a square grid, determine the number of cells in each connected group of 1 values. There will be an array of queries, each one an integer. Create a return array of integer where each element is the number of groups in the matrix that have a size that matches the query.

```python
count = 0

def onesGroups(grid, queries):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    global count

    def bfs(i,j,grid):
        global count
        if i<0 or j<0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
            return
        else:
            grid[i][j] = 0
            count += 1
        bfs(i+1,j,grid)
        bfs(i,j+1,grid)
        bfs(i,j-1,grid)
        bfs(i-1,j,grid)
      
    group = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count = 0
                bfs(i,j,grid)
                group.append(count)

    ans = {}
    for element in group:
        ans[element]=0
    for element in group:
        ans[element] += 1
    res = []
    for element in queries:
        try: res.append(ans[element])
        except: res.append(0)
    return res
```



