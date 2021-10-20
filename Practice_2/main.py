import pygame, os
pygame.init()
# init pygame before importing other dependencies

from screens.blank_screen import Blank

def main():
    main_screen = Blank()
    main_screen.run()

if __name__ == "__main__":
    main()
