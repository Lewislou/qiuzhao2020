class Solution1:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        maxLength,link = 1,0
        result = []
        size = len(nums)
        nums.sort(reverse=True)
        ##可以降序也可以升序
        dp = [(1,i) for i in range(size)]
        for i in range(size):
            for j in range(i):
                if(nums[j] % nums[i]==0 and dp[i][0] < dp[j][0] + 1):
                    dp[i] = (dp[j][0] + 1,j)
                    ##保存到第i个数据的距离以及它的上一节点
            if(dp[i][0] > maxLength):
                maxLength = dp[i][0]
                link = i
        for k in range(maxLength):
            result.append(nums[link])
            link = dp[link][1]
            

        return result
        

class Solution2:
    def largestDivisibleSubset(self, nums):
        dp = [[]] #初始化列表中有一个空列表，应对nums=0
        for n in sorted(nums):
            dp.append(max((s+[n] for s in dp if not s or n % s[-1] == 0),key=len))
        return max(dp, key=len)
            ## 若s为空，dp为s+n，之后n%s[-1]=0也就是若n为dp每一个子列表的最后一个元素的倍数，加在这个子列表中
            ## 同时根据key=len来取出最长列表，append到dp中，最终返回最长子列表
            ### Example dp: [[],[1],[1,3],[1,5],[1,3,6],[1,7]]  n: 7  nums: [1,3,5,6,7,8,9,14,15,17]
