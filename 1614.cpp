class Solution {
public:
    int maxDepth(string s) {
        int stk = 0;
        int result = 0;

        for(const char ch: s){
            if(ch == '(')
                stk += 1;
            else if(ch == ')')
                stk -= 1;
            result = max(result, stk);

        }
        return result;

    }
};