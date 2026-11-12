from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*


def showScreen():
    
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)

    glViewport(0, 0, 1000, 1000)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

  

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    

    glutSwapBuffers()




glutInit()

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

glutInitWindowSize(1000, 1000)

glutInitWindowPosition(100, 50)

glutCreateWindow(b" DNA Replication Simulator")

glutDisplayFunc(showScreen)

glutMainLoop()
