# For a given singly linked list of integers, find and return the node present at the middle of the list.
# Note :
# If the length of the singly linked list is even, then return the first middle node.

# Example: Consider, 10 -> 20 -> 30 -> 40 is the given list, then the nodes present at the middle with respective data values are, 20 and 30. We return the first node with data 20.
#  Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space. 
# Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
#  Output Format :
# For each test case/query, print the data value of the node at the middle of the given list.

# Output for every test case will be printed in a seperate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5 
# Where M is the size of the singly linked list.

# Time Limit: 1sec
# Sample Input 1 :
# 1
# 1 2 3 4 5 -1
# Sample Output 1 :
# 3
# Sample Input 2 :
# 2 
# -1
# 1 2 3 4 -1
# Sample Output 2 :
# 2
from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def midPoint(head) :
    # Write your code here
    if head is None or head.next is None:
        return head
    slow=head
    fast=head.next.next
    while fast is not None:
        slow=slow.next
        if(fast.next is not None):
            fast=fast.next.next
        else:
            break
    return slow



















def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    mid = midPoint(head)

    if mid is not None :
        print(mid.data)

    t -= 1