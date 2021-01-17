class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        priority_queue <pair<int,int>, vector<pair<int,int>>, greater<>> start;
        priority_queue <pair<int,int>, vector<pair<int,int>>, greater<>> end;

        for(int i = 0; i< intervals.size(); i++){

            start.push(make_pair(intervals[i][0], i));
            end.push(make_pair(intervals[i][1], i));

        }

        vector<int> result(intervals.size(), -1);

        while(!end.empty()){

            auto now_serve = end.top();
            end.pop();

            while (!start.empty() and start.top().first < now_serve.first)
                start.pop();

            if(!start.empty())
                result[now_serve.second] = start.top().second;
            else
                result[now_serve.second] = -1;




        }

        return result;
    }
};