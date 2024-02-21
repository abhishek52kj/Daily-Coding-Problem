class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def rearrangeLinkedList(head):
  if not head or not head.next:
    return head

  dummy = ListNode(0)
  dummy.next = head

  prev = dummy
  current = head

  while current and current.next:
    if current.val > current.next.val:
      current.val, current.next.val = current.next.val, current.val
    if current.val < prev.val:
      current.val, prev.val = prev.val, current.val
    current = current.next.next
    prev = prev.next.next

  return dummy.next


# Helper function to print the linked list
def printLinkedList(head):
  current = head
  while current:
    print(current.val, end=" -> ")
    current = current.next
  print("None")


# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
printLinkedList(head)

head = rearrangeLinkedList(head)

print("Linked list after rearranging:")
printLinkedList(head)
