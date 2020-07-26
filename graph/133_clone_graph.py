
class Node:
   def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

test = Node(5)

print(test.val)
