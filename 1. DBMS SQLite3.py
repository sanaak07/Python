#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sqlite3


# In[15]:


db=sqlite3.connect("student_detail_database21Aug.db")


# In[16]:


cur=db.cursor()


# In[17]:


results=cur.execute("select * from student")

for i in results:
    print(i)


# In[22]:


results=cur.execute("select * from student where id=101")


# In[23]:


results.fetchone()


# In[24]:


results=cur.execute('select * from student where id=104')
results.fetchone()


# In[28]:


results=cur.execute("select * from student where name='Richard'")

results.fetchall()


# In[29]:


results=cur.execute("select * from student where name='Branson'")

for i in results:
    print(i)


# In[30]:


results=cur.execute('select * from student')
for i in results:
    print(i)


# In[32]:


results=cur.execute('select * from student where marks=78')
for i in results:
    print(i)


# In[33]:


results=cur.execute('select * from student where marks=55')
for i in results:
    print(i)


# In[36]:


results=cur.execute('select * from student limit 4')
for i in results:
    print(i)


# In[46]:


results=cur.execute("select * from student where id in (101,102,103)")
for i in results:
    print(i)


# In[48]:


results=cur.execute("select * from student where name in ('john','jack')")
for i in results:
    print(i)


# In[49]:


results=cur.execute('select * from student where id in (101,102,103)')

results.fetchall()


# In[50]:


results=cur.execute('select * from student where marks in (78,90)')
for i in results:
    print(i)


# In[51]:


results=cur.execute('select * from student')
for i in results:
    print(i)


# In[53]:


results=cur.execute('select * from student order by marks asc limit 3')

for i in results:
    print(i)


# In[55]:


results=cur.execute('select * from student order by marks desc limit 2')

for i in results:
    print(i)


# In[56]:


results=cur.execute('select * from student where marks>60 and marks<90')

for i in results:
    print(i)


# In[57]:


results=cur.execute('select * from student where marks>40 and marks<60')

for i in results:
    print(i)


# In[65]:


results=cur.execute('select * from student where id=101 or marks=100')

results.fetchall()


# # AGGREGATE FUNCTIONS

# MIN--find minimum
# MAX-- find maximum
# AVG--find average 
# SUM--find sum
# COUNT--count the number of rows

# In[67]:


# to find minimum marks

results=cur.execute('select min(marks) from student')
results.fetchone()


# In[68]:


# find maximum marks

results=cur.execute('select max(marks) from student')
results.fetchone()


# In[69]:


# find average marks

results=cur.execute('select avg(marks) from student')
results.fetchone()


# In[70]:


# find sum

results=cur.execute('select sum(marks) from student')
results.fetchone()


# In[71]:


# to count the number of rows

results=cur.execute('select count(id) from student')
results.fetchone()


# In[72]:


# to select between a range
results=cur.execute('select * from student where marks between 65 and 85')

for i in results:
    print(i)


# In[73]:


# to select empty column
results=cur.execute('select * from student where marks is null')

for i in results:
    print(i)


# In[74]:


results=cur.execute('select * from student where marks is not null')

for i in results:
    print(i)


# LIKE Operators (shows pattern of a data)

# In[77]:


# to see data with only 'd' alphabet
results=cur.execute('select * from student where name like "D%"')
                    
for i in result:
    print(i)


# In[80]:


# to see data with only 'j' alphabet

results=cur.execute('select * from student where name like "j%"')

for i in result:
    print(i)
    


# In[81]:


# to see second character is 'a' alphabet

results=cur.execute('select * from student where name like "_a%"')

for i in result:
    print(i)


# In[83]:


# to see if last character is 'm' alphabet

results=cur.execute('select * from student where name like "%n"')

for i in results:
    print(i)


# In[85]:


# to see if somewhere 'e' alphabet should be there

results=cur.execute('select * from student where name like "%e%"')

for i in result:
    print(i)


# In[86]:


results=cur.execute('select * from student')
results.fetchall()


# In[87]:


# to display only 4 letter character
results=cur.execute('select * from student where name like "____"')

for i in result:
    print(i)


# In[88]:


# to see marks above 70
results=cur.execute('select * from student where marks NOT in (70)')

results.fetchall()


# In[98]:


results=cur.execute('select * from student where name NOT in ("kim")')

for i in results:
    print(i)


# In[100]:


# UPDATE record


# In[106]:


# update record using set marks

sql='update student set marks=81 where id=104'
cur.execute(sql)


# In[107]:


result=cur.execute('select * from student where id=104')
for row in results:
    print(row)


# In[105]:


results=cur.execute('select * from student')
for row in results:
    print(row)


# In[108]:


# multiple record update using 'IN'

sql='UPDATE student SET marks=68 WHERE id IN(104,105)'
cur.execute(sql)

#verify if its updated
results=cur.execute('SELECT * FROM STUDENT')
for row in results:
    print (row)


# # DELETE ANY UNWANTED RECORDS

# In[110]:


sql='delete from student where id=101'

cur.execute(sql)


# In[111]:


results=cur.execute('select * from student')
results.fetchall()


# In[112]:


sql='delete from student where id=104'

cur.execute(sql)


# In[114]:


results=cur.execute('select * from student')
results.fetchall()


# # DROP table 

# In[115]:


sql='drop table student'
results=cur.execute(sql)


# In[116]:


results=cur.execute('select * from student')
results.fetchall()


# In[117]:


db.close()


# In[ ]:




