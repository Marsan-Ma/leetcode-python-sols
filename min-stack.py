# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving 
# the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.



class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x): # O(log(n))
        """
        :type x: int
        :rtype: nothing
        """
        m = min(self.stack[-1][1], x) if self.stack else x
        self.stack += [(x, m)]

    def pop(self): # O(log(n))
        """
        :rtype: nothing
        """
        return self.stack.pop()

    def top(self): # O(1)
        """
        :rtype: int
        """
        return self.stack[-1][0] if self.stack else None
        

    def getMin(self): # O(1)
        """
        :rtype: int
        """
        return self.stack[-1][1] if self.stack else None
        