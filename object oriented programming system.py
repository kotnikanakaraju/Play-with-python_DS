#!/usr/bin/env python
# coding: utf-8

# # Abstraction 

# if a class one or more than one abstract method then the class
# is called abstract class

# if the method is declared without implemetation it is 
# called as abstraction method

# In[1]:


from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("This is a concrete method")
obj1=A()
obj1.method1()

#its getting error becuase we cannot create object for
# abstract class but we can inherit abstract class& we can create object


# In[ ]:


# Rules for inheriting the abstract class
# absttrat methods in abstract class must implement in subclass


# In[2]:


from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("This is a concrete method")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemnted in subclass")
    def method3(self):
        print("method3 is implemented in sub class ")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()


# In[ ]:


# Abstract class is useful for blueprint for subclass
# it iused for design purpose
# when we creating classes,if the classes have same methods&
# implemetations is different then we create abstract class


# In[7]:


from abc import ABC

class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
    def figure(self):
        return 'it is 2-dimensional plane figure'
    
class Rectangle(Polygon):
    def sides(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        print(self.length*self.breadth)
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def extramethod(self):
        return 'rectangle has 4 sides'
Rec=Rectangle()
Rec.sides(10,20)
Rec.area()
Rec.perimeter()


# # Static varaibles and instance variables

# In[9]:


# the variable which is declared outside the class &
# inside the class then it is called class variable or 
# static variable

class A:
    staticVariable1=10
    staticVariable2=20
    
    def samplemethod(self):
        print("sample method")
    
A.staticVariable3=30
obj=A()
print(obj.staticVariable1)
print(obj.staticVariable2)
print(obj.staticVariable3)


# In[13]:


class A:
    staticVariable1=10
    staticVariable2=20
    
    def samplemethod(self):
        print("sample method")
        
    def method(self):
        print(self.staticVariable1)
        print(A.staticVariable1)
    
A.staticVariable3=30
print(A.staticVariable1)
print(A.staticVariable2)
print(A.staticVariable3)
obj=A()
obj.method()


# In[ ]:


#we can create,update,access,delete class variables using class
# name.but we can only access class variable using object


# In[19]:


class A:
    def __init__(self,a,b):
        self.instancevariable1=a
        self.instancevariable2=b

obj=A(10,20)
obj.instancevariable3=30
obj.instancevariable4=20
obj.instancevariable1=200
print(obj.instancevariable1)
print(obj)


# In[ ]:


#if we create an new variable to an object which is not present
# ,then it will create a new variable for an object
# we can access ,update,delete,create object by using instance variables


# In[ ]:


# if all objects has same value then we declare it as class variable


# In[21]:


class student:
    schoolName="MGR"
    def __init__(self,name,roll,add,phone):
        self.name=name
        self.roll=roll
        self.add=add
        self.phone=phone
        
s1=student("A",1,'a',884993003)
s2=student("B",2,'b',838979399)
s3=student("C",3,'c',8738398393)

s1.schoolName="savita"

for obj in [s1,s2,s3]:
    print(obj.name)
    print(obj.roll)
    print(obj.add)
    print(obj.phone)
    print(obj.schoolName)


# Instance

# In[ ]:


#By default the methods we create in class are instance method
# Instance method is also called as method of object
# instace methods create/update/access/modify/delete the objects attributes

# attributes of object or instance variable  both are same
# instance method performs operations on objectr attributes


# # Instance methods

# In[2]:


class Employee:
    def instancemethod1(self):
        print("instance method created")
    
    def instancemethod(self,a,b):
        print(a,b)
        
obj=Employee()
obj.instancemethod(3,4)
obj.instancemethod1()


# In[4]:


#create instance variables using instance method
class employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    
    def getemployeeName(self):
        print(self.name)
emp=employee('pavan',101000,822992)
emp.getemployeeName()


# In[5]:


# we can access class variable & instance variables using object


# In[14]:


class employee:
    A=10
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    
    def getemployeeName(self):
        print(self.name)
        
    def getclassvariable(self):
        print(self.A)
        
    def updateName(self,new_name):
        self.name=new_name
        
    def updateclassvariable(self,new_value):
        self.__class__.A=new_value
        
    def deleteinstancevariable(self):
        del self.name
        
    def deleteclassvariable(self):
        self.__class__.A
emp=employee('pavan',101000,822992)
# emp.getemployeeName()
emp.getclassvariable()
emp.updateName('ravi')
emp2=employee("ravi",83884,83883)
emp2.updateName("laxmi")
emp2.getemployeeName()
emp.updateclassvariable(200)
print(employee.A)
emp.deleteinstancevariable()
print(emp.name)
emp.deleteclassvariable()
print(emp2.A)


# In[21]:


from types import MethodType

class employee:
    A=10
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    
    def getemployeeName(self):
        print(self.name)
        
    def getclassvariable(self):
        print(self.A)
        
    def updateName(self,new_name):
        self.name=new_name
        
    def updateclassvariable(self,new_value):
        self.__class__.A=new_value
        
    def deleteinstancevariable(self):
        del self.name
        
    def deleteclassvariable(self):
        self.__class__.A
emp=employee('pavan',101000,822992)
def addingmethod(self):
    print("method added successfully")
    
emp.newInstanceMethod=MethodType(addingmethod,emp)
emp.newInstanceMethod()


# In[ ]:





# # class method
#generally any method we create within class are called
 instance methods
#to perform operations on instance variables we create instance method

# To perform operations on class variables we create class method
# we cannot access instance variable using class methods
# we can access class variables using objects & access using class
# class method can be accessed using object & accessed using class
# In[ ]:


class methods not only used for accessing class variables 
but also used to deal with factory methods

# Python Code for Object
# Oriented Concepts without
# using Factory method
 
class FrenchLocalizer:
 
    """ it simply returns the french version """
 
    def __init__(self):
 
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
 
    def localize(self, msg):
 
        """change the message using translations"""
        return self.translations.get(msg, msg)
 
class SpanishLocalizer:
    """it simply returns the spanish version"""
 
    def __init__(self):
 
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
 
    def localize(self, msg):
 
        """change the message using translations"""
        return self.translations.get(msg, msg)
 
class EnglishLocalizer:
    """Simply return the same message"""
 
    def localize(self, msg):
        return msg
 
if __name__ == "__main__":
 
    # main method to call others
    f = FrenchLocalizer()
    e = EnglishLocalizer()
    s = SpanishLocalizer()
 
    # list of strings
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg)# Python Code for factory method
# it comes under the creational
# Design Pattern
 
class FrenchLocalizer:
 
    """ it simply returns the french version """
 
    def __init__(self):
 
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
 
    def localize(self, msg):
 
        """change the message using translations"""
        return self.translations.get(msg, msg)
 
class SpanishLocalizer:
    """it simply returns the spanish version"""
 
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
 
    def localize(self, msg):
 
        """change the message using translations"""
        return self.translations.get(msg, msg)
 
class EnglishLocalizer:
    """Simply return the same message"""
 
    def localize(self, msg):
        return msg
 
def Factory(language ="English"):
 
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
 
    return localizers[language]()
 
if __name__ == "__main__":
 
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")
 
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
# In[ ]:


why to create class method ?
# to perform operations on class level variables or deal with factory methods


# In[25]:


class student:
    college="DR mgr"
    @classmethod
    def classmethod1(cls,new_value):
#         print("class method created succesfully")
        print(cls.college)
        cls.college=new_value
        print(cls.college)
        
student.classmethod1("AAA")
student1=student()
student1.classmethod1("BBB")


# In[27]:


class student:
    college="DR mgr"
    @classmethod
    def classmethod1(cls):
#         print("class method created succesfully")
        print(cls.college)
        del cls.college
        print(cls.college)
        
# student.classmethod1()
student1=student()
student1.classmethod1()


# In[32]:


import datetime
class student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        
        @classmethod
        def getAgeDob(cls,name,id,age):
            return cls(name,id,datetime.datetime.now().year-age)
        
stud=student.getAgeDob('Rakhi',100001,2002)
print(stud.name,stud.id,stud.age)


# # static method

# In[ ]:


# we create a class method to deal with class variables
# & to create alternate constructors

# static methods doesnot perform operations on object & class variables


# In[ ]:


#static method called utility function
# Only do Related general task for which the class is created


# In[34]:


class Calculator:
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
    @staticmethod
    def mul(a,b):
        return a*b
    
    @staticmethod
    def div(a,b):
        return a/b
print(Calculator.add(10,20))
print(Calculator.mul(10,20))
print(Calculator.sub(10,20))
print(Calculator.div(10,20))
        


# # dunder methods
# it is a method has double underscores in front & back it is dunder method# In python every class we created its child to object classif you inherit or doesnot inherit the object class.The object 
class is parent class to class we created
# In[35]:


dir(object)


# In[ ]:


# to overide the built in operations we can use dunder methods

#when we call a class object is created & __init__method will call


# In[1]:


#How to create dunder method
class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,object2):
        print(self.a+object2.a)

obj1=A(10)
obj2=A(20)
obj1+obj2


# In[7]:


class A:
    def __init__(self,a):
        self.a=a
    def __issub__(self,object2):
        print(self.a-object2.a)

obj1=A(10)
obj2=A(20)
obj1-obj2


# In[ ]:





# In[6]:


class A:
    def __init__(self,a):
        self.a=a
    def __len__(self):
        return len(self.a)
    
object1=A([1,2,3,4,5])
print(len(object1))


# In[8]:


class B:
    def __init__(self,a):
        self.a=a
    def __isub__(self,object2):
        self.a-=object2.a
        print(self.a)
obj1=B(10)
obj2=B(20)
obj1-=obj2


# In[9]:


class C:
    print("object deleted successfully")
obj1=C()
del obj1


# In[10]:


class B:
    def __setitem__(self,attr,val):
        print("setitem method called")
a=B()
a['k']=10


# In[ ]:





# In[ ]:





# In[ ]:




