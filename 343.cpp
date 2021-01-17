class Solution {
public:
    int integerBreak(int n) {
        vector<int> DP(n + 1, 0);

        for(int i = 2; i <=n; i++){
            for(int j = 1; j<i;j++){
                DP[i] = max(DP[i], max(j, DP[j])*max(i-j, DP[i-j]));

            }

        }
        return DP.back();
    }
};