"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        if not self.head and not self.tail:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
        elif self.head == self.tail:
            oldhead = self.head
            self.head = ListNode(value, None, oldhead)
            oldhead.prev = self.head
        else:
            new_node = ListNode(value, None, self.head)
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.head or not self.tail:
            return None
        else:
            value = self.tail.value
            self.delete(self.tail)
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if not self.tail or not self.head:
            return None
        elif self.head == self.tail:
            return None
        else:
            self.delete(node)
            self.add_to_head(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node == self.tail:
            return
        elif node == self.head:
            self.head = self.head.next
            self.head.prev == None
            self.tail.next = node
            self.tail = node
            self.tail.next = None
        self.tail.next = node
        self.tail = node
        self.tail.next = None


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            self.delete(node)
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.delete(node)
        self.delete(node)
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None
        current = self.head.next
        largest = self.head.value
        while current is not None:
            if current.value > largest:
                largest = current.value
            current = current.next
        return largest
