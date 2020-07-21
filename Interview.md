
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

4. probability 

10 keys, only 3 of them can open the door. Pick 2, and calculate the probability to open the door.
```
7*6 / (10*9) = 7/15
1- 7/15 = 8/15
```


5. Deep Learning

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
- Gradient Descent: after active function mapping, how to deal with the points which don't have gradent descent


7. OCR <br/>
- Pipeline: image preprocessing
- DL Architecture
- https://zhuanlan.zhihu.com/p/42719047

8. Others
- Tell me something about time series
- n-gram model
- Intern project
- Visualization tools

9. coding

```python
# TODO 1: count elements in a list
def count_(List):
    answer = {}
    for element in List:
        if element in answer.keys():
            answer[element] += 1
        else:
            answer[element] = 1
    return answer

def count_(List):
    answer = {}
    for element in List:
        try:
            answer[element] += 1
        except:
            answer[element] = 1
    return answer

# TODO 2: stratified sampling, input: [{'value': 1.2, 'type': 'type1'}, {}, {}]
def stratified_samping(List, ratio):
    length = len(List)
    numpy.random.shuffle(List)
    count_ = {}
    result =  []
    value_ = defaultdict(list)
    for element in List:
        try:
            count_[element['type']] += 1
        except:
            count_[element['type']] = 1
        value_[element['type']].append(element['value'])
    keys = list(count_.keys())
    for key in keys:
        bound = int(count_[key]*ratio)
        result += value_[key][:bound]
    return result

# TODO 3: Modify corresponding value to 0 in a 2d-array, if i+j > x
def solution(Array, val, target):
    shape = Array.shape
    ind = numpy.array([False]*(shape[0]*shape[1]))
    ind.shape = shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            if i+j > val:
                ind[i][j] = True
    Array[ind] = target
    return Array

```

10. [coding](https://github.com/ZhijunLiu96/leetcode_algorithm/blob/master/is_in_convexhull.ipynb)
```python
import matplotlib.pyplot as plt
import numpy as np

def is_in_convexhull(points,newpoint):
    points.insert(0,points[-1])
    points.append(points[1])
    for i in range(1,len(points)-1):
        vector1 = np.array(points[i-1]) - np.array(points[i])
        vector2 = np.array(points[i+1]) - np.array(points[i])
        vector3 = np.array(newpoint) - np.array(points[i])
        angle1 = np.angle(complex(vector1[0],vector1[1]),deg=True) if np.angle(complex(vector1[0],vector1[1]),deg=True)>=0 else 360+np.angle(complex(vector1[0],vector1[1]),deg=True)
        angle2 = np.angle(complex(vector2[0],vector2[1]),deg=True) if np.angle(complex(vector2[0],vector2[1]),deg=True)>=0 else 360+np.angle(complex(vector2[0],vector2[1]),deg=True)
        angle3 = np.angle(complex(vector3[0],vector3[1]),deg=True) if np.angle(complex(vector3[0],vector3[1]),deg=True)>=0 else 360+np.angle(complex(vector3[0],vector3[1]),deg=True)
        mini = min(angle1, angle2)
        maxi = max(angle1, angle2)
        if maxi-mini > 180:
             if mini <= angle3 <= maxi:
                 return False
        else:
            if angle3 >= maxi or angle3 <= mini:
                return False
    return True
```




