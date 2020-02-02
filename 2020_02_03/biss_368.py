class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        sort_nums = sorted(nums)
        dp = [[] for i in range(len(nums))]  # dp[0] = [1], dp[1] = [1,2], dp[2] = [1,2,4] 
        # 最长上升子序列问题
        dp[0] = [sort_nums[0]]
        for i in range(1, len(nums)):
            tmp_res = [sort_nums[i]]
            for j in range(i):
                if sort_nums[i] % dp[j][-1] == 0 and len(dp[j]) + 1 > len(tmp_res):
                    tmp_res = dp[j] + [sort_nums[i]]
            dp[i] = tmp_res
        # [1,2] + [4] -> [1,2,4]
        res = []
        for arr in dp:
            if len(arr) > len(res):
                res = arr
        return res