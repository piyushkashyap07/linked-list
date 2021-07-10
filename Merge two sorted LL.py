# You have been given two sorted(in ascending order) singly linked lists of integers.
# Write a function to merge them in such a way that the resulting singly linked list is also sorted(in ascending order) and return the new head to the list.
# Note :
# Try solving this in O(1) auxiliary space.

# No need to print the list, it has already been taken care.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the first sorted singly linked list separated by a single space. 

# The second line of the input contains the elements of the second sorted singly linked list separated by a single space. 
# Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
# Output :
# For each test case/query, print the resulting sorted singly linked list, separated by a single space.

# Output for every test case will be printed in a seperate line.
# Constraints :
# 1 <= t = 10^2
# 0 <= N <= 10 ^ 4
# 0 <= M <= 10 ^ 4
# Where N and M denote the sizes of the singly linked lists. 

# Time Limit: 1sec
# Sample Input 1 :
# 1
# 2 5 8 12 -1
# 3 6 9 -1
# Sample Output 1 :
# 2 3 5 6 8 9 12 
# Sample Input 2 :
# 2
# 2 5 8 12 -1
# 3 6 9 -1
# 10 40 60 60 80 -1
# 10 20 30 40 50 60 90 100 -1
# Sample Output 2 :
# 2 3 5 6 8 9 12 
# 10 10 20 30 40 40 50 60 60 60 80 90 100
from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def mergeTwoSortedLinkedLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    finalhead=None
    finaltail=None
    if head1.data>head2.data:
        finalhead = Node(head2.data)
        head2 = head2.next
    else:
        finalhead = Node(head1.data)
        head1 = head1.next
        
    finaltail=finalhead

    # Write your code here
    while head1 != None and head2 != None:
        if head1.data>head2.data:
            finaltail.next=Node(head2.data)
            head2=head2.next
            finaltail = finaltail.next
        else:
            finaltail.next=Node(head1.data)
            head1=head1.next
            finaltail = finaltail.next
    
    if head1 != None:
        finaltail.next=head1
    else:
        finaltail.next=head2
    return finalhead

























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




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1