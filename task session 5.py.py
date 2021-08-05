#!/usr/bin/env python
# coding: utf-8

# # task1
# 

# In[1]:


y =[ ]


# # task 2

# In[2]:


def unordered (elements):
    y.append(elements)
    list( dict.fromkeys(y))


# In[3]:


unordered(2) 
unordered(2) 
unordered(3) 
unordered(6) 
unordered(8) 
unordered(1) 


# In[4]:


y


# In[6]:


def search(list, n):

    l = 0
    u = len(list)-1
    index=0
    
    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['index'] = mid
            return True
            
        else:
            if list[mid] < n:
                l = mid+1;
            else:
                u = mid-1;

    return False


list = [4,7,8,12,24,50,200]

n = int(input('Enter the number'))

if search(list, n):
     print("Found at  index",index)
    
else:
    print("Not Found")

