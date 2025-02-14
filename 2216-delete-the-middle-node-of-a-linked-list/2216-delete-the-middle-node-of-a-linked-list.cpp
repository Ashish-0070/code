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
    ListNode* deleteMiddle(ListNode* head) {
        if(head==NULL or head->next==NULL) return NULL;
        ListNode *s1=head, *s2=head, *prev=NULL;
        while(s2!=NULL and s2->next!=NULL){
            s2=s2->next->next;
            prev=s1;
            s1=s1->next;
        }
        prev->next=s1->next;
        s1->next=NULL;
        delete s1;

    return head;        
    }
};