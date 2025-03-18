#include <queue>

class MyStack {
public:
    MyStack() {
    }
    
    void push(int x) {
        q1.push(x); 
    }
    
    int pop() {
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int topElement = q1.front();
        q1.pop();
        
        swap(q1, q2);
        
        return topElement;
    }
    
    int top() {
        while (q1.size() > 1) {
            q2.push(q1.front());
            q1.pop();
        }
        int topElement = q1.front();
        
       
        q2.push(q1.front());
        q1.pop();
        
        // Swap the queues
        swap(q1, q2);
        
        return topElement;
    }
    
    bool empty() {
        // If q1 is empty, the stack is empty
        return q1.empty();
    }

private:
    queue<int> q1, q2;
};
