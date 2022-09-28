#!/usr/bin/env python
# coding: utf-8

# In[1]:


for index in [10,20,30,40]:
    print(index)


# In[2]:


for index in [50,60,70,80]:
    print(index)


# In[3]:


for index in[90,100,110,120]:
    print(index)


# In[4]:


for index in[130,140,150,160]:
    print(index)


# In[5]:


for index in [32,45,53,68]:
    print(index)


# In[6]:


for index in[0.12,1.26,3.35,68.59]:
    print(index)


# In[7]:


for index in ['a','b','c','d']:
    print(index)


# In[8]:


for index in['cat','dog','rat','mouse']:
    print(index)


# In[10]:


for i in [100,200,300,400]:
    print(i)


# In[11]:


for x in [500,600,700,800]:
    print(x)


# In[12]:


for y in [1000,2000,3000,4000]:
    print(y)


# In[13]:


for p in['e','f','g','h']:
    print (p)


# In[14]:


for m in[12.3,56.2,68.9,25.1]:
       print(m)


# In[15]:


for k in ['apple','mango','guava','grapes']:
    print(k)


# In[16]:


for mix in[2,'apple',0.32,'a',45,'cat']:
    print(mix)


# In[17]:


for mix in[3,'cat',14.25,'apple',5620,'galaxy stars']:
    print(mix)


# In[24]:


for mix in [120,'guava',15.23,'apple',650]:
    print(mix)


# In[19]:


list1=[10,20,30,40,50]


# In[20]:


for i in [list1]:
    print(i)


# In[21]:


for i in list1:
    print(i)


# In[23]:


list2=['apple','banana','guava','oranges']

for x in list2:
    print (x)


# In[25]:


list3=['dell','mac','lenovo','apple']

for brands in list3:
    print(brands)


# In[26]:


list4=['apple','mango','banana','grapes']

for fruits in[list4]:
    print(fruits)


# In[27]:


list5=[30.4,96.5,70.5,62.5]

for percent in list5:
    print(percent)


# In[28]:


list6=['earth','jupiter','mars','saturn']

for planets in list6:
    print(planets)


# In[30]:


list7=[10,20,30,40,50]

for numbers in list7:
    print(numbers, end=' ')


# In[31]:


list8=[10,20,30,40,50]

for numbers in [list8]:
    print(numbers)


# In[32]:


list9=['rose','jasmine','lily','hibiscus']

for flowers in list9:
    print(flowers,end=' ')


# In[33]:


for flowers in list9:
    print(flowers)


# In[34]:


for flowers in [list9]:
    print(flowers)


# In[35]:


for flowers in [list9]:
    print(flowers)


# In[36]:


for flowers in [list9]:
    print(flowers)


# In[37]:


list10=['maths','physics','chemistry','biology']

for subjects in [list10]:
    print (subjects)


# In[41]:


list10=['maths','physics','chemistry','biology']

for subjects in list10:
    print (subjects)


# In[45]:


list11=['red','blue','pink','maroon','yellow']
        
for colours in list11:
    print (colours)


# In[48]:


list11=['red','pink','maroon','yellow']

for colours in list11:
    print(colours, end='')


# In[49]:


list11=['pink','blue','yellow','red','maroon']

for colours in list11:
    print(colours)


# In[51]:


list12=['spoons','fork','plate','saucer','teapot']

for utensils in [list12]:
    print(list12)


# In[52]:


#range

range(3)


# In[53]:


range(5)


# In[54]:


list(range(3))


# In[55]:


list(range(10))


# In[56]:


list(range(15))


# In[57]:


list(range(20))


# In[58]:


list(range(12))


# In[59]:


list(range(16))


# In[60]:


list(range(19))


# In[61]:


list(range(21))


# In[62]:


list(range(25))


# In[63]:


list(range(30))


# In[64]:


list(range(11))


# In[65]:


for i in (range(10)):
    print(i)


# In[66]:


for x in (range(20)):
    print(x)


# In[67]:


for x in (range(10)):
    print(x)


# In[68]:


for i in (range(20)):
    print(i,end=' ')


# In[71]:


for i in (range(30)):
    print(i, end='    ')


# In[72]:


range(0,7)


# In[73]:


list(range(0,7))


# In[74]:


list(range(5,20))


# In[75]:


list(range(10,20))


# In[76]:


list(range(10,15))


# In[77]:


for i in (range(2,10)):
    print(i)


# In[78]:


for x in (range(5,10)):
    print(x,end=' ')


# In[79]:


for x in (range(20,30)):
    print(x)


# In[80]:


for x in (range(40,50)):
    print(x, end=' ')


# In[81]:


#range(start,end,jump/skip)


# In[82]:


list(range(2,10,2))


# In[83]:


list(range(1,30,3))


# In[84]:


list(range(1,50,5))


# In[86]:


list(range(0,50,5))


# In[88]:


list(range(1,51,5))


# In[89]:


for i in (range(1,11)):
    print(i)


# In[90]:


for i in (range(2,20)):
    print(i, end=' ')


# In[94]:


u=int(input ('Enter any number to generate table'))

for i in (range(1,11)):
    print(u,'*',i,'=',u*i)


# In[95]:


u=int(input('Enter any number to generate table'))

for i in (range(1,11)):
    print(u,'*',i,'=',u*i)


# In[96]:


u=int(input('Enter any value to generate table'))

for i in (range(1,11)):
    print(u,'*',i,'=',u*i)


# In[97]:


u=int(input('Enter any value to generate table'))

for i in (range(1,11)):
    print(u,'*',i,'=',u*i)


# In[101]:


u=int(input('Enter any value to generate table: '))

for i in (range(1,11)):
    print(u,'*',i,'=',u*i)


# In[104]:


u=int(input('Enter any value to generate division: '))

for i in (range(1,11)):
    print(u,'/',i,'=',u/i)


# In[105]:


k=[]
for i in (range(5)):
    k.append(i)
    print(k)


# In[106]:


k=[]
for i in (range(6)):
    k.append(i)
    print(k)


# In[107]:


k=[]
for i in(range(11)):
    k.append(i)
    print(k)


# In[108]:


k=[]
for i in (range(6)):
    k.append(i)
    
print(k)


# In[109]:


k=[]
for i in (range(11)):
    k.append(i)
    
print(k)


# In[110]:


k=[]
for i in (range(5)):
    string1=input('Enter any city name to be appended: ')
    k.append(string1)
    print(k)


# In[113]:


k=[]
for i in (range(5)):
    string2=input('Enter sujects to append: ')
    k.append(string2)
    print(k)


# In[115]:


k=[]
for i in(range(5)):
    string3=input('Enetr any 3 digit numbers')
    k.append(string3)
    print(k)


# In[117]:


k=[]
for i in (range(5)):
    string4=input('Enter movie name to be appended: ')
    k.append(string4)
    print(k)


# In[119]:


k=[]
for i in (range(3)):
    string5=input('Enter any name of colors to be appended: ')
    k.append(string5)
    print(k)


# In[126]:


k=[]
for i in (range(5)):
    string6=input('Enter names to be appended: ')
    k.append(string6)
    print(k)


# #if-else constructs

# In[127]:


marks=100

if(marks>=70):
    print('Good')
else:
    print('Average')


# In[132]:


marks=100

if(marks>=70):
    print('Good')
else:
    print('Average')


# In[133]:


if(10%2==0):
    print('Even number')
else:
    print('Odd Number')


# In[134]:


if(13%2==0):
    print('Even')
else:
    print('Odd')


# In[135]:


u=int(input('Enetr any number to be tested: '))

if (u%2==0):
    print('Even')
else:
    print('Odd')


# In[137]:


u-int(input('Enter any number for testing: '))

if (u%2==0):
    print('Even number')
else:
    print('Odd number')


# In[138]:


grade=int(input('Enter any grade: '))

if grade>90:
    print('Excellent')
elif grade>80 and grade<=90:
    print('very good')
elif grade>70 and grade<=80:
    print('Good')
elif grade>60 and grade<=70:
    print('Average')
else:
    print('Poor')


# In[143]:


grade=float(input('Enter any grade: '))

if grade>90:
    print('Your Result is Excellent')
elif grade>80 and grade<=90:
    print('Your Result is very good')
elif grade>70 and grade<=80:
    print('Your Result is Good')
elif grade>60 and grade<=70:
    print('Your Result is Average')
else:
    print('Your Result is Poor')


# In[ ]:




