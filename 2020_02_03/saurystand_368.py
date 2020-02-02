class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []

        numsLength = len(nums)
        sortedNums = sorted(nums)
        # dp = [[] for i in range(len(nums))]  # dp[0] = [1], dp[1] = [1,2], dp[2] = [1,2,4] 
        dp = [(1, i) for i in range(numsLength)]
        maxlen, tail = 1, 0
        for i in range(numsLength):
            for j in range(i):
                if sortedNums[i] % sortedNums[j] == 0 and dp[i][0] < dp[j][0] + 1:
                    dp[i] = (dp[j][0] + 1, j)
            if dp[i][0] > maxlen:
                maxlen, tail = dp[i][0], i

        res = []
        while maxlen > 0:
            res.append(sortedNums[tail])
            tail = dp[tail][1]
            maxlen -= 1
        # for l in dp:
        #     if len(l) > len(res):
        #         res = l

        return res
