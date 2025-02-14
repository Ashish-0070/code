class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) {
            return head;
        }
        
        ListNode* temp = head;
        int length = 1;  
        while (temp->next) {
            temp = temp->next;
            length++;
        }
        
        k = k % length;
        if (k == 0) return head;
        
        temp->next = head;
        
        ListNode* newTail = head;
        for (int i = 0; i < length - k - 1; i++) {
            newTail = newTail->next;
        }
        ListNode* newHead = newTail->next;
        newTail->next = nullptr;
        
        return newHead;
    }
};
