"""
Created on:  Tue Mar  5 14:31:36 2019
Developer:   Roy TWu
File Name:   opengl_basic.py
Description: First steps about OpenGL with Python,
             creating a cuboid and rotate it
Reference:   https://bit.ly/2ENkI1Q
"""
import pygame
from pygame.locals import * #* constains various constants used by pygame
from OpenGL.GL import *     #* contains standard OpenGL functions
from OpenGL.GLU import *    #* OpenGL Utility Library (GLU)

#* 8 nodes of the cuboid, tuple of tuples (nested tuples)
vertices= (
    ( 1.0, -1.2, -0.5),  #* lower right back
    ( 1.0,  1.2, -0.5),  #* upper right back
    (-1.0,  1.2, -0.5),  #* upper left back
    (-1.0, -1.2, -0.5),  #* lower left back
    ( 1.0, -1.2,  0.5),  #* lower right front
    ( 1.0,  1.2,  0.5),  #* upper right fromt
    (-1.0,  1.2,  0.5),  #* upper left front 
    (-1.0, -1.2,  0.5)   #* lower left front
)

#* 12 edges of the cuboid
#* each tuple contains 2 numbers, each number corresponds to a vertex
#* edge is drawn between these 2 vertices
edges = (    
    (0,1), (0,3), (0,4),
    (2,1), (2,3), (2,6),
    (7,3), (7,4), (7,6),
    (5,1), (5,4), (5,6)
)


def Cuboid_draw():
    glBegin(GL_LINES)
    for edge in edges:
        for node in edge:
            glVertex3fv(vertices[node])
    glEnd()
    
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #* parameter: (filed of view, aspect ratio, znear, zfar)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    #* translation
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        glRotatef(1.0, 3, 1, 1)
        #glRotatef(1.5, 1, 0, 0)
        
        #* clear buffers to preset value
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        Cuboid_draw()
        
        pygame.display.flip() #* update entire display
        pygame.time.wait(20)  #* millisconds


main()