class MyQueue(object):

    def __init__(self):
        self.queue = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        self.empty()
        

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        else:
            removed = self.queue.pop(0)
            return removed


    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        else:
            return self.queue[0]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Notes:
# __init__ only needed to initialize the queue, it doesn't need to initialize empty boolean
# To check size of stack use len(queue)
# To check the front of the queue, use pop(0). Just pop() would remove the back of the queue (first in stack)