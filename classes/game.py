class Game:
    def __init__(self, size_x, size_y):
        self.set_size_x(size_x)
        self.set_size_y(size_y)
        self.__field = []
        for y in range(self.__size_y):
            self.__field.append([])
            for x in range(self.__size_x):
                self.__field[y].append(0)
        self.__level = 1
        self.__score = 0
        self.__lines = 0

    def __del__(self):
        pass

    def get_size_x(self):
        return self.__size_x

    def get_size_y(self):
        return self.__size_y

    def get_field(self):
        return self.__field

    def get_level(self):
        return self.__level

    def get_score(self):
        return self.__score

    def get_lines(self):
        return self.__lines

    def set_level(self, level):
        self.__level = level

    def set_score(self, score):
        self.__score = score

    def set_lines(self, lines):
        self.__lines = lines

    def add_score(self, rows_removed):
        self.__score += self.__level * 40
        if rows_removed == 1:
            self.__score += self.__level * 100
        elif rows_removed == 2:
            self.__score += self.__level * 300
        elif rows_removed == 3:
            self.__score += self.__level * 500
        elif rows_removed == 4:
            self.__score += self.__level * 800
        self.__lines += rows_removed
        self.__level = self.__lines // 10 + 1
        return rows_removed

    def fall_time(self):
        if self.__level == 1:
            return 0.8
        elif self.__level == 2:
            return 0.72
        elif self.__level == 3:
            return 0.63
        elif self.__level == 4:
            return 0.55
        elif self.__level == 5:
            return 0.47
        elif self.__level == 6:
            return 0.38
        elif self.__level == 7:
            return 0.3
        elif self.__level == 8:
            return 0.22
        elif self.__level == 9:
            return 0.13
        elif self.__level == 10:
            return 0.1
        elif self.__level >= 11 and self.__level <= 13:
            return 0.08
        elif self.__level >= 14 and self.__level <= 16:
            return 0.07
        elif self.__level >= 17 and self.__level <= 19:
            return 0.05
        elif self.__level >= 20 and self.__level <= 29:
            return 0.03
        elif self.__level >= 30:
            return 0.02

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
        rows_removed = 0
        y = self.__size_y - 1
        while(y >= 0):
            row_to_be_removed = True
            for x in range(self.__size_x):
                if(self.__field[y][x] == 0):
                    row_to_be_removed = False
                    break
            if row_to_be_removed:
                rows_removed += 1
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
        return rows_removed

    def check_running(self, coords):
        for coord in coords:
            if self.__field[coord[1]][coord[0]] != 0:
                return False
        return True