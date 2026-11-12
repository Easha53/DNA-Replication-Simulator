
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


fork_x = 4.5
speed = 0.025
playing = True
completed = False

WIDTH = 1000
HEIGHT = 700

ANGLE = 0.0
DNA_RADIUS = 0.65

# Colors
CYAN = (0.0, 0.85, 1.0)
GREEN = (0.1, 1.0, 0.45)
RED = (1.0, 0.25, 0.35)
YELLOW = (1.0, 0.8, 0.1)
PURPLE = (0.7, 0.3, 1.0)




def sphere(x, y, z, radius, color):

    glColor3f(*color)

    glPushMatrix()

    glTranslatef(x, y, z)

    glutSolidSphere(radius, 16, 16)

    glPopMatrix()




def cylinder_between(p1, p2, radius, color):

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]

    length = math.sqrt(dx*dx + dy*dy + dz*dz)

    if length == 0:
        return

    direction = (dx, dy, dz)

    axis = (-dy,dx,0)

    dot = max(-1.0, min(1.0, dz / length))

    angle = math.degrees(math.acos(dot))

    glPushMatrix()

    glTranslatef(*p1)

    if abs(axis[0]) + abs(axis[1]) > 0.00001:
        glRotatef(angle, *axis)
    elif dz < 0:
        glRotatef(180, 1, 0, 0)

    glColor3f(*color)

    quad = gluNewQuadric()

    gluQuadricNormals(quad, GLU_SMOOTH)

    gluCylinder(
        quad,
        radius,
        radius,
        length,
        16,
        4
    )

    gluDeleteQuadric(quad)

    glPopMatrix()




def draw_helix(start, end, center_y,
               color1, color2, phase=0):

    if end <= start:
        return

    step = 0.12

    points1 = []
    points2 = []

    x = start

    while x <= end:

        angle = x * 2.5 + phase

        y1 = center_y + DNA_RADIUS * math.cos(angle)
        z1 = DNA_RADIUS * math.sin(angle)

        y2 = center_y - DNA_RADIUS * math.cos(angle)
        z2 = -DNA_RADIUS * math.sin(angle)

        points1.append((x, y1, z1))
        points2.append((x, y2, z2))

        x += step

   
    for i in range(len(points1) - 1):

        cylinder_between(
            points1[i],
            points1[i+1],
            0.085,
            color1
        )

        cylinder_between(
            points2[i],
            points2[i+1],
            0.085,
            color2
        )

    # Nucleotide base pairs
    for i in range(0, len(points1), 4):

        p1 = points1[i]
        p2 = points2[i]

        # Alternating A-T and G-C
        if (i // 4) % 2 == 0:
            base1 = RED
            base2 = YELLOW
        else:
            base1 = GREEN
            base2 = PURPLE

        # Molecular bond
        cylinder_between(
            p1,
            p2,
            0.035,
            (0.45, 0.45, 0.5)
        )

        # Nucleotide molecules
        sphere(*p1, 0.13, base1)
        sphere(*p2, 0.13, base2)


        x += 0.35

    glLineWidth(1)




def draw_original_dna():

    draw_helix(
        -5.0,
        fork_x,
        0,
        CYAN,
        GREEN
    )



def draw_daughter_dna():

    # Daughter DNA 1
    draw_helix(
        fork_x,
        5.0,
        1.6,
        CYAN,
        RED)

    # Daughter DNA 2
    draw_helix(
        fork_x,
        5.0,
        -1.6,
        GREEN,
        YELLOW)




def draw_helicase():

    sphere(
        fork_x,
        0,
        0,
        0.48,
        PURPLE
    )

    # Inner core
    sphere(
        fork_x,
        0,
        0,
        0.22,
        (0.3, 0.1, 0.55)
    )




def draw_fork():

    glLineWidth(5)

    glColor3f(1, 1, 1)

    glBegin(GL_LINES)

    glVertex3f(fork_x, 0, 0)
    glVertex3f(fork_x, 1.0, 0)

    glVertex3f(fork_x, 0, 0)
    glVertex3f(fork_x, -1.0, 0)

    glEnd()

    glLineWidth(1)


def draw_grid():

    glColor3f(0.08, 0.16, 0.25)

    glLineWidth(1)

    glBegin(GL_LINES)

    for i in range(-5, 6):

        glVertex3f(i, -3, -2)
        glVertex3f(i, -3, 2)

        glVertex3f(-5, -3, i * 0.4)
        glVertex3f(5, -3, i * 0.4)

    glEnd()


def draw_text(x, y, message):

    glRasterPos2f(x, y)

    for char in message:

        glutBitmapCharacter(
            GLUT_BITMAP_HELVETICA_18,
            ord(char)
        )


def draw_ui():

    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    gluOrtho2D(0, WIDTH, 0, HEIGHT)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor3f(0.3, 0.9, 1.0)


    glColor3f(1, 1, 1)

    

    if completed:

        draw_text(400, 80, "REPLICATION COMPLETED!")

    elif not playing:

        draw_text(400, 80, "SIMULATION PAUSED")

    else:

        draw_text(400, 80, "REPLICATION IN PROGRESS")

    glPopMatrix()

    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)


def update(value):

    global fork_x, completed, ANGLE

    if playing and not completed:

        fork_x -= speed

        ANGLE += 0.005

        if fork_x <= -4.5:

            fork_x = -4.5
            completed = True

    glutPostRedisplay()

    glutTimerFunc(30, update, 0)



def keyboard(key, x, y):

    global playing, fork_x
    global completed, speed

    if key == b' ':

        playing = not playing

    elif key in (b'r', b'R'):

        fork_x = 4.5
        playing = True
        completed = False

    elif key in (b'+', b'='):

        speed = min(speed + 0.01, 0.1)

    elif key == b'-':

        speed = max(speed - 0.01, 0.005)

    glutPostRedisplay()


def setup_lighting():
    

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)

    glColorMaterial(
    GL_FRONT_AND_BACK,
    GL_AMBIENT_AND_DIFFUSE
)

    glMaterialfv(
    GL_FRONT_AND_BACK,
    GL_SPECULAR,
    (0.8, 0.8, 0.8, 1)
)

    glMaterialf(
    GL_FRONT_AND_BACK,
    GL_SHININESS,
    80
)

    glLightfv(
        GL_LIGHT0,
        GL_DIFFUSE,
        (1.0, 1.0, 1.0, 1.0)
    )

    glLightfv(
        GL_LIGHT0,
        GL_SPECULAR,
        (1.0, 1.0, 1.0, 1.0)
    )

    glEnable(GL_NORMALIZE)



def showScreen():
    
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT |GL_DEPTH_BUFFER_BIT)

    glViewport(0, 0, WIDTH, HEIGHT)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluPerspective(
        45,
        WIDTH / HEIGHT,
        0.1,
        100
    )

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

    gluLookAt(0, 7, 15,
        0, 0, 0,
        0, 1, 0)

    glEnable(GL_DEPTH_TEST)

    setup_lighting()

    draw_grid()

    glPushMatrix()


    glRotatef(-12, 1, 0, 0)

    draw_original_dna()

    draw_daughter_dna()

    draw_fork()

    draw_helicase()

    glPopMatrix()

    draw_ui()

    glutSwapBuffers()




glutInit()

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

glutInitWindowSize(WIDTH, HEIGHT)

glutInitWindowPosition(100, 50)

glutCreateWindow(b" DNA Replication Simulator")

glutDisplayFunc(showScreen)

glutKeyboardFunc(keyboard)

glutTimerFunc(30, update, 0)

glutMainLoop()
