# https://leetcode.com/problems/largest-divisible-subset/

# Given a set of distinct positive integers, find the largest 
# subset such that every pair (Si, Sj) of elements in this subset 
# satisfies: Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:
# nums: [1,2,3]
# Result: [1,2] (of course, [1,3] will also be ok)

# Example 2:
# nums: [1,2,4,8]
# Result: [1,2,4,8]


class Solution(object):


    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        1. (s_1, s_2, ..., s_n) is a divisible subset sorted in increasing order, 
            so s_n is a multiple of s1, s1, ...,s_{n-1}, if s_{n+1} is larger than 
            s_n and is a multiple of s_n, than (s_1, s_2, s_3, ..., s_n, s_{n+1}) 
            is also a divisible subset.

        2. let s[i] denote the largest divisible subset that ends with nums[i] as the 
            largets element. s[i] = max(j in [0, i), nums[i] % nums[j] = 0}{s[j]} + 1

            Ex: as long as latest number are equal (24), they will have same future            
            # [1, 2, 6, 24]
            # [1, 2, 4, 8, 24]
            this shorter sequence will never grow longer than the currently longer one

        3. base case: s[0] = [nums[0]]
        """
        l = len(nums)
        if not l:
            return []
        nums.sort()
        s = [(1, [nums[0]])] # base case, [size, elements]
        for i in range(1, l):
            # every time, try all existing largestDivisibleSubset ended in 0 to i-1,
            # to form the largestDivisibleSubset ended in i
            ms = max([s[j] for j in range(i) if nums[i] % nums[j] == 0] or [(0, [])], key = lambda x:x[0]) 
            s.append((ms[0] + 1, ms[1] + [nums[i]]))
        return max(s, key = lambda x:x[0])[1]


    # shorter, https://discuss.leetcode.com/topic/49455/4-lines-in-python
    def largestDivisibleSubset(self, nums):
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))



    # def largestDivisibleSubset(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
        
    #     # [Ideas]
    #     # 1> building a graph, which i and j are connected 
    #     #    if (i % j) == 0 or (j % i) == 0, cost O(n**2)
    #     # (X)2. find largest connected block, which could be in O(n)
    #     # 3. if we know i1 % i2 == 0 and i2 % i3 == 0,
    #     #    we know i1 % i3 == 0
    #     # 4. we are actually finding a "clique"
    #     # 5. sort nums, and find relationships from the smaller side
    #     # 6> for group S and it's largest number Sn, if Sm % Sn == 0
    #     #    then Sm could divisible by any Si in S
    #     # 7. do dfs to search all possibility, and keep best one.
    #     # 8. some way to do DP? to stop early?
    #     #    we won't divide same number twice in our DFS
    #     #--[Summary]---------------------------
    #     # 1. sort
    #     # 2. choose 1st number (not 1)
    #     # 3. compare current largest number with new number
    #     # 4. even a number is good to add-in => 
    #     #       still 2 branch: choose /or not
    #     #    for example in: 1, 2, (6), 8, 16, we don't choose 6
        
    #     if not nums: return []
        
    #     self.nums = sorted(nums)
    #     self.best = None
    #     self.dp = {}    # dp[(seq[-1], idx)] = [a, b, c ...]
    #     ans = self.dfs([], 0)
    #     # print("DP:", self.dp)
    #     return ans
        
        
    # def dfs(self, seq, idx):
    #     # collect solution
    #     head = seq[-1] if seq else ''
    #     key = "%s_%s" % (head, idx)
    #     if idx == len(self.nums):
    #         return seq
    #     elif self.best and (head in self.best):
    #         return None
    #     elif key in self.dp:
    #         return seq + self.dp[key]
    #     # do dfs
    #     i, best = idx, seq
    #     while i < len(self.nums):
    #         cur = self.nums[i]
    #         if (seq == []) or (cur % head == 0):
    #             sol = self.dfs(seq + [cur], i+1)
    #             # print("CP", best, sol, seq)
    #             if sol and (len(best) < len(sol)):
    #                 best = sol
    #                 # print("best:", seq, best)
    #         i += 1
    #     if best:
    #         self.dp[key] = [s for s in best if s not in seq]
    #         if (not self.best) or (len(self.best) < len(best)):
    #             self.best = best
    #     return best
            
            
    def test(self):
        cases = [
            [],
            [1,2,3],
            [1,2,4,8],
            [1,2,4,8,16,32,64,3,6,9,18,27,81],
        ]
        for c in cases:
            print(c, self.largestDivisibleSubset(c))
        
                  
Solution().test()