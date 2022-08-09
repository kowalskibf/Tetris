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

    def get_coords(self):
        if self.__variant == 1: # I
            if self.__rotation == 1:
                return [(self.__x - 1, self.__y), (self.__x, self.__y), (self.__x + 1, self.__y), (self.__x + 2, self.__y)]
            elif self.__rotation == 2:
                return [(self.__x, self.__y - 1), (self.__x, self.__y), (self.__x, self.__y + 1), (self.__x, self.__y + 2)]
        elif self.__variant == 2: # Sq
            return [(self.__x, self.__y), (self.__x + 1, self.__y), (self.__x, self.__y + 1), (self.__x + 1, self.__y + 1)]
        elif self.__variant == 3: # T
            if self.__rotation == 1:
                return [(self.__x - 1, self.__y), (self.__x, self.__y), (self.__x + 1, self.__y), (self.__x, self.__y + 1)]
            elif self.__rotation == 2:
                return [(self.__x, self.__y - 1), (self.__x - 1, self.__y), (self.__x, self.__y), (self.__x, self.__y + 1)]
            elif self.__rotation == 3:
                return [(self.__x, self.__y - 1), (self.__x - 1, self.__y), (self.__x, self.__y), (self.__x + 1, self.__y)]
            elif self.__rotation == 4:
                return [(self.__x, self.__y - 1), (self.__x, self.__y), (self.__x + 1, self.__y), (self.__x, self.__y + 1)]
        elif self.__variant == 4: # S
            if self.__rotation == 1:
                return [(self.__x, self.__y), (self.__x + 1, self.__y), (self.__x - 1, self.__y + 1), (self.__x, self.__y + 1)]
            elif self.__rotation == 2:
                return [(self.__x - 1, self.__y - 1), (self.__x - 1, self.__y), (self.__x, self.__y), (self.__x, self.__y + 1)]
        elif self.__variant == 5: # Z
            if self.__rotation == 1:
                return [(self.__x - 1, self.__y), (self.__x, self.__y), (self.__x, self.__y + 1), (self.__x + 1, self.__y + 1)]
            elif self.__rotation == 2:
                return [(self.__x, self.__y - 1), (self.__x - 1, self.__y), (self.__x, self.__y), (self.__x - 1, self.__y + 1)]
        elif self.__variant == 6: # J
            if self.__rotation == 1:
                return [(self.__x - 1, self.__y), (self.__x, self.__y), (self.__x + 1, self.__y), (self.__x + 1, self.__y + 1)]
            elif self.__rotation == 2:
                return [(self.__x, self.__y - 1), (self.__x, self.__y), (self.__x - 1, self.__y + 1), (self.__x, self.__y + 1)]
            elif self.__rotation == 3:
                return [(self.__x - 1, self.__y - 1), (self.__x - 1, self.__y), (self.__x, self.__y), (self.__x + 1, self.__y)]
            elif self.__rotation == 4:
                return [(self.__x, self.__y - 1), (self.__x + 1, self.__y - 1), (self.__x, self.__y), (self.__x, self.__y + 1)]
        elif self.__variant == 7: # L
            if self.__rotation == 1:
                return [(self.__x - 1, self.__y), (self.__x, self.__y), (self.__x + 1, self.__y), (self.__x + 1, self.__y + 1)]
            elif self.__rotation == 2:
                return [(self.__x - 1, self.__y - 1), (self.__x, self.__y - 1), (self.__x, self.__y), (self.__x, self.__y + 1)]
            elif self.__rotation == 3:
                return [(self.__x + 1, self.__y - 1), (self.__x - 1, self.__y), (self.__x, self.__y), (self.__x + 1, self.__y)]
            elif self.__rotation == 4:
                return [(self.__x, self.__y - 1), (self.__x, self.__y), (self.__x, self.__y + 1), (self.__x + 1, self.__y + 1)]

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

    def increment_rotation(self):
        two_rotations = [1, 4, 5]
        four_rotations = [3, 6, 7]
        if self.__variant in two_rotations:
            if self.__variant == 1:
                self.__rotation = 2
            else:
                self.__rotation = 1
        elif self.__variant in four_rotations:
            if self.__variant <= 3:
                self.__rotation += 1
            else:
                self.__rotation = 1

    def decrement_rotation(self):
        two_rotations = [1, 4, 5]
        four_rotations = [3, 6, 7]
        if self.__variant in two_rotations:
            if self.__variant == 2:
                self.__rotation = 1
            else:
                self.__rotation = 2
        elif self.__variant in four_rotations:
            if self.__variant >= 2:
                self.__rotation -= 1
            else:
                self.__rotation = 4

    def is_able_to_rotate(self, field):
        two_rotations = [1, 4, 5]
        four_rotations = [3, 6, 7]
        if self.__variant in two_rotations or self.__variant in four_rotations:
            self.increment_rotation()
            for coord in self.get_coords():
                if coord[1] < 0 or coord[1] >= len(field) or coord[0] < 0 or coord[0] >= len(field[0]) or field[coord[1]][coord[0]] != 0:
                    self.decrement_rotation()
                    return False
            self.decrement_rotation()
            return True
        return False

    def rotate(self, field):
        if self.is_able_to_rotate(self, field):
            self.increment_rotation()
            return True
        return False

    def is_able_to_fall(self, field):
        for coord in self.get_coords():
            if coord[1] + 1 >= len(field) or field[coord[1] + 1][coord[0]] != 0:
                return False
        return True

    def is_able_to_move_left(self, field):
        for coord in self.get_coords():
            if coord[0] < 1 or field[coord[1]][coord[0] - 1] != 0:
                return False
        return True

    def is_able_to_move_right(self, field):
        for coord in self.get_coords():
            if coord[0] + 1 >= len(field[0]) or field[coord[1]][coord[0] + 1] != 0:
                return False
        return True

    def fall(self, field):
        if self.is_able_to_fall(field):
            self.__y += 1
            return True
        return False

    def max_fall(self, field):
        while self.is_able_to_fall(field):
            self.__y += 1

    def move_left(self, field):
        if self.is_able_to_move_left(field):
            self.__x -= 1
            return True
        return False

    def move_right(self, field):
        if self.is_able_to_move_right(field):
            self.__x += 1
            return True
        return False