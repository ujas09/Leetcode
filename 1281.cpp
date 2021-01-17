class Solution {
public:
    int subtractProductAndSum(int n) {
        int summation = 0;
        int multi = 1;

        while(n){
            int tem = n % 10;
            n = n/10;

            summation += tem;
            multi = multi * tem;
        }

        return multi - summation;

    }
};