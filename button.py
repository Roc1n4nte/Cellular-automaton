# -*- coding: utf-8 -*-

from parameters import *  # импортировать все постоянные и необходимые пакеты


# Класс Button содержит характеристики кнопки.
class Button:
    """
    При инициализации используются характеристики главного окна и пользовательского интерфейса
    :param window: экземпляр класса MainWindow с активированным create
    Также добавляются характеристики кнопки
    :param (x, y): координаты левого верхнего края кнопки
    :param text: надпись на кнопке
    :param width: ширина кнопки
    :param height: высота кнопки
    :param inactive_color: цвет кнопки в пассивном состоянии
    :param active_color: цвет кнопки в активном состоянии
    :param action: действие при нажатии на кнопку
    """
    def __init__(self, window, x=None, y=None, text=None, width=WIDTH_BUTTON, height=HEIGHT_BUTTON,
                 inactive_color=INACTIVE_COLOR, active_color=ACTIVE_COLOR, action=None):
        """

        :rtype: object
        """
        self.width_user_interface = window.width_user_interface  # ширина пользовательского интерфейса
        self.height_user_interface = window.height  # высота пользовательского интерфейса
        self.surface = window.surface  # поверхность, на которой рисуется пользовательский интерфейс
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action

    # Для рендеринга (отрисовки) текста.
    # (x, y) - координаты центра прямоугольной области, занимаемой текстом
    def print_text(self, text, x, y, font_color=FONT_COLOR, font_size=FONT_SIZE, font_type=FONT_TYPE):
        # pygame.font.match_font() ищет наиболее подходящий шрифт в системе
        font = pygame.font.Font(pygame.font.match_font(font_type), font_size)  # тип и размер шрифта
        text_surface = font.render(text, True, font_color)  # вычисление структуры пикселей (рендеринг)
        text_rect = text_surface.get_rect()  # получить прямоугольную область, занимаемый текстом
        text_rect.center = (x, y)  # задать координаты центра прямоугольной области, занимаемой текстом
        self.surface.blit(text_surface, text_rect)  # наложение текста на поверхность surface

    # Отрисовка кнопки
    def draw(self):
        mouse = pygame.mouse.get_pos()  # найти позицию курсора

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(self.surface, self.active_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.surface, self.inactive_color, (self.x, self.y, self.width, self.height))

        self.print_text(self.text, self.x+self.width//2, self.y+self.height//2)  # Отрисовка текста на кнопке

    # Активирование действия кнопки
    def activate_action(self, parameters=(), have_return=False):
        mouse = pygame.mouse.get_pos()  # найти позицию курсора

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            if self.action is not None:
                # Задаем временную задержку, чтобы кнопка не нажималась несколько раз подряд (если понадобится)
                if have_return:
                    return self.action(*parameters)
                else:
                    self.action(*parameters)
