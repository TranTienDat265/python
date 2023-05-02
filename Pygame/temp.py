# https://youtu.be/WagJ-OjRtCM
# https://codelearn.io/sharing/lap-trinh-game-co-ban-voi-pygame
# https://codelearn.io/sharing/lap-trinh-game-co-ban-voi-pygame
import pygame

# Fuction xét con trỏ chuột có nằm trong một khoảng hay không
def isIn(x,y,xA,xB,yA,yB):
    return x>=xA and x<=xB and y>=yA and y<=yB

def Positioning():
    # Get Position của mouse
    mouse_x , mouse_y = pygame.mouse.get_pos()

    # Nếu trong hình chữ nhật thì hiện chữ đỏ
    if isIn(mouse_x,mouse_y,225,225+50,150,150+275) == False:
        # Hiển thị tọa độ của con trỏ
        pos = str(mouse_x) + "," + str(mouse_y)
        text_pos = font.render(pos,True, BLACK)
        screen.blit(text_pos,(mouse_x+10,mouse_y+10))

        # Vẽ các line để xác định vị trị tọa độ của con trỏ
        pygame.draw.line(screen, BLACK, (mouse_x, mouse_y), (mouse_x,600), 1)
        pygame.draw.line(screen, BLACK, (mouse_x, mouse_y), (mouse_x,1), 1)
        pygame.draw.line(screen, BLACK, (mouse_x, mouse_y), (1,mouse_y), 1)
        pygame.draw.line(screen, BLACK, (mouse_x, mouse_y), (500,mouse_y), 1)
    else:
        # Hiển thị tọa độ của con trỏ
        pos = str(mouse_x) + "," + str(mouse_y)
        text_pos = font.render(pos,True, RED)
        screen.blit(text_pos,(mouse_x+10,mouse_y+10))

        # Vẽ các line để xác định vị trị tọa độ của con trỏ
        pygame.draw.line(screen, RED, (mouse_x, mouse_y), (mouse_x,600), 1)
        pygame.draw.line(screen, RED, (mouse_x, mouse_y), (mouse_x,1), 1)
        pygame.draw.line(screen, RED, (mouse_x, mouse_y), (1,mouse_y), 1)
        pygame.draw.line(screen, RED, (mouse_x, mouse_y), (500,mouse_y), 1)

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
BROWN = (139,  69,  19)

font = pygame.font.SysFont('monospace', 25)

running = True

text_1 = font.render('Hello', True, BLACK)
pos = ""
text_pos = font.render(pos, True, BLACK)

while running: 
    # Fill color của Screen
    screen.fill(GREY)

    pygame.draw.rect(screen, WHITE, (225,150,50,275)) # Thân chim
    pygame.draw.rect(screen, BROWN, (155,425,70,70)) # Bi trái
    pygame.draw.rect(screen, BROWN, (275,425,70,70)) # Bi phải
    pygame.draw.rect(screen, BROWN, (225,150,50,50)) # Buoi
    pygame.draw.line(screen, BLACK, (250,150) , (250,199)) # Phân cách 2 buoi

    screen.blit(text_1,(50,50))

    for event in pygame.event.get():
        # pass
        if event.type == pygame.QUIT:
            running = False

    Positioning()
    
    # Cần flip để tất cả mọi thứ vẽ trên màn hình có hiệu lực
    pygame.display.flip()

# Khi chạy xong chương trình sẽ xóa mọi thứ mà chương trình sử 
# dụng, làm giảm dung lượng bộ nhớ --> Không làm nặng máy
pygame.quit()