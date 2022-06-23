#!/usr/bin/python3
"""Singly Linked List"""


class Node:
    """A Node Class"""

    def __init__(self, data,  next_node=None):
        """Initialise a new node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the data of the node"""

        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node"""

        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the  next_node_node of the linked list"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node node of the linked list"""

        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """String representation of Node instance
        Returns:
            Formatted string representing the node
        """
        return str(self.__data)


class SinglyLinkedList:
    """A class to Implement a single linked list"""

    def __init__(self):
        """Initialise the linked list"""

        self.head = None

    def sorted_insert(self, value):
        """Inserts a value into the linked list in a sorted order"""

        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            if value <= self.head.data:
                new_node.next_node = self.head
                self.head = new_node
                return
            temp_head = self.head
            while temp_head.next_node is not None:
                if value <= temp_head.next_node.data:
                    new_node.next_node = temp_head.next_node
                    temp_head.next_node = new_node
                    return
                temp_head = temp_head.next_node
            temp_head.next_node = new_node

    def __str__(self):
        """An Informal string representation of the singly list object"""

        res = ""
        temp = self.head
        while temp.next_node is not None:
            res += str(temp.data) + '\n'
            temp = temp.next_node
        res += str(temp.data)
        return res
