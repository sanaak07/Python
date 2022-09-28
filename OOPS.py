#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[12]:


class student:
    def __init__(self,rollno,name):       #initialisation constructor
        self.rollno=rollno
        self.name=name
    
    def display(self):                    #user defined function
        print('the roll no.of student is: ',self.rollno)
        print('the name of student is: ',self.name)


# In[7]:


obj1=student(201,'john')   #this line will automatically invoke the initialisation constructor
obj1.display()             #user defined function is called explicitly


# In[8]:


stud1=student(202,'andrew') #this line will automatically invoke the initialisation constructor
stud1.display()             #user defined function is called explicitly


# In[9]:


stud2=student(203,'tom') #this line will automatically invoke the initialisation constructor
stud2.display()          #user defined function is called explicitly


# In[14]:


stud3=student(204,'maria')
stud3.display()


# In[15]:


stud4=student(205,'jerry')
stud4.display()


# In[25]:


class employee:
    
    def __init__(self,empno,name,sal):
        self.empno=empno
        self.name=name
        self.sal=sal
        
    def display(self):
        print(self.empno,'',self.name,'',self.sal)


# In[28]:


emp1=employee(101,'ABC',6000)
emp1.display()

emp2=employee(102,'DEF',8000)
emp2.display()

emp3=employee(103,'XYZ',10000)
emp3.display()


# In[29]:


stud1.rollno


# In[30]:


stud1.name


# In[31]:


stud2.rollno


# In[33]:


stud2.name


# In[34]:


class student:
    fees=8000
    
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def display(self):
        print('name:',self.name,'grade:',self.grade)


# In[35]:


s1=student('lisa',6)
s1.display()


# In[36]:


s2=student('john',8)
s2.display()


# In[37]:


s3=student('tom',9)
s3.display()


# In[40]:


class company:
    revenue=80000
    
    def __init__(self,name,location,no_of_employees):
        self.name=name
        self.location=location
        self.no_of_employees=no_of_employees
        


# In[41]:


c=company('george','london',400)
print(c.name)
print(c.location)
print(c.no_of_employees)


# In[48]:


class car:
    def __init__(self,company,color):
        self.company=company
        self.color=color
        
    def display(self):
        print('this is a ',self.color,self.company)


# In[49]:


def main():
    c=car('ferrari','red')
    c.display()


# In[50]:


if __name__=='__main__':   #entry point of the compiler
    main()


# In[65]:


class employee:
    
    def __init__(self,name,age):
        print('initialised method called')
        self.name=name
        self.age=age
        
    def getdata(self,name,age):
            print('getdata method called')
            self.name=name
            self.age=age
            
    def displaydata(self):
            print('hello',self.name,self.age)   
    


# In[66]:


def main():
    e=employee('william',35)   #here initialise will work
    e.displaydata()
    
    e.getdata('john',25)
    e.displaydata()


# In[67]:


if __name__=='__main__':
    main()


# In[69]:


class player:
    
    def __init__(self,name,age,sport):
        print('initialised data for players')
        self.name=name
        self.age=age
        self.sport=sport
    
    def getdata(self,name,age,sport):
        print('getting data for players')
        self.name=name
        self.age=age
        self.sport=sport
        
    def displaydata(self):
        print('player details: ',self.name,self.age,self.sport)
        
def main():
    p1=player('virat',35,'cricket')
    p1.displaydata()
    
    p1.getdata('richard',45,'tennis')
    p1.displaydata()
    
    p2=player('dhoni',25,'cricket')
    p2.displaydata()
    
    p2.getdata('vivian',65,'cricket')
    p2.displaydata()
    
if __name__=='__main__':
    main()


# In[ ]:




