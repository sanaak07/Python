#!/usr/bin/env python
# coding: utf-8

# # anonymous functions

# GLOBAL AND LOCAL VARIABLES

# In[3]:


testx=100


# In[9]:


def func():
    global testx
    p=45
    print(p)
    print(testx)


# In[10]:


func()


# In[6]:


testx


# In[11]:


m=345


# In[12]:


def func2():
    m=900
    print(m)


# In[13]:


func2()


# In[14]:


def f1():
    a=10
    print(a)


# In[15]:


def f2():
    f1()


# In[16]:


f2()


# In[17]:


def func1():
    x=10
    y=5
    print('add',x+y)


# In[22]:


def func2():
    func1()
    a=100
    b=20
    print('subtraction: ',a-b)


# In[23]:


func2()


# # RETURN keyword

# In[26]:


def func1():
    a=40
    b=30
    c=a+b
    return c


# In[30]:


h=func1()


# In[31]:


h


# In[32]:


def f1(h):
    print(h-10)


# In[33]:


f1(h)


# In[34]:


def function2():
    x=100
    y=40
    z=x+y
    return z


# In[35]:


function2()


# In[36]:


h2=function2()


# In[37]:


h2


# In[38]:


def func2(h1):
    print(h1-20)


# In[39]:


func2(h2)


# In[46]:


def func3():
    x=100
    y=40
    z=x-y
    print('z= ',z)
    return z
    print('end')


# In[43]:


func3()


# In[44]:


t=func3()


# In[45]:


t


# Variable Number of Arguments
# 
# in case where you dont know the exact number of arguments that you want to pass to a function, you can use the following syntax with *args:

# In[47]:


def plusfunction(*args):
    return sum(args)


# In[48]:


plusfunction(6,4,10)


# In[49]:


plusfunction(2,2,1,4,5)


# In[50]:


def maxfunction(*args):
    return max(args)


# In[51]:


maxfunction(9,90,78,45)


# In[52]:


maxfunction(19,80)


# In[55]:


def minfunction(*args):
    return min(args)


# In[56]:


minfunction(10,214,152,364,25,8)


# In[57]:


def sumfunc(*numbers):
    s=0
    for n in numbers:
        s+=n
    return s


# In[58]:


print (sumfunc(1,3))


# In[59]:


print (sumfunc(1,45,15,26))


# In[ ]:




