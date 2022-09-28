#!/usr/bin/env python
# coding: utf-8

# #object serialisation: create an object file in a drive, shows in jupuyter notebook ome page
# 
# #object de-serialisation: extract the file in python from the drive
# 
# # PICKLE:
#     1. Dump (serialisation)
#     2. Load (de-serialisation)

# In[1]:


import pickle


# In[2]:


flower_dict={1:'rose',2:'lily',3:'lotus',4:'tulip'}


# In[3]:


filename='flower'
outfile=open(filename,'wb')   #wb=write binary mode


# In[4]:


outfile=open('flower.obj','wb')   #filename=flower


# In[7]:


pickle.dump(flower_dict,outfile)   # pickling the file 
outfile.close()                    # dump method serialise


# In[8]:


infile=open(filename,'rb')     #rb=read binary


# In[9]:


infile=open('flower.obj','rb')


# In[10]:


# because its binary, its not readable format


# In[12]:


new_dict=pickle.load(infile)


# In[13]:


infile.close()


# In[14]:


print(new_dict)


# In[16]:


print(new_dict==flower_dict)


# # RUN TIME ERRORS

# In[17]:


for i in [1,2,3,4,5]:
    print(i)


# In[18]:


56/2


# In[19]:


56/0     #zero division error


# In[21]:


np1=input('enter value')
np2=input('enter value')
np1/np2                      #typo error


# # EXCEPTION HANDLING  (try...except)

# In[24]:


try:
    79/0
except ZeroDivisionError as err:
        print('Handling run time error: ',err)


# In[25]:


try:
    8+m*2
except NameError as err:
    print('handling run time error:',err)


# In[27]:


try:
    i=int(input('value'))
    p=50/i
except ZeroDivisionError:
    print('Zero division error')
except NameError:
    print('check name of variable: Nme error')
except IndentationError:
    print('check indentation')
else:
    print(p)


# In[28]:


a=[10,20,30]

try:
    print(a[1])
    print(b[2])
    print(c[3])
except:
    print('out of range')
else:
    print('hello')
finally:
    print('end')


# In[29]:


try:
    i=int(input('value'))
    p=50/i
except:
    print('an error occurred')
else:
    print(p)


# In[31]:


try:
    c=2
    print(c)
except NameError:
    print('check name')
except IndentationError:
    print('check indent')
else:
    print(c)
finally:
    print('this line will be executed always')


# In[33]:


try:
    #k=5
    print(k)
except NameError:
    print('check name')
else:
    print(k)
finally:
    print('this line will be executed always')
    


# In[39]:


def testf():
    a=int(input('enter'))
    b=int(input('enter'))
    c=a/b
    print('c=',c)


# In[40]:


try:
    testf()
except ZeroDivisionError:
    print('divide by zero')


# In[41]:


try:
    testf()
except ArithmeticError:
    print('some error')
    print(ArithmeticError)


# In[42]:


def typecasting_func():
    x=input('enter value')
    y=input('enter value')
    z=x*y
    print('z=',z)


# In[43]:


try:
    typecasting_func()
except TypeError:
    print('typecast error')


# In[45]:


try:
    appendfile=open('demofile.txt','a')
except IOError:
        print('file not found')
else:
    print('file opened successfully')
    print(appendfile.write('\n this is the new line'))


# In[46]:


readme=open('demofile.txt','r')


# In[47]:


print(readme.read())


# In[ ]:




