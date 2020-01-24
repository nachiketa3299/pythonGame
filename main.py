import pygame
import random

###  파이게임 초기화 하고 시작
# 이걸 안 쓰면 일부 모듈은 작동하지 않는다.
# 이 함수는 또한 모든 초기화 성공 및 실패의 튜플 반환.
successes, failures = pygame.init()
print("게임을 초기화 하는 중입니다: {0} successes and {1} failures." .format(successes, failures))


# 전역 변수 설정
WIDTH   = 360
HEIGHT  = 480
FPS     = 30 # This variable will define how many frames we update per second


WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
RED     = (255,   0,   0)
GREEN   = (  0, 255,   0)
BLUE    = (  0,   0, 255)


### 필수품 만들기
## 디스플레이 만들기
# 파이게임은 이미 숨겨진 디스플레이를 만들었고 모드만 설정하면 됨.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jaemin's Game")

## 시계 만들기
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect() # Get rect of some size as 'image'
        self.velocity = [0, 0]
    
    def update(self):
        self.rect.move_ip(*self.velocity)


player = Player()
running = True

while running:
    dt = clock.tick(FPS) / 1000 # Returns milliseconds between each call to tick.
    screen.fill(BLACK) # Fill the screen with background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.velocity[1] = -200 * dt
            elif event.key == pygame.K_s:
                player.velocity[1] = 200 * dt
            elif event.key == pygame.K_a:
                player.velocity[0] = -200 * dt
            elif event.key == pygame.K_d:
                player.velocity[0] = 200 * dt

    pygame.draw.circle(screen, WHITE, (20, 20), 4, 4)

    player.update()

    screen.blit(player.image, player.rect)
    pygame.display.update()

print("게임 루프를 빠져나왔습니다. 게임을 종료합니다...")
quit()
