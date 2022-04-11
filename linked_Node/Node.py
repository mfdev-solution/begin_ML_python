from typing import Any

from requests import head


class Node:
    def __init__(self , data  , next = None) -> None:
        self.data = data
        self.next = next
    def replace(self, head,target,val):
        prode = head
        while prode != None and target != prode.data:
            prode = prode.next
        if prode != None:
            prode.data = val
            return True
        else:
            return False
    def createNode(max)->Any:
        head = Node(0,None)
        for count in range(1,max):
            head = Node(count , head)
        return head
    def printNode(self,root):
        while root != None :
            print(f"{root.data} ",end='')
            root = root.next
        print()
    def insert(self,root,val):
        newNode = Node(val)
        if root is None:
            root = newNode
        else:
            prode = root
            while prode.next != None:
                prode = prode.next
            prode.next = newNode
        return root