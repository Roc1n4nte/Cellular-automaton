# -*- coding: utf-8 -*-
import _tkinter  # для выхода из ошибки
from main_window import *  # импортировать класс MainWindow
from cellular_automaton import *  # импортировать класс CellularAutomaton
from button import *  # импортировать класс Button
from text import *  # импортировать класс Text


# Класс Application представляет собой приложение для запуска клеточного автомата:
class Application:
    """
    При инициализации создаются глобальные параметры приложения (если не указано, default параметры)
    :param run: инициализирует запуск приложения
    :param time_evolution: инициализирует временную эволюцию клеточного автомата
    :param n: инициализируем начальный момент времени
    :param passive_fps: задаем частоту смены кадров при простое
    :param active_fps: задаем частоту смены кадров временной эволюции
    :param pbcs: задаем спокойные граничные условия
    """
    def __init__(self, run=True, time_evolution=False, n=1, passive_fps=PASSIVE_FPS, active_fps=ACTIVE_FPS, pbcs=False):
        self.run = run
        self.time_evolution = time_evolution
        self.n = n
        self.passive_fps = passive_fps
        self.active_fps = active_fps
        self.pbcs = pbcs

    # Отрисовка и переворот экрана
    @staticmethod
    def fill_draw_flip(window, automaton, buttons_and_texts):
        # Отрисовка
        window.fill()
        automaton.draw()
        for p in buttons_and_texts:
            buttons_and_texts[p].draw()

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    # изменить граничные условия
    def change_pbcs(self, button):
        if self.pbcs:
            self.pbcs = False
        else:
            self.pbcs = True
        button.active_color, button.inactive_color, button.another_color = button.another_color, button.another_color, \
            button.active_color

    # Изменить параметры клеточного автомата
    def change_parameter_automaton(self, window, automaton, buttons_and_texts, button):
        # сменить цвет кнопки, чтобы показывал активированный режим
        inactive_color = button.inactive_color
        button.inactive_color = button.active_color
        change = True
        while change:
            # Держим цикл на правильной скорости
            window.clock.tick(self.passive_fps)

            # Вводим процесс (событие) для ответа
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Проверить закрытие окна
                    self.run = False
                    change = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # проверить нажатие кнопки мыши
                    if event.button == 1:  # левая кнопка мыши
                        mouse = pygame.mouse.get_pos()  # найти позицию курсора
                        if button.x < mouse[0] < button.x + button.width and \
                                button.y < mouse[1] < button.y + button.height:
                            change = False
                            button.inactive_color = inactive_color  # отключить режим
                # ввод текста
                elif change and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        button.text = button.text[:-1]
                    else:
                        if len(button.text) < 4:
                            button.text += event.unicode

            # Отрисовка и переворот экрана
            self.fill_draw_flip(window, automaton, {i: buttons_and_texts[i] for i in buttons_and_texts
                                                    if i != "Stop"})

    # добавить пейсмейкер 1
    def add_1(self, window, automaton, buttons_and_texts):
        # сменить цвет кнопки, чтобы показывал активированный режим
        inactive_color = buttons_and_texts["Add 1"].inactive_color
        buttons_and_texts["Add 1"].inactive_color = buttons_and_texts["Add 1"].active_color
        start_add_1 = True
        while start_add_1:
            # Держим цикл на правильной скорости
            window.clock.tick(self.passive_fps)

            # Вводим процесс (событие) для ответа
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Проверить закрытие окна
                    self.run = False
                    start_add_1 = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # проверить нажатие кнопки мыши
                    if event.button == 1:  # левая кнопка мыши
                        mouse = pygame.mouse.get_pos()  # найти позицию курсора
                        if buttons_and_texts["Add 1"].x < mouse[0] < buttons_and_texts["Add 1"].x + \
                                buttons_and_texts["Add 1"].width and \
                                buttons_and_texts["Add 1"].y < mouse[1] < buttons_and_texts["Add 1"].y + \
                                buttons_and_texts["Add 1"].height:
                            start_add_1 = False
                            buttons_and_texts["Add 1"].inactive_color = inactive_color  # отключить режим

            # Добавить пейсмейкер 1
            automaton.add_pacemaker_1()
            buttons_and_texts["T_1_value"].text = str(automaton.t_1)

            # Отрисовка и переворот экрана
            self.fill_draw_flip(window, automaton, {i: buttons_and_texts[i] for i in buttons_and_texts
                                                    if i != "Stop"})

    # добавить пейсмейкер 2
    def add_2(self, window, automaton, buttons_and_texts):
        # сменить цвет кнопки, чтобы показывал активированный режим
        inactive_color = buttons_and_texts["Add 2"].inactive_color
        buttons_and_texts["Add 2"].inactive_color = buttons_and_texts["Add 2"].active_color
        start_add_2 = True
        while start_add_2:
            # Держим цикл на правильной скорости
            window.clock.tick(self.passive_fps)

            # Вводим процесс (событие) для ответа
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Проверить закрытие окна
                    self.run = False
                    start_add_2 = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # проверить нажатие кнопки мыши
                    if event.button == 1:  # левая кнопка мыши
                        mouse = pygame.mouse.get_pos()  # найти позицию курсора
                        if buttons_and_texts["Add 2"].x < mouse[0] < buttons_and_texts["Add 2"].x + \
                                buttons_and_texts["Add 2"].width and \
                                buttons_and_texts["Add 2"].y < mouse[1] < buttons_and_texts["Add 2"].y + \
                                buttons_and_texts["Add 2"].height:
                            start_add_2 = False
                            buttons_and_texts["Add 2"].inactive_color = inactive_color  # отключить режим

            # Добавить пейсмейкер 2
            automaton.add_pacemaker_2()
            buttons_and_texts["T_2_value"].text = str(automaton.t_2)

            # Отрисовка и переворот экрана
            self.fill_draw_flip(window, automaton, {i: buttons_and_texts[i] for i in buttons_and_texts
                                                    if i != "Stop"})

    # Очистить клеточное поле и перейти в начальный момент времени
    def clear_cell_field(self, automaton, buttons_and_texts):
        automaton.clear()
        self.n = 1
        buttons_and_texts["n_value"].text = "n = " + str(self.n)
        buttons_and_texts["T_1_value"].text = str(automaton.t_1)
        buttons_and_texts["T_2_value"].text = str(automaton.t_2)

    # Останавливаем временную эволюцию клеточного автомата
    def time_evolution_stop(self):
        self.time_evolution = False

    # Инициализируем временную эволюцию клеточного автомата
    def time_evolution_start(self, window, automaton, buttons_and_texts):
        # Создаем цикл отрисовки
        self.time_evolution = True
        t = time()
        while self.time_evolution:
            # Держим цикл на правильной скорости
            window.clock.tick_busy_loop(self.active_fps)

            # Вводим процесс (событие) для ответа
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # проверить закрытие окна
                    self.time_evolution = False
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # проверить нажатие кнопки мыши
                    if event.button == 1:  # левая кнопка мыши
                        # остановить временную эволюцию
                        buttons_and_texts["Stop"].activate_action()

            # Обновление
            if time()-t >= int(buttons_and_texts["dt_value"].text)/1000:
                automaton.update(pbcs=self.pbcs)
                self.n += 1  # переходим к следующему моменту времени
                buttons_and_texts["n_value"].text = "n = " + str(self.n)
                t = time()

            # Отрисовка и переворот экрана
            self.fill_draw_flip(window, automaton, buttons_and_texts)

    # Сохраняет данную конфигурацию
    def save_configuration(self, window, automaton):
        try:
            pygame.display.set_mode((300, 1))
            root = Tk()
            root.withdraw()  # скрыть окно tkinter
            data = dict()
            filename = asksaveasfilename(initialdir=os.getcwd()+u"\configurations",
                                         title='Сохранить данную конфигурацию', filetypes=[('*.json', '.json')])
            if not filename.endswith('.json'):
                filename += '.json'
            with open(filename, "w") as write_file:
                data["row_value"] = automaton.row_number_cell
                data["column_value"] = automaton.column_number_cell
                data["t_e_value"] = automaton.t_e
                data["t_r_value"] = automaton.t_r
                data["g_value"] = automaton.g
                data["h_value"] = automaton.h
                data["u1_ij_value"] = automaton.u1_ij
                data["T_1_value"] = automaton.t_1
                data["T_2_value"] = automaton.t_2
                data["pacemaker_1_xy"] = automaton.pacemaker_1_xy.tolist()
                data["pacemaker_2_xy"] = automaton.pacemaker_2_xy.tolist()
                data["PBCs"] = self.pbcs
                data["phase"] = automaton.phase.tolist()
                json.dump(data, write_file)
            root.destroy()
        except FileNotFoundError:
            pass
        except _tkinter.TclError:
            pass
        finally:
            pygame.display.set_mode((window.width, window.height))

    # Открывает данную конфигурацию
    @staticmethod
    def load_configuration(window):
        try:
            pygame.display.set_mode((300, 1))
            root = Tk()
            root.withdraw()  # скрыть окно tkinter
            filename = askopenfilename(initialdir=os.getcwd() + u"\configurations",
                                       title='Открыть существующую конфигурацию', filetypes=[('*.json', '.json')])
            if not filename.endswith('.json'):
                filename += '.json'
            with open(filename, "r") as read_file:
                root.destroy()
                data = json.load(read_file)
                return data
        except FileNotFoundError:
            pass
        except _tkinter.TclError:
            pass
        finally:
            pygame.display.set_mode((window.width, window.height))

    # Возвращает кнопки и текст в виде словаря
    def get_buttons_and_texts(self, window, automaton):
        # записываем все кнопки и тексты в словарь
        buttons_and_texts = dict()

        # инициализируем кнопку сохранения данной конфигурации клеточного автомата
        buttons_and_texts["Save configuration"] = Button(window, x=0, y=0, text="Save configuration",
                                                         width=window.width_user_interface//2,
                                                         action=self.save_configuration)
        # инициализируем кнопку загрузки готовой конфигурации клеточного автомата
        buttons_and_texts["Load configuration"] = Button(window, x=buttons_and_texts["Save configuration"].x +
                                                         buttons_and_texts["Save configuration"].width,
                                                         y=buttons_and_texts["Save configuration"].y,
                                                         text="Load configuration", width=window.
                                                         width_user_interface//2 + window.width_user_interface % 2,
                                                         action=self.load_configuration)
        # инициализируем текст на экране без возможности и с возможностью изменения
        buttons_and_texts["row = "] = Text(window, x=buttons_and_texts["Save configuration"].width//2,
                                           y=buttons_and_texts["Save configuration"].y + 110, text="row = ")
        buttons_and_texts["row_value"] = Button(window, x=buttons_and_texts["row = "].x,
                                                y=buttons_and_texts["row = "].y-25,
                                                text=str(automaton.row_number_cell),
                                                action=self.change_parameter_automaton)
        buttons_and_texts["column = "] = Text(window, x=buttons_and_texts["Save configuration"].width +
                                              buttons_and_texts["Load configuration"].width//2,
                                              y=buttons_and_texts["row = "].y, text="column = ")
        buttons_and_texts["column_value"] = Button(window, x=buttons_and_texts["column = "].x,
                                                   y=buttons_and_texts["column = "].y-25,
                                                   text=str(automaton.column_number_cell),
                                                   action=self.change_parameter_automaton)
        buttons_and_texts["t_e = "] = Text(window, x=buttons_and_texts["row = "].x,
                                           y=buttons_and_texts["row = "].y + 50, text="t_e = ")
        buttons_and_texts["t_e_value"] = Button(window, x=buttons_and_texts["row_value"].x,
                                                y=buttons_and_texts["t_e = "].y-25, text=str(automaton.t_e),
                                                action=self.change_parameter_automaton)
        buttons_and_texts["t_r = "] = Text(window, x=buttons_and_texts["column = "].x, y=buttons_and_texts["t_e = "].y,
                                           text="t_r = ")
        buttons_and_texts["t_r_value"] = Button(window, x=buttons_and_texts["column_value"].x,
                                                y=buttons_and_texts["t_e_value"].y, text=str(automaton.t_r),
                                                action=self.change_parameter_automaton)
        buttons_and_texts["g = "] = Text(window, x=buttons_and_texts["t_e = "] .x, y=buttons_and_texts["t_e = "].y+50,
                                         text="g = ")
        buttons_and_texts["g_value"] = Button(window, x=buttons_and_texts["t_e_value"] .x,
                                              y=buttons_and_texts["t_e_value"].y+50, text=str(automaton.g),
                                              action=self.change_parameter_automaton)
        buttons_and_texts["h = "] = Text(window, x=buttons_and_texts["t_r = "].x, y=buttons_and_texts["g = "].y,
                                         text="h = ")
        buttons_and_texts["h_value"] = Button(window, x=buttons_and_texts["t_r_value"].x,
                                              y=buttons_and_texts["g_value"].y, text=str(automaton.h),
                                              action=self.change_parameter_automaton)
        buttons_and_texts["u1_ij = "] = Text(window, x=buttons_and_texts["g = "].x, y=buttons_and_texts["g = "].y + 50,
                                             text="u1_ij = ")
        buttons_and_texts["u1_ij_value"] = Button(window, x=buttons_and_texts["g_value"].x,
                                                  y=buttons_and_texts["g_value"].y + 50, text=str(automaton.u1_ij),
                                                  action=self.change_parameter_automaton)
        buttons_and_texts["(ms) dt = "] = Text(window, x=buttons_and_texts["h = "].x, y=buttons_and_texts["u1_ij = "].y,
                                               text="(ms) dt = ")
        buttons_and_texts["dt_value"] = Button(window, x=buttons_and_texts["h_value"].x,
                                               y=buttons_and_texts["u1_ij_value"].y,
                                               text=str(int(DT)),
                                               action=self.change_parameter_automaton)
        # инициализируем кнопки добавления пейсмейкера 1 и 2
        buttons_and_texts["Add 1"] = Button(window, x=buttons_and_texts["u1_ij_value"].x,
                                            y=buttons_and_texts["u1_ij_value"].y+100, text="Add 1",
                                            action=self.add_1)
        buttons_and_texts["Add 2"] = Button(window, x=buttons_and_texts["dt_value"].x,
                                            y=buttons_and_texts["Add 1"].y, text="Add 2", action=self.add_2)
        # инициализируем периоды пейсмейекера 1 и 2
        buttons_and_texts["T_1 = "] = Text(window, x=buttons_and_texts["u1_ij = "].x,
                                           y=buttons_and_texts["u1_ij = "].y+150, text="T_1 = ")
        buttons_and_texts["T_2 = "] = Text(window, x=buttons_and_texts["(ms) dt = "].x,
                                           y=buttons_and_texts["T_1 = "].y, text="T_2 = ")
        buttons_and_texts["T_1_value"] = Button(window, x=buttons_and_texts["Add 1"].x,
                                                y=buttons_and_texts["Add 1"].y+50, text=str(automaton.t_1),
                                                action=self.change_parameter_automaton)
        buttons_and_texts["T_2_value"] = Button(window, x=buttons_and_texts["Add 2"].x,
                                                y=buttons_and_texts["T_1_value"].y, text=str(automaton.t_2),
                                                action=self.change_parameter_automaton)
        # инициализируем кнопки запуска и остановки клеточного автомата
        buttons_and_texts["Start"] = Button(window, x=buttons_and_texts["T_1_value"].x,
                                            y=buttons_and_texts["T_1_value"].y+100,
                                            text="Start", width=100, action=self.time_evolution_start)
        buttons_and_texts["Stop"] = Button(window, x=buttons_and_texts["Start"].x, y=buttons_and_texts["Start"].y,
                                           text="Stop", width=buttons_and_texts["Start"].width,
                                           action=self.time_evolution_stop)
        # инициализируем счетчик временной эволюции клеточного автомата
        buttons_and_texts["n_value"] = Text(window,
                                            x=window.width_user_interface-30,
                                            y=buttons_and_texts["Start"].y+25, text="n = " + str(self.n))
        # инициализируем кнопку очистки клеточного поля
        buttons_and_texts["Clear cell field"] = Button(window, x=buttons_and_texts["Start"].x,
                                                       y=buttons_and_texts["Start"].y+100, text="Clear cell field",
                                                       width=180, action=self.clear_cell_field)
        # инициализируем кнопку задания периодических или спокойных граничных условий
        buttons_and_texts["PBCs"] = Button(window, x=buttons_and_texts["T_2_value"].x,
                                           y=buttons_and_texts["Clear cell field"].y, text="PBCs",
                                           action=self.change_pbcs)
        if self.pbcs:
            buttons_and_texts["PBCs"].another_color = buttons_and_texts["PBCs"].inactive_color
            buttons_and_texts["PBCs"].inactive_color = buttons_and_texts["PBCs"].active_color
        else:
            buttons_and_texts["PBCs"].another_color = buttons_and_texts["PBCs"].active_color
            buttons_and_texts["PBCs"].active_color = buttons_and_texts["PBCs"].inactive_color

        return buttons_and_texts

    # Инициализируем запуск приложения
    def run_application(self):
        main_window = MainWindow()  # инициализируем главное окно
        main_window.create()  # создаем поверхность для главного окна

        cellular_automaton = CellularAutomaton(main_window)  # инициализируем клеточный автомат
        # инициализируем пользовательский интерфейс
        buttons_and_texts = self.get_buttons_and_texts(main_window, cellular_automaton)

        # Создаем цикл отрисовки
        while self.run:
            # Держим цикл на правильной скорости
            main_window.clock.tick_busy_loop(self.passive_fps)

            # Вводим процесс (событие) для ответа
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Проверить закрытие окна
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # проверить нажатие кнопки мыши
                    if event.button == 1:  # левая кнопка мыши
                        mouse = pygame.mouse.get_pos()  # найти позицию курсора
                        if 0 < mouse[0] < main_window.width_user_interface and 0 < mouse[1] < main_window.height:
                            # начать временную эволюцию клеточного автомата
                            buttons_and_texts["Start"].activate_action(parameters=(main_window, cellular_automaton,
                                                                                   {i: buttons_and_texts[i] for i in
                                                                                    buttons_and_texts if i != "Start"}))
                            # очистить клеточное поле и перевести время в начальное положение
                            buttons_and_texts["Clear cell field"].activate_action(parameters=(cellular_automaton,
                                                                                  buttons_and_texts))
                            # добавить пейсмейкер 1 или 2
                            buttons_and_texts["Add 1"].activate_action(parameters=(main_window, cellular_automaton,
                                                                                   buttons_and_texts))
                            buttons_and_texts["Add 2"].activate_action(parameters=(main_window, cellular_automaton,
                                                                                   buttons_and_texts))
                            # так как инициализировать клеточный автомат нужно при изменении количества строк и столбцов
                            old_value = [buttons_and_texts["row_value"].text, buttons_and_texts["column_value"].text]
                            buttons_and_texts["row_value"].activate_action(parameters=(main_window, cellular_automaton,
                                                                                       buttons_and_texts,
                                                                                       buttons_and_texts["row_value"]))
                            buttons_and_texts["column_value"].activate_action(parameters=(main_window,
                                                                              cellular_automaton, buttons_and_texts,
                                                                              buttons_and_texts["column_value"]))

                            if not old_value == [buttons_and_texts["row_value"].text,
                                                 buttons_and_texts["column_value"].text]:
                                cellular_automaton = CellularAutomaton(main_window, row_number_cell=int(
                                    buttons_and_texts["row_value"].text), column_number_cell=int(
                                    buttons_and_texts["column_value"].text))
                                buttons_and_texts["T_1_value"].text = str(cellular_automaton.t_1)
                                buttons_and_texts["T_2_value"].text = str(cellular_automaton.t_2)

                            # изменить параметры, в случае необходимости
                            old_value = [buttons_and_texts["t_e_value"].text, buttons_and_texts["t_r_value"].text,
                                         buttons_and_texts["g_value"].text, buttons_and_texts["h_value"].text,
                                         buttons_and_texts["u1_ij_value"].text, buttons_and_texts["dt_value"].text,
                                         buttons_and_texts["T_1_value"].text, buttons_and_texts["T_2_value"].text]

                            for key in ["t_e_value", "t_r_value", "g_value", "h_value", "u1_ij_value", "dt_value",
                                        "T_1_value", "T_2_value"]:
                                buttons_and_texts[key].activate_action(parameters=(main_window,
                                                                       cellular_automaton, buttons_and_texts,
                                                                       buttons_and_texts[key]))

                            if not old_value == [buttons_and_texts["t_e_value"].text,
                                                 buttons_and_texts["t_r_value"].text,
                                                 buttons_and_texts["g_value"].text, buttons_and_texts["h_value"].text,
                                                 buttons_and_texts["u1_ij_value"].text,
                                                 buttons_and_texts["T_1_value"].text,
                                                 buttons_and_texts["T_2_value"].text]:
                                cellular_automaton.t_e, cellular_automaton.t_r, cellular_automaton.g, \
                                    cellular_automaton.h, cellular_automaton.u1_ij = \
                                    int(buttons_and_texts["t_e_value"].text), \
                                    int(buttons_and_texts["t_r_value"].text), \
                                    float(buttons_and_texts["g_value"].text), \
                                    float(buttons_and_texts["h_value"].text), \
                                    float(buttons_and_texts["u1_ij_value"].text)
                                cellular_automaton.activator = cellular_automaton.u1_ij*np.ones((
                                    cellular_automaton.row_number_cell, cellular_automaton.column_number_cell))
                                if buttons_and_texts["T_1_value"].text != "None":
                                    cellular_automaton.t_1 = int(buttons_and_texts["T_1_value"].text)
                                if buttons_and_texts["T_2_value"].text != "None":
                                    cellular_automaton.t_2 = int(buttons_and_texts["T_2_value"].text)

                            # изменить граничные условия
                            buttons_and_texts["PBCs"].activate_action(parameters=(buttons_and_texts["PBCs"], ))
                            # сохранить данную конфигурацию
                            buttons_and_texts["Save configuration"].activate_action(parameters=(main_window,
                                                                                                cellular_automaton, ))
                            # открыть готовую конфигурацию
                            data = buttons_and_texts["Load configuration"].activate_action(parameters=(main_window, ),
                                                                                           have_return=True)
                            if data is not None:
                                cellular_automaton = CellularAutomaton(
                                    main_window, row_number_cell=data["row_value"],
                                    column_number_cell=data["column_value"], t_e=data["t_e_value"],
                                    t_r=data["t_r_value"], h=data["h_value"], g=data["g_value"],
                                    u1_ij=data["u1_ij_value"], t_1=data["T_1_value"], t_2=data["T_2_value"])
                                cellular_automaton.pacemaker_1_xy = np.array(data["pacemaker_1_xy"])
                                cellular_automaton.pacemaker_2_xy = np.array(data["pacemaker_2_xy"])
                                cellular_automaton.phase = np.array(data["phase"])
                                self.pbcs = data["PBCs"]
                                self.n = 1
                                buttons_and_texts = self.get_buttons_and_texts(main_window, cellular_automaton)

            # Создание пользовательской конфигурации
            cellular_automaton.choice()

            # Отрисовка и переворот экрана
            self.fill_draw_flip(main_window, cellular_automaton, {i: buttons_and_texts[i] for i in buttons_and_texts
                                                                  if i != "Stop"})

        pygame.quit()  # закрываем приложение
