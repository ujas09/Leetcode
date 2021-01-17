class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        unordered_set<int>visited;
        vector<int> stk;
        visited.insert(0);

        for (int i = 0;i< rooms[0].size(); i++){
            if(visited.find(rooms[0][i]) == visited.end()){
                stk.push_back(rooms[0][i]);
                visited.insert(rooms[0][i]);
            }


        }

        while(!stk.empty()){
            int room = stk.back();
            stk.pop_back();


            for (int i = 0;i< rooms[room].size(); i++){
            if(visited.find(rooms[room][i]) == visited.end()){
                stk.push_back(rooms[room][i]);
                visited.insert(rooms[room][i]);

            }

            }




        }
        return rooms.size() == visited.size();

    }
};