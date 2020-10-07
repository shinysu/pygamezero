import pgzrun
from random import randint

ball = Actor('ball')
paddle = Actor('paddle')
ball_velocity_x = 5
ball_velocity_y = 5
WHITE = (255, 255, 255)
is_game_over = False
score = 0
missed = False
miss_count = 0
WIDTH = 800
HEIGHT = 600

def draw():
    screen.fill((0, 0, 0))
    ball.draw()
    paddle.draw()
    draw_score()
    draw_game_end()

def update():
    if not missed and not is_game_over:
        move_ball()
        bounce()
        check_paddle_miss()
        detect_paddle_collision()

def move_ball():
    ball.left += ball_velocity_x
    ball.bottom += ball_velocity_y

def on_mouse_move(pos):
    paddle.left = pos[0]
    if paddle.left < 0:
        paddle.left = 0
    elif paddle.right > WIDTH:
        paddle.right = WIDTH

def on_mouse_down():
    global missed
    if missed:
        missed = False
        position_objects()

def on_key_down(key):
    global is_game_over
    if is_game_over and key == keys.SPACE:
        reset()

def bounce():
    global ball_velocity_x, ball_velocity_y
    if ball.right > WIDTH or ball.left < 0:
        ball_velocity_x *= -1
    if ball.top < 0 :
        ball_velocity_y *= -1

def check_paddle_miss():
    global missed, miss_count
    if ball.bottom > paddle.top + abs(ball_velocity_y):
        missed = True
        miss_count = miss_count + 1
        check_game_over()

def detect_paddle_collision():
    global ball_velocity_y, score
    if ball.colliderect(paddle):
        score += 1
        ball_velocity_y *= -1

def draw_game_end():
    global is_game_over
    if is_game_over:
       screen.draw.text("GAME OVER !!", (WIDTH/2, 10), fontsize=30, color=WHITE)
       screen.draw.text("Press SPACE key to start a new game", (WIDTH / 2 - 50, 30), fontsize=25, color=WHITE)
    elif missed:
        screen.draw.text("Missed it! Click to continue", (WIDTH / 3, 30), fontsize=30, color=WHITE)

def check_game_over():
    global is_game_over, miss_count
    if miss_count >= 5:
        is_game_over = True

def reset():
    global score, miss_count, missed, is_game_over
    score = 0
    miss_count = 0
    missed = False
    is_game_over = False
    position_objects()

def position_objects():
    ball.x = randint(100, WIDTH-100)
    ball.y = 100
    paddle.pos = 100, 580

def draw_score():
    screen.draw.text("Score: " + str(score), (10, 10), fontsize=25, color=WHITE)
    screen.draw.text("Miss: " + str(miss_count), (10, 30), fontsize=25, color=WHITE)

position_objects()
pgzrun.go()
