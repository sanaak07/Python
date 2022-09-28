#!/usr/bin/env python
# coding: utf-8

# DATA STRUCTURE-Sets
# - Unmutable, cant be modified after creation
# - No duplicate/repetitions are allowed
# - should be put in round and curly brackets
# - is a collection of unordered items.
# - there is  o index attached to the elements.
# - we can completely direct print them to access
# - as there is no index attached, new elements are added in any order
# - set objects do not support index numbers
# - as there is no indexing we also cannot update any item.
# - in pop operation, it will remove any element.
# - remove can operation can be applied to remove a specific value.
# - These operations work: 
# add 'item/value'
# pop (it ramdomly removes any item/value)
# remove(item/value)
# clear(clear the set data)

# In[1]:


x={22,33,56,78,90}


# In[2]:


x


# In[3]:


y=set([33,44,55,66,77])
y


# In[4]:


x={22,33,56,78,90,90,22}
x


# In[5]:


days={'monday', 'tuesday','thursday','wednesday'}
type(days)


# In[6]:


days.add('sunday')
days


# In[7]:


print(days[0])


# In[8]:


days[1]='june'


# In[9]:


days.remove('sunday')


# In[10]:


days


# In[11]:


days.pop()


# In[12]:


days


# In[13]:


days.clear()


# In[14]:


days


# In[ ]:




