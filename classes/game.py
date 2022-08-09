class Game:
    def __init__(self, size_x, size_y):
        self.set_size_x(size_x)
        self.set_size_y(size_y)
        self.__field = []
        for y in range(self.__size_y):
            self.__field.append([])
            for x in range(self.__size_x):
                self.__field[y].append(0)

    def __del__(self):
        pass

    def get_size_x(self):
        return self.__size_x

    def get_size_y(self):
        return self.__size_y

    def get_field(self):
        return self.__field

    def set_size_x(self, size_x):
        if(type(size_x) is int):
            if(size_x >= 4):
                self.__size_x = size_x

    def set_size_y(self, size_y):
        if(type(size_y) is int):
            if(size_y >= 4):
                self.__size_y = size_y

    def solidify_block(self, coords, color):
        for coord in coords:
            self.__field[coord[1]][coord[0]] = color

    def remove_rows(self):
        y = self.__size_y - 1
        while(y >= 0):
            row_to_be_removed = True
            for x in range(self.__size_x):
                if(self.__field[y][x] == 0):
                    row_to_be_removed = False
                    break
            if row_to_be_removed:
                for x in range(self.__size_x):
                    self.__field[y][x] = 0
                y2 = y
                while(y2 > 0):
                    for x in range(self.__size_x):
                        self.__field[y2][x] = self.__field[y2 - 1][x]
                    y2 -= 1
                for x in range(self.__size_x):
                    self.__field[0][x] = 0
                y += 1
            y -= 1