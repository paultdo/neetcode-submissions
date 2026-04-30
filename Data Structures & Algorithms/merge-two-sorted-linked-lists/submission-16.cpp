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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* h1 = list1;
        ListNode* h2 = list2;
        ListNode* i = list1;
        ListNode* j = list2;
        bool end_reached = false;

        if(!i) {
            return j;
        }

        if(!j) {
            return i;
        }

        while(!end_reached) {
            ListNode* temp = nullptr;

            while(i->next && i->next->val <= j->val) {
                i = i->next;
            }

            while(j->next && j->next->val < i->val) {
                j = j->next;
            }

            if(i->val > j->val) {
                temp = j->next;
                j->next = i;
                j = temp;
            } else {
                temp = i->next;
                i->next = j;
                i = temp;
            }
            if(!temp) {
                end_reached = true;
            }
        }

        if(list1->val <= list2->val) {
            return list1;
        } else {
            return list2;
        }


    }
};
