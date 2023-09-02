#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next_node=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def is_empty(self):
        return self.head is None
    
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        curr=self.head
        while curr.next_node:
            curr=curr.next_node
        curr.next_node=new_node
    
    
    


# In[2]:


##single linked list insetion
class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None
        
    def insertNode(head,newNode):
        newNode.next=head
        head=newNode
        return head
    
    def insertmiddle(head,newNode):
        curr=head
        while curr.data!=None:
            curr=curr.next
        newNode.next=curr.next
        curr.next=newNode
        return head
    
    def insertend(head,newNode):
        curr=head
        while curr.next!=None:
            curr=curr.next
        curr.next=newNode
        newNode.next=None
        return head
    
    def printlist(head):
        temp=head
        while(temp):
            print(temp.data)
            temp=temp.next
head = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF


# In[4]:


#deletion of node
def delete(self,data):
    if self.head is None:
        return
    if self.head.data=data:
        self.head=self.head.next_node
        return
    curr=self.head
    while curr.next_node:
        if curr.next_node.data=data:
            curr.next=curr.next_node.next_node
            return
        curr=curr.next_node


# In[5]:


class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def length(head):
    tempNode=head
    count=0
    while tempNode!=None:
        count=count+1
        tempNode=tempNode.next
    print(count)
    
def length_recur(node):
    if node==None:
        return 0
    else:
        return 1+length_recur(node.next)
    
head = ListNode('d')
node2 = ListNode('g')
node3 = ListNode('r')
node4 = ListNode('o')


head.next=node2
node2.next=node3
node3.next=node4
node4.next=None

print(length_recur(head))


# In[6]:


def deleteduplicates(head):
    if head==None and head.next==None:
        return head
    prevNode=head
    nextNode=head.next
    
    while nextNode!=None:
        if nextNode.val==preNode.val:
            prevNode.next=nextNode.next
            nextNode=nextNode.next
        else:
            prevNode=nextNode
            nextNode=nextNode.next
    return head


# In[9]:


## Double Linked list

class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None
        Node.prev=None
        
def insertNodestart(head,newNode):
    newNode.next=head
    head.prev=newNode
    newNode.prev=None
    head=newNode
    return head

def insertmiddle(head,newNode):
    temp=head
    while temp.data!=None:
        temp=temp.next
    buffer=temp.next
    temp.next=newNode
    newNode.prev=temp
    newNode.next=buffer
    buffer.prev=newNode
    return head

def insertend(head,newNode):
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=newNode
    newNode.prev=temp
    newNode.next=None
    return head

def printList(head):
    temp=head
    while temp:
        print(temp.data)
        temp=temp.next
        
head = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')



head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD



nodeB.prev=head
nodeC.prev=nodeB
nodeD.prev=nodeC
      
head = insertend(head, Node('z'))
printList(head)
      


# In[11]:


## deletion of single linked list

class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None
def del_Node_start(head):
    if head==None:
        return
    if head.next==None:
        head=None
        return
    head=head.next
    return head

def delNode_mid(head,del_node):
    temp=head
    while temp.next.data!=del_node:
        temp=temp.next
    temp.next=temp.next.next
    return head

def delNode_end(head):
    temp=head
    while temp.next.next!=None:
        temp=temp.next
    temp.next=None
    return head

def printList(head):
    temp=head
    while(temp):
        print(temp.data)
        temp=temp.next


# In[4]:


class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next =None
        
def reverse(head):
    if head is None:
        return head
    curr=head
    prev=None
    nextNode=None
    while(curr!=None):
        nextNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
    return prev

def plallindrome(head):
    fast=head
    slow=head
    while fast is not None and fast.next is not None:
        fast=fast.next.next
        if fast is None:
            mid=slow.next
            break
        if fast.next is None:
            mid=slow.next.next
            break
        slow=slow.next
    slow.next=None
    mid=reverse(mid)
    return head,mid
    
    
def compare(head,mid_reverse):
    while head is not None or mid_reverse is not None:
        if head.data!=mid_reverse.data:
            return -1
        head=head.next
        mid_reverse=mid_reverse.next
    return 1

def printList(head):
    temp=head
    while(temp):
        print(temp.data)
        temp=temp.next
        
head=Node('R')
nodeB=Node('A')
nodeC=Node('D')

nodeD=Node('T')
nodeE=Node('A')
nodeF=Node('R')

head.next=nodeB
nodeB.next=nodeC
nodeC.next=nodeD
nodeD.next=nodeE
nodeE.next=nodeF

a,r=plallindrome(head)
a=compare(a,r)
if a==1:
    print("palindrome")
else:
    print("not plaindrome")
    


# In[6]:


class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None
        
def delNode(head,del_node):
    temp=head
    while temp.next.data!=4:
        temp=temp.next
    temp.next=temp.next.next
    return head
def printlist(head):
    temp=head
    while(temp):
        print(temp.data)
        temp=temp.next
head=Node(1)
nodeB=Node(2)
nodeC=Node(3)

nodeD=Node(4)
nodeE=Node(5)
nodeF=Node(6)
head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF

head=delNode(head,4)
printlist(head)


# In[15]:


class Node:
    def __init__(Node,data):
        Node.data=data
        Node.next=None
        
def duplicate(head):
    if head is None and head.next is None:
        return head
    prevNode=head
    nextNode=head.next
    while nextNode!=None:
        if prevNode.val==nextNode.val:
            prevNode.next=nextNode.next
            nextNode=nextNode.next
        else:
            prevNode=nextNode
            nextNode=nextNode.next
    return head
def printlist(head):
    temp=head
    while(temp):
        print(temp.data)
        temp=temp.next
            
head=Node(1)
nodeB=Node(2)
nodeC=Node(2)

nodeD=Node(3)
nodeE=Node(3)
nodeF=Node(6)
head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
head=duplicate(head)
printlist(head)
           


# In[21]:


class Node:
    def __init__(Node, data):
        Node.data = data
        Node.next = None
def detectCycle(head):
    fast=head
    slow=head
    loopexist=0
    while fast!=None and slow!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            loopexist=1
            break
            
        if(loopexist):
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
        return None
head = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')
nodeG = Node('g')
nodeH = Node('h')
nodeI = Node('i')
nodeJ = Node('j')

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = nodeH
nodeH.next = nodeI
nodeI.next = nodeJ
nodeJ.next = nodeD

head=detectCycle(head)
print(head.data)
    


# In[19]:


class Node:
    def __init__(Node, data):
        Node.data = data
        Node.next = None


def detectCycle(head):
    fast=head
    slow=head
    loopexist=0
    while(fast!=None and slow!=None and fast.next!=None):
        fast=fast.next.next
        slow=slow.next
        if(fast==slow):
            loopexist=1
            break

    if(loopexist):
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow
    return None


head = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')
nodeG = Node('g')
nodeH = Node('h')
nodeI = Node('i')
nodeJ = Node('j')

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = nodeH
nodeH.next = nodeI
nodeI.next = nodeJ
nodeJ.next = nodeD

head=detectCycle(head)
print(head.data)


# In[25]:


class LinkedList(object):
    def __init__(self):
        self.head=None
        
    class Node(object):
        def __init__(self,data):
            self.data=data
            self.next=None
            
    def sortlist(self):
        count=[0,0,0]
        temp=self.head
        while temp!=None:
            count[temp.data]+=1
            temp=temp.next
            
        i=0
        temp=self.head
        while temp!=None:
            if count[i]==0:
                i+=1
            else:
                temp.data=i
                count[i]-=1
                temp=temp.next
                
    def push(self,new_data):
        new_Node=self.Node(new_data)
        new_Node.next=self.head
        self.head=new_Node
        
    def printlist(self):
        temp=self.head
        while temp!=None:
            print(str(temp.data))
            temp=temp.next
        print("")
        
llist = LinkedList()
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(2) 
print("Linked List before sorting")
llist.printlist()
llist.sortlist()

print("Linked List after sorting")
llist.printlist()


# In[27]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def newNode():
    return newNode(data)

def reverse(head):
    if head is None:
        return head
    curr=head
    prev=None
    nextNode=None
    while curr!=None:
        newNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
    return prev
    
def addone(head):
    head=reverse(head)
    k=head
    carry=0
    prev=None
    head.data +=1
    
    while(head!=None) and (head.data>9 or carry>0):
        prev=head
        head.data+=carry
        carry=head.data//10
        head.data=head.data%10
        head=head.next
    if carry>0:
        prev.next=Node(carry)
    return reverse(k)
def printlist(head):
    if not head:
        return
    while(head):
        print("{}".format(head.data),end="")
        head=head.next
        
if __name__=="__main__":
    head=newNode(1)
    head.next=newNode(9)
    head.next.next=newNode(9)
    head.next.next.next=newNode(9)
    head=addone(head)
    printlist(head)


# In[28]:


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def newNode(data):
	return Node(data)

def reverseList(head):
	if not head:
		return
	curNode = head
	prevNode = head
	nextNode = head.next
	curNode.next = None

	while(nextNode):
		curNode = nextNode
		nextNode = nextNode.next
		curNode.next = prevNode
		prevNode = curNode

	return curNode


def addOne(head):

	head = reverseList(head)
	k = head
	carry = 0
	prev = None
	head.data += 1

	while(head != None) and (head.data > 9 or carry > 0):
		prev = head
		head.data += carry
		carry = head.data // 10
		head.data = head.data % 10
		head = head.next

	if carry > 0:
		prev.next = Node(carry)
	return reverseList(k)

def printList(head):
	if not head:
		return
	while(head):
		print("{}".format(head.data), end="")
		head = head.next

if __name__ == '__main__':
	head = newNode(1)
	head.next = newNode(9)
	head.next.next = newNode(9)
	head.next.next.next = newNode(9)

	print("List is: ", end="")
	printList(head)

	head = addOne(head)

	print("\nResultant list is: ", end="")
	printList(head)


# In[1]:


##add two numbers:

def addtwonumbers(self,l1,l2):
    head=l3=listNode(0)
    carry=0
    while l1 or l2 or carry:
        if l1:
            carry+=l1
            l1=l1.next
        if l2:
            carry+l2
            l2=l2.next
        l3=carry%10
        carry=carry//10
        
        if l1 or l2 or carry:
            l3.next=listNode(0)
            l3=l3.next
            
    return head


# In[7]:


##remove nth node from end of the list
# class ListNode(Node,val):
#     Node.val=x
#     Node.next=None
    
class solution(object):
    
    def removenthNode(Node,head,n):
        if head==None:
            return head
        else:
            dummy=ListNode(0)
            dummy.next=head
            fast=dummy
            slow=dummy
            for i in range(n):
                fast=fast.next
                
            while fast.next!=None:
                fast=fast.next
                slow=slow.next
            slow.next=slow.next.next
            return dummy.next
            


# In[ ]:




