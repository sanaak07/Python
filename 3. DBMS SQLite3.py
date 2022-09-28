#!/usr/bin/env python
# coding: utf-8

# # REFERENTIAL INTEGRITY

# In[1]:


import sqlite3


# In[2]:


db=sqlite3.connect('student_course.db')


# In[3]:


cur=db.cursor()


# #constraints
# unique--enter only unique values, no duplicate values
# not null--no blank values can be inserted in table

# In[5]:


cur.execute("create table course(courseid int primary key, coursename text,duration int)")


# In[6]:


cur.execute("create table student(roll_no int primary key,studentsname text,age int,courseid int,foreign key(courseid) references course(courseid))")


# In[7]:


cur.execute("insert into course values(78,'data science',12),(56,'python course',4),(101,'database',7)")


# In[8]:


print(cur.rowcount,'records(s) inserted')


# In[9]:


db.commit;


# In[10]:


cur.execute("insert into student values(1,'jack',22,78),(2,'john',21,56),(3,'rudolf',18,78),(4,'jim',21,56)")


# In[11]:


print(cur.rowcount,'record(s) inserted')


# In[12]:


db.commit()


# In[16]:


results=cur.execute('select * from course')
results.fetchall()


# In[17]:


results=cur.execute('select * from student')

results.fetchall()


# In[18]:


results=cur.execute('select courseid from course where coursename="data science"')

for i in results:
    print(i)


# # Subquery

# In[22]:


results=cur.execute('select * from student where courseid=(select courseid from course where coursename="Data Science")')

results.fetchall()


# In[23]:


results=cur.execute('select * from student where courseid=(select courseid from course where coursename="python course")')

results.fetchall()


# # JOIN

# # DIFFERENT TYPES OF SQL JOINs: 

# - (INNER) JOIN: Returns records that have matching values in both tables
# - LEFT (OUTER) JOIN: Returns all the records fromt he left table and the mathched records from the right table
# - RIGHT (OUTER) JOIN: Returns all records from right table, and the matched records from the left table
# - FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

# # INNER JOIN

# In[26]:


sql="select student.roll_no,student.studentsname,course.courseid,course.coursename from student inner join course on student.courseid=course.courseid"
results=cur.execute(sql)
for row in results:
    print(row)


# # LEFT JOIN

# In[28]:


sql="select student.roll_no,student.studentsname,course.courseid,course.coursename from student left join course on student.courseid=course.courseid"
results=cur.execute(sql)
for row in results:
    print(row)


# RIGHT JOIN and FULL OUTER JOIN is not supported in SQLite

# In[ ]:




