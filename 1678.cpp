class Solution {
public:
    string interpret(string command) {

        string result = "";

        vector<int> stk;

        for(int i= 0;i < command.size();i++){
            if(command[i] == 'G')
                result = result + 'G';
            else if(command[i] == '(')
                stk.push_back(i);
            else if(command[i] == ')'){
                int position = stk.back();
                stk.pop_back();
                if(i - position == 1)
                    result = result + 'o';
                else
                    result = result + "al";
            }



        }
        return result;

    }
};