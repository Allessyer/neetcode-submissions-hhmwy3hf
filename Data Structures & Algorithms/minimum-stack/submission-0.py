class MinStack:

    """
    [1,2]
    [1,1]
    
    """

    def __init__(self):
        self.stack = []
        self._min = []
        

    def push(self, val: int) -> None:
        
        if len(self._min) == 0:
            self._min.append(val)
        else:
            if val < self._min[-1]:
                self._min.append(val)
            else:
                self._min.append(self._min[-1])

        self.stack.append(val)
        
    def pop(self) -> None:
        self._min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self._min[-1]
        
