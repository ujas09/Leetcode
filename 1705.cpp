class Solution {
public:
    int eatenApples(vector<int>& apples, vector<int>& days) {

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;

        int result = 0;
        for(int i = 0; i< apples.size(); i++){
            pq.push(make_pair(i + days[i], apples[i]));
            while (!pq.empty() and pq.top().first <= i)
                pq.pop();

            if (!pq.empty()){
                result += 1;
                pair<int,int> top = pq.top();
                pq.pop();
                top.second -= 1;
                if (top.second != 0)
                    pq.push(make_pair(top.first, top.second));

                    }



            }

            int i = apples.size();

            while(!pq.empty()){
                while (!pq.empty() and pq.top().first <= i)
                    pq.pop();

                if (!pq.empty()){
                    result += 1;
                    pair<int,int> top = pq.top();
                    pq.pop();
                    top.second -= 1;
                    if (top.second != 0)
                        pq.push(make_pair(top.first, top.second));

                }

                i+=1;

            }
        return result;

        }



};