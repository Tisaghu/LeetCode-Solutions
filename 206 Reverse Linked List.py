# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #initialize variables
        current = head
        prev = None

        while current:
            nextNode = current.next
            current.next = prev 
            prev = current
            current = nextNode

        return prev

def arrayToLinkedList(arr):
    if len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


test = Solution()
print(test.reverseList(arrayToLinkedList([1,2,3,4,5]))) #5->4->3->2->1->None