"""
Created on:  Tue Mar  5 14:31:36 2019
Developer:   wur
File Name:   opengl_basic.py
Description: First steps about OpenGL with Python
Reference:   https://bit.ly/2ENkI1Q
"""
import pygame
from pygame.locals import * #* constains various constants used by pygame
from OpenGL.GL import *     #* contains standard OpenGL functions
from OpenGL.GLU import *    #* OpenGL Utility Library (GLU)

#* 8 nodes of the cuboid
vertices= (
    ( 1.0, -1.2, -1.0),  #* lower right back
    ( 1.0,  1.2, -1.0),  #* upper right back
    (-1.0,  1.2, -1.0),  #* upper left back
    (-1.0, -1.2, -1.0),  #* lower left back
    ( 1.0, -1.2,  1.0),  #* lower right front
    ( 1.0,  1.2,  1.0),  #* upper right fromt
    (-1.0,  1.2,  1.0),  #* upper left front 
    (-1.0, -1.2,  1.0)   #* kiwer left front
)

#* 12 edges of the cuboid
edges = (    
    (0,1), (0,3), (0,4),
    (2,1), (2,3), (2,6),
    (7,3), (7,4), (7,6),
    (5,1), (5,4), (5,6)
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()