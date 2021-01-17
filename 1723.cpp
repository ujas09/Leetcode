class Solution {

    int result = INT_MAX;
    vector<int> amount;
    int len = 0;
    void helper(int pos, vector<int>& jobs, vector<int>& amount){

        if (pos == jobs.size()){

            int max_in_arr = *max_element(amount.begin(), amount.end());
            result = min(result, max_in_arr);
            return;
        }

        unordered_set<int> seen;

        for(int i = 0;i< amount.size();i++){
            if (seen.find(amount[i]) == seen.end() and amount[i] + jobs[pos] < result){
                amount[i] += jobs[pos];
                helper(pos + 1, jobs, amount);
                amount[i] -= jobs[pos];
                seen.insert(amount[i]);
            }

        }
        return ;

    }
    public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        vector<int> amount;
        for(int i = 0;i<k;i++)
            amount.push_back(0);
        helper(0,jobs,amount);
        return result;

    }
};