class Nextblock:
    def __init__(self, variant, rotation, color):
        self.set_variant(variant)
        self.set_rotation(rotation)
        self.set_color(color)

    def __del__(self):
        pass

    def get_variant(self):
        return self.__variant

    def get_rotation(self):
        return self.__rotation

    def get_color(self):
        return self.__color

    def set_variant(self, variant):
        self.__variant = variant

    def set_rotation(self, rotation):
        self.__rotation = rotation

    def set_color(self, color):
        self.__color = color