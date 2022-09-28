#!/usr/bin/env python
# coding: utf-8

# # DBMS

# DBMS:
#     1. Relational Databases Eg.Oracle, MSSQL Server, SQ Lite, My SQL
#     2. Non relational databases

# DBMS:
#     1. Open Source Software-eg.SQLite Software (free,open source, relational database)
#     2. Propreitor Software-licensed

# SQLite:
#     - Relational Database
#     -Free available
#     -rows and coloumns can be easily created

# SQL (Structured Query Language):
#     1. DDL (Data Definition Language-create,alter,draw)
#     2. DML (Data Manipulation Language-select,insert,update,delete)
#     3. DCL (Data control Language-commit,revoke,grant)
# 

# # Create Database

# In[3]:


import sqlite3


# In[4]:


db=sqlite3.connect('student_detail_database21Aug.db')


# # Create cursor

# In[10]:


cur=db.cursor()


# In[11]:


cur.execute('create table student(id int primary key,name text,marks int)')


# In[13]:


cur.execute("insert into student(id,name,marks)values(101,'john',80)")


# In[14]:


db.commit()     #DCL


# In[18]:


cur.execute("insert into student(id,name,marks) values(102,'jack',75)")

db.commit()


# In[19]:


cur.execute("insert into student(id,name,marks) values(103,'dorsey',55)")

db.commit()


# In[20]:


results=cur.execute('select * from student')

for i in results:
    print(i)


# In[21]:


cur.execute("insert into student(id,name,marks) values(104,'elon',78)")
db.commit()


# In[25]:


cur.execute("insert into student values(105,'grey',90),(106,'Richard',55),(107,'Branson',95)")
db.commit()


# In[27]:


results=cur.execute('select * from student')

for i in results:
    print(i)


# In[28]:


results=cur.execute('select * from student')

results.fetchall()


# In[29]:


results=cur.execute('select id from student')

for i in results:
    print(i)


# In[30]:


results=cur.execute('select name from student')

for i in results:
    print(i)


# In[31]:


results=cur.execute('select marks from student')

for i in results:
    print(i)


# In[32]:


results=cur.execute('select id,name from student')

results.fetchall()


# In[33]:


results=cur.execute('select name, marks from student')

results.fetchall()


# In[34]:


results=cur.execute('select * from student')

results.fetchall()


# In[38]:


results=cur.execute('select * from student where id=101')

for i in results:
    print(i)


# In[42]:


results=cur.execute('select * from student where id=105')

results.fetchone()    #fetch one column


# In[43]:


results=cur.execute('select * from student where name="jack"')
results.fetchone()


# In[44]:


results=cur.execute('select * from student where name="dorsey"')
results.fetchone()


# In[45]:


results=cur.execute('select * from student where marks=78')

results.fetchone()


# In[47]:


results=cur.execute('select * from student where name in ("jack","john")')

for i in results:
    print(i)


# In[48]:


results=cur.execute('select * from student where id in (101,102,103)')

for i in results:
    print(i)


# In[52]:


results=cur.execute('select * from student')

for i in results:
    print(i)


# In[54]:


results=cur.execute('select * from student order by name asc')  # shows column in alphabetical order

for i in results:
    print(i)


# In[55]:


results=cur.execute('select * from student order by name desc')  # shows list in descending order

for i in results:
    print(i)


# In[ ]:




