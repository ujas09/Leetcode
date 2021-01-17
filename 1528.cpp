class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string result = "";

        for(int i = 0; i< s.size();i++)
            result = result + "a";

        for(int i = 0; i< indices.size(); i++)
            result[indices[i]] = s[i];

        return result;

    }

};