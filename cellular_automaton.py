# -*- coding: utf-8 -*-

from parameters import *  # импортировать все постоянные и необходимые пакеты


# Класс CellularAutomaton содержит характеристики клеточного автомата.
class CellularAutomaton:
    """
    При инициализации используются характеристики главного окна.
    :param window: экземпляр класса MainWindow с активированным create
    При инициализации:
    1. Задаем параметры клеточного поля (если не указано, default параметры)
    :param row_number_cell: число строк
    :param column_number_cell: число столбцов
    :param empty_space: расстояние между клеточками в пикселях
    :param color_rest_zone: цвет зоны покоя,
    :param color_excitation_zone: цвет зоны возбуждения
    :param color_refractoriness_zone: цвет зоны рефрактерности
    :param color_background: цвет фона клеточного автомата
    2. Задаем параметры среды (если не указано, default параметры)
    :param t_e: дискретная длительность возбужденного состояния
    :param t_r: дискретная длительность рефрактерного состояния
    :param h: порог возбуждения состояния покоя
    :param g: 1/(1-g) есть характерное время полураспада активатора
    :param u1_ij: начальная концентрация активатора
    :param t_1: период пейсмейкера 1
    :param t_2: период пейсмейкера 2
    """

    def __init__(self, window, row_number_cell=ROW, column_number_cell=COLUMN, empty_space=CELL_EMPTY_SPACE,
                 color_rest_zone=COLOR_REST_ZONE, color_excitation_zone=COLOR_EXCITATION_ZONE,
                 color_refractoriness_zone=COLOR_REFRACTORINESS_ZONE, color_background=COLOR_BACKGROUND,
                 t_e=T_E, t_r=T_R, h=H, g=G, u1_ij=U1_IJ, t_1=None, t_2=None):
        self.t_e, self.t_r, self.h, self.g, self.u1_ij = t_e, t_r, h, g, u1_ij
        self.t_1, self.t_2 = t_1, t_2
        self.empty_space = empty_space
        self.color = {"color_rest_zone": color_rest_zone, "color_excitation_zone": color_excitation_zone,
                      "color_refractoriness_zone": color_refractoriness_zone, "color_background": color_background}
        self.surface = window.surface  # поверхность, на которой рисуется клеточный автомат
        self.row_number_cell = row_number_cell
        self.column_number_cell = column_number_cell

        # Делаем отступы от границ окна и от пользовательского интерфейса.
        x_first = window.width_user_interface + self.empty_space
        y_first = self.empty_space
        # Вычисляем размер каждой клетки с учетом пустого пространства между ними
        width_cell = (window.width_cellular_automaton - self.empty_space * (
                1 + self.column_number_cell)) / self.column_number_cell
        height_cell = (window.height - self.empty_space * (1 + self.row_number_cell)) / self.row_number_cell
        self.size_cell = int(min(width_cell, height_cell))
        # Увеличиваем отступ от границ окна, чтобы центрировать клеточное поле
        if self.size_cell < width_cell:
            x_first += int((width_cell - self.size_cell) * self.column_number_cell / 2)
        if self.size_cell < height_cell:
            y_first += int((height_cell - self.size_cell) * self.row_number_cell / 2)
        # Координаты левых верхних углов клеточек по горизонтали и по вертикали
        self.x = np.arange(x_first, x_first + (self.size_cell + self.empty_space) * self.column_number_cell,
                           self.size_cell + self.empty_space)
        self.y = np.arange(y_first, y_first + (self.size_cell + self.empty_space) * self.row_number_cell,
                           self.size_cell + self.empty_space)

        # Массив фиксирования пользовательского выбора
        self.user_choice = np.zeros((self.row_number_cell, self.column_number_cell), dtype=int)
        self.phase = np.zeros((self.row_number_cell, self.column_number_cell), dtype=int)  # Массив фаз клеточек
        # Массив концентрации активатора
        self.activator = self.u1_ij * np.ones((self.row_number_cell, self.column_number_cell))
        # Логический массив того, является ли клетка пейсмейкером (1 или 2) или нет
        self.pacemaker_1_xy = np.zeros((self.row_number_cell, self.column_number_cell), dtype=bool)
        self.pacemaker_2_xy = np.zeros((self.row_number_cell, self.column_number_cell), dtype=bool)

    # Для рендеринга (отрисовки) текста.
    # (x, y) - координаты центра прямоугольной области, занимаемой текстом
    def print_text(self, text, x, y, font_color=FONT_COLOR, font_type=FONT_TYPE):
        # pygame.font.match_font() ищет наиболее подходящий шрифт в системе
        font = pygame.font.Font(pygame.font.match_font(font_type), self.size_cell)  # тип и размер шрифта
        text_surface = font.render(text, True, font_color)  # вычисление структуры пикселей (рендеринг)
        text_rect = text_surface.get_rect()  # получить прямоугольную область, занимаемый текстом
        text_rect.center = (x, y)  # задать координаты центра прямоугольной области, занимаемой текстом
        self.surface.blit(text_surface, text_rect)  # наложение текста на поверхность surface

    # Отрисовка клеточного автомата
    def draw(self):
        # Отрисока фона клеточного автомата
        self.surface.fill(self.color["color_background"], rect=(self.x[0] - self.empty_space,
                                                                self.y[0] - self.empty_space,
                                                                self.x[-1] - self.x[0] + self.size_cell +
                                                                2 * self.empty_space,
                                                                self.y[-1] - self.y[0] + self.size_cell +
                                                                2 * self.empty_space))
        # Отрисовка фаз клеток и пейсмейкеров 1 и 2
        for i in range(self.row_number_cell):
            for j in range(self.column_number_cell):
                if self.phase[i, j] == 0:
                    pygame.draw.rect(self.surface, self.color["color_rest_zone"], (self.x[j], self.y[i],
                                                                                   self.size_cell, self.size_cell))
                    if self.pacemaker_1_xy[i, j]:
                        self.print_text("1", self.x[j]+self.size_cell//2, self.y[i]+self.size_cell//2)
                    elif self.pacemaker_2_xy[i, j]:
                        self.print_text("2", self.x[j] + self.size_cell // 2, self.y[i] + self.size_cell // 2)
                elif 0 < self.phase[i, j] <= self.t_e:
                    pygame.draw.rect(self.surface, self.color["color_excitation_zone"], (self.x[j], self.y[i],
                                                                                         self.size_cell,
                                                                                         self.size_cell))
                    if self.pacemaker_1_xy[i, j]:
                        self.print_text("1", self.x[j]+self.size_cell//2, self.y[i]+self.size_cell//2)
                    elif self.pacemaker_2_xy[i, j]:
                        self.print_text("2", self.x[j] + self.size_cell // 2, self.y[i] + self.size_cell // 2)
                else:
                    pygame.draw.rect(self.surface, self.color["color_refractoriness_zone"], (self.x[j], self.y[i],
                                                                                             self.size_cell,
                                                                                             self.size_cell))
                    if self.pacemaker_1_xy[i, j]:
                        self.print_text("1", self.x[j]+self.size_cell//2, self.y[i]+self.size_cell//2)
                    elif self.pacemaker_2_xy[i, j]:
                        self.print_text("2", self.x[j]+self.size_cell//2, self.y[i]+self.size_cell//2)

    # Очистка фаз и концентрации активатора
    def clear(self):
        self.phase = np.zeros((self.row_number_cell, self.column_number_cell), dtype=int)
        self.activator = self.u1_ij * np.ones((self.row_number_cell, self.column_number_cell))
        self.pacemaker_1_xy = np.zeros((self.row_number_cell, self.column_number_cell), dtype=bool)
        self.pacemaker_2_xy = np.zeros((self.row_number_cell, self.column_number_cell), dtype=bool)
        self.t_1, self.t_2 = None, None

    # Создать начальную конфигурацию из пользовательских предпочтений
    def choice(self):
        click = pygame.mouse.get_pressed()  # проверить нажатие кнопки мыши
        mouse = pygame.mouse.get_pos()  # найти позицию курсора
        try:
            i, j = self.y == self.y[self.y - mouse[1] < 0][-1], self.x == self.x[self.x - mouse[0] < 0][-1]
            if click[0]:  # левая кнопка мыши создает и уничтожает активную зону
                if self.user_choice[i, j] == 0:
                    self.user_choice[i, j] = 1
                    if self.phase[i, j] == 1:
                        self.phase[i, j] = 0
                    else:
                        self.phase[i, j] = 1
            elif click[2]:  # правая кнопка мыши создает и уничтожает зону рефрактерности
                if self.user_choice[i, j] == 0:
                    self.user_choice[i, j] = 1
                    if self.phase[i, j] == self.t_e + 1:
                        self.phase[i, j] = 0
                    else:
                        self.phase[i, j] = self.t_e + 1
            elif self.user_choice.any() == 1:
                self.user_choice = np.zeros((len(self.y), len(self.x)), dtype=int)
        except IndexError:
            pass

    # добавить пейсмейкер 1
    def add_pacemaker_1(self):
        click = pygame.mouse.get_pressed()  # проверить нажатие кнопки мыши
        mouse = pygame.mouse.get_pos()  # найти позицию курсора
        # задание начального периода пейсмейкера 1
        if self.t_1 is None:
            self.t_1 = self.t_e+self.t_r+1
        try:
            i, j = self.y == self.y[self.y - mouse[1] < 0][-1], self.x == self.x[self.x - mouse[0] < 0][-1]
            if click[0]:  # левая кнопка мыши создает и уничтожает пейсмейкер 1
                if self.user_choice[i, j] == 0:
                    self.user_choice[i, j] = 1
                    if self.pacemaker_1_xy[i, j]:
                        self.pacemaker_1_xy[i, j] = False
                    else:
                        self.pacemaker_1_xy[i, j] = True
            elif self.user_choice.any() == 1:
                self.user_choice = np.zeros((len(self.y), len(self.x)), dtype=int)
        except IndexError:
            pass
        # если нет ни одной клетки - период убрать
        if not self.pacemaker_1_xy.any():
            self.t_1 = None

    # добавить пейсмейкер 2
    def add_pacemaker_2(self):
        click = pygame.mouse.get_pressed()  # проверить нажатие кнопки мыши
        mouse = pygame.mouse.get_pos()  # найти позицию курсора
        # задание начального периода пейсмейкера 2
        if self.t_2 is None:
            self.t_2 = self.t_e + self.t_r + 1
        try:
            i, j = self.y == self.y[self.y - mouse[1] < 0][-1], self.x == self.x[self.x - mouse[0] < 0][-1]
            if click[0]:  # левая кнопка мыши создает и уничтожает пейсмейкер 2
                if self.user_choice[i, j] == 0:
                    self.user_choice[i, j] = 1
                    if self.pacemaker_2_xy[i, j]:
                        self.pacemaker_2_xy[i, j] = False
                    else:
                        self.pacemaker_2_xy[i, j] = True
            elif self.user_choice.any() == 1:
                self.user_choice = np.zeros((len(self.y), len(self.x)), dtype=int)
        except IndexError:
            pass
        # если нет ни одной клетки - период убрать
        if not self.pacemaker_2_xy.any():
            self.t_2 = None

    # Функция J для изменения концентрации активатора в узле (i, j)
    def function_j(self, phase):
        return np.logical_and(0 < phase, phase <= self.t_e)

    # Функция изменения концентрации активатора клеточного автомата.
    # Изменение концентрации активатора в узле (i, j) зависит только от фаз соседей
    def u(self, pbcs=True):
        # периодические граничные условия
        neighbor_u, neighbor_d = np.roll(self.phase, 1, axis=0), np.roll(self.phase, -1, axis=0)
        neighbor_l, neighbor_r = np.roll(self.phase, 1, axis=1), np.roll(self.phase, -1, axis=1)
        neighbor_u_l, neighbor_u_r = np.roll(neighbor_u, 1, axis=1), np.roll(neighbor_u, -1, axis=1)
        neighbor_d_l, neighbor_d_r = np.roll(neighbor_d, 1, axis=1), np.roll(neighbor_d, -1, axis=1)
        # спокойные граничные условия
        if not pbcs:
            neighbor_u[0], neighbor_d[-1], neighbor_l[:, 0], neighbor_r[:, -1] = 0, 0, 0, 0
            neighbor_u_l[0], neighbor_u_r[0], neighbor_d_l[-1], neighbor_d_r[-1] = 0, 0, 0, 0
            neighbor_u_l[:, 0], neighbor_u_r[:, -1], neighbor_d_l[:, 0], neighbor_d_r[:, -1] = 0, 0, 0, 0

        self.activator = self.g*self.activator + self.function_j(neighbor_u) + self.function_j(neighbor_d) + \
            self.function_j(neighbor_l) + self.function_j(neighbor_r) + self.function_j(neighbor_u_l) + \
            self.function_j(neighbor_u_r) + self.function_j(neighbor_d_l) + self.function_j(neighbor_d_r)

    # Функция изменения фаз клеточного автомата.
    # Изменение фазы в узле (i, j) идет после изменения концентрации активатора в этом узле
    def phi(self):
        # меняем фазы для клеток, не принадлежащим пейсмейкерами
        phase = np.where(np.logical_or(self.pacemaker_1_xy, self.pacemaker_2_xy),
                         -np.ones((self.row_number_cell, self.column_number_cell)), self.phase)
        self.phase[np.logical_and(0 < phase, phase < self.t_e + self.t_r)] += 1
        self.phase[phase == self.t_e + self.t_r] = 0
        self.phase[np.logical_and(phase == 0, self.activator < self.h)] = 0
        self.phase[np.logical_and(phase == 0, self.activator >= self.h)] = 1
        # меняем фазы для клеток, принадлежащим пейсмейкерам
        if self.t_1 is not None:
            phase = np.where(self.pacemaker_1_xy, self.phase,
                             -np.ones((self.row_number_cell, self.column_number_cell)))
            self.phase[np.logical_and(0 <= phase, phase < self.t_1-1)] += 1
            self.phase[phase >= self.t_1 - 1] = 0
        if self.t_2 is not None:
            phase = np.where(self.pacemaker_2_xy, self.phase,
                             -np.ones((self.row_number_cell, self.column_number_cell)))
            self.phase[np.logical_and(0 <= phase, phase < self.t_2 - 1)] += 1
            self.phase[phase >= self.t_2 - 1] = 0

    # Результирующее обновление фаз и концентрации активатора
    def update(self, pbcs=True):
        self.u(pbcs)  # концентрация активатора меняется
        self.phi()  # фазы меняются
