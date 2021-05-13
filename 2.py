# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Return a linked list
        #head -> tail
        #Use mod to easily get remainder
        head_val = (l1.val + l2.val)
        #Use floor division to ge the quotient
        carry_over = (head_val // 10)
        head = ListNode(head_val % 10)
        current_node = head
        
        #Scenarios:
        #1: Same number of elements in l1 and l2
            #: While loop until there are no more elements, while adding the sum of elements at each indices
        #2: Different number of elements in l1 and l2
            #: Depending on which list ends first, simply add the remaining elements to the first list

            #: l1: [1 2 3 4 5 6]
            #   +
            #: l2: [/ / / 1 1 1]
            #   =
            #: sum:[/ / / 5 6 7]
            #   =
            #: sum:[1 2 3 5 6 7]

        #Scenario 1
        while(l1.next and l2.next):
            #First pass: current_node = head
            l1 = l1.next
            l2 = l2.next
            next_val = (l1.val + l2.val + carry_over)
            current_node.next = ListNode(next_val % 10)
            carry_over = (next_val // 10)
            current_node = current_node.next

        #Here with all the sums for matching indices
        #: l1: [1 2 3 4 5 6]
        #   +
        #: l2: [/ / / 1 1 1]
        #   =
        #: sum:[/ / / 5 6 7]
        #   =
        #: sum:[1 2 3 5 6 7]

        if(l1.next == None):
            remaining = l2
        else:
            remaining = l1

        while(remaining.next):
            remaining = remaining.next
            next_val = (remaining.val + carry_over)
            current_node.next = ListNode(next_val % 10)
            carry_over = (next_val // 10)
            current_node = current_node.next
            
        if not remaining.next and carry_over > 0:
            current_node.next = ListNode(carry_over)

        return head
