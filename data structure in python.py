#!/usr/bin/env python
# coding: utf-8

# # Data structures in python

# In[2]:


squares=[1,4,9,16,25]


# In[3]:


squares


# In[4]:


squares[0]


# In[5]:


squares[-1]


# In[6]:


squares[-3]


# In[7]:


squares[:]


# In[8]:


squares +


# In[9]:


squares + [36,49,64,81,100]


# In[10]:


cubes=[1,8,27,65,125]


# In[11]:


cubes[3]=64


# In[12]:


cubes


# In[13]:


cubes.append(216)   #add cube of 6


# In[14]:


cubes.append(7**3) #and the cube of 7


# In[15]:


cubes


# In[16]:


letters=['a','b','c','d','e','f','g']


# In[17]:


letters


# In[20]:


letters[2:5]=['C','D','E']


# In[21]:


letters


# In[22]:


len(letters)


# In[23]:


fruits=['orange','apple','pear','banana','kiwi','apple','banana']


# In[24]:


fruits.count('apple')


# In[25]:


fruits.count('tangerine')#return the number oftimes x appears in list


# In[26]:


fruits.index('banana')


# In[27]:


fruits.index('banana',4)  #find next banana starting poistion 4


# In[28]:


fruits.reverse()


# In[29]:


fruits


# In[30]:


fruits.sort()


# In[31]:


fruits


# In[32]:


fruits.pop()


# In[33]:


stack=[3,4,5]


# In[34]:


stack.append(7)


# In[36]:


stack.append(6)


# In[37]:


stack


# In[38]:


stack.pop()


# In[40]:


list1=[100,200,300,400,500]
list1.reverse()
print(list1)


# In[41]:


list1=list1[::-1]
print(list1)


# In[42]:


basket={'apple','orange','apple','pear','orange','banana'}


# In[43]:


print(basket)


# In[45]:


tel={'jack':4098,'sape':4139}
tel['guido']=4127
tel


# In[46]:


tel['jack']


# In[47]:


del tel['sape']


# In[48]:


tel['irv']=4127
tel


# In[49]:


my_dict={'username':'XYZ','email':'xyz@gmail.com','location':'mumbai'}


# In[50]:


print('username:',my_dict['username'])


# In[51]:


print('email:',my_dict['email'])


# In[52]:


print('location:',my_dict['location'])


# In[53]:


my_dict['name']='nick'


# In[54]:


print(my_dict)


# In[ ]:




