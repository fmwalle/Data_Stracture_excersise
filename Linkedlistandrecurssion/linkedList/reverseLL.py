class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def reverse_iterative(head):

    if not head:
        return None
    
    current=head
    prev=None
    while current:
        next_Node=current.next
        current.next=prev
        prev=current
        current=next_Node
    return prev

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage
# Creating a linked list 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print("Original linked list:")
print_linked_list(head)

reversed_head = reverse_iterative(head)

print("Reversed linked list:")
print_linked_list(reversed_head)    