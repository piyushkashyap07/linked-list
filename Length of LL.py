# For a given singly linked list of integers, find and return its length. Do it using an iterative method.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First and the only line of each test case or query contains elements of the singly linked list separated by a single space. 
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
# Output format :
# For each test case, print the length of the linked list.

# Output for every test case will be printed in a separate line.
#  Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# Time Limit: 1 sec
# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1
# Sample Output 1 :
# 7
# Sample Input 2 :
# 2
# 10 76 39 -3 2 9 -23 9 -1
# -1
# Sample Output 2 :
# 8
# 0

from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None






def length(head) :
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count

# coding ninjas answer

# def lenght(head):
#     count=0
#     temp=head
#     while temp is not None:
#         count+=1
#         temp=temp.next
#     return count









        




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
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    print(length(head))

    t -= 1