class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mark;
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            if( mark.find(target - nums[i]) == mark.end() )
                mark[nums[i]] = i;
            else
                res = {mark[target - nums[i]], i};
        }
        return res;
    }
};