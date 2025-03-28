# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #create initial dummy node
        head = ListNode(None, None)
        current = head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1 and not list2:
            current.next = list1
        elif list2 and not list1:
            current.next = list2

        return head.next
                
                



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
print(test.mergeTwoLists(arrayToLinkedList([1,2,4]), arrayToLinkedList([1,3,4]))) #1->1->2->3->4->4->None
