# learn_Python
This is a repo about Python programming. 

💾 Projects
------------
## _plot
Extracting data from a text file and then making plot for analysis utilizing `matplotlib`

## attitude 
Operations about SO(3) utilizing the following custom modules:  
- **SO3.py** - attitude represntation and transformation
  - `Rx()`, `Ry()`, `Rz()`: rotation along *x*, *y* and *z* axis in SO(3).
  - `hat()`: Hat map, it transfers a 3x1 vector to a 3x3 skew-symmetric matrix, which is very useful in describing rotational motion
  - `vee()`: Vee map: inverse of hat map
  - `glRotate()`: mimicing `glRotate()` function in OpenGL
  - `rodriguesToSO3()`: converting Rodrigues formula to rotation matrix
  - `unitQuatToSO3()`: converting unit quaternion to rotation matrix
  - `SO3ToUnitQuat()`: mapping rotation matrix to unit quaternion
- **S3.py** 
  - `multiplication()`: multiplication of 2 quaternions

## OOP
Object-orientated programming in Python

## opengl
Following [tutorial](https://bit.ly/2ENkI1Q) to learn about baisc OpenGL in Python. 


## sympy
Symbolic matrix operations, including matrix transpose, inverse, determinant, and multiplication.


## palindrome
Tell if a word is a palindrome

## pySerial
basic commands about pySerial


🎮 Deployment
--------------
Code in this repos is devloped and tested under Python 3.7.1 with Anaconda3 (4.5.12) 


🤖 Developer
------
Roy T Wu
