import random
import time
import os

# Set up the console window
CONSOLE_WIDTH = 50
CONSOLE_HEIGHT = 20
os.system('mode con: cols={} lines={}'.format(CONSOLE_WIDTH, CONSOLE_HEIGHT))

# Set up the car
CAR_WIDTH = 5
car_x = CONSOLE_WIDTH // 2 - CAR_WIDTH // 2
car_y = CONSOLE_HEIGHT - 2

# Set up the obstacles
OBSTACLE_WIDTH = 5
OBSTACLE_HEIGHT = 1
obstacles = []
obstacle_speed = 1

# Set up the score
score = 0

# Main game loop
running = True
while running:
    # Move the car
    if kbhit():
        key = getch()
        if key == b'a' and car_x > 0:
            car_x -= 1
        elif key == b'd' and car_x < CONSOLE_WIDTH - CAR_WIDTH:
            car_x += 1
        elif key == b'q':
            running = False

    # Spawn obstacles
    if len(obstacles) < 10:
        obstacle_x = random.randint(0, CONSOLE_WIDTH - OBSTACLE_WIDTH)
        obstacle_y = 0
        obstacles.append((obstacle_x, obstacle_y))

    # Move obstacles
    for i in range(len(obstacles)):
        obstacles[i] = (obstacles[i][0], obstacles[i][1] + obstacle_speed)

    # Remove obstacles that have gone off the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < CONSOLE_HEIGHT]

    # Check for collisions
    car_rect = (car_x, car_y, CAR_WIDTH, 1)
    for obstacle in obstacles:
        obstacle_rect = (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        if rect_overlap(car_rect, obstacle_rect):
            running = False

    # Update score
    score += 1

    # Draw everything
    console = ''
    console += ' ' * car_x + '#' * CAR_WIDTH + ' ' * (CONSOLE_WIDTH - car_x - CAR_WIDTH) + '\n'
    for obstacle in obstacles:
        console += ' ' * obstacle[0] + '=' * OBSTACLE_WIDTH + ' ' * (CONSOLE_WIDTH - obstacle[0] - OBSTACLE_WIDTH) + '\n'
    console += 'Score: {}\n'.format(score)
    print(console)

    time.sleep(0.1)
    os.system('cls')

# Clean up
print('Game over! Your score is {}'.format(score))