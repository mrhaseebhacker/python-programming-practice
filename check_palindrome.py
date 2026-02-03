class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    # Step 1: Find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Step 3: Compare both halves
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

# Example: Palindrome
values = [1, 2, 3, 2, 1]
head = create_linked_list(values)
print(isPalindrome(head))  # Output: True

# Example: Not a palindrome
values = [1, 2, 3, 4]
head = create_linked_list(values)
print(isPalindrome(head))  # Output: False
