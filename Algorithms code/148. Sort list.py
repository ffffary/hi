class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        def getMid(self, head):


#from leetcode:
#version1:
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head 
        
        left = head 
        right = self.getMid(head)
        temp = right.next
        right.next = None 
        right = temp 
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next 
                    
        return slow 
    
    def merge(self, left, right):
        tail = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left 
                left = left.next
            else:
                tail.next = right 
                right = right.next 
            tail = tail.next
            
        if left:
            tail.next = left 
            left = left.next 

        if right:
            tail.next = right
            right = right.next 
            
        return dummy.next 


#version2:
class Solution:
    def getMid(self, head):            # we will be using two pointers
        slow = fast = head             # what we want? Middle right, but we will stop the loop at one node before the middle
        while fast and fast.next:      # try to think about odd and even length of the list to completely understand the while loop
            fast = fast.next.next
            if fast: slow = slow.next
        mid, slow.next = slow.next, None   # assign None to the last node's next of left half, that is why we broke the loop one node before the middle.
        return mid
        
    def merge(self, left, right):
        head = prev = None    # taking prev pointers to point previous
        while left and right:  
		#Find the minimum value node and change its pointer to next accordingly
            mini = right        
            if left.val < right.val:
                mini = left
                left = left.next
            else: right = right.next
        
            if not head: head = prev = mini      # if head is None assign the head
            else: prev.next = prev = mini        # point the previous next and prev to minimum node just found
        if left: prev.next = left                # adding the remainings of left, while loop could have stopped because of right
        if right: prev.next = right              # adding the remainings of right, while loop could have stopped because of left
        return head
        
    def sortList(self, head: Optional[ListNode]):
        if not (head and head.next): return head     # if lesser than 2 element no need to divide
        mid = self.getMid(head)                      # get the middle node
        left = self.sortList(head)                   # further divide the left part list
        right = self.sortList(mid)                   # further divide the right part of the list
        return self.merge(left, right)               # merge the sorted lists


def insertionSort(self, arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [3, 5, 9, 10, 40, 4, 34, 12, 33, 2]
insertionSort(arr)
for i in range(len(arr)):
    print("%d" % arr[i])

    


