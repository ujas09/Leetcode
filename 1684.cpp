class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_set<char>allowed_char;

        for(const char ch:allowed)
            allowed_char.insert(ch);
        int result;

        for(const string word: words){

            bool valid = 1;
            for(const char ch:word){
                if(allowed_char.find(ch) == allowed_char.end())
                    valid = 0;



            }

            if(valid){
                result += 1;

            }

        }
        return result;
    }
};