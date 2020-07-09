
1. Ones Groups <br/>
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

2. Cross Entropy
```python

```


3. rotate 2d array 90 degree

```python
#  [[1,2,3],
#  [1,2,3],
#  [3,3,3]]

# i,j

def t(A):
    result = A
    for i in range(len(A)):
        for j in range(len(A)): 
            result[i][j] = A[j][i] # swap could be better
    return result

def revert(A):
    length = len(A[0])
    for i in range(len(A)):
        start, end = 0, length-1
        while start < end:
            cache = A[i][start]
            A[i][start] = A[i][end]
            A[i][end] = cache
            start +=1
            end -= 1
    return A
```

3. Gradient Descent Example
```python
y = (x-2)^2 #y' = 2x-4

x = 0

for i in range(100):
    x = x-0.05*(2*x-4)
```

4. probability <br/>
10 keys, only 3 of them can open the door. Pick 2, and calculate the probability to open the door.
```
7*6 / (10*9) = 7/15
1- 7/15 = 8/15
```


5. Deep Learning <br/>
**CNN** <br/>
- Several examples about Kernel, filters
- how kernel function works

**RNN** <br/>
- Recurrent Neural Network
- https://zhuanlan.zhihu.com/p/22266022?utm_source=qq&utm_medium=social

**LSTM** <br/>
- Long Short Term Memory
- Gates (forget, information, output), and their function
- https://zhuanlan.zhihu.com/p/32085405

6. Machine Learning Things
- Assume I know nothing about machine learning, tell me about the model you are most familiar with.
- How to use gradient descent to update the parameter
- Softmax

7. OCR <br/>
- Pipeline: image preprocessing
- DL Architecture
- https://zhuanlan.zhihu.com/p/42719047





