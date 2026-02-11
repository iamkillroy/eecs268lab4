#!/usr/bin/env python3
# By Lucas Frias KU EECS 268
# Lab 3 - Dated Feb 10th 2026
#       <@
#       (KU//
#        "
# Rock Chalk!
from typing import Union #type declaration
class Node:
    """Node Class that stores entry and reference to self
    I added an iterable part to this Node that returns next as the value of the Node"""
    def __init__(self, entry, next: Union[None, Node] = None) -> None:
        """Creates a Node"""
        self.entry = entry
        self.next = next
    def __iter__(self):
        oldnext = self.next
        self.next = self.next.next
        yield oldnext

class LinkedList:
    def __init__(self) -> None:
        """Creates a Linked List that can be inserted and traversed"""
        self.head = None
        self.linkedListLength = 0
    def insert(self, index: int, entry) -> None:
        """Inserts the index at either 0 (front) or length inclusively"""
        print("insert" + entry)
        if self.head == None:
            self.head = Node(entry)
            self.linkedListLength += 1
            return None
        currentNode = self.head
        j = 0
        while j != index and currentNode.next is not None: #if we're not at the index or we're at the end of the list
            currentNode = currentNode.next #recursively go through each element A -> B -> C
            j += 1
        currentNode.next = Node(entry) #se the next entry to the next Node
        self.linkedListLength += 1
    def ___reallength(self) -> int:
        if self.head == None: return 0 #quick zero node check
        currentNode = self.head #set the current entry to the head
        lengthCounter = 1
        while currentNode.next != None: #while the entry is not none
            lengthCounter += 1 #increment by 1
            currentNode = currentNode.next #set the current entry to the the next entry
        return lengthCounter #return the length
    def length(self) -> int:
        return self.linkedListLength
    def get_entry(self, index) -> Node:
        currentNode = self.head
        j = 0
        while j != abs(index):
            pass
ll = LinkedList()
print(ll.length())
ll.insert(0, "hello")
ll.insert(1, "world")
ll.insert(2, "big")
ll.insert(3, "boy")

input("e")
print(ll.length())
