"""
Developer:   Roy TWu
File Name:   SO3.py
Description: Custom module about attitude representation and transformation
             This module aslo consists useful tools such as hat and vee map
"""
import sympy
from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy          import asin, acos, atan, atan2
from sympy.matrices import Matrix
#from sympy.printing import pprint
#from sympy          import simplify as simp

eye3 = Matrix([ [1,0,0], [0, 1, 0], [0, 0, 1] ])

#* ----- hat map -----
def hat(tup_v):
    v1 = tup_v[0]   #* axis-x
    v2 = tup_v[1]   #* axis-y
    v3 = tup_v[2]   #* axis-z
    hatMap = Matrix([ [0,-v3, v2], [v3, 0, -v1], [-v2, v1, 0] ])   
    return hatMap 


#* ----- vee map -----
def vee(skewMatx):
    v1 = skewMatx[2, 1] #*accessing matrix element
    v2 = skewMatx[0, 2]
    v3 = skewMatx[1, 0]
    return (v1, v2, v3)


#* ----- trace -----
def trace(Matx):  
   result = Matx[0,0] + Matx[1,1] + Matx[2,2] 
   return result


#* ----- basic rotations of SO(3) -----
#G^R_B along x axis
def Rx(th):  
    rx = Matrix([ [1,0,0], 
                  [0, cos(th), -sin(th)], 
                  [0, sin(th), cos(th)] ])
    return rx

#G^R_B along y axis
def Ry(phi):
    ry = Matrix([ [cos(phi), 0, sin(phi)], 
                  [0,1,0], 
                  [-sin(phi), 0, cos(phi)] ])
    return ry

#G^R_B along z axis
def Rz(psi):
    rz = Matrix([ [cos(psi), -sin(psi), 0], 
                  [sin(psi), cos(psi), 0], 
                  [0,0,1] ])
    return rz


#* ----- glRotate in OpenGL -----
#* glRotate definition: 
#* https://www.cs.sfu.ca/~haoz/teaching/htmlman/rotate.html
def glRotateToSO3(ang, tup_v3):
    a1 = tup_v3[0]  #* axis-x
    a2 = tup_v3[1]  #* axis-y
    a3 = tup_v3[2]  #* axis-z
    foo = (1-cos(ang))
    rotate = Matrix([ 
         [a1*a1*foo+cos(ang), a1*a2*foo-a3*sin(ang), a1*a3*foo+a2*sin(ang)], 
         [a1*a2*foo+a3*sin(ang), a2*a2*foo+cos(ang), a2*a3*foo-a1*sin(ang)], 
         [a1*a3*foo-a2*sin(ang), a2*a3*foo+a1*sin(ang), a3*a3*foo+cos(ang)] 
         ])
    return rotate


#* ----- Rodrigues formula -----
def rodriguesToSO3(angle, tup_v3):
    v3_hat = hat(tup_v3)
    rod = eye3 + sin(angle)*v3_hat + (1-cos(angle))*v3_hat*v3_hat
    return rod
    

#* ----- Unit Quaternion ----- 
def unitQuatToSO3(uQuat):
    q0 = uQuat[0]
    tup_q = (uQuat[1], uQuat[2], uQuat[3])
    
    q_hat = hat(tup_q)
    rot = eye3 + 2*q_hat*q_hat +2*q0*q_hat
    return rot
    
    
def SO3ToUnitQuat(Matx):
    tr =trace(Matx)
    q0 = ( sympy.sqrt(tr+1) )/2
    q1 = vee(Matx -Matx.T)[0]/(4*q0)
    q2 = vee(Matx -Matx.T)[1]/(4*q0)
    q3 = vee(Matx -Matx.T)[2]/(4*q0)
    quat = (q0, q1, q2, q3)
    return quat    
    