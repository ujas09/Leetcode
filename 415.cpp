class Solution {
public:
    string addStrings(string num1, string num2) {
        int pos1 = num1.size() - 1;
        int pos2 = num2.size() - 1;
        string result = "";
        int carry = 0;
        int summation = 0;
        while (pos1 >= 0 || pos2 >= 0){

            if(pos1 == -1){
                summation = carry + num2[pos2] - 48;
                pos2 -= 1;

            }
            else if(pos2 == -1){
                summation = carry + num1[pos1] - 48;
                pos1 -= 1;

            }

            else{
                summation = carry + int(num2[pos2]) + int(num1[pos1]) - 96;
                pos2 -= 1;
                pos1 -= 1;

            }

            result += to_string(summation % 10);
            carry = int(summation / 10);





        }
        if (carry > 0)
            result += to_string(carry);
        string result2  = "";
        for(int i = result.size() - 1; i>= 0; i--){
            result2 += result[i];

        }
    return result2;
    }

};