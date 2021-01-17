class Solution {
public:
    int minFlips(string target) {
        int result = 0;
        int start = 0;

        while(start != target.size() and target[start] == '0')
            start += 1;

        if (start == target.size())
            return 0;
        if (start == 0)
            result += 1;
        for (int i = start; i< target.size(); i++)
            if (i != 0 and target[i] != target[i-1])
                result += 1;

        return result;

    }
};