class Solution {
public:
    int balancedStringSplit(string s) {
        int result = 0;
        int left = 0;
        int right = 0;

        for(const char ch : s){
            if(ch == 'R')
                right += 1;
            else
                left += 1;
            if (left == right)
                result += 1;
        }
        return result;
    }
};