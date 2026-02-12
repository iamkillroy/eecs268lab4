#!/usr/bin/env python3
# By Lucas Frias KU EECS 268
# Lab 3 - Dated Feb 10th 2026
#       <@
#       (KU//
#        "
# Rock Chalk!

from inspect import Attribute
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
    def display(self, debugInput=False, displayOutput=True) -> tuple[str, str]:
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
            distanceBetweenValue = " " + (len(valueOfNodeEntry)-3) * "-" + "> " #evil little offset
            nodeElementString = nodeElementString + charDisplayList[charDisplayPoint%25] + distanceBetweenValue #to display A B etc
            currentNode = currentNode.next
            charDisplayPoint += 1
        if displayOutput:
            print("LinkedList Display: ")
            print(nodeElementString)
            print(nodeValueString)
        if debugInput: input("OK > ")
        return nodeElementString, nodeValueString
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
    def pop(self) -> None:
        "Removes the top element"
        self.remove(self.length()-1) #nth element offset
    def remove(self, index) -> None:
        """Removes element from given index and links all Nodes back together"""
        if self.head == None: raise IndexError(f"Can't delete from non-existant index {index}")
        try:
            j = 0
            currentNode: Node = self.head #the current Node
            previousNode: Node = None #the next Node
            while j != index:
                previousNode = currentNode
                currentNode = currentNode.next
                j += 1
            #okay now that we've found it, we need to set the previous node's value to the currentNode.next
            try:
                previousNode.next = currentNode.next
            except AttributeError:
                pass #just means that the previous Node isn't actually real
                #like there's just no node that exist because it's like the 0th index
            self.linkedListLength -= 1
        except:
            raise IndexError(f"Can't delete from non-existant index {index}")
class WebBrowser:
    """Simulates the motions of a web browser using a linked list"""
    def __init__(self) -> None:
        """Creates a web browser"""
        self.linkedhistory: LinkedList = LinkedList()
        self.position: int = 0
    def navigate_to(self, url: str) -> None:
        """Navigates to the webpage """
        self.linkedhistory.insert(self.position, url)
        self.position += 1
    def forward(self) -> None:
        """Moves foward to the next page, if it exists"""
        if (self.linkedhistory.length() -1) < self.position + 1:
            #check to make sure that the new position isn't greater
            # than the indexable length of the array
            return None
        self.position += 1
    def backward(self) -> None:
        """Moves backwards to the last page, if it exists"""
        if self.position != 0:
            self.position -= 1
    def history(self) -> None:
        """Displays the history in a specific format"""
        _, historyValuesAsString = self.linkedhistory.display(displayOutput=False)
        historyValuesAsString.replace("VALUE | ", "")
        print("OLDEST\n===========\n")
        for i, websiteVisted in enumerate(historyValuesAsString.split(" ")):
            if i == self.position:
                print(websiteVisted + " <-- CURRENT")
            else:
                print(websiteVisted)

class Executive:
    """Reads file output as website nstructions"""
    def __init__(self) -> None:
        self.wb = WebBrowser()
        self.file = open(input("Web Browser -- Lucas Frias Lab 4 EECS 268 \nPlease give the file name >"), "r").read()
        self.commandList = self.file.split("\n")
        self.loop()
    def loop(self):
        """Loops the executive class"""
        for command in self.commandList:
            if len(command) == 0:
                continue #empty command
            if command[0] == "F": #FORWARD
                self.wb.forward()
            if command[0] == "B":
                self.wb.backward()
            if command[0] == "N": #navigate
               self.wb.navigate_to(command.split(" ")[1])
            if command[0] == "H": #history
                self.wb.history()
if __name__ == "__main__":
    Executive()
