import keyboard
from time import sleep
from random import randint
from classes.block import Block
from classes.controls import Controls
from classes.game import Game
from classes.interface import Interface

def main():
    controls = Controls()
    interface = Interface()
    game = Game(10, 20)
    nextblock = Block(randint(1, 7), 1, randint(1, 6), 4, 0)
    block = Block(randint(1, 7), 1, randint(1, 6), 4, 0)
    keyboard.on_press(controls.on_key_press_out(block, nextblock, game, interface))
    interface.render(game, block.get_coords(), block.get_color())
    running = True
    while running:
        sleep(game.fall_time())
        if not block.fall(game.get_field()):
            game.solidify_block(block.get_coords(), block.get_color())
            interface.render(game, block.get_coords(), block.get_color())
            if game.add_score(game.remove_rows()):
                interface.render(game, block.get_coords(), block.get_color())
            del block
            block = nextblock
            if not game.check_running(block.get_coords()):
                running = False
            keyboard.on_press(controls.on_key_press_out(block, nextblock, game, interface))
            del nextblock
            nextblock = Block(randint(1, 7), 1, randint(1, 6), 4, 0)
        interface.render(game, block.get_coords(), block.get_color())

if __name__ == "__main__":
    main()