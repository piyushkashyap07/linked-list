# You have been given a linked list of integers. Your task is to write a function that deletes a node from a given position, 'pos'.
# Note :
# Assume that the Indexing for the linked list always starts from 0.

# If the position is greater than or equal to the length of the linked list, you should return the same linked list without any change.
# Illustration :
# The following images depict how the deletion has been performed.
# Image-I :
# Alt txt

# Image-II :
# Alt txt

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the linked list separated by a single space. 

# The second line of each test case contains the integer value of 'pos'. It denotes the position in the linked list from where the node has to be deleted.
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
# Output format :
# For each test case/query, print the resulting linked list of integers in a row, separated by a single space.

# Output for every test case will be printed in a separate line.
# You don't need to print explicitly, it has been taken care of.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# pos >= 0
# Time Limit: 1sec

# Where 'N' is the size of the singly linked list.
# Sample Input 1 :
# 1 
# 3 4 5 2 6 1 9 -1
# 3
# Sample Output 1 :
# 3 4 5 6 1 9
# Sample Input 2 :
# 2
# 3 4 5 2 6 1 9 -1
# 0
# 10 20 30 40 50 60 -1
# 7
# Sample Output 2 :
# 4 5 2 6 1 9
# 10 20 30 40 50 60
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def deleteNode(head, pos) :
    if pos<0 or pos> length(head):
        return head
    count=0
    prev=None
    curr=head
    while curr is not None:
        if pos== count:
            if  prev is not None:
                prev.next=prev.next.next
            else:
                head=head.next
            break
        prev=curr
        curr=curr.next
        count+=1
    return head

def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count























#Taking Input Using Fast I/O
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



#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1