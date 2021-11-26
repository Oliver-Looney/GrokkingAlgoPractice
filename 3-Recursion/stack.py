class StackNode:
    next = None

    def __init__(self, dataInput):
        self.data = dataInput


class Stack:
    topOfStack = None

    def __init__(self):
        pass

    def pop(self):
        if self.topOfStack:
            result = self.topOfStack
            self.topOfStack = self.topOfStack.next
            return result
        else:
            return StackNode("Empty")

    def push(self, newNode):
        if isinstance(newNode, StackNode):
            newNode.next = self.topOfStack
            self.topOfStack = newNode
            return True
        else:
            return False


node1 = StackNode("dog")
node2 = StackNode("cat")
node3 = StackNode("cow")

stack = Stack()
print(stack.push(node1))
print(stack.push(node2))
print(stack.push(node3))

print(stack.pop().data)
print(stack.pop().data)
print(stack.pop().data)
print(stack.pop().data)

