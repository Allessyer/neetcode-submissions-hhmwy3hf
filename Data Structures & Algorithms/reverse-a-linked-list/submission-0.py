# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            current = head
            previous = None
            
            while current.next is not None:
                save_link = current.next
                current.next = previous
                previous = current
                current = save_link

            current.next = previous
            head = current

        return head
