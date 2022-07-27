class Block:
    def __init__(self, variant, rotation, color, x, y):
        self.set_variant(variant)
        self.set_rotation(rotation)
        self.set_color(color)
        self.set_x(x)
        self.set_y(y)

    def __del__(self):
        pass

    def get_variant(self):
        return self.__variant

    def get_rotation(self):
        return self.__rotation

    def get_color(self):
        return self.__color

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_variant(self, variant):
        if(type(variant) is int):
            if(variant >= 1 and variant <= 7):
                self.__variant = variant

    def set_rotation(self, rotation):
        if(type(rotation) is int):
            if(rotation >= 1 and rotation <= 4):
                self.__rotation = rotation

    def set_color(self, color):
        if(type(color) is int):
            if(color >= 1 and color <= 6):
                self.__color = color

    def set_x(self, x):
        if(type(x) is int):
            self.__x = x

    def set_y(self, y):
        if(type(y) is int):
            self.__y = y

    def rotate(self):
        pass