"""
 Implement Linked list in Python
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None        

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        if node:
            while node:
                nodes.append(str(node.data))
                node = node.next
            return "->".join(nodes)
        return "None"
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_at_first_position(self, node):
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def add_at_last_position(self, node):
        if not self.head:
            self.head = node
            return
        for existing_node in self:
            if existing_node.next is None:
                existing_node.next = node
        
    def add_after(self, targeted_data, node):
        if self.head is None:
            raise Exception("Linked List Is Empty")
        for existing_node in self:
            if existing_node.data == targeted_data:
                node.next = existing_node.next
                existing_node.next = node
                return
        raise Exception("No Node Found With Provided Data")

    def add_before(self, targeted_data, node):
        if self.head is None:
            raise Exception("Linked List Is Empty")
        
        if self.head.data == targeted_data:
            self.add_at_first_position(node)

        previous_node = self.head        
        for existing_node in self:
            if existing_node.data == targeted_data:
                previous_node.next = node
                node.next = existing_node                
                return
            previous_node = existing_node
        raise Exception("No Node Found With Provided Data")
    
    def remove_node(self, targeted_data):
        if self.head is None:
            raise Exception("Linked List Is Empty")
        
        if self.head.data == targeted_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == targeted_data:
                previous_node.next = node.next
            previous_node = node                
        raise Exception("No Node Found With Provided Data")