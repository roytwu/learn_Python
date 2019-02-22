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
    
foo = ClassRoy
foo.counter = 1

while foo.counter < 10:
  foo.counter = foo.counter*2

print('Shall print out 16...')
print(foo.counter)
del foo.counter  

