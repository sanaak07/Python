#!/usr/bin/env python
# coding: utf-8

# LOOPS
# - the code is running/lines of statements is iterated(repeated) until condition is true, the loop will run or else it will return false.
# - there are 2 loops in python. 1. while and 2. for
# - as soon as loop is false the code will be terminated.
# - most important statements- 1. initialisation 2. condition 3. increment
# - initialisation: i=0
# - condition:  while (i<5):    (.....putting colon is very important)
#               print (i)
# - increment: i=i+1
# - indentation gaps are required

# In[2]:


#initialisation
i=0
#condition
while (i<5):
    print (i)
    i=i+1        #increment


# In[4]:


i=0

while(i<7):
    print (i)
    i=i+1


# In[6]:


i=0
while (i<8):
    print (i)
    i=i+1


# In[7]:


i=0
while (i<9):
    print(i)
    i=i+1


# In[8]:


i=0
while(i<10):
    print (i)
    i=i+1


# In[9]:


i=0
while(i<11):
    print(i)
    i=i+1


# In[10]:


i=0
while(i<12):
    print(i)
    i=i+1


# In[11]:


i=0
while(i<13):
    print(i)
    i=i+1


# In[13]:


i=0
while(i<14):
    print(i)
    i=i+2


# In[14]:


i=0
while(i<15):
    print(i)
    i=i+1.5


# In[15]:


i=0
while(i<16):
    print(i)
    i=i+4


# In[16]:


i=2
while(i<18.2):
    print(i)
    i=i+2


# In[17]:


i=19
while(i<20):
    print(i)
    i=i+10


# In[20]:


i=5
while (i<50):
    print('The value of i is: ',i)
    i=i+5


# In[24]:


i=10
while (i<100):
    print('The value of i is ', i)
    i=i+10


# In[22]:


j=1
while (j<100):
    print ('The value of j is: ',j)
    j=j+50


# In[23]:


k=10
while(k<100):
    print('the value of k is: ', k)
    k=k+10


# In[26]:


k=50
while(k<500):
    print ('the value of k is ', k)
    k=k+100


# In[28]:


a=200
while(a<1000):
    print('the value of a is ',a)
    a=a+100


# In[30]:


i=1
while(i<=10):
    print('the value of i is ',i)
    i=i+1


# In[31]:


i=100
while(i<=1000):
    print('the value of i is ',i)
    i=i+100


# In[32]:


i=1
while(i<=10):
    print ('the multiplication of 2 is ',2*i)
    i=i+1


# In[34]:


i=1
while(i<=10):
    print('the multiplication table of 3 is ', i*3)
    i=i+1


# In[40]:


i=1
s=int(input('enter any value to be multiplied by 2 '))

while(i<=5):
    print ('your answer is ',2*i)
    i=i+1


# In[48]:


i=1
s=int(input('Enter any value for multiplication '))

print ('the multiplication table for ',s,'is')

while(i<=10):
    print(s*i)
    i=i+1


# In[50]:


i=1
s=int(input('Enter any value for division '))

print ('the division for ',s,'is')

while(i<=10):
    print(s*i)
    i=i+1


# In[51]:


i=1
s=int(input('Enter any value for multiplication table '))

while(i<=10):
    print(s, '*',i,"=",i*s)
    i=i+1


# In[54]:


i=1
s=int(input('Enter any value for multiplication table '))
while(i<=10):
    print(s,'*',i,'=',i*s)
    i=i+1


# In[55]:


i=1
s=int(input('Which multiplication table do you want? '))

while (i<=10):
    print(s,'*',i,'=',i*s)
    i=i+1


# In[58]:


i=1
s=int(input('Which multiplication table do you want? '))

while(i<=10):
    print(s,'*',i,'=',i*s)
    i=i+1


# 

# In[64]:


i=1
s=int(input('Which multiplication table do you want? '))
print('The multiplication table of ',s, 'is')

while (i<=10):
    
    print(s,'*',i,'is',i*s)
    i=i+1


# In[65]:


i=1
s=int(input('Which multiplication table do you want? '))
print('The multiplication table of ',s, 'is')

while (i<=10):
    
    print(s,'*',i,'is',i*s)
    i=i+1


# In[71]:


i=1
while(i<10):
    print(i, end=' ')
    i=i+1


# In[72]:


i=1
while(i<10):
    print(i, end=' ')
    i=i+1


# In[73]:


i=1
while(i<50):
    print(i,end=' ')
    i=i+1


# In[74]:


i=1
while(i<10):
    print('inside loop')
    print('the value of i = ',i)
    i=i+1


# In[ ]:




