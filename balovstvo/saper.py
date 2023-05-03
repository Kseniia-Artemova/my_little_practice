import random


class Cell:
    """Класс, описывающий отдельную клетку поля"""
    def __init__(self) -> None:
        self.mine = False
        self.around_mines = 0
        self.fl_open = True

    def __str__(self) -> str:
        return f"Это клетка поля. Мина: {'есть' if self.mine else 'нет'}. " \
               f"Мин вокруг: {self.around_mines}. {'Открыта' if self.fl_open else 'закрыта'}"

    def __repr__(self) -> str:
        return f"Cell(mine={self.mine}, around_mines={self.around_mines}, fl_open={self.fl_open})"


class GamePole:
    """
    Класс, описывающий игровое поле.

    n: длина и ширина квадратного поля, выражается в количестве клеток
    m: количество мин на поле
    """
    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.pole = self.init()

    def __str__(self) -> str:
        return f"Поле со сторонами {self.n} x {self.n} клеток. Количество мин: {self.m}."

    def __repr__(self) -> str:
        return f"GamePole(n={self.n},m={self.m})"

    def init(self) -> list:
        """
        Метод, создающий поле с заданным количеством клеток и
        известным количеством мин, расположенных случайным образом.
        Клетки поля также получают значение количества мин, расположенных на соседних клетках.
        """
        cells = self.init_pole()
        self.set_mines(cells)
        self.count_mines(cells)
        return cells

    def init_pole(self) -> list:
        """Вспомогательный метод, создает поле с 'пустыми' клетками"""
        return [[Cell() for _ in range(self.n)] for _ in range(self.n)]

    def set_mines(self, cells: list) -> None:
        """
        Метод 'устанавливает' мины в клетки поля в случайном порядке.
        Число мин задается при создании объекта класса.
        """
        count = 0
        while count < self.m:
            random_cell = random.choice(random.choice(cells))
            if random_cell.mine is False:
                random_cell.mine = True
                count += 1

    @staticmethod
    def count_mines(cells) -> None:
        """Подсчитывает количество мин в соседних клетках и
        устанавливает это значение в параметр around_mines класса Cell."""
        for i in range(len(cells)):
            for j in range(len(cells)):
                if cells[i][j].mine is False:
                    index = (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)
                    cells[i][j].around_mines = sum([cells[i+x][j+y].mine
                                                    for x, y in index
                                                    if 0 <= i + x < len(cells) and 0 <= j + y < len(cells)])

    def show(self) -> None:
        """Метод печатает игровое поле"""
        for line in self.pole:
            for cell in line:
                if not cell.fl_open:
                    print("#", end=" ")
                elif cell.mine:
                    print("*", end=" ")
                else:
                    print(cell.around_mines, end=" ")
            print()


pole_game = GamePole(10, 12)
pole_game.show()
print(pole_game)