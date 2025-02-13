import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Тест")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)


class Hero:
    def __init__(self, race, job, weapon):
        self.race = race
        self.job = job
        self.weapon = weapon

def main_loop():
    is_running = True
    race = "Гуманоид"
    job = "Охотник"
    weapon = "Монтировка"
    hero = Hero(race, job, weapon)

    while is_running:
        window.fill(WHITE)

        text = font.render(f"Раса: {race}, Работа: {job}, Оружие: {weapon}", True, BLACK)
        window.blit(text, (50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    race = "Elf"
                elif event.key == pygame.K_p:
                    job = "Mage"
                elif event.key == pygame.K_w:
                    weapon = "Bow"
                hero = Hero(race, job, weapon)
        pygame.display.flip()



    pygame.quit()




if __name__ == "__main__":
    main_loop()
