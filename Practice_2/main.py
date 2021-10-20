import sys
from typing import Type

import pygame
from pygame.transform import scale

from buttons.button import Button
from buttons.input_box import InputBox
from image_button import ImageButton

login: Type[InputBox] = InputBox

window = (1150, 1050)
screen = pygame.display.set_mode(window)
pygame.font.init()
clock = pygame.time.Clock()


BG_COLOR = (30, 30, 30)
BLACK_COLOR = (0, 0, 0)


class Blank:

    def __init__(self):
        self.width = 600
        self.height = 600

        self.setup_screen()

        self.click = False
        self.running = True

        self.button = Button(self.screen, self.width // 2 - 100, self.height // 2 - 25, 200, 50, "esc to go back", (BLACK_COLOR))
        self.start = ImageButton(self.screen, self.width, self.height, image_path, scale)


        self.clock = pygame.time.Clock()

    def start(self):
        cats = ImageButton(screen, 200, 250, "assets/cats.png", 1)
        esc = Button(screen, 50, 40, 800, 600, "esc to go back", (BLACK_COLOR))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if esc.collides(pygame.mouse.get_pos()):
                        pygame.quit()
                    elif cats.collides(pygame.mouse.get_pos()):
                        login.draw()
            pygame.display.update()
        pygame.quit()



    def draw(self):
        self.screen.fill(BG_COLOR)
        # screen.fill always in beginning of draw func

        #self.button.draw()
        #self.start.draw()

        # display.update() always in end of draw func
        pygame.display.update()
        #####

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Blank Template Screen")

    def run(self):
        while self.running:
            pos = pygame.mouse.get_pos()
            print(pos)
            self.draw()
            if self.start.collides(pos):
                if self.click:
                    print("BUTTON CLICKED")

            self.click = False
            for event in pygame.event.get():
                self.handle_event(event)

            self.clock.tick(60)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.click = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

cats = ImageButton(screen, 200, 250, "assets/cats.png", 1)

pygame.display.flip()
done = False
while not done:
    cats.draw()
    go = Blank()
    go.start()
pygame.display.update()
clock.tick(60)

