#!/usr/bin/env python
# coding: utf-8

# In[1]:


class stack:
    def __init__(self,limit=5):
        self.stk=[]
        self.limit=limit
    def isEmpty(self):
        return len(self.stk)<=0
    def push(self,item):
        if(len(self.stk)>=self.limit):
            print("stack overflow!")
        else:
            self.stk.append(item)
            print("stack after push",self.stk)
    def pop(self):
        if(len(self.stk)<=0):
            print("stack underflow!")
            return 0
        else:
            return self.stk[-1]
    def peek(self):
        return len(self.stk)
our_stack=stack(5)
our_stack.push("3")
our_stack.push("6")
our_stack.push("7")
our_stack.push("2")
our_stack.push("6")
print(our_stack.peek())
print(our_stack.pop())


# In[2]:


def redudancy_brackets(N):
    stk=[]
    for i in range(len(N)):
        if N[i] in '(+-*/)':
            stk.append(N[i])
        elif N[i]==')':
            if stack.pop()=='(':
                return 1
            stk.pop()
        return 0
    
N="((a)+b)"
a=redudancy_brackets(N)
if a==1:
    print("redundant")
else:
    print("not a redundant")


# In[7]:


def balence(N):
    stk=[]
#     braces="[{{}}]"
    for i in range(len(N)):
        if N[i]=="[" or N[i]=="{" or N[i]=="(" not in stk:
            stk.append(i)
        elif N[i]==")" or N[i]=="}" or N[i]=="]":
            stk.pop()
            return 1
        return 0
N="[{{}}]"
a=balence(N)
if a==1:
    print("balenced")
else:
    print("not balenced")


# In[8]:


def arepairs(open,close):
    if open=='[' and close==']':
        return True
    if open=='{' and close=='}':
        return True
    if open=='(' and close==')':
        return True
    return False

def Balenced(N):
    stk=[]
    for i in range(len(N)):
        if N[i]=="[" or N[i]=="{" or N[i]=="(":
            stk.append(i)
        elif N[i]==")" or N[i]=="}" or N[i]=="]":
            if arepairs(stk[-1],N[i] or len(stk)!=0):
                stk.pop()
            else:
                return False
            


# In[10]:


def min_bracket_rev(expr):
    size=len(expr)
    if size%2!=0:
        return None
    stk=[]
    for i in range(size):
        if expr[i]=="}" and len(stk)>0:
            if stk[0]=="{":
                stk.pop(0)
            else:
                stk.insert(0,expr[i])
        else:
            stk.insert(0,expr[i])
    
    total_left=len(stk)
    open=0
    while len(stk)>0 and stk[0]=="{":
        stk.pop(0)
        open=open+1
    return total_left//2+open%2
expr="{{}{{}{{"
print(min_bracket_rev(expr))


# In[19]:


def calculateSpan(price,s):
    n=len(price)
    st=[]
    st.append(0)
    s[0]=1
    for i in range(1,n):
        while (len(st)>0 and price[st[-1]]<=price[0]):
            st.pop()
        if len(st)<=0:
            s[i]=i+1
        else:
            s[i]=i-st[-1]
        st.append(i)
    return s
price=[60,70,80,100,90,75,80,120]
s=[0 for i in range(len(price))]
calculateSpan(price,s)


# In[ ]:




