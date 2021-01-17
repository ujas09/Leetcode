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
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        if (k == arr.size())
            return arr;
        if(x <= arr[0])
            return {arr.begin(), arr.begin() + k};
        int n = arr.size();
        if (x >= arr.back())
            return {arr.begin() + n - k, arr.end()};

        int pos = binary(arr, x);

        int start = max(0, pos - k);
        int end = min(n - 1, pos + k);

        while (end - start >= k){

            if (x - arr[start] > arr[end] - x)
                start += 1;
            else
                end -= 1;



        }

        return {arr.begin() + start, arr.begin() + end + 1};
    }
};