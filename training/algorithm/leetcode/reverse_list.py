from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse linked list iteratively"""
    prev = None
    current = head
    
    while current is not None:
        next_temp = current.next  # Store next node
        current.next = prev  # Reverse the link
        prev = current  # Move prev to current
        current = next_temp  # Move to next node
    
    return prev  # New head of the reversed list


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse linked list recursively"""
    # Base case: if head is null or only one node, return head
    if head is None or head.next is None:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    head.next.next = head  # Make the next node point to current node
    head.next = None  # Set current node's next to null
    
    return new_head  # Return new head of reversed list


def main():
    # Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    reversed_head = reverse_list(head)
    
    # Print reversed list
    current = reversed_head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()
    
    new_reversed_head = reverse_list_recursive(reversed_head)
    
    # Print reversed list using recursive method
    current = new_reversed_head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()


if __name__ == "__main__":
    main()
