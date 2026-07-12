class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,x):
        if not self.stack:
            self.stack.append(x)
            self.min_stack.append(x)
        else:
            self.stack.append(x)
            if self.min_stack[-1] > x:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])
    def pop(self):
        self.min_stack.pop()
        self.stack.pop()
    
    def get_min(self):
        return self.min_stack[-1]
    def top(self):
        return self.stack[-1]


ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
print(ms.get_min())   # 3 chiqadi — to'g'ri
print(ms.stack)  