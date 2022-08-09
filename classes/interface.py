from colorama import Fore, Back, Style
from os import system, name

class Interface():
    def __init__(self):
        pass

    def __del__(self):
        pass

    def render(self, field, coords, color):
        if(name == "nt"):
            system("cls")
        else:
            system("clear")
        prnt = ""
        prnt = prnt + (Back.WHITE + " " * (len(field[0]) * 2 + 4)) + "\n"
        for y in range(len(field)):
            prnt = prnt + (Back.WHITE + " " * 2)
            for x in range(len(field[0])):
                if (x, y) in coords:
                    if color == 1:
                        prnt = prnt + (Back.RED + " " * 2)
                    elif color == 2:
                        prnt = prnt + (Back.GREEN + " " * 2)
                    elif color == 3:
                        prnt = prnt + (Back.YELLOW + " " * 2)
                    elif color == 4:
                        prnt = prnt + (Back.BLUE + " " * 2)
                    elif color == 5:
                        prnt = prnt + (Back.MAGENTA + " " * 2)
                    elif color == 6:
                        prnt = prnt + (Back.CYAN + " " * 2)
                else:
                    if field[y][x] == 0:
                        prnt = prnt + (Style.RESET_ALL + " " * 2)
                    elif field[y][x] == 1:
                        prnt = prnt + (Back.RED + " " * 2)
                    elif field[y][x] == 2:
                        prnt = prnt + (Back.GREEN + " " * 2)
                    elif field[y][x] == 3:
                        prnt = prnt + (Back.YELLOW + " " * 2)
                    elif field[y][x] == 4:
                        prnt = prnt + (Back.BLUE + " " * 2)
                    elif field[y][x] == 5:
                        prnt = prnt + (Back.MAGENTA + " " * 2)
                    elif field[y][x] == 6:
                        prnt = prnt + (Back.CYAN + " " * 2)  
            prnt = prnt + (Back.WHITE + " " * 2 + Style.RESET_ALL + "\n")
        prnt = prnt + (Back.WHITE + " " * (len(field[0]) * 2 + 4)) + "\n"
        print(prnt)