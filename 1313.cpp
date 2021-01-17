class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> result;

        for(int i = 0; i< nums.size()/2; i++){

            for(int j = 0; j < nums[i*2];j++)
                result.push_back(nums[i*2 + 1]);

        }
        return result;
    }
};