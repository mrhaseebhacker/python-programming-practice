class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # store next node
        current.next = prev       # reverse the link
        prev = current            # move prev forward
        current = next_node       # move current forward

    return prev  # new head of the reversed list

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Example usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
print("Original List:")
print_linked_list(head)

reversed_head = reverseList(head)
print("Reversed List:")
print_linked_list(reversed_head)
