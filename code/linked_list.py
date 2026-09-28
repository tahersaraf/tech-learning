class Node:
    """A single node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Only points forward

class SinglyLinkedList:
    """A manager class to handle head pointers and insertions."""
    def __init__(self):
        self.head = None  # The starting node of the list

    def append(self, data):
        """Add a new node to the very end of the list."""
        new_node = Node(data)
        
        # If the list is empty, make this the head
        if not self.head:
            self.head = new_node
            return
            
        # Otherwise, traverse from head to the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Link the last node to our new node
        current.next = new_node

    def prepend(self, data):
        """Add a new node to the very beginning (head) of the list."""
        new_node = Node(data)
        new_node.next = self.head  # Point new node to the old head
        self.head = new_node       # Update head to be the new node

    def display(self):
        """Print the entire list from start to finish."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None


linkedlist = SinglyLinkedList()

linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)


linkedlist.display()
print(linkedlist.find_middle())



