class Controls:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def on_key_press_out(self, block, nextblock, game, interface):
        def on_key_press_in(key):
            key = key.name
            if key == "w" or key == "up":
                if(block.rotate(game.get_field())):
                    interface.render(game, block.get_coords(), block.get_color())
            elif key == "a" or key == "left":
                if(block.move_left(game.get_field())):
                    interface.render(game, block.get_coords(), block.get_color())
            elif key == "s" or key == "down":
                if(block.fall(game.get_field())):
                    interface.render(game, block.get_coords(), block.get_color())
            elif key == "d" or key == "right":
                if(block.move_right(game.get_field())):
                    interface.render(game, block.get_coords(), block.get_color())
            elif key == "space":
                if(block.max_fall(game.get_field())):
                    interface.render(game, block.get_coords(), block.get_color())
        return on_key_press_in