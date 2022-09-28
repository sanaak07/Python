#!/usr/bin/env python
# coding: utf-8

# Data frame is a 2 dimentional data structure i.e.data is aligned in tabular fashion in rows and columns.
# 
# features of DataFrame:
# - potentially columns are of different types
# - size-mutable
# - labelled axes (rows and columns)
# - can perform arithmetic operations on rows and columns
# 
# pandas dataframe
# a pandas dataframe can be created using the following constructor:
# pandas.DataFrame(data,index,coulmns,dtype,copy)

# # Pandas DataFrame

# In[1]:


import pandas as pd


# In[2]:


data=[1,2,3,4]
df=pd.DataFrame(data)
df


# In[4]:


data=[['Alex',10],['Bob',12],['Clarke',13]]
df=pd.DataFrame(data)
df


# In[5]:


data=[['Alex',10],['Bob',12],['Clarke',13]]
df=pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)


# In[6]:


data={'Name':['tom','jack','steve','ricky'],'Age':[28,34,29,42]}
df=pd.DataFrame(data)
print(df)


# # NaN

# NaN (Not ANumber) is appended in missing areas

# In[8]:


data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df=pd.DataFrame(data,dtype=float)
print (df)


# In[9]:


data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df1=pd.DataFrame(data,index=['first','second'],columns=['a','b'])
print(df1)


# Addition of rows
# add new rows to a DataFrame using the append function. This function will append the rows at the end.
# df1=pd.DataFrame([[1,2],[3,4]], columns=['a','b'])
# df2=pd.DataFrame([[5,6],[7,8]], columns=['a','b'])
# 
# df3=df1.append(df2)
# print(df3)

# # INDEXING AND SLICING IN PANDAS
# 

# using label based (loc) function and index location based (iloc) function
# 
# .loc()Pandas provide b=various methods to have purely label based indexing

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
df


# In[4]:


# loc[rowstart:rowend,'label or column name']


# In[5]:


print(df.loc[:,'A'])  #give all rows of A column


# In[ ]:


# df.loc[['indexname1','indexname2'],[labelA,labelB]] as location will take label only, it will not work with indexing in numeric format


# In[6]:


print(df.loc[:,['C','D']])


# In[8]:


#  .iloc() Pandas provide various methods in order to get purely integer based indexing like python and numoy, these are 0-based indexing


# In[9]:


import pandas as pd
df=pd.DataFrame(np.random.randn(8,4))
print(df)


# In[10]:


print (df.iloc[:4,:])


# In[11]:


print(df.iloc[:,0])


# In[12]:


df.iloc[:,2]


# In[13]:


print(df.iloc[1:5,1])


# In[14]:


df


# In[15]:


print(df.iloc[2:6,2])


# In[16]:


print(df.iloc[:,3])


# In[18]:


print(df.iloc[3:6,3])


# In[19]:


df


# In[20]:


print(df.iloc[1:5,2:4])    #4 is exclusive


# In[21]:


print(df.iloc[1:3,:])


# In[22]:


print(df.iloc[:,1:3])


# In[23]:


# NEGATIVE INDEXING


# In[24]:


df


# In[25]:


print(df.iloc[:,-1])


# In[27]:


print(df.iloc[:,-2])


# In[29]:


print(df.iloc[:,-3])


# In[30]:


print(df.iloc[:,-4])


# In[ ]:




