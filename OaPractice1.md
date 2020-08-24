## Practice Before Akuna Capital OA [Leetcode](https://leetcode.com/company/akuna-capital/)
### From Easy to Hard

1370. Increasing Decreasing String
```python
class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        alpha = list(set(s))
        alpha.sort()
        res = ''
        while len(s)>0:
            for ele in alpha:
                if ele in s:
                    res += ele
                    s.remove(ele)
            for ele in alpha[::-1]:
                if ele in s:
                    res += ele
                    s.remove(ele)
        return res
```

121. Best Time to Buy and Sell Stock
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        prof = 0
        mini = prices[0]
        for i in range(len(prices)-1):
            if prices[i]< mini:
                mini = prices[i]
            p = prices[i+1] - mini
            if p > prof:
                prof = p
        return prof
```

443. String Compression
```python

```

1338. Reduce Array Size to The Half
```python
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = dict()
        for element in arr:
            if element in cnt:
                cnt[element] += 1
            else: cnt[element] = 1
        val = list(cnt.values())
        val.sort(reverse = True)
        size = 0
        Sum = 0
        for num in val:
            Sum += num
            size += 1
            if Sum >= len(arr)/2:
                return size
```

48. Rotate Image
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
# i, j in range(0, n)
# 1. Give a point x1 [i, j]
# 2. After transposing, it will go to the point [j, i]
# 3. After reversing, it goes to the point x2 [j, n-1-i]
```

39. Combination Sum
```python

```

1048. Longest String Chain
```python

```

677. Map Sum Pairs
```python
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.diction = dict()
        self.keys = set()

    def insert(self, key: str, val: int) -> None:
        self.diction[key]=val
        self.keys.add(key)

    def sum(self, prefix: str) -> int:
        total = 0
        length = len(prefix)
        for item in self.keys:
            if item[:length]==prefix:
                total += self.diction[item]
        return total
```

1319. Number of Operations to Make Network Connected
```python

```

740. Delete and Earn
```python

```

1223. Dice Roll Simulation
```python

```

743. Network Delay Time
```python

```

713. Subarray Product Less Than K
```python

```

1177. Can Make Palindrome from Substring
```python

```

152. Maximum Product Subarray
```python

```

324. Wiggle Sort II
```python

```

15. 3Sum
```python

```

1411. Number of Ways to Paint N × 3 Grid
```python

```

995. Minimum Number of K Consecutive Bit Flips
```python

```

995. Minimum Number of K Consecutive Bit Flips
```python

```

1425. Constrained Subsequence Sum
```python

```

1326. Minimum Number of Taps to Open to Water a Garden
```python

```

741. Cherry Pickup
```python

```
