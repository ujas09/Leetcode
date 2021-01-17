class CustomStack {
public:
    int maxsize;
    vector<int>stk;
    CustomStack(int maxSize) {
        maxsize = maxSize;

    }

    void push(int x) {

        if(stk.size() != maxsize)
            stk.push_back(x);

    }

    int pop() {
        if(!stk.empty()){
            int result = stk.back();
            stk.pop_back();
            return result;}
        return -1;

    }

    void increment(int k, int val) {
        int n = stk.size();
        for(int i = 0; i< min(k, n); i++)
            stk[i] += val;


    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */