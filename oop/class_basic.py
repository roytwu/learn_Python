"""
File name:   class_basic.py
Date:        Feb 22 2019
Author:      wur
Description: basic concepts about Python class
"""
#* -----clss sample #1-----
class ClassToto:
  i = 12345  #* class attribute, shared by all instances
  
  def func_hello(self):
    return 'hello world!' 

#* create a new instance of the class and assigns this object to the local variable foo    
o_foo = ClassToto()
o_foo.counter = 1

while o_foo.counter < 10:
  o_foo.counter = o_foo.counter*2

print('Shall print out 16...')
print(o_foo.counter)
del o_foo.counter #* delete counter  


print('\n--- Hello function in Class example #1 ---')
print(o_foo.func_hello())


result1=type(ClassToto.func_hello)
result2=type(o_foo.func_hello)
print('Type of "Class.method" is.. ', result1)
print('Type of "object.method" is.. ', result2)
print('\n')
"""
A method is a function that belongs to an object!
"""


bar = o_foo.func_hello #* create a method object
i = 0
while True: 
    print(bar())
    i=i+1
    
    if i == 9:
        break
    
#* -----clss sample #2----- 
print('\n----- class example #2 -----')        
class Dog:
    m_kind = 'canine' #* variable shared by all instances
    
    def __init__(self, name):
        self.m_name = name #* variable unique to each instance 
        self.m_tricks = []
        
    def add_trick(self, trick):
        self.m_tricks.append(trick)

o_fido = Dog('Fido')
o_buddy = Dog('Buddy')
print(o_fido.m_kind)
print(o_fido.m_name)

o_buddy.add_trick('roll over')
print(o_buddy.m_tricks)






    