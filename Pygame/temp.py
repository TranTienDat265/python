# https://youtu.be/WagJ-OjRtCM
# https://codelearn.io/sharing/lap-trinh-game-co-ban-voi-pygame
# https://codelearn.io/sharing/lap-trinh-game-co-ban-voi-pygame
import pygame

# Khởi tạo những thứ mà pygame có thể dùng được
pygame.init()

# Set độ lớn của Screen (width, height)
screen = pygame.display.set_mode((500,600))

# Set màu RGB của Screen
GREY  = (150, 150, 150)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

font = pygame.font.SysFont('monospace', 50)

running = True

text_1 = font.render('Hello', True, BLACK)

while running: 
    # Fill color của Screen
    screen.fill(GREY)

    pygame.draw.rect(screen, WHITE, (50,50,100,50))
    screen.blit(text_1,(50,50))

    for event in pygame.event.get():
        # pass
        if event.type == pygame.QUIT:
            running = False
    # Cần flip để tất cả mọi thứ vẽ trên màn hình có hiệu lực
    pygame.display.flip()

# Khi chạy xong chương trình sẽ xóa mọi thứ mà chương trình sử 
# dụng, làm giảm dung lượng bộ nhớ --> Không làm nặng máy
pygame.quit()