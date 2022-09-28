#!/usr/bin/env python
# coding: utf-8

# # functions
# 1. Built-in functions pre defined
# 2. User defined functions
# 3. Anonymous Lambda Functions

# In[ ]:


help()


# In[7]:


help()


# In[1]:


help(len)


# In[2]:


help(min)


# In[3]:


help(max)


# In[4]:


help(input)


# In[8]:


k=[40,50,60,70,80]
min(k)


# In[9]:


max(k)


# In[13]:


def hello():
         print('functions in python')


# In[14]:


hello()


# In[15]:


def smart():
    print('I am smart')


# In[16]:


smart()


# In[17]:


help()


# # user defined functions

# In[19]:


def function1():
    print ('hello world')


# In[21]:


function1()


# In[25]:


def function2():
    print('inside function2')


# In[26]:


function2()


# In[28]:


def function3():
    print('learning python with Deepki maam')


# In[30]:


function3()


# In[32]:


def function4():
    print('learning')
    print('inside function3')
    print('user defined function')


# In[33]:


function4()


# In[34]:


def addition():
    a=10
    b=20
    c=a+b
    print('the value of c=',c)


# In[35]:


addition()


# In[39]:


def subtraction():
    a=90
    b=20
    print('the value of subtraction is=',a-b)


# In[37]:


subtraction()


# In[42]:


def multiply_func():
    x=5
    y=4
    z=x*y
    print('multiplication of x=',x,'x and y=',y,'=',x*y)


# In[44]:


multiply_func()


# In[45]:


def square_func():
    x=6
    print('the value of squaring 6 is=',x**2)


# In[46]:


square_func()


# In[1]:


def area_of_circle():
    pi=3.14
    r=5
    area=pi*(r**2)
    print('The area of circle is= ',area)


# In[3]:


area_of_circle()


# In[7]:


def area_of_rectangle():
    l=200
    b=100
    area_rect=l*b
    print('the area of rectangle is= ',l*b,'meter')
    


# In[8]:


area_of_rectangle()


# In[ ]:




