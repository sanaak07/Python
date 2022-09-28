#!/usr/bin/env python
# coding: utf-8

# # String Functions

# In[1]:


word1='computer'


# In[2]:


word1


# In[4]:


word1.upper()


# In[5]:


word2='MOBILE'


# In[6]:


word2


# In[7]:


word2.lower()


# In[10]:


word3='TeSlA'


# In[11]:


word3


# In[12]:


word3.swapcase()


# In[13]:


string1='LENOVO'
string1.lower()


# In[14]:


a=string1.lower()
a


# In[15]:


string2='planets'
b=string2.upper()
b


# In[18]:


string3='apple'
c=string3.upper()
c


# In[20]:


string4='WONDERLAND'
d=string4.lower()
d


# In[22]:


string5='tRaInInG'
e=string5.swapcase()
e


# In[25]:


string6='data science'
f=string6.capitalize()
f


# In[26]:


string7='elon musk'
g=string6.title()
g


# In[28]:


string8='there are many galaxies in the universe'
string8.title()


# In[30]:


word4='mars rover'


# In[31]:


word4


# In[32]:


word4.capitalize()


# In[33]:


word4.title()


# In[34]:


string9='there are many galaxies in the universe'
string9.split()


# In[37]:


string1.isupper()


# In[38]:


string1.islower()


# In[39]:


string2.isupper()


# In[40]:


string3.islower()


# In[45]:


string10='1234'


# In[46]:


string10.isalpha()


# In[47]:


string11='watermelon'


# In[48]:


string11.isdigit()


# In[49]:


string12='123456'


# In[50]:


string12.isdigit()


# In[51]:


string13='mango'


# In[52]:


string13.isalpha()


# In[53]:


string14='water123'


# In[54]:


string14.isalnum()


# In[55]:


string15='lemon20'


# In[57]:


string15.isalnum()


# In[58]:


string17='there are many stars in galaxy'


# In[61]:


string17.startswith('there')


# In[62]:


string17.startswith('many')


# In[66]:


string17.endswith('galaxy')


# In[67]:


string17.endswith('stars')


# In[73]:


string18='elon musk is a ceo of tesla'


# In[74]:


string18.find('musk')


# In[75]:


string18.find('tesla')


# In[77]:


string18.find('is',6,20)


# In[78]:


string17


# In[79]:


string17.find('many',1,25)


# In[82]:


string19=('6789')


# In[83]:


string19.isdigit()


# In[84]:


string19


# In[85]:


string18


# In[86]:


string18.count('e')


# In[87]:


string18.count('s')


# In[88]:


string18.replace('tesla','ford')


# In[89]:


string18.replace('ford','tesla')


# In[90]:


string19=('NASA is building a hotel project on Mars')


# In[91]:


string19.replace('NASA','SPACEX')


# In[92]:


string20=('data science is growing feild based on data')


# In[93]:


string20.replace('science','analytics')


# In[97]:


text1=['NASA','is','building','hotel','project','on','mars']


# In[98]:


text1


# In[99]:


''.join(text1)


# In[100]:


' '.join(text1)


# In[101]:


text2=['the','twin','towers','noida','were','destructed']


# In[102]:


text2


# In[103]:


' '.join(text2)


# In[106]:


text2


# # casefold

# In[109]:


string1='Tesla'
string2='tesla'

if string1.casefold()==string2.casefold():
    print('the two strings are matching')
else:
    print('the two strings are not matching')


# In[110]:


string1='stars'
string2='starry'

if string1.casefold()==string2.casefold():
    print('the 2 strings are matching')
else:
    print('the 2 strings are not matching')


# In[111]:


string1='watermelon'
string2='watERMelon'

if string1.casefold()==string2.casefold():
    print('strings are matching')
else:
    print ('strings are not matching')


# # string concatenation

# In[113]:


str1='NEW'
str2='Horizon'
print(str1+str2)
print(str1+' '+str2)


# In[114]:


str1='Blue'
str2='bells'

print(str1+' '+str2)


# In[115]:


str1='the sky is'
str2='blue'

print(str1+' '+str2)


# # string printing format
# 1. C-style format
# 2. string format

# #  C-style format

# In[117]:


name='John'
print('Hello,%s!'%name)


# In[118]:


name='John'
print('Hello',name,'!')


# # in C++ data types are of 3 types: 
# 
# 1. char(%s) 2. int(%d) 3.float(%f)

# In[119]:


name='John'
age=23
salary=688.564
print('%s is %d years old taking salary %f '%(name,age,salary))


# In[125]:


name='Sarah'
age=25
pincode=411048
print('%s is a %d years old with pincode %f '%(name,age,pincode))


# In[128]:


fruit1='apple'
fruit2='mango'
fruit3='grapes'

print('I like to make a salad of %s,%s and %s.'%(fruit1,fruit2,fruit3))


# In[129]:


col1=('violet')
col2=('indigo')
col3=('blue')

print('%s,%s and %s are the colours in a rainbow!'%(col1,col2,col3))


# In[133]:


b1='Apple'
b2='Lenovo'
b3='Dell'

print('%s, %s and %s are the brands of a laptop'%(b1,b2,b3))


# In[134]:


n1=154
n2=564
n3=758

print('The salaries of John, Bob and Ben are %d, %d and %d'%(n1,n2,n3))


# # string format

# In[136]:


print ('People usually take {}with{}'.format('coke','pizza'))


# In[137]:


print ('people usually take {} with {}'.format('coke','pizza'))


# In[140]:


print('people generally take {0} with {1}'.format('coke','pizza'))


# In[139]:


print('people generally take {1} with {0}'.format('coke','pizza'))


# In[ ]:




