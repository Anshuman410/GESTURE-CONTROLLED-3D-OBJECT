import cv2
import mediapipe as mp
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# ------------------ CUBE DATA ------------------
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

faces = (
    (0, 1, 2, 3),   # Back
    (4, 5, 1, 0),   # Right
    (7, 6, 4, 5),   # Front
    (2, 3, 7, 6),   # Left
    (1, 5, 7, 2),   # Top
    (4, 0, 3, 6)    # Bottom
)

colors = (
    (1, 0, 0),   # Red
    (0, 1, 0),   # Green
    (0, 0, 1),   # Blue
    (1, 1, 0),   # Yellow
    (1, 0, 1),   # Magenta
    (0, 1, 1)    # Cyan
)

def draw_cube():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()


# ------------------ OPENGL SETUP ------------------
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
gluPerspective(45, display[0]/display[1], 0.1, 50)
glTranslatef(0, 0, -6)

# ------------------ HAND TRACKING ------------------
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

rot_x = 0
rot_y = 0
rot_z = 0

# ------------------ MAIN LOOP ------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            cap.release()
            quit()

    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        lm = hand.landmark

        # Palm center (landmark 9)
        cx = lm[9].x
        cy = lm[9].y

        # Thumb & index for Z axis
        x1, y1 = lm[4].x, lm[4].y
        x2, y2 = lm[8].x, lm[8].y

        dist = math.hypot(x2 - x1, y2 - y1)

        # Map hand position to rotation (NO CONTINUOUS)
        rot_y = (cx - 0.5) * 180
        rot_x = (cy - 0.5) * 180
        rot_z = (dist - 0.05) * 300

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glRotatef(rot_x, 1, 0, 0)
    glRotatef(rot_y, 0, 1, 0)
    glRotatef(rot_z, 0, 0, 1)

    draw_cube()

    glPopMatrix()
    pygame.display.flip()
