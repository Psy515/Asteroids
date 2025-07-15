import pygame
import constants
import player as player_obj
import asteroid as asteroid_obj
import asteroidfield as asteroidfield_obj
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    clock =  pygame.time.Clock()
    
    dt = 0

    print(f"""Starting Asteroids!
Screen width: {constants.SCREEN_WIDTH}
Screen height: {constants.SCREEN_HEIGHT}"""
            )
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    asteroidfield_obj.AsteroidField.containers = (updatable,)
    player_obj.Player.containers = (updatable, drawable)
    player_obj.Shot.containers = (updatable, drawable, shot)
    asteroid_obj.Asteroid.containers = (updatable, drawable, asteroids)
    player = player_obj.Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
    asteroidfield = asteroidfield_obj.AsteroidField()
    




    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print(f"Game over!")
                sys.exit()
            for s in shot:
                if s.collision(asteroid):
                    asteroid.split()
                    s.kill()
                    break
        
        for sprite in drawable:
            sprite.draw(screen)        
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

    
