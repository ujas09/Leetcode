class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        auto maxcandies = max_element(candies.begin(), candies.end());

        vector<bool> result;

        for(int i:candies){
            if (i + extraCandies >= *maxcandies){
                result.push_back(true);
            }
            else{result.push_back(false);}

        }
        return result;
    }
};