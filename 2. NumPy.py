#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


b=np.array([[1.5,2,3],[4,5,6]], dtype='int32')


# In[5]:


b


# In[6]:


np.zeros([3,4])


# In[7]:


np.ones([3,4])


# In[8]:


np.arange(5)


# In[9]:


np.arange(0,10)


# In[10]:


# start, end, skip or jump

np.arange(0,12,2)


# In[11]:


np.arange(10,30,5)


# In[12]:


b=np.arange(12).reshape(4,3)


# In[13]:


b


# # BROADCASTING IN NUMPY

# The term braodcasting describes how numpy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is 'broadcast' across the larger array so that they have commandable shapes. Broadcasting provides a means of vestorizing array operations

# In[14]:


a=np.array([1.0,2.0,3.0])   # the vector array data columns are multiplied
b=np.array([2.0,2.0,2.0])
a*b


# In[15]:


a=np.array([1.0,2.0,3.0])   # can be done keeping a common element too
b=2.0
a*b


# In[16]:


a=np.array([20,30,40,50])  # this variable will print given values
b=np.arange(4)    # this variable will print a range of 4 values
print(a)
print(b)


# In[17]:


c=a-b    # this subtracted the array of variable b from a
print(c)


# In[18]:


b**2   # does the square of the b variable


# In[19]:


b=np.random.random([2,3])   # generate any random numbers in row of 2 rows and 3 columns


# In[20]:


b


# In[21]:


c=np.ones([2,3])  # give me 2 rows of 3 columns


# In[22]:


c


# In[23]:


d=b+c   # simply added 1 (c variable) to random numbers (b variable)


# In[24]:


d


# # UNIVERSAL FUNCTIONS

# In[25]:


B=np.arange(3)


# In[26]:


B


# In[27]:


np.exp(B)  #exponential function


# In[28]:


np.sqrt(B)


# In[29]:


c=np.array([2,1,4])  #add B and c
np.add(B,c)


# # INDEXING, SLICING AND ITERATING

# In[30]:


a=np.arange(10)


# In[31]:


a


# In[32]:


a[2]


# In[33]:


a[2:5]


# In[34]:


a[-1]  # negative slicing. Value at -1 is 9


# In[35]:


a[-2]


# In[36]:


a[-3]


# In[37]:


a[-4:]


# In[38]:


a[-4:-2]


# In[39]:


d2=np.arange(20)


# In[40]:


d2


# In[41]:


d2[5:]   # slicing from 5th index position to end of array


# In[42]:


d3=np.array([np.nan,1,2,3,np.nan,6,7,8])  #np.nan means missing data that we do not know


# In[43]:


d3


# #The random module provides nice funstions to generate random numbers (and also statistical distributions) of any given shape. rand functions will generate any number between 0 and 1

# In[45]:


np.random.rand(2,2)         # uniform distribution similar to random


# #randn will generate any number for normal distribution in the guevn dimension format

# In[47]:


np.random.randn(2,3)


# In[ ]:




