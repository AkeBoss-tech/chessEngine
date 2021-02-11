from Board import game
from Utilities import *
from Screen import screen

import pygame
import sys
import os
print("\n\n\n\n\tSystem Start")

def main():
    pygame.init()
    window = screen()
    board = game()
    runGame(board, window)

if __name__ == "__main__":
    main()
