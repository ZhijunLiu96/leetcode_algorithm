leetcode

1029. Two City Scheduling
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        difference = []
        N = int(len(costs)/2)
        for i in range(2*N):
            total += costs[i][0]
            difference.append(costs[i][1]-costs[i][0])
        difference.sort()
        total = total + sum(difference[:N])
        return total

723. Candy Crush
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        R, C = len(board), len(board[0])
        todo = False

        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    todo = True

        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True

        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

        return self.candyCrush(board) if todo else board

797. All Paths From Source to Target
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph) - 1
        paths = [[0]]
        ans = []
        while paths:
            path = paths.pop() 
            if graph[path[-1]]: ## if graph[path[-1]] is empty just pop out
                for n in graph[path[-1]]: 
                    if n==N:
                        ans.append(path+[n])
                    else:
                        paths.append(path+[n])
        return ans


253. Meeting Rooms II
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        points = []
        for point in intervals:
            points.append((point[0], 1))
            points.append((point[1],0))
            # [(0, 1), (30, 0), (5, 1), (10, 0), (15, 1), (20, 0)]
        points.sort(key = lambda x:(x[0],x[1])) # sort by time
        res = 0; cur = 0 ## cur means current meeting
        for (val,type) in points:
            if type ==1:
                cur += 1
            else:
                cur -= 1
            res = max(res, cur)
        return res

390. Elimination Game
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 0:
            return
        arr = range(1,n+1)
        while len(arr) >1:
            arr = arr[1::2][::-1] # reverse each time
        return arr[0]

139. Word Break
""" Dynamic Programming """
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:    
        dp = [False]*(len(s)+1)
        dp[0] = True # initialize a head
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                if dp[i] == True and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]

2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        result = l1.val + l2.val
        if result < 10:
            result_list = ListNode(result)
            result_list.next = self.addTwoNumbers(l1.next, l2.next)
            return result_list
        else:
            result = l1.val + l2.val - 10
            result_list = ListNode(result)
            result_list.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return result_list

611. Valid Triangle Number
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:    
        count = 0
        if len(nums) < 3:
            return count
        n = len(nums)
        nums.sort()
        for i in range(n-1,1,-1):
            low = 0
            high = i-1
            while low < high:
                if nums[low] + nums[high] > nums[i]:
                    count += high-low ## for low could move from low to high-1
                    high -= 1
                else:
                    low += 1
        return count

1047. Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, S: str) -> str:
        output = []
        for ch in S:
            if output and ch == output[-1]: 
                output.pop()
            else: 
                output.append(ch)
        return ''.join(output)

155. Min Stack
class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> None:
        # element = self.stack[-1]
        # self.stack = self.stack[:-1]
        # return element
        return self.stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return
    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        else:
            return

33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

1060. Missing Element in Sorted Array
""" try binary search next time """
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        miss = []
        miss.append(0)
        for i in range(1,len(nums)):
            ith = nums[i]-nums[i-1]-1+miss[-1]
            miss.append(ith)
            if ith >= k:
                return nums[i-1] + k - miss[i-1]
        return nums[-1] + k - miss[-1]

283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, n):
            nums[i] = 0
        return nums

1. Two Sum
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
#         diction, j = {}, 0
#         for n in nums:
#             if target-n in nums:
#                 ind = nums.index(target-n)
#                 if ind != j:
#                     return [j, ind]
#             j += 1
116. Populating Next Right Pointers in Each Node
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        cur = root
        leftnode = root
        while cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur=leftnode.left
                leftnode = cur
        return root

328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head or not head.next):
            return head
        else:
            odd=head
            even=head.next
            evenhead=head.next ## denote the node
            while even and even.next:
                odd.next = odd.next.next
                odd = odd.next
                even.next = even.next.next
                even = even.next
            odd.next=evenhead
            return head

445. Add Two Numbers II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = 0, 0
        while l1:
            s1 = s1*10+l1.val
            l1 = l1.next
        while l2:
            s2 = s2*10 + l2.val
            l2 = l2.next
        s = str(s1+s2)
        node = ListNode(int(s[0]))
        head = node
        for i in range(1,len(s)):
            node.next = ListNode(int(s[i]))
            node = node.next
        return head

387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        diction, j = {}, -1
        for ch in s:
            diction[ch] = 0
        for ch in s:
            diction[ch] += 1
        # count = collections.Counter(s)
        for ch in s:
            j += 1
            if diction[ch] == 1:
                return j
        return -1

12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        res = [['M',1000,0],['CM',900,0],['D',500,0],['CD',400,0],['C',100,0],['XC',90,0],['L',50,0],['XL',40,0],['X',10,0],['IX',9,0],['V',5,0],['IV',4,0],['I',1,0]]
        for i in range(13):
            res[i][2] = num//res[i][1]
            num = num%res[i][1]
            result += res[i][0] * res[i][2]
        return result

171. Excel Sheet Column Number
class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        n = len(s)
        for i in range(n):
            total += (ord(s[i])-64)*26**(n-1-i)
        return total

242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(1,27):
            dic[i] = 0
        for ch in s:
            dic[ord(ch)-96] += 1
        for ch in t:
            dic[ord(ch)-96] -= 1
        for i in range(1,27):
            if dic[i] != 0:
                return False
        return True

716. Max Stack
class MaxStack:
    def __init__(self):
        """ initialize your data structure here. """
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        element = self.stack[-1]
        self.stack.pop()
        return element
    def top(self) -> int:
        return self.stack[-1]
    def peekMax(self) -> int:
        return max(self.stack)
    def popMax(self) -> int:
        m = max(self.stack)
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] == m:
                return self.stack.pop(i)

252. Meeting Rooms
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key = lambda x:x[0])
        l = len(intervals)
        if l == 1:
            return True
        else:
            for i in range(1,l):
                if intervals[i][0]<intervals[i-1][1]:
                    return False
            return True

232. Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        """ Initialize your data structure here. """
        self.stack = []
    def push(self, x: int) -> None:
        """ Push element x to the back of queue. """
        self.stack.append(x)
    def pop(self) -> int:
        """ Removes the element from in front of queue and returns that element. """
        return self.stack.pop(0)
    def peek(self) -> int:
        """ Get the front element. """
        return self.stack[0]
    def empty(self) -> bool:
        """ Returns whether the queue is empty. """
        if self.stack:
            return False
        else:
            return True

451. Sort Characters By Frequency
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        res = ''
        for ch in s:
            dic[ch] = 0
        for ch in s:
            dic[ch] += 1
        item = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for (ch, count) in item:
            res += ch*count
        return res

121. Best Time to Buy and Sell Stock
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

56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals = sorted(intervals, key = lambda x : (x[0],x[1]))
        i,j = 0, 0
        if n < 2:
            return intervals
        elif n > 2:
            while j < n-1: #
                if intervals[i][1] >= intervals[i+1][0]:
                    intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                    intervals.pop(i+1)
                    j += 1
                else:
                    j += 1; i += 1
        else:
            if intervals[0][1] >= intervals[1][0]:
                intervals[0][1] = max(intervals[0][1], intervals[1][1])
                intervals.pop(1)
        return intervals

125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = []
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                l.append(ch)
                continue
        i, j = 0, len(l)-1
        while i < j:
            if l[i] != l[j]:
                return False
            i += 1; j -= 1
        return True

88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m+n and j < n:
            if nums1[i]<= nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                i += 1
                j += 1
        for k in range(j, n):
            nums1[n+k] = nums2[k]

692. Top K Frequent Words """ how to denote asc and desc """
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic, res = {}, []
        for ch in words:
            dic[ch] = 0
        for ch in words:
            dic[ch] += 1
        items = sorted(dic.items(), key=lambda x: (-x[1],x[0]))
        for i in range(k):
            res.append(items[i][0])
        return res

20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(0)
        for ch in s:
            if ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(ch)
        if len(stack)==1:
            return True
        else:
            return False

344. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i < j:
            # cache = s[i]
            # s[i] = s[j]
            # s[j] = cache
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

114. Flatten Binary Tree to Linked List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            result = []
            head = root
            while head.left or head.right:
                if not head.left:
                    head = head.right
                else:
                    if head.right:
                        result.append(head.right)
                    head.right = head.left
                    head.left = None
                    head = head.right
                if not head.left and not head.right and len(result) != 0:
                    head.right = result.pop()

437. Path Sum III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        
        def dfs(root, tar):
            if not root:
                return
            if root.val == tar:
                self.res += 1
            dfs(root.left, tar-root.val)
            dfs(root.right, tar-root.val)
            return
        def trav(root):
            if not root:
                return
            dfs(root,sum)
            trav(root.left)
            trav(root.right)
            return
        
        trav(root)
        return self.res 

202. Happy Number """ why last two return are required??? """
class Solution:
    def isHappy(self, n: int) -> bool:
        Sum = []
        def cal_sum(number):
            s = 0
            while number != 0:
                s += (number%10)**2
                number = number//10
            if s == 1:
                return True
            elif s in Sum:
                return False
            else:
                Sum.append(s)
                total = s
                return cal_sum(total)
        return cal_sum(n)


557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        split = s.split(' ')
        for i in range(len(split)):
            split[i] = split[i][::-1]
        return ' '.join(split)



78. Subsets """ three solutions """
## recursion (how to combine two list)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(len(nums)):
            for j in range(len(result)):
                result += [result[j] + [nums[i]]]
        return result
## Backtracking


222. Count Complete Tree Nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 1
        def binarySearch(node):
            if node.left:
                self.count += 1
                binarySearch(node.left)
            if node.right:
                self.count += 1
                binarySearch(node.right)
        binarySearch(root)
        return self.count


695. Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        length = len(grid[0])
        bredth = len(grid)
        def dfs(i,j):
            if grid[i][j]==1:
                grid[i][j] = 0
                self.count += 1
                if i-1>=0:
                    dfs(i-1, j)
                if i+1 < bredth:
                    dfs(i+1, j)
                if j-1 >= 0:
                    dfs(i, j-1)
                if j+1 < length:
                    dfs(i, j+1)   
        for i in range(bredth):
            for j in range(length):
                if grid[i][j] == 1:
                    self.count = 0
                    dfs(i,j)
                    if self.count> area:
                        area = self.count
        return area

102. Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        result = [[root]]
        while len(result[-1]) >0:
            cur = []
            for node in result[-1]:
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            result.append(cur)
        result.pop()
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = result[i][j].val
        return result

384. Shuffle an Array
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.set = list(nums)
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.set
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        num = self.nums
        n = len(num)
        for i in range(n):
            ind = random.choice(list(range(n)))
            num[ind],num[i] = num[i],num[ind]
        return num

422. Valid Word Square
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if len(words) == 0:
            return True
        nrow = len(words)
        for i in range(nrow):
            cache = ''
            for j in range(nrow):
                try:
                    cache += words[j][i]
                except:
                    pass
            if cache != words[i]:
                return False
        return True

42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        if not height:
            return total
        left, right = [],[]
        right.append(height[0])
        left.append(height[-1])
        height_v = height[::-1]
        for i in range(1, len(height)):
            right.append(max(height[i],right[i-1]))
            left.append(max(height_v[i],left[i-1]))
        left_new = left[::-1]
        for i in range(len(height)):
            total += min(left_new[i],right[i])-height[i]
        return total

1192. Critical Connections in a Network
"""
This is a wrong answer, because of the incorrect partition
solution should use Tarjan algorithm
"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        node = list(range(n))
        part, res, cache = [], [], []
        while node:
            part.append(node.pop())
            for item in connections:
                if (item[0] in part and item[1] in node) or (item[1] in part and item[0] in node):
                    cache.append(item)
            if len(cache) == 1:
                res += cache
            cache = []
        return res

238. Product of Array Except self
		left, right = [1], [1]
        n = len(nums)
        for i in range(n-1):
            left.append(left[i]*nums[i])
            right.append(right[i]*nums[n-1-i])
        for i in range(n):
            nums[i] = left[i]*right[n-1-i]
        return nums

4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        
        def sortTwo(nums1,nums2):
            if len(nums1) == 0:
                return nums2
            if len(nums2) == 0:
                return nums1
            if nums1[0]<nums2[0]:
                return [nums1[0]]+sortTwo(nums1[1:],nums2)
            else:
                return [nums2[0]]+ sortTwo(nums1, nums2[1:])

        total = sortTwo(nums1,nums2)
        if (n+m)%2 == 0:
            return (total[int((n+m)/2)] + total[int((n+m)/2)-1])/2
        else:
            return total[int((m+n)//2)]

1007. Minimum Domino Rotations For Equal Row
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        total = {A[0], B[0]}
        for i in range(1, len(A)):
            total = total.intersection({A[i], B[i]})
        if len(total)==0:
            return -1
        else:
            count1 = 0
            element1 = total.pop()
            for i in range(len(A)):
                if A[i] == element1:
                    count1 += 1
            count1 =  min(count1, len(A)-count1)
            count2 = 0
            for i in range(len(B)):
                if B[i] == element1:
                    count2 += 1
            count2 =  min(count2, len(B)-count2)
            return min(count1, count2)

240. Search a 2D Matrix II
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        for i in range(len(matrix)):
            if matrix[i][n-1] < target or matrix[i][0] > target:
                pass
            else:
                if target in matrix[i]:
                    return True
        return False

528. Random Pick with Weight
import random
class Solution:
    def __init__(self, w: List[int]):
        self.accum = w
        for i in range(1,len(w)):
            self.accum[i] += self.accum[i-1]          
    def pickIndex(self) -> int:
        if len(self.accum) == 1:
            return 0
        target = random.randint(1, self.accum[-1])
        i, j = 0, len(self.accum)-1
        while i+1 < j :
            mid = (i+j)//2
            if self.accum[mid] > target:
                j = mid
            elif self.accum[mid] < target:
                i = mid
            else:
                return mid
        if self.accum[i] < target:
            return j
        else:
            return i

349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = set(nums1).intersection(set(nums2))
        # return list(res)
        return list(set(nums1) & set(nums2))

875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if sum((i-1)// mid+1 for i in piles) > H:
                low = mid + 1
            else:
                high = mid
        return low

647. Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for center in range(2*n-1):
            left = center//2
            right = left + center%2
            while left>=0 and right<n and s[left]==s[right]:
                left -= 1
                right += 1
                ans += 1
        return ans

151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split(' ')
        ans = []
        for i in range(len(string)):
            cache = string.pop()
            if cache != '':
                ans.append(cache)
        return ' '.join(ans)

622. Design Circular Queue
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None]*k
        self.front = 0
        self.rear = -1
        self.capacity = 0
        self.k = k
    def enQueue(self, value: int) -> bool:
        if self.capacity < self.k:
            self.capacity += 1
            if self.rear == self.k-1:
                self.rear=0
            else:
                self.rear += 1
            self.queue[self.rear] = value
            return True
        else:
            return False       
    def deQueue(self) -> bool:
        if self.capacity == 0:
            return False
        else:
            self.queue[self.front] = None
            if self.front == self.k-1:
                self.front = 0
            else:
                self.front += 1
            self.capacity -= 1
            return True 
    def Front(self) -> int:
        if self.capacity > 0:
            return self.queue[self.front]
        else:
            return -1
    def Rear(self) -> int:
        if self.capacity > 0:
            return self.queue[self.rear]
        else:
            return  -1    
    def isEmpty(self) -> bool:
        if self.capacity == 0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if self.capacity == self.k:
            return True
        else: return False

225. Implement Stack using Queues
class MyStack:
    def __init__(self)
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        else:
            return False

32. Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        string = list(enumerate(list(s)))
        stack = []
        while 
        string:
            ele = string.pop(0)
            if len(stack)==0:
                stack.append(ele)
            elif ele[1] == ')' and stack[-1][1]=='(':
                stack.pop()
            else:
                stack.append(ele)
        ind = [item[0] for item in stack]
        ind.insert(0,-1)
        ind.append(len(s))
        for i in range(len(ind)-1,0,-1):
            ind[i] -= ind[i-1]+1
        return max(ind[1:])
        
1048. Longest String Chain
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        diction, result = {}, 1
        words.sort(key = len)
        for word in words:
            diction[word] = 1
        for word in words:
            for i in range(len(word)):
                if word[:i]+word[i+1:] in diction:
                    diction[word] = diction[word[:i]+word[i+1:]] + 1
                    result = max(result, diction[word])
        return result


