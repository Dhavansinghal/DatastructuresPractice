class Stack{
    def __init__(self,size = -1):
      (size == -1) ? self.container = [] : self.container = [None]*size
      self.size = size
      self.top = -1

    def push(nextData):
        if (self.top == self.size) or (self.size == 0):
            print("Stackoverflow: Stack is full")
        else:
            self.container.append(nextData);
            self.top += 1
    
    

}