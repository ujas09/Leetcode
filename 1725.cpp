class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        int max_length = 0;
        int count  = 0;
        int length;
        for(auto const rectangle: rectangles){
            length = min(rectangle[0], rectangle[1]);

            if(length > max_length){
                max_length = length;
                count = 1;
            }
            else if(length == max_length)
                count += 1;

        }

        return count;

    }
};