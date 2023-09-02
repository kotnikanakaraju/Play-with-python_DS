#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import namedtuple


# In[6]:


x=namedtuple('courses','name,technology')
t=x('data sciemce','python')
print(t)
t._asdict


# In[7]:


l=['DBMS','SQL']
print(x._make(l))


# In[13]:


from collections import deque
a=['r','f','g','t','y','o']
a=deque(a)
a.append('python')
a.appendleft('python mole')
a.pop()
a.popleft()
a.extendleft('b')
print(a)


# In[17]:


from collections import ChainMap

baseline={'a':'laddu','v':'vada'}
love={'a':'gas','d':'bura'}
cm=ChainMap(baseline,love)
print(cm)


# In[18]:


print(list(cm))


# In[19]:


from collections import Counter
a=[2,2,3,4,4,6,7,7,8,3,5,6,7,8,8,3,4,5,5,6,6]
print(Counter(a))


# In[20]:


c=Counter(a)
print(list(c.elements()))


# In[21]:


print(c.most_common())


# In[23]:


s={4:2,8:3}
c.subtract(s)
print(c)


# In[24]:


from collections import OrderedDict


# In[25]:


d=OrderedDict()

d[1]='r'
d[2]='c'
d[3]='d'
print(d)


# In[26]:


print(d.keys())


# In[27]:


print(s.values())


# In[28]:


print(d.items())


# In[29]:


from collections import defaultdict

x={1:'rfinder',2:'python',3:'collections'}
print(x[4])


# In[30]:


y=defaultdict(int)
y[1]='rfinder'
y[2]='python'
print(y[3])


# In[1]:


import time as t


# In[ ]:


user_pin=9876
user_balence=948383.50
user_name="Ms.ABC"
print("welcome to bank account",user_name,end=" ")
while True:
    print("\t\t0.logout and Exist")
    print("\t\t1.View Account Balence")
    print("\t\t2.withdraw cash")
    print("\t\t3.Deposit Pin")
    print("\t\t4.Change Pin")
    print("\t\t5.Return Card")
    choice =int(input("enter the number to proceed>"))
    print("\n\n")
    if choice ==0:
        print("existing")
        t.sleep(2)
        print("you have been loged out")
        break
    elif choice in (1,2,3,4,5):
        num_of_tries=3
        while(num_of_tries!=0):
            number_of_tries=3
            

