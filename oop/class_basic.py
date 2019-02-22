"""
File name:   class_basic.py
Date:        Feb 22 2019
Author:      wur
Description: basic concepts about Python class
"""

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


bar = foo.hello
i = 0
while True: 
    print(bar())
    i=i+1
    
    if i == 9:
        break