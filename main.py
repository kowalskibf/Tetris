import keyboard
from time import sleep
from random import randint
from classes.block import Block
from classes.game import Game
from classes.interface import Interface
from classes.nextblock import Nextblock

def main():
    interface = Interface()
    game = Game(10, 20)
    nextblock = Nextblock(randint(1, 7), 1, randint(1, 6))
    block = Block(randint(1, 7), 1, randint(1, 6), 4, 0)
    interface.render(game.get_field(), block.get_coords(), block.get_color())
    running = True
    while running:
        if(block.fall(game.get_field())):
            interface.render(game.get_field(), block.get_coords(), block.get_color())
        sleep(1)

if __name__ == "__main__":
    main()