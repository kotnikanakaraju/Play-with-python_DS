#!/usr/bin/env python
# coding: utf-8

# In[2]:


def isAnagrams(s,t):
    if len(s)!=len(t):
        return False
    elif sorted(s)==sorted(t):
        return True
    else:
        return False
s="hello"
t="lelho"
isAnagrams(s,t)


# In[10]:


import re
def ispalidrome(s):
    if len(s)==0:
        return True
    else:
        start=0
        s=s.lower()
        newS=re.sub([r"[^a-zA-Z0-9]","",s)
        end=len(newS)-1
        while start<end:
            if newS[start]==newS[end]:
                start+=1
                end+=1
            else:
                return False
        return True
s="malayalam"
ispalidrome(s)


# In[12]:


def wordPattern(pattern,str):
    if pattern==None or str==None:
        return False
    else:
        len_str=len(str.split(" "))
        len_pattern=len(pattern)
        if len(str)!=len(pattern):
            return False
        str=str.split(" ")
        lookup={}
        for i in range(0,len(pattern)):
            s=str[i]
            p=pattern[i]
            if p in lookup:
                if lookup[p]!=s:
                    return False
                else:
                    if s in lookup.values():
                        return False
                    lookup[p]=s
            return True
        
if __name__ == "__main__":
    pattern = "abba"
    str = "dog cat cat dog"
    print(wordPattern(pattern, str))


# In[13]:


def isvalid(s):
    if s==[]:
        return False
    else:
        stack=[]
        balenced=True
        index=0
        while index<len(s) and balenced:
            symbol=s[index]
            if symbol in "({[":
                stack.append(symbol)
            else:
                if stack==[]:
                    balenced=False
                else:
                    top=stack.pop()
                    if not self.matches(top,symbol):
                        balenced=False
            index=index+1
            
        if balenced and stack==[]:
            return True
        else:
            return False
        

def matches(open,close):
    openings="({["
    closings=")}]"
    
    return openings.index(open)==closings.index(close)


# In[14]:


def isIsomorphic(s,t):
    if s==None or t==None:
        return False
    elif s=="" and t=="":
        return True
    else:
        if len(s)!=len(t):
            return False
        
        lookup={}
        for i in range(0,len(s)):
            c1=s[i]
            c2=t[i]
            
            if c1 in lookup:
                if lookup[c1]!=c2:
                    return False
            else:
                if c2 in lookup.values():
                    return False
                lookup[c1]=c2
                
        return True
s="abb"
t="cdd"
isIsomorphic(s,t)


# In[17]:


def reverseString(s):
    curr_str=[char for char in s]
    i=0
    j=len(s)-1
    while i<j:
        temp=curr_str[i]
        curr_str[i]=curr_str[j]
        curr_str[j]=temp
        j-=1
        i+=1
    return "".join(curr_str)
s="hello"
reverseString(s)


# In[5]:


class sloution:
    def eval(self,tokens):
        operators={"+","-","*","/"}
        stack=[]
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                num2=stack.pop()
                num1=stack.pop()
                if char=="+":
                    stack.append(num1+num2)
                elif char=="*":
                    stack.append(num1*num2)
                elif char=="-":
                    stack.append(num1-num2)
                else:
                    stack.append(int(num/num2))
        return stack[-1]
        
        


# In[20]:


import string
class solution:
    def ladderlength(beginWord,endWord,wordList):
        wordList=set(wordList)
        queue=[]
        queue.append([beginWord,1])
        while queue:
            word,count=queue.pop()
            if word==endword:
                return count
            
            for i in range(len(word)):
                for c in string.ascii_lowercase[:26]:
                    next_word=word[:i]+c+word[i+1:]
                    
                    if next_word in wordList:
                        queue.append([next_word,count])
                        wordList.remove(next_word)
        return 0
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
ladderlength(beginWord,endWord,wordList)


        


# In[22]:


def ladderlength(beginWord,endWord,wordList):
        wordList=set(wordList)
        queue=[]
        queue.append([beginWord,1])
        while queue:
            word,count=queue.pop()
            if word==endWord:
                return count
            
            for i in range(len(word)):
                for c in string.ascii_lowercase[:26]:
                    next_word=word[:i]+c+word[i+1:]
                    
                    if next_word in wordList:
                        queue.append([next_word,count])
                        wordList.remove(next_word)
        return 0
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
ladderlength(beginWord,endWord,wordList)


# In[23]:


from collections import defaultdict, deque

def findLadders(start, end, wordList):
    wordSet = set(wordList)
    if end not in wordSet:
        return []

    # Build a graph to represent word relationships
    graph = defaultdict(list)
    for word in wordSet:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            graph[pattern].append(word)

    # Perform BFS to find shortest paths
    queue = deque([(start, [start])])
    visited = set([start])
    result = []

    while queue:
        level_length = len(queue)
        level_visited = set()

        for _ in range(level_length):
            current, path = queue.popleft()

            if current == end:
                result.append(path)
            else:
                for i in range(len(current)):
                    pattern = current[:i] + '*' + current[i+1:]
                    for neighbor in graph[pattern]:
                        if neighbor not in visited:
                            level_visited.add(neighbor)
                            queue.append((neighbor, path + [neighbor]))

        visited.update(level_visited)

        if result:
            break

    return result

# Example usage
start = "hit"
end = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]
print(findLadders(start, end, wordList))


# In[26]:


def getmaxCounter(charArray):
    max=0
    ch=''
    for i in range(26):
        if countArray[i]>max:
            max=countArray[i]
            ch=chr(i-ord('a'))
    return ch

def rearrange(s):
    countArray=[0]*26
    n=len(s)
    for i in s:
        countArray[ord(c)-ord('a')]+=1
    c=getmaxCounter(countArray)
    maxcount=countArray[ord(c)-ord('a')]
    
    if maxcount>(n+1)/2:
        return ""
    res=['']*n
    idx=0
    while maxcount:
        res[idx]=c
        idx+=2
        maxcount=1
        
        
    countArray[ord(c)-ord('a')]=0
    for i in range(26):
        while countArray[i]>0:
            if idx>=n:
                idx=1
            res[idx]=chr(ord('a')+i)
            idx+=2
            countArray[i]-=1
    return ''.join(res)

s="bbbaaccdde"
res=rearrange(s)
if res=="":
    print("not valid")
else:
    print(res)


# In[ ]:




