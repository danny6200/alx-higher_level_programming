#!/usr/bin/python3

'''
This is a singly linked list module

It provides the class and various methods
of a singly linked list
'''


class Node:
    '''
    This is a Node class

    It Provides the blueprint to instantiate
    a node object
    '''

    def __init__(self, data, next_node=None):
        '''
        This is the class constructor
        '''
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''
        This is property getter function

        It is used to retrieve the value of data
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''
        This is a property setter function

        It sets the value of data
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''
        This is a property getter function
        It retrieves the value of next_node
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        This is a property setter function
        It sets the value of the next node
        '''
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    '''
    This class defines a singly linked list

    It uses the Node class to create a linked list
    '''
    def __init__(self):
        '''
        This defines the Singly Linked List Constructor
        '''
        self.__head = None

    def sorted_insert(self, value):
        '''
        This function adds a new node to the
        singly linked list in increasing order
        of value
        '''
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while current.next_node is not None and current.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        '''
        This makes the singly linked list printable
        '''
        result = ""
        current = self.__head

        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
