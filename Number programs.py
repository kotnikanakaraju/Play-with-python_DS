#!/usr/bin/env python
# coding: utf-8

# In[1]:


# print all the digits of a number on different lines

n=268
m=n
while m!=0:
    d=m%10
    print(d)
    m=m//10


# In[2]:


#palindrome number
n=268
m=n
sum=0
while m!=0:
    d=m%10
    sum=sum*10+d
    m=m//10
if sum==m:
    print("palindrome")
else:
    print("not palidrome")


# In[4]:


#check number is spy number or not
#mean sum its digits equals the product of the digits

n=123
m=n
sum=0
prod=1
while m!=0:
    d=m%10
    sum=sum+d
    prod=prod*d
    m=m//10
if sum==prod:
    print("spy number")
else:
    print("not spy number")
    


# In[6]:


# check special number or not.
# sum of digits+ product of digits =original number
# 59=(5+9)+(5*9)

num=59
m=num
sum=0
prod=1
while m!=0:
    d=m%10
    sum=sum+d
    prod=prod*d
    m=m//10
    result=sum+prod
if num==result:
    print("special number")
else:
    print("not a special number")


# In[7]:


# if the number is Harshad/Niven Number or not
# A number which is divisible by the of the digit
# 156=1+5+5=12
num=156
m=num
sum=0
while m!=0:
    d=m%10
    sum=sum+d
    m=m//10
if num%sum==0:
    print("Niven Number")
else:
    print("not niven")


# In[8]:


# Check number is duck number or not
# A number which has zeroes present in it
# eg 402,280
num=402
m=n
count=0
while m!=0:
    d=m%10
    if d==0:
        count+=1
    m=m//10
if count>0:
    print("duck number")
else:
    print("not Duck number")


# In[9]:


# check if number is neon number or not
# where sum of digits of square number is equal to the number
# num=9  9*9=81   8+1=9   9==9
num=9
m=num*num
sum=0
while m!=0:
    d=m%10
    sum=sum+d
    m=m//10
if num==sum:
    print("neon Number")
else:
    print("not neon number")
    


# In[11]:


# check the number is automorphic number or not
# it is a number which is contained in the last digit(s)
# of its square eg.25 in 625
num=25
m=n
flag=0;q=n*n
while m!=0:
    d=m%10;d1=q%10
    if d!=d1:
        flag=1
    m=m//10;q=q//10
if flag==0:
    print("automorphic number")
else:
    print("not automorphic number")


# In[13]:


# check if the number Krishana Murthy number,special number or not
# where sum of factorial of digits is equal to the number of digits
# 145=1!+4!+5!
import math
num=145
m=num
sum=0
while m!=0:
    d=m%10
    sum=sum+math.factorial(d)
    m=m//10
if sum==num:
    print("Krishnan murthy number")
else:
    print("not krishnan murthy  number")


# In[ ]:


#solve factor program
#a factor is a number which divides into it exactly without
# leaving a remainder
n=int(input("enter the number:"))
def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)


# In[ ]:


#prime number
n=int(input("enter the number: "))
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
if count==2:
    print("prime number")
else:
    print("not a prime number")


# In[ ]:


#composite number
n=int(input("enter the number: "))
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
if count>2:
    print("composite number")
else:
    print("not a compisite number")


# In[ ]:


#perfect Number
n=6
sum=0
for i in range(1,n):
    if num%i==0:
        sum=sum+i
if sum==n:
    print("perfect Number")
else:
    print("not perfect Number")


# In[ ]:


#Abandunt number
n=int(input("enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum>n:
    print("abandunt number")
else:
    print("not a abandunt number")


# In[ ]:


#deficient number
n=int(input("enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum<n:
    print("deficient  number")
else:
    print("not a deficient  number")


# In[ ]:


#pronic number
n=int(input("enter the number:"))

