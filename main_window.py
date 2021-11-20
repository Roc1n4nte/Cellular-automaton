# -*- coding: utf-8 -*-

from parameters import *  # импортировать все постоянные и необходимые пакеты


# Класс MainWindow содержит характеристики окна, в котором лежит пользовательский интерфейс и клеточный автомат.
class MainWindow:
    """
    Инифиализируем параметры главного окна (если не указано, default параметры)
    :param width: ширина окна в пикселях
    :param height: высота окна в пикселях
    :param width_user_interface: ширина пользовательского интерфейса в пикселях
    :param width_cellular_automaton: ширина клеточного автомата в пикселях
    :param color: цвет фона
    :param surface: поверхность, на которой лежит главное окно (до create не существует)
    :param clock: для контроля частоты кадров при простое (до create не существует)
    """
    def __init__(self, width=WIDTH_MAIN_WINDOW, height=HEIGHT_MAIN_WINDOW, width_user_interface=WIDTH_USER_INTERFACE,
                 width_cellular_automaton=WIDTH_CELLULAR_AUTOMATON, color=COLOR_MAIN_WINDOW, surface=None, clock=None):
        self.width = width
        self.height = height
        self.width_user_interface = width_user_interface
        self.width_cellular_automaton = width_cellular_automaton
        self.color = color
        self.surface = surface
        self.clock = clock

    # Инициализируем использование pygame и печатаем главное окно на поверхности для последующего отображения
    def create(self):
        pygame.init()  # запускаем pygame
        self.surface = pygame.display.set_mode((self.width, self.height))  # поверхность рисования
        pygame.display.set_caption('Cellular automaton')  # название окна
        self.clock = pygame.time.Clock()

    # Заполнение окна фоновым цветом
    def fill(self):
        self.surface.fill(self.color)
