"""
File name:   class_basic.py
Date:        Feb 22 2019
Author:      wur
Description: basic concepts about Python class
"""
#* -----clss sample #1-----
class ClassRoy:
  #* A sample example class
  i = 12345
  
  def hello(self):
    return 'hello world!' 

#* create a new instance of the class and assigns this object to the local variable foo    
foo = ClassRoy()
foo.counter = 1

while foo.counter < 10:
  foo.counter = foo.counter*2

print('Shall print out 16...')
print(foo.counter)
del foo.counter #* delete counter  


print('\n')
print(foo.hello())

bar = foo.hello #* create a method object
i = 0
while True: 
    print(bar())
    i=i+1
    
    if i == 9:
        break
    
#* -----clss sample #2----- 
print('\n')        
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






    