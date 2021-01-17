#include <bits/stdc++.h>
class Solution {
public:
    vector<int> runningSum(vector<int>& nums){

        if (nums.size() == 0) return {};
        vector<int> result;
        result.reserve(1000);
        result.push_back(nums[0]);

        for(int i = 1; i<nums.size();i++)
            result.push_back(result.back() + nums[i]);

        return result;

    }
};