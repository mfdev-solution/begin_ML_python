"""

File : testNode.py
Tests the Node class.

"""
from Node import Node
#head = Node(0)
head = Node.createNode(8)


# #modifier une valeur
head.printNode(head)
target = 10
val = 9
res = head.replace(head,target,val)
print(f"{target} is replaced by {val} => {res}")
head.printNode(head)
head = head.insert(head,12)
head.printNode(head)











