#!/usr/bin/env python
# coding: utf-8

# DATA STRUCTURE- DICTIONARY
# - key:value pair
# - given in curly bracket{}
# - give name of variable
# - d1={key:value,key:value,key:value}
# - Eg. d1={'id':1,'name':ABC,'age':22}
# - values are mutable(can be changed even after creation of dictionary)
# - keys can be updated, but cannot be changed
# - values can be updated/changed

# d1={key1:value1,key2:value2,key3:value3}

# In[1]:


d1={'id':1,'name':'Andrew','age':14}


# In[2]:


d1


# In[3]:


d1.keys()


# In[4]:


d1.values()


# In[5]:


d1.items()


# In[6]:


d1['id']


# In[7]:


d1['name']


# In[8]:


d1['age']


# In[9]:


print("The Id is ",d1['id'])


# In[10]:


print("The name is ",d1['name'])


# In[11]:


print("The age is ",d1['age'])


# In[12]:


d1['age']


# In[13]:


d1['age']=22


# In[14]:


d1['age']


# In[15]:


d1['name']='Jack'


# In[16]:


d1['name']


# In[17]:


d1


# In[18]:


d1.update({'fees':5000})


# In[19]:


d1


# In[20]:


d1.keys()


# In[21]:


d1.values()


# In[22]:


d1.items()


# In[23]:


d1['id']


# In[24]:


d1['name']


# In[25]:


d1['age']


# In[26]:


d1['fees']


# In[27]:


d1


# In[28]:


print('The id is ',d1['id'])


# In[29]:


print('The name is ',d1['name'])


# In[30]:


print ('The age is ',d1['age'])


# In[31]:


print('The fees is ',d1['fees'])


# In[32]:


del d1['age']


# In[33]:


d1


# In[34]:


d1.update({'fees':9500})


# In[35]:


d1


# In[36]:


print('The updated fees is ',d1['fees'])


# In[37]:


del d1['name']


# In[38]:


d1


# In[39]:


d1.update({'roll no':101})


# In[40]:


d1


# In[44]:


d2={'apple':'red','mango':'yellow','tree':'green'}


# In[45]:


d2


# In[46]:


d2.keys()


# In[47]:


d2.values()


# In[48]:


d2.items()


# In[49]:


d2.update({'brinjal':'purple'})


# In[50]:


d2


# In[51]:


d2['apple']


# In[52]:


d2['apple']='red_yellow'


# In[53]:


d2


# In[54]:


del d2['tree']


# In[55]:


d2


# In[56]:


d2.clear()


# In[57]:


d2


# In[58]:


del d2


# In[59]:


d2


# In[60]:


#Dictionary with integer keys:

intdict={10:'C++', 20:'java',30:'python',40:'ruby'}


# In[61]:


intdict


# In[62]:


intdict.keys()


# In[63]:


intdict.values()


# In[64]:


intdict.items()


# In[65]:


#adding new key to dictionary

intdict.update({50:'rails'})


# In[66]:


intdict


# In[67]:


#updating value in given key

intdict[40]='csharp'


# In[68]:


intdict


# In[69]:


#delete a key

del intdict[50]


# In[70]:


intdict


# In[71]:


#delete with pop

intdict.pop(30)


# In[72]:


intdict


# In[75]:


d3={1:['red','yellow','green'], 2:['apple','mango','grapes'],3:['rose','sunflower','lily']}


# In[76]:


d3


# In[77]:


d3.keys()


# In[78]:


d3.values()


# In[79]:


d3.items()


# In[80]:


d3[1]


# In[81]:


d3[2]


# In[82]:


d3[3]


# In[83]:


del d3[3]


# In[84]:


d3


# In[85]:


d3.pop(2)


# In[86]:


d3


# In[91]:


d3.update({2:['apple','mango','grapes']})


# In[92]:


d3


# In[93]:


d3


# In[94]:


d3


# In[95]:


d3[1][0]


# In[96]:


d3[2][1]


# In[97]:


d3[2]


# In[98]:


d3[1]


# SETS
# - A Python set is a collection of unordered items
# - no duplicate values allowed
# - it is immutable
# - repeated values are  ot printed
# - can be created in square brackets and curly brackets too
# - only itmes are there, no key values
# - values cannot be modified/updated ater creation
# - no index number is attached to any element of the set
# - we cant access any element, but we can print it out
# - any added element is added anywhere randomly
# - 'pop' will remove any element
# - in 'remove' it can be mentioned what to be removed

# In[99]:


x={22,33,56,78,90}
x


# In[100]:


y=set([33,22,56,78,90])
y


# In[101]:


x=([22,33,56,78,90])
x


# In[103]:


days={'monday','tuesday','wednesday','thursday'}
type(days)


# In[104]:


days.add('sunday')
days


# In[106]:


days[0]


# In[107]:


days.remove('sunday')
days


# In[108]:


days.pop()


# In[109]:


days


# In[110]:


days.clear()
days


# In[ ]:




