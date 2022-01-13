"""
Main entry point for your game!
"""

import pygame
from pyggui import Game

# Main game object
game = Game(
    display_size=[1280, 720]
)


if __name__ == "__main__":
    game.run()  # Run game
