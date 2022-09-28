#!/usr/bin/env python
# coding: utf-8

# # Packages

# - Packages contain a collection of various sub package
# - sub package contains modules
# - Modules contain classes

# # Modules

# In[2]:


import keyword


# In[3]:


print(keyword.kwlist)


# Python Module Search Path
# 
# While importing a module, python looks at several places. Interpreter first looks for a built-in module then (if not found) into a list of directories defined in sys.path. the search is in this order. the current directory.

# In[4]:


import sys


# In[5]:


sys.path


# In[6]:


import os


# In[7]:


os.getcwd()     #get current working directory(cwd)


# In[8]:


os.listdir()   #shows the list of files and folders in current working directory


# In[9]:


import math


# In[11]:


math.pi


# In[12]:


math.sqrt(25)


# In[13]:


math.sqrt(36)


# In[14]:


math.pow(2,2)


# In[15]:


radius=7


# In[17]:


areaofcircle=math.pi*(radius**2)
round(areaofcircle,2)


# In[30]:


def find_sqrt(x):
    return math.sqrt(x)


x=int(input('enter any value'))
find_sqrt(x)


# In[28]:


def func_power():
    return math.pow(a,b)
 
a=int(input('enter any value'))
b=int(input('enter any value'))
func_power(a,b)


# In[31]:


from math import pi


# In[32]:


pi


# In[33]:


from math import sqrt


# In[35]:


sqrt(4)


# In[38]:


math._dict_.keys()


# In[39]:


# get current date and time


# In[40]:


import datetime


# In[42]:


dt=datetime.datetime.now()
dt


# commonly used classes in the datetime module are:
#     date class
#     time class
#     datetime class
#     timedelta class

# In[44]:


import datetime
d=datetime.date(2022,8,14)
d


# In[46]:


from datetime import date
a=date(2021,5,26)
a


# In[47]:


#get current date
td=date.today()
td


# In[48]:


print('year=',td.year)
print('month',td.month)
print('day',td.day)

a time object initiated from the time class represents local time
# In[49]:


from datetime import time
a=time()
print(a)

b=time(11,35,36)
print(b)


# In[50]:


print('hour',b.hour)
print('minute',b.minute)
print('second',b.second)


# In[51]:


from datetime import datetime
a=datetime(2021,4,26)
print(a)


# In[52]:


b=datetime(2021,2,27,17,30,50)
print(b.year)
print(b.month)
print(b.day)
print(b.hour)
print(b.minute)
print(b.second)


# In[53]:


pip-python package manager


# # FILE INPUT/OUTPUT OPERATIONS

# In[54]:


savefile=open('E:\IBM-Data Science and Neural Networking\File Input Output practise\demofile14Aug.txt','w')


# In[55]:


savefile.write('this is the first line for input output operations')


# In[56]:


savefile.close()


# In[57]:


readme=open('E:\IBM-Data Science and Neural Networking\File Input Output practise\demofile14Aug.txt','r')


# In[58]:


print(readme.read())


# In[59]:


readme.close()


# In[60]:


appendfile=open('E:\IBM-Data Science and Neural Networking\File Input Output practise\demofile14Aug.txt','a')


# In[61]:


appendfile.write('\n this is the second line, tomorrow is independence day')


# In[62]:


appendfile.close()


# In[63]:


readme=open('E:\IBM-Data Science and Neural Networking\File Input Output practise\demofile14Aug.txt','r')


# In[64]:


print(readme.read())


# In[65]:


readme.close()


# In[ ]:




