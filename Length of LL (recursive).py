# Given a linked list, find and return the length of the given linked list recursively.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First and the only line of each test case or query contains elements of the singly linked list separated by a single space. 
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
# Output format :
# For each test case, print the length of the linked list.

# Output for every test case will be printed in a separate line.
#  Constraints :
# 1 <= t <= 20
# 0 <= N <= 10^4
# Time Limit: 1 sec
# Sample Input 1:
# 1 
# 3 4 5 2 6 1 9 -1
# Sample Output 1:
# 7
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

def lengthRecursive(head):
    return lr(head)
    
def lr(head,count=0):
    
    curr=head
    if curr==-1 or curr== None:
        return count
    else:
        curr=curr.next
        return lr(curr,count+1)













# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    head = takeInput()
    ans=lengthRecursive(head)
    print(ans)
    t -= 1 