class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def rearrange(head):
  dummy_head = ListNode(0, head)
  low = dummy_head.next
  high = low.next

  while high and high.next:
    low.next = high.next
    low = low.next
    high.next = low.next
    high = high.next

  # Check if high is not None before connecting
  if high:
    high.next = low.next
  low.next = None

  return dummy_head.next


# Example usage (same as before)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = rearrange(head)
while result:
  print(result.val, end=" -> ")
  result = result.next
