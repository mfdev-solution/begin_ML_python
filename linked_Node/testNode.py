"""
File : testNode.py
Tests the Node class.
"""
from email import header
from Node import Node
head = None
for count in range(1,6):
    head = Node(count , head)

while head != None :
    print(head.data)
    head = head.next