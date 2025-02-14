class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next) return NULL;  // If the list is empty or has only one node, no cycle.

        ListNode *slow = head;
        ListNode *fast = head;

        // Step 1: Detect if a cycle exists using Floyd's Tortoise and Hare Algorithm
        while (fast && fast->next) {
            slow = slow->next;          // Move slow by one step
            fast = fast->next->next;    // Move fast by two steps

            if (slow == fast) {         // Cycle detected
                // Step 2: Find the node where the cycle begins
                ListNode *start = head;
                while (start != slow) {
                    start = start->next;
                    slow = slow->next;
                }
                return start;  // The starting node of the cycle
            }
        }

        return NULL;  // No cycle detected
    }
};
