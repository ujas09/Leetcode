class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {

        for(int i = 1; i<matrix.size(); i++)
            for(int j = 0; j< matrix[0].size();j++){

                if(matrix[i][j] == 1){

                    matrix[i][j] += matrix[i-1][j];
                }

            }

        int result = 0;
        for(int i = 0; i<matrix.size(); i++){
            sort(matrix[i].begin(), matrix[i].end(),std::greater<int>());
            for(int j = 0; j< matrix[0].size();j++){

                result = max(result, matrix[i][j]*(j+1));

            }
        }
        return result;

    }
};