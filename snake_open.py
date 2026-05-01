from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import random
from math import cos, sin, pi

# ------------------ Window Setup ------------------
window_width = 600
window_height = 600
cell_size = 20
cols = window_width // cell_size
rows = window_height // cell_size

BOUNDARY_THICKNESS = 20  # ✅ Updated boundary thickness

# ------------------ Game State ------------------
snake = [[cols//2, rows//2]]
direction = [0, 0]
food = [random.randint(1, cols-2), random.randint(1, rows-2)]
score = 0
game_started = False
game_paused = False
game_over_state = False
demo_direction = 1
demo_snake_length = 5

# ------------------ Utility ------------------
def reset_game():
    global snake, direction, food, score, game_paused, game_over_state
    snake = [[cols//2, rows//2]]
    direction = [0, 0]
    food = [random.randint(1, cols-2), random.randint(1, rows-2)]
    score = 0
    game_paused = False
    game_over_state = False

# ------------------ Drawing ------------------
def draw_text(x, y, text, color):
    glColor3f(*color)
    glRasterPos2f(x, y)
    for c in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))

def draw_circle(cx, cy, r, g, b, radius=cell_size//2):
    glColor3f(r, g, b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(361):
        angle = i * pi / 180
        glVertex2f(cx + cos(angle)*radius, cy + sin(angle)*radius)
    glEnd()

# ------------------ Display ------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # ===== SOLID BOUNDARY =====
    glColor3f(0.0, 0.3, 0.0)
    t = BOUNDARY_THICKNESS
    glBegin(GL_QUADS)
    # Top
    glVertex2f(0, rows*cell_size-t); glVertex2f(cols*cell_size, rows*cell_size-t)
    glVertex2f(cols*cell_size, rows*cell_size); glVertex2f(0, rows*cell_size)
    # Bottom
    glVertex2f(0, 0); glVertex2f(cols*cell_size, 0)
    glVertex2f(cols*cell_size, t); glVertex2f(0, t)
    # Left
    glVertex2f(0, 0); glVertex2f(t, 0)
    glVertex2f(t, rows*cell_size); glVertex2f(0, rows*cell_size)
    # Right
    glVertex2f(cols*cell_size-t, 0); glVertex2f(cols*cell_size, 0)
    glVertex2f(cols*cell_size, rows*cell_size); glVertex2f(cols*cell_size-t, rows*cell_size)
    glEnd()

    # ===== FOOD =====
    if game_started:
        draw_circle(food[0]*cell_size + cell_size//2,
                    food[1]*cell_size + cell_size//2, 1, 0, 0)

    # ===== SNAKE =====
    for i, s in enumerate(snake):
        x = s[0]*cell_size + cell_size//2
        y = s[1]*cell_size + cell_size//2
        draw_circle(x, y, 1.0, 0.5 if i == 0 else 0.65, 0.2)

    # ===== SCORE =====
    if game_started:
        draw_text(15, rows*cell_size + 12, f"Score: {score}", (0.0, 0.4, 0.0))

    # ===== PAUSE / RESUME BUTTON =====
    btn_w = 100
    btn_h = 35
    btn_x = cols*cell_size - btn_w - 10
    btn_y = rows*cell_size + 7

    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(btn_x, btn_y)
    glVertex2f(btn_x + btn_w, btn_y)
    glVertex2f(btn_x + btn_w, btn_y + btn_h)
    glVertex2f(btn_x, btn_y + btn_h)
    glEnd()

    label = "Resume" if game_paused else "Pause"
    text_x = btn_x + (btn_w - len(label) * 9) / 2
    text_y = btn_y + (btn_h - 18) / 2 + 2
    draw_text(text_x, text_y, label, (1, 1, 1))

    # ===== START BUTTON =====
    if not game_started:
        bw, bh = 160, 50
        bx = cols*cell_size/2 - bw/2
        by = rows*cell_size/2 - bh/2
        glColor3f(0.1, 0.6, 0.3)
        glBegin(GL_QUADS)
        glVertex2f(bx, by); glVertex2f(bx+bw, by)
        glVertex2f(bx+bw, by+bh); glVertex2f(bx, by+bh)
        glEnd()
        draw_text(bx+30, by+18, "START GAME", (1,1,1))

    # ===== GAME OVER =====
    if game_over_state:
        draw_text(cols*cell_size/2 - 90,
                  rows*cell_size/2 + 10,
                  "GAME OVER!", (0.0, 0.4, 0.0))
        draw_text(cols*cell_size/2 - 85,
                  rows*cell_size/2 - 20,
                  f"Final Score: {score}", (0.0, 0.4, 0.0))

    glutSwapBuffers()

# ------------------ Logic ------------------
def update(v):
    global snake, direction, food, score, game_over_state, demo_direction

    if not game_started:
        hx = snake[0][0]
        demo_direction = -1 if hx >= cols-2 else 1 if hx <= 1 else demo_direction
        new_head = [hx + demo_direction, rows//2]
        snake = [new_head]
        for i in range(1, demo_snake_length):
            snake.append([new_head[0]-i*demo_direction, rows//2])

    elif not game_paused and not game_over_state and direction != [0,0]:
        new_head = [snake[0][0]+direction[0], snake[0][1]+direction[1]]
        # Collision check
        if (new_head[0] <= 0 or new_head[0] >= cols-1 or
            new_head[1] <= 0 or new_head[1] >= rows-1 or
            new_head in snake):
            game_over_state = True
        else:
            snake.insert(0, new_head)
            if new_head == food:
                score += 10
                # Regenerate food away from snake
                while True:
                    food = [random.randint(1, cols-2), random.randint(1, rows-2)]
                    if food not in snake:
                        break
            else:
                snake.pop()

    glutPostRedisplay()
    glutTimerFunc(150, update, 0)

# ------------------ Controls ------------------
def key_pressed(key, x, y):
    global game_paused
    if key == b'\x1b':
        sys.exit()
    if key in (b'p', b'P'):
        game_paused = not game_paused
    if key in (b'r', b'R'):
        reset_game()

def special_key_pressed(key, x, y):
    global direction
    if not game_started:
        return
    if key == GLUT_KEY_UP and direction != [0,-1]:
        direction = [0,1]
    elif key == GLUT_KEY_DOWN and direction != [0,1]:
        direction = [0,-1]
    elif key == GLUT_KEY_LEFT and direction != [1,0]:
        direction = [-1,0]
    elif key == GLUT_KEY_RIGHT and direction != [-1,0]:
        direction = [1,0]

def mouse_click(button, state, x, y):
    global game_paused, game_started, direction
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        gl_y = (rows*cell_size + 50) - y
        gl_x = x
        # Pause/Resume button
        if cols*cell_size - 110 <= gl_x <= cols*cell_size - 10 and rows*cell_size + 7 <= gl_y <= rows*cell_size + 42:
            game_paused = not game_paused
        # Start button
        if not game_started:
            bw, bh = 160, 50
            bx = cols*cell_size/2 - bw/2
            by = rows*cell_size/2 - bh/2
            if bx <= gl_x <= bx+bw and by <= gl_y <= by+bh:
                reset_game()
                game_started = True
                direction = [0,0]

# ------------------ Main ------------------
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(cols*cell_size, rows*cell_size + 50)
glutCreateWindow(b"Snake Game OpenGL")

glClearColor(0.8, 1.0, 0.8, 1)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, cols*cell_size, 0, rows*cell_size + 50)

glutDisplayFunc(display)
glutKeyboardFunc(key_pressed)
glutSpecialFunc(special_key_pressed)
glutMouseFunc(mouse_click)
glutTimerFunc(150, update, 0)
glutMainLoop()
