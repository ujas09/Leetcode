class Solution {
public:
    int calculateTime(string keyboard, string word) {
        int result = 0;

        int now_position = 0;
        unordered_map<char,int>map;

        for(int i = 0;i<keyboard.size();i++){

            map[keyboard[i]] = i;

        }

        for (int i = 0; i < word.size(); i++){

            result += abs(map[word[i]] - now_position);

            now_position = map[word[i]];
        }

        return result;

    }
};