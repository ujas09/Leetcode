class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        multiset<int>numbers;

        for(auto num:nums)
            numbers.insert(num);
        vector<int> result;

        for(int num:nums){

            result.push_back(distance(numbers.begin(), numbers.find(num)));

        }
        return result;
    }
};