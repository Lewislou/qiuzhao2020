class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums
        
        sorted_nums = sorted(nums)
        dp = []
        for _ in range(len(nums)):
            dp.append([])

        dp[0].append(sorted_nums[0])

        for i in range(1, len(sorted_nums)):
            temp_dp = [sorted_nums[i]]
            for j in range(i):
                if sorted_nums[i] % dp[j][-1] == 0 and len(dp[j])+1 > len(temp_dp):
                    temp_dp = dp[j] + [sorted_nums[i]]
            dp[i] = temp_dp
            

        result = []
        for e in dp:
            if len(result) < len(e):
                result = e
        return result
