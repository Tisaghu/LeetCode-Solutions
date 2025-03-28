def arrayToLinkedList(arr):
    if len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head