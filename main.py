import pygame
import constants
import player as player_obj

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    clock =  pygame.time.Clock()
    
    #dt = 0

    print(f"""Starting Asteroids!
Screen width: {constants.SCREEN_WIDTH}
Screen height: {constants.SCREEN_HEIGHT}"""
            )
    
    player = player_obj.Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
     
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        screen.fill(000000)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

    
