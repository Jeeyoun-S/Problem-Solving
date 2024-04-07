# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next

        nums = []
        for _ in range(n // 2):
            nums.append(head.val)
            head = head.next

        if n % 2 == 1:
            head = head.next

        for i in range(n // 2):
            if nums[-i - 1] != head.val:
                return False
            head = head.next

        return True