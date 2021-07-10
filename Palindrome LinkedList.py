# class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count=0
    temp=head
    while temp is not None:
        temp=temp.next
        count=count+1
    return count

def print_ll(head):
    if head==None:
        return
    print(head.data,end=" ")
    print_ll(head.next)
  
def reverse(head): 
        prev = None
        current = head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        head = prev
        return head
  
def check_palindrome(head) :
    if head is None or head.next is None:
        return True
    h1=head
    temp=head
    l=length(head)
    mid=0
    if l%2==0:
        mid=(l//2)-1
    else:
        mid=l//2
    i=0
    while i<mid:
        temp=temp.next
        i+=1
    h2=temp.next
    temp.next=None
    h2=reverse(h2)
    while h2 is not None:
        if h1.data==h2.data:
            h1=h1.next
            h2=h2.next
        else:
            return False
    return True
    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head
for _ in range(int(input())):
# Main
# Read the link list elements including -1
    arr=list(int(i) for i in input().strip().split(' '))
    # Create a Linked list after removing -1 from list
    l = ll(arr[:-1])
    ans = check_palindrome(l)
    if ans:
        print("true")
    else:
        print("false")