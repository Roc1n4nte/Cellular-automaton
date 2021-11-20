# -*- coding: utf-8 -*-

from parameters import *  # импортировать все постоянные и необходимые пакеты


# Класс Text содержит характеристики текста.
class Text:
    """
        При инициализации используются характеристики главного окна и пользовательского интерфейса
        :param window: экземпляр класса MainWindow с активированным create
        Также добавляются характеристики текста
        :param (x, y): координаты правой середины прямоугольной области, занимаемой текстом
        :param text: сам текст
        """

    def __init__(self, window, x=None, y=None, text=None):
        self.width_user_interface = window.width_user_interface  # ширина пользовательского интерфейса
        self.height_user_interface = window.height  # высота пользовательского интерфейса
        self.surface = window.surface  # поверхность, на которой рисуется пользовательский интерфейс
        self.x = x
        self.y = y
        self.text = text

    # Для рендеринга текста.
    # (x, y) - координаты правой середины прямоугольной области, занимаемой текстом
    def print_text(self, text, x, y, font_color=FONT_COLOR, font_size=FONT_SIZE, font_type=FONT_TYPE):
        # pygame.font.match_font() ищет наиболее подходящий шрифт в системе
        font = pygame.font.Font(pygame.font.match_font(font_type), font_size)  # тип и размер шрифта
        text_surface = font.render(text, True, font_color)  # вычисление структуры пикселей (рендеринг)
        text_rect = text_surface.get_rect()  # получить прямоугольную область, занимаемый текстом
        text_rect.midright = (x, y)  # задать координаты правого центра прямоугольной области, занимаемой текстом
        self.surface.blit(text_surface, text_rect)  # наложение текста на поверхность surface

    # Отрисовка текста
    def draw(self):
        self.print_text(self.text, self.x, self.y)
