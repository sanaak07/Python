#!/usr/bin/env python
# coding: utf-8

# # Scipy library gives all statistics functions

# In[3]:


import scipy
import numpy as np
import warnings
warnings.filterwarnings("ignore")

scipy.__version__


# In[5]:


#create an array
a=np.array([[3,7,5],[8,4,3],[2,4,9]])


# In[7]:


#check a
a


# In[8]:


#find out mean
print(scipy.mean(a))


# In[9]:


#find out median
print(scipy.median(a))


# In[13]:


#find out variance
print(scipy.var(a))


# In[11]:


#find out variance and round it off to 2 decimals
print(round(scipy.var(a),2))


# In[14]:


#find out standard deviation
print(scipy.std(a))


# In[12]:


#find out std.deviation and round off to 2 decimals
print(round(scipy.std(a),2))


# In[15]:


#import libraries
import numpy as np
import scipy.stats as st

p=np.array([5,8,9,5,6,5,10,14])
st.mode(p)


# In[17]:


#create an array
b=np.array([[1,3,4,2,2,7],[5,2,2,1,4,1],[3,3,2,2,1,1]])
b


# In[21]:


#find out mode, axis columnwise
m=st.mode(b,axis=0)
m


# In[22]:


#find out mode, axis row wise
m=st.mode(b,axis=1)
m


# In[44]:


#working on students marks csv file
import pandas as pd
import numpy as np
df=pd.read_csv('student_marks.csv')
df.head()


# In[40]:


#find out mean of maths marks
df['Maths'].mean()


# In[42]:


#find out mean of english marks
df['English'].mean()


# In[43]:


#find out mean of chemistry marks
df['Chemistry'].mean()


# In[45]:


#find out median of chemistry marks
df['Chemistry'].median()


# In[46]:


#find out median of biology marks
df['Biology'].median()


# In[47]:


#find out mode of maths marks
df['Maths'].mode()


# In[48]:


#find out mean of biology marks
df['Biology'].mode()


# In[49]:


#describe all the statistical summary
df.describe()


# In[50]:


#find out percentile of score in scipy
import scipy
from scipy import stats
from scipy.stats import percentileofscore


# In[53]:


#find out 25 percentile of maths
percentileofscore(df['Maths'],25)


# In[55]:


#find out 25 percentile of maths
percentileofscore(df['English'],75)


# In[57]:


#find out 25 percentile of maths
percentileofscore(df['Biology'],25)


# In[58]:


#find out max marks of maths
max_m=df['Maths'].max()


# In[59]:


max_m


# In[65]:


#find out min marks of maths
min_m=df['Maths'].min()
min_m


# In[66]:


#findout range of maths
r=max_m-min_m
r


# In[73]:


#find variance of maths marks
df['Maths'].var()


# In[74]:


#find standard deviation of maths score
df['Maths'].std()


# In[75]:


#find var and std.dev.of English marks
print(df['English'].var())
print(df['English'].std())


# # Spread of Data
# Q1=25th percentile
# Q2=50th percentile
# Q3=75th percentile
# 
# IQR (Interquartile)= Q3-Q1

# In[67]:


#find 25th percentile of maths marks
q1=df['Maths'].quantile(0.25)
q1


# In[68]:


#find 75th percentile of maths marks
q3=df['Maths'].quantile(0.75)
q3


# In[71]:


#find out total IQR 
IQR=q3-q1
IQR


# In[70]:


IQR


# # z-Score

# In[76]:


from scipy.stats import zscore


# In[77]:


zscore([56,34,21,33])


# In[78]:


df.iloc[:,3:-1]


# In[79]:


df.iloc[:,3:10]


# In[ ]:





# In[27]:


#working on a csv file president_heights
import pandas as pd
data=pd.read_csv('president_heights')
data


# In[28]:


#save all heights values/data in 'heights'
heights=data['height']


# In[35]:


#print the mean heights, standard deviation, minimum height, maximum height 
print('Mean height:           ',heights.mean())
print('Standard Deviation:    ',heights.std())
print('Minimum height:        ',heights.min())
print('Maximum height:        ',heights.max())


# In[33]:


#print 25th percentile, median, 75th percentile
print('25th percentile:   ',np.percentile(heights,25))
print('Median:            ',np.median(heights))
print('75th percentile:   ',np.percentile(heights,75))


# In[37]:


#see visual representaion of this data 
import matplotlib.pyplot as plt


# In[38]:


#plot a histogram
#give plot title
#give x axis label
#give y axis label
plt.hist(heights)
plt.title('Heights distribution of US presidents')
plt.xlabel('height(cm)')
plt.ylabel('number')


# In[ ]:




