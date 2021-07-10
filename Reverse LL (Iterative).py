# Given a singly linked list of integers, reverse it iteratively and return the head to the modified list.
#  Note :
# No need to print the list, it has already been taken care. Only return the new head to the list.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
# Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
# Output format :
# For each test case/query, print the elements of the updated singly linked list.

# Output for every test case will be printed in a separate line.
#  Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^4
# Where N is the size of the singly linked list.

# Time Limit: 1 sec
# Sample Input 1 :
# 1
# 1 2 3 4 5 6 7 8 -1
# Sample Output 1 :
# 8 7 6 5 4 3 2 1
# Sample Input 2 :
# 2
# 10 -1
# 10 20 30 40 50 -1
# Sample Output 2 :
# 10 
# 50 40 30 20 10 

from sys import stdin , setrecursionlimit
setrecursionlimit(10**6)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Taking Input Using Fast I/O
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


# To print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


def reverse(head):
    if  head is None or head.next is None:
        return head
    prev=None
    curr=head
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev













# Main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    
    ans=reverse(head)
    printLinkedList(ans)

    t -= 1 

