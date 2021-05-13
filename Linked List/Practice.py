class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None  # make None as the default value for next.
        
def count_nodes(head):
    # assuming that head != None
    count = 1
    current = head
    while current.next is not None:
        current = current.next
        count += 1
    return count


nodeA = ListNode(1)
nodeB = ListNode(5)
nodeC = ListNode(5)
nodeD = ListNode(5)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD

nodeAA = ListNode(1)
nodeBB = ListNode(5)
nodeCC = ListNode(5)
nodeDD = ListNode(5)

nodeAA.next = nodeBB
nodeBB.next = nodeCC
nodeCC.next = nodeDD

# print("This linked list's length is: (should print 5)")
# print(count_nodes(nodeA))

def getNum(Head):
    num = []
    current = Head
    counter = 0
    while current is not None:
        current_num = current.val
        num.append(ListNode(current_num))
        current = current.next
        counter += 1
    return num, counter

# num here is still in reverse order to properly add

def addTwoNum(l1: ListNode, l2: ListNode):

    # List of ListNode objects
    num_1_list, counter_1 = getNum(nodeA)
    num_2_list, counter_2 = getNum(nodeAA)
    
    my_sum = []
    
    remainder = 0
    index = 0

    print(f'Before loop, remainder is: {remainder}')
    
    for i in range(counter_1):
        
        current_sum = num_1_list[i].val + num_2_list[i].val

        if current_sum >= 10:
            to_add = current_sum - 10
            if current_sum == 10 and remainder >= 1:
                my_sum.insert(index, remainder)
                remainder = 1
            elif current_sum > 10 and remainder >= 1:
                new_add = remainder + to_add - 10
                my_sum.insert(index, new_add)
                remainder = 1
            else:
                my_sum.insert(index, to_add)
                remainder += 1
                
        elif current_sum < 10:
            to_add = current_sum + remainder
            if to_add >= 10:
                new_add = current_sum - 10
                my_sum.insert(index, new_add)
                remainder = 1
            else:
                my_sum.insert(index, to_add)
                remainder = 0
                
        print(f'Looping back! Remainder is: {remainder}')
        index -= 1

    if remainder == 0:
        print('Returning')
        linked_list = ListNode(index, my_sum)
        return my_sum
    
    elif remainder >= 1:
        print(f'In here')
        index -= 1
        my_sum.insert(index, 1)
        return my_sum

print(addTwoNum(nodeA, nodeAA))
