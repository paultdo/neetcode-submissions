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
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        int size = 0;

        while(curr) {
            size++;
            curr = curr->next;
        }

        curr = head;

        int i = 0;
        int j = size - 1;
        
        while (i < size/2) {
            ListNode* tail = head;
            for(int k = 0; k < j; k++) {
                tail = tail->next;
            }

            int temp = curr->val;
            curr->val = tail->val;
            tail->val = temp;

            curr = curr->next;
            i++;
            j--;
        }

        return head;
        
    }
};
