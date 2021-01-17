class Solution {
public:
    string removeVowels(string s) {
        string result = "";
        unordered_set<char>vowel = {'a','e','i','o','u'};

        for(char ch: s){
            if(vowel.find(ch) == vowel.end())
                result = result + ch;


        }

        return result;
    }
};