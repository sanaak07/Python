#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas
#import numpy
import pandas as pd
import numpy as np


# In[4]:


#read csv file
import pandas as pd
df=pd.read_csv('student_marks.csv')
df.head()


# In[5]:


df['Maths'].mean()


# In[6]:


df['Physics'].mean()


# In[7]:


df['Chemistry'].mean()


# In[8]:


df['English'].mean()


# In[9]:


df['Biology'].mean()


# In[10]:


df['Economics'].mean()


# In[11]:


df['History'].mean()


# In[12]:


df['Civics'].mean()


# In[14]:


df['Chemistry'].median()


# In[15]:


df['Civics'].median()


# In[17]:


df['English'].median()


# In[19]:


df['Maths'].mode()


# In[20]:


df['English'].mode()


# In[ ]:




