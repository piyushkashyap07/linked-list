# Given a singly linked list of integers and an integer n, find and return the index for the first occurrence of 'n' in the linked list. -1 otherwise.
# Follow a recursive approach to solve this.
# Note :
# Assume that the Indexing for the linked list always starts from 0.
#  Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case or query contains the elements of the singly linked list separated by a single space.

# The second line of input contains a single integer depicting the value of 'n'.
# Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
#  Output format :
# For each test case/query, print the elements of the updated singly linked list.

# Output for every test case will be printed in a seperate line.
#  Constraints :
# 1 <= t <= 10^2
# 0 <= M <= 10^5
# Where M is the size of the singly linked list.

# Time Limit:  1sec
# Sample Input 1 :
# 1
# 3 4 5 2 6 1 9 -1
# 100
# Sample Output 1 :
# -1
# Sample Input 2 :
# 2
# 10 20010 30 400 600 -1
# 20010
# 100 200 300 400 9000 -34 -1
# -34
# Sample Output 2 :
# 1
# 5
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def findNodeRec(head, n) :
    if head is None :
        return -1
    
    count=findNodeRec(head.next,n)
    if head.data==n or count !=-1:
        count+=1
        return count
    else:
        return count































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


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    n = int(stdin.readline().rstrip())    

    print(findNodeRec(head, n))

    t -= 1