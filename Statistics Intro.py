#!/usr/bin/env python
# coding: utf-8

# STATISTICS
# 1. Descriptive
#     a. Central Tendency
#         - Mean / Average  Eg. Sum of data divided by counts 11+2+5+7+3/5
#         - Median  Eg. Make data in ascending order. In case of odd values-15 18 21 38 46 take mid value, here median is 21. In case of even value-11 10 14 13 14 16, take 2 mid values and divide by 2.
#         - Mode highest frequency value
#     b. Dispersion of Data
#         - range
#         - variance
#         - standard deviation
#         - skew
#         - percentile
#         - kurtosis
#         - skewness
#         
# 2. Inferential
# 
# Dependent and independent variavle
# dependent variable: Eg.name, id, qualification, experience are dependent variable
# independent variable: Eg. Salary is a dependent variable on qualification and experience in this case.
# 
# Data
#     1. Categorical type- Eg.Marital Status, political perty, eye color
#     2. Numerical type
#         - Discrete Eg.number of children, defects per hour
#         - Continous Eg. weight, voltage

# In[1]:


#import numpy database
import numpy as np 


# In[2]:


#create a array
a=np.array([20,90,56,45,12,10])


# In[3]:


#find mean of a
np.mean(a)


# In[6]:


#create a variable with mean of a
p=np.mean(a)


# In[7]:


#print p
p


# In[8]:


#round off p by 2 decimal digits
round (p,2)  


# In[10]:


#create b array
b=np.array([10,20,30,40,50,60,70])


# In[11]:


#find mean of b
np.mean(b)


# In[12]:


#find median of b
np.median(b)


# In[13]:


#find median of a
np.median(a)


# In[14]:


#find min value in a
a.min()


# In[15]:


#find max value in a
a.max()


# In[16]:


#formula of range
range_of_a=a.max()-a.min()


# In[17]:


#find range of a
range_of_a


# In[18]:


#find what array is in a
a


# In[19]:


#find out variance
a.var()


# In[20]:


#find mean value of array a
np.mean(a)


# In[21]:


#find std.deviation of a
a.std()


# In[22]:


#round off to 2 decimal value
round(a.std(),2)


# In[23]:


#find for b array
b


# In[24]:


#find variance of b
b.var()


# In[25]:


#find Std.deviation of b
b.std()


# In[ ]:




