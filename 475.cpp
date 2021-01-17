class Solution {
public:

    int binary(vector<int>&arr, int value){
        int result = -1;
        int low = 0;
        int high = arr.size();

        while (low <= high){
            int mid = low + (high - low)/2;

            if (arr[mid] > value)
                high = mid - 1;
            else{
                result = mid;
                low = mid + 1;
            }

        }
        return result;


    }


    int findRadius(vector<int>& houses, vector<int>& heaters) {
        int result = 0;
        int tem_result = INT_MAX;

        sort(houses.begin(), houses.end());
        sort(heaters.begin(),heaters.end());


        for(const int& house: houses){

            if(house <= heaters[0])
                result = max(result,heaters[0] - house);
            else if(house >= heaters.back())
                result = max(result,house - heaters.back());
            else{
                int pos = binary(heaters, house);

                result = max(result, min(house - heaters[pos], heaters[pos + 1] - house));
            }





        }

        return result;
    }
};