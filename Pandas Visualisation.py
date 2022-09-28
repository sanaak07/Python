#!/usr/bin/env python
# coding: utf-8

# # Pandas Visualisation

# # These methods can be provided as the kind keyword argument to plot(). These include: 
# 
# - bar or barh for bar plots
# - hist for histogram
# box for boxplot
# - scatter for scatter plots

# In[2]:


# bar plot

import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
print(df)
df.plot.bar()


# In[4]:


df.plot.bar(stacked=True)


# In[5]:


#to get horizontal bar plots, use the barh method
df.plot.barh(stacked=True)


# # Histograms 
# 
# Histograms can be plotted using the plot hist()method. We can specify the number of bins (bins are the intervals between 2 plots)

# In[6]:


df.plot.hist()


# # Box Plots
# Can be drawn using series .box.plot() and DataFrame.box.plot( or DataFrame.boxplot() to visualise the distribution of values within each column
# 
# For instance, here is a boxplot representing five trials of 10 observations of a uniform random variable on (0,1)

# In[7]:


df=pd.DataFrame(np.random.randn(10,5),columns=['A','B','C','D','E'])
print(df)
df.plot.box()


# In[9]:


df=pd.DataFrame(np.random.randn(50,4),columns=['a','b','c','d'])
df.plot.scatter(x='a',y='b')


# # WORKING WITH PANDAS FINAL

# Set Index
# 
# CHANGE THE INDEX
# 
# Well understand how to change the index values ina dataframe.
# For example: let us  craet a dataframe with some key value pairs in a dictionary and change the index values.
#     let us consider the example below:

# In[10]:


import pandas as pd

df=pd.DataFrame({'day':[1,2,3,4], 'visitors':[200,100,230,300], 'bounce_rate':[20,45,60,10]})
print(df)

df1=df.set_index('day')
df1


# In[11]:


df.set_index('day',inplace=True)    #escapes the index value 0, starts data with day
print(df)


# # Change column header
# 
# 

# In[12]:


df=df.rename(columns={'visitors':'users'})
print(df)


# # DATA ANALYSIS IN PYTHON

# # are
# - head 
# - tail
# - sample

# In[13]:


import pandas as pd
data={'day':[1,2,3,4,5,6],'visitors':[1000,700,6000,1000,400,350], 'bounce_rate':[20,20,23,15,10,34]}
df=pd.DataFrame(data)
print(df)


# In[14]:


df.head()  #shows top 5 rows


# In[15]:


df.head(3)    #shows top 3 rows


# In[16]:


df.tail()  #shows rows till end


# In[17]:


df.sample()   #shows any row


# In[18]:


df.sample(3)    #shows any 3 sample rows


# In[ ]:




