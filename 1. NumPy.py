#!/usr/bin/env python
# coding: utf-8

# # NUMPY

# Numerical Python

# In[1]:


import numpy


# In[2]:


a=numpy.array([1,2,3,4,5])  # array is an internal function, square brackets give contigous internal memory


# In[3]:


a


# In[6]:


a.shape  # only one vector holding 5 elements


# In[4]:


b=numpy.array([11,12,33,44,55])


# In[5]:


b


# In[7]:


b.shape


# In[8]:


c=numpy.array([34,89,56])


# In[9]:


c


# In[10]:


c.shape


# In[13]:


d=numpy.array([11,13,15,3])


# In[14]:


d


# In[15]:


d.shape


# In[16]:


import numpy as np


# In[17]:


a=np.array([11,12,13,14])


# In[18]:


a


# In[19]:


a.shape


# In[20]:


b=np.array([23,13,14,15,678,45])


# In[21]:


b


# In[22]:


b.shape


# In[23]:


a.min()


# In[24]:


a.max()


# In[25]:


a.shape


# # TWO DIMENSIONAL NUMPY ARRAY

# c=np.array([c1,c2] , [c1,c2])
#             row1       row2
# 
# [c1,c2] are column1 and column2 for row1 
# [c1,c2] are column1 and column2 for row2

# dtype(32) this is the memory allocation to each element. 
# (this means 1byte=8bits, so 32/8=4byte)
# Hence, computer is allocating 4byte memory to these elements
# 
# this memory allocation can be increased too by:
# dtype(64)
# this will give 64/8=8byte memory to each element
# 
# this is too much memory allocation, hence computer takes dtype(32) by default.

# In[27]:


c=np.array([[1,2],[3,4]])


# In[28]:


c


# In[29]:


c.shape


# In[30]:


c.min()


# In[31]:


c.max()


# In[32]:


c.size


# In[33]:


c.dtype


# In[38]:


f=np.array([12,13,14,15,16,17])   # by default one more element is tunning in backend dtype('int32') even if you are not mentioning it


# In[35]:


f


# In[36]:


f.shape


# In[39]:


f.dtype # dtype= data type; int=integer; 32 is 32 bits (calculating computer memory in bits 1 byte=8bits so 32/8=4 byte. So 4 bytes memory is being allocated to these 4 elements (1 byte for each element))


# In[40]:


g=np.array([12,13,14])


# In[41]:


g


# In[42]:


g.dtype


# In[51]:


g.itemsize # that is 4 byte of memory is allocated to each element, you can increase dtype to 64 also.


# In[44]:


h=np.array([11,10])


# In[45]:


h


# In[46]:


h.dtype    #gives the data type


# In[47]:


h.itemsize


# In[49]:


h.shape


# In[50]:


h.size


# In[52]:


p=np.array([[12,13],[14,15]])


# In[53]:


p


# In[54]:


p.shape


# In[55]:


p.size


# In[56]:


p.itemsize


# In[57]:


p.min()


# In[58]:


p.max()


# In[59]:


p.size


# k=np.array([[c1,c2,c3],[c1,c2,c3],[c1,c2,c3]])

# In[68]:


k=np.array([[11,12,13],[14,15,16],[17,18,19]])  #by default dtype(32)is running at backened i=even if you dont mention it.


# In[69]:


k


# In[62]:


k.size    # gives the count of number of elements


# In[63]:


k.shape  # gives the shape in dimensions; rows and columns


# In[64]:


k.min()


# In[65]:


k.max()


# In[66]:


k.itemsize   # gives the number of bytes/memory allocation by each element


# In[70]:


l=np.array([[100,200,300],[400,500,600]])


# In[71]:


l


# In[72]:


l.shape


# In[73]:


l.size


# In[74]:


l.itemsize


# In[75]:


l.min()


# In[76]:


l.max()


# In[82]:


m=np.array([[1,22.3,67],[3,8,5]],dtype='int32')


# In[83]:


m  # see here it did not take float data 22.3. it will take only integer data type by default


# In[84]:


# so to take float value you will have to mention it

m=np.array([[1,22.3,67],[3,8,5]], dtype='float32')


# In[85]:


m


# In[87]:


type(m)   #ndarray=number of dimensional data


# In[88]:


m.dtype


# In[89]:


m.ndim  # ndim=number of dimesional data


# In[90]:


m.shape  #2=2 row and 3=3 columns


# In[91]:


m


# In[92]:


m.reshape(3,2)  # it will reshape but it will adjust accordingly


# In[94]:


y=np.arange(5)


# In[95]:


y


# In[96]:


x=np.arange(15)


# In[97]:


x


# In[98]:


a=x.reshape(3,5)


# In[99]:


a


# In[100]:


k=np.arange(35)


# In[101]:


k


# In[102]:


k.reshape(7,5)


# In[103]:


k.reshape(5,7)


# In[ ]:




