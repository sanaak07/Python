#!/usr/bin/env python
# coding: utf-8

# # Lambda-anonymous function

# lambda variable function

# In[1]:


t1=lambda x:x+2


# In[2]:


t1(2)


# In[3]:


t1(8)


# In[4]:


t2=lambda x:x+6


# In[5]:


t2(12)


# In[6]:


t2(19)


# In[7]:


t3=lambda x:x+11


# In[8]:


t3(14)


# In[9]:


t4=lambda x:x+10


# In[10]:


t4(20)


# In[11]:


t5=lambda y:y+21


# In[12]:


t5(22)


# In[13]:


t6=lambda x,y:x+y


# In[14]:


t6(12,10)


# In[15]:


t6(11,22)


# In[16]:


t7=lambda x,y:x*y


# In[17]:


t7(12,10)


# In[18]:


t8=lambda p:p**2


# In[19]:


t8(4)


# In[20]:


t8(12)


# In[21]:


t9=lambda s:s*s**3


# In[22]:


t9(3)


# In[28]:


t10=lambda m:m**(1/2)


# In[29]:


t10(25)


# In[30]:


t11=lambda var1,var2:var1+var2


# In[31]:


t11(8,5)


# In[32]:


carea=lambda pi,radius:pi*(radius**2)


# In[33]:


carea(3.14,20)


# In[34]:


carea(3.14,12)


# In[35]:


addvar=lambda arg1,arg2:arg1+arg2
print ('value of total: ',addvar(5,10))
print ('value of total: ',addvar(30,40))


# In[36]:


def farenheit(t):
    return(9/5)*t+32


# In[38]:


f=farenheit(35)
f


# In[40]:


def celsius(t):
    return((5/9)*(t-32))


# In[42]:


ce=celsius(95)
ce


# In[57]:


def testin():
    ax-int(input('Enter ax'))
    bx=int(input('Enter bx'))
    t=lambda ax,bx:ax**bx
    print(t(ax,bx))


# In[58]:


testin()


# In[60]:


list1=[10,20,30,40]
list(map(lambda x:x+2,list1))


# In[61]:


list2=[1,2,3,4,5,6]

list(map(lambda y:y**2,list2))


# In[63]:


list3=[4,9,16,25,36]
list(map(lambda p:p**(1/2),list3))


# In[64]:


c=[35.2,36.5,37.3,38,39.8]


# In[65]:


f=list(map(lambda x:(9/5)*x+32,c))
print(f)


# In[66]:


c=list(map(lambda x:(5/9)*(x-32),f))


# In[67]:


print(c)


# In[68]:


newclist=[round(x,2) for x in c]
newclist


# In[69]:


newlist=['%.2f'%j for j in c]
newlist


# In[70]:


radius=[4,6,8,10]
cir=list(map(lambda y:2*3.14*y,radius))
print(cir)


# In[71]:


cirnew=['%.2f'%k for k in cir]
cirnew


# In[72]:


# filter in lambda


# In[73]:


mylist=[1,2,3,4,5,6,7]
list(filter(lambda x:x>2,mylist))


# In[74]:


even=lambda x:x%2==0
list(filter(even,range(11)))


# In[75]:


[x for x in range(11) if x%2==0]


# In[ ]:




