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
        print("insert " + str(entry))
        if self.head == None:
            self.head = Node(entry)
            self.linkedListLength += 1
            return None
        currentNode = self.head
        j = 0
        while j != index and currentNode.next is not None: #if we're not at the index or we're at the end of the list
            currentNode = currentNode.next #recursively go through each element A -> B -> C
            j += 1
        #REALLY IMPORTANT
        # to keep the list "linked" i'm going to get the next.next value
        # but if this is none, we gotta just add it on
        try:
            insertLocationNextNode = currentNode.next.next
        except AttributeError:
            insertLocationNextNode = None
        currentNode.next = Node(entry, next = insertLocationNextNode) #se the next entry to the next Node
        self.linkedListLength += 1
    def length(self) -> int:
        """Fuction that recursively goes through every single element, but also doesn't
        necessarily need to go through every value because we're just counting and is an overengineered
        solution because I don't trust the methods and I'd rather be dead certain of the length"""
        if self.head == None: return 0 #quick zero node check
        currentNode = self.head #set the current entry to the head
        lengthCounter = 1
        while currentNode.next != None: #while the entry is not none
            lengthCounter += 1 #increment by 1
            currentNode = currentNode.next #set the current entry to the the next entry
        return lengthCounter #return the length
    def add(self, entry, front: bool=False) -> None:
        """Adds a linked list's element to the top (like a stack) or bottom (like a queue)"""
        if front: #if we wanna add to the front
                previousNode = self.head
                self.head = Node(entry, previousNode)
        else: #get the length, insert there
            self.insert(self.length(), entry) #no offset needed on the length, it's the last nth indexable + 1 so next
    def display(self) -> str:
        """Displays the entire node in a human readable output way"""
        #converting from writing rust all break kinda made me like type
        # declarations that are explicit like this. it might be just a phase mom :(
        if self.head == None: raise RuntimeError("No Nodes in this list")
        nodeElementString: str = "START | "
        nodeValueString: str =   "VALUE | "
        currentNode: Node = self.head #start
        charDisplayList: tuple = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "X", "Z")
        charDisplayPoint: int = 0
        while hasattr(currentNode, "next"):
            #first let's see if the entry can actually be displayed
            # for real for real by python's inbuilt str()
            try:
                valueOfNodeEntry = str(currentNode.entry)
            except TypeError:
                #that's okay let's just say the type as a string
                valueOfNodeEntry = str(type(currentNode.entry))
            nodeValueString = nodeValueString + valueOfNodeEntry + " " #set value and offset
            distanceBetweenValue = (len(valueOfNodeEntry)//2 ) * " " #evil little offset
            nodeElementString = nodeElementString + distanceBetweenValue + charDisplayList[charDisplayPoint%25] + " " #to display A B etc
            currentNode = currentNode.next
            charDisplayPoint += 1
        print(nodeElementString)
        print(nodeValueString)
        return nodeElementString + "\n" + nodeValueString
    def get_entry(self, index: int) -> Node:
        """Gets entry with negative indexing"""
        if self.head == None: raise IndexError("List is empty")#quick zero node check
        currentNode: Node = self.head
        j: int = 0
        #two modes, negative and positive addressing
        # postive addressing here
        if index >= 0:
            finalValue: int = index
        else: #negative addressing
            finalValue: int = (self.length() - 2) - index #-1 is for the list len versus index offset
        try:
            while j != abs(finalValue): #while we're not there
                    currentNode = currentNode.next #increment
                    j += 1
            return currentNode.entry #return entry
        except TypeError:
            raise IndexError("The index can't be found in the list")
    def clear(self) -> None:
        """Clears the list"""
        self.head = None #just clear it, thanks garbage collection in python!!!
        return None
    def remove(self, index) -> None:
        if self.head == None: raise IndexError(f"Can't delete from non-existant index {index}")
        try:
            j = 0
            currentNode: Node = self.head
            previousNode: Node = None
            while j != index:
                previousNode = currentNode
                currentNode = currentNode.next

                j += 1
            #okay now that we've found it, we need to set the previous node's value to the currentNode.next
            previousNode.next = currentNode.next
            self.linkedListLength -= 1
        except:
            raise IndexError(f"Can't delete from non-existant index {index}")
