#!/usr/bin/python3
class Node:
    """ Defines node of a singlylinkedlist"""

    def __init__(self, data, next_node=None):
        """ Initialize a newnode

        Args:
        data (int) - data to add in the newly created list
        next_node(Node) - address of the nextnode
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Method to retrive data of a node
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ Method to add data to a node
        """
        # make sure data is int
        if not isinstance(value, int):
            # raise a Typeerror exception
            raise TypeError("data must be an integer")
        # add data if its of type int
        self.__data = value

    @property
    def next_node(self):
        """ Method to retrive nextnode
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            # raise an exception
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list
    """

    def __init__(self):
        """ initialize a singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """ methode to insert node in sorted ascending order
        """
        # create a new node
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head

        # traverse the list to find the appropriate position to insert node
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn
