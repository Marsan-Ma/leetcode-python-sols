# https://leetcode.com/problems/logger-rate-limiter/

# Design a logger system that receive stream of messages along 
# with its timestamps, each message should be printed if and 
# only if it is not printed in the last 10 seconds.

# Given a message and a timestamp (in seconds granularity), 
# return true if the message should be printed in the given timestamp, 
# otherwise returns false.

# It is possible that several messages arrive roughly at the same time.

# Example:

# Logger logger = new Logger();

# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true; 

# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;

# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;

# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;

# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;

# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;


class Logger(object):

    # [Ideas]
    # store when it's ok for a message to be printed again

    def __init__(self):
        self.ok = {}

    def shouldPrintMessage(self, timestamp, message):
        if timestamp < self.ok.get(message, 0):
            return False
        self.ok[message] = timestamp + 10
        return True




# Key: Includes a last pointer to TTL old records
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.last = None
        self.dic = {}  # saving timestamp and last message link
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        info = self.dic.get(message)    # info = (timestamp, last)
        # print(info)
        
        if info == None:
            self.dic[message] = (timestamp, self.last)
            self.last = message
            return True
        elif timestamp - info[0] < 10:
            return False
        else: # timestamp - t >= 10:
            # TTL old records
            _, last = self.dic[message]
            while (last in self.dic) and (timestamp - self.dic[last][0] > 10):
                _, lastlast = self.dic[last]
                del self.dic[last]
                if not lastlast: break
                last = lastlast
            # update record
            self.dic[message] = (timestamp, self.last)
            self.last = message
            print("recover:", self.dic)
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

