# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd tortoise and hare algorithm
        hare = tortoise = head

        # hare steps by 1, tortoise by 2
        # if there is a cycle, the tortoise will lap the hare and eventually meet
        while tortoise and tortoise.next:
            hare = hare.next
            tortoise = tortoise.next.next
            if hare is tortoise:
                return True
        
        return False
