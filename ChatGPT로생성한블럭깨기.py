import pygame
import random

# 게임 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 패들 설정
paddle_width = 400
paddle_height = 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 50
paddle_speed = 10

# 공 설정
ball_size = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = -4

# 블록 설정
block_rows = 5
block_cols = 8
block_width = WIDTH // block_cols
block_height = 30
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        blocks.append(pygame.Rect(col * block_width, row * block_height, block_width, block_height))

# 게임 루프
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed
    
    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # 벽과 충돌
    if ball_x <= 0 or ball_x >= WIDTH - ball_size:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1
    
    # 패들과 충돌
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle_rect.colliderect((ball_x, ball_y, ball_size, ball_size)):
        ball_speed_y *= -1
    
    # 블록과 충돌
    ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
    for block in blocks[:]:
        if block.colliderect(ball_rect):
            blocks.remove(block)
            ball_speed_y *= -1
            break
    
    # 게임 오버 조건
    if ball_y > HEIGHT:
        running = False
    
    # 화면 그리기
    pygame.draw.rect(screen, WHITE, paddle_rect)
    pygame.draw.ellipse(screen, RED, ball_rect)
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
