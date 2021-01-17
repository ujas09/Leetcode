/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* temHead = head;
        int n = 0;

        while(temHead){
            n += 1;
            temHead = temHead->next;
        }

        int first = min(k, n -k + 1);
        int second = max(k , n - k + 1);

        ListNode* nextHead = head;
        int length = 0;
        ListNode* firstNode;
        ListNode* secondNode;
        while(nextHead){
            length += 1;
            if(length == first)
                firstNode = nextHead;
            if(length == second)
                secondNode = nextHead;
            nextHead = nextHead->next;
        }

        int tem = 0;
        tem = firstNode->val;
        firstNode->val = secondNode->val;
        secondNode->val = tem;

        return head;

    }
};