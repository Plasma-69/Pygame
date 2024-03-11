import pygame 
import time
import random
pygame.font.init()
  
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption('Space invaders') 
bg = pygame.transform.scale(pygame.image.load('BG.jpg'), (WIDTH, HEIGHT))
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 50
PLAYER_VEL = 5
start_time = time.time()
elasped_time = 0
FONT = pygame.font.SysFont('comicsans', 30)
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3
def draw(player, elasped_time, stars):
    WIN.blit(bg , (0,0))
    time_text = FONT.render(f"Time: {round(elasped_time)}s", 1, "white")
    WIN.blit(time_text, (10,10))
    
    pygame.draw.rect(WIN, "red", player)
    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()

    
def main():
    run = True
    clock = pygame.time.Clock()
    star_add_increment = 2000
    star_count = 0

    stars = []

    

    player = pygame.Rect(200 , HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    elasped_time = time.time() - start_time
    hit = False

    while run:
        star_count += clock.tick(60)
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
        for event in pygame.event.get():     
            if event.type == pygame.QUIT: 
                run = False
                break
            draw(player, elasped_time, stars)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL 
        if key[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL       

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break 
            if hit:
                lost_text = FONT.render("You lost!" , 1, "white")
                WIN.blit(lost_text, (WIDTH/2- lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))    
                pygame.display.update()
                pygame.time.delay(4000)     
                break  
    pygame.quit()        

if __name__ == "__main__":
    main()        