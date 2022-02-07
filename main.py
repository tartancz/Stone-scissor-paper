import sys
import time

from PyQt5 import QtGui, QtCore
import PyQt5.QtWidgets as qtw
import random




class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("kamen, nuzky, papir")
        self.setWindowIcon(QtGui.QIcon("kalkulacka.png"))
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.setting_window = SettingWindow()
        self.player_one_option = None
        self.player_two_option = None
        self.left_button_pressed = False
        self.right_button_pressed = False
        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        #buttons
        self.result_field = qtw.QLabel("Vitej v kamen, nuzky, papir.")
        btn_scissor_left = qtw.QPushButton("scissor", clicked = lambda: self.option_pressed_player_one(btn_scissor_left))
        btn_stone_left = qtw.QPushButton("stone", clicked = lambda: self.option_pressed_player_one(btn_stone_left))
        btn_paper_left = qtw.QPushButton("paper", clicked = lambda: self.option_pressed_player_one(btn_paper_left))
        btn_scissor_right = qtw.QPushButton("scissor", clicked= lambda: self.option_pressed_player_two(btn_scissor_right))
        btn_stone_right = qtw.QPushButton("stone", clicked= lambda: self.option_pressed_player_two(btn_stone_right))
        btn_paper_right = qtw.QPushButton("paper", clicked= lambda: self.option_pressed_player_two(btn_paper_right))
        btn_setting = qtw.QPushButton(QtGui.QIcon("ikony/setting.png"), "", clicked = lambda : self.setting_window.show())
        btn_reset = qtw.QPushButton("reset", clicked = lambda: self.reset())


            #right side
        self.right_option = []
        self.right_option.append(btn_paper_right)
        self.right_option.append(btn_stone_right)
        self.right_option.append(btn_scissor_right)
            #left side
        self.left_option = []
        self.left_option.append(btn_paper_left)
        self.left_option.append(btn_stone_left)
        self.left_option.append(btn_scissor_left)

        #editing result_field
        self.result_field.setStyleSheet("background-color: rgb(255, 179, 179);")
        self.result_field.setAlignment(QtCore.Qt.AlignCenter)

        #adding buttons to layout
        container.layout().addWidget(self.result_field,0,0,1,3)
        container.layout().addWidget(btn_scissor_left,1,0)
        container.layout().addWidget(btn_stone_left,2,0 )
        container.layout().addWidget(btn_paper_left,3,0 )
        container.layout().addWidget(btn_scissor_right,1,2)
        container.layout().addWidget(btn_stone_right,2,2 )
        container.layout().addWidget(btn_paper_right,3,2 )
        container.layout().addWidget(btn_setting, 5,1)
        container.layout().addWidget(btn_reset, 4,0,1,3)
        self.layout().addWidget(container)





    def option_pressed_player_one(self, option):
        if self.setting_window.check_box_1.isChecked() and not self.left_button_pressed:        # PLAYER vs BOT
            self.player_one_option = option
            option.setStyleSheet("background-color : green")
            self.left_button_pressed = True
            self.player_vs_bot()
        elif not self.setting_window.check_box_1.isChecked() and not self.left_button_pressed:  # PLAYER vs PLAYER
            self.player_one_option = option
            self.left_button_pressed = True

    def option_pressed_player_two(self, option):
        if not self.setting_window.check_box_1.isChecked() and not self.right_button_pressed and self.left_button_pressed:
            self.player_two_option = option
            self.right_button_pressed = True
            self.player_vs_player()

    def player_vs_bot(self):
        self.player_two_option = self.right_option [random.randint(0,2)]
        self.player_two_option.setStyleSheet("background-color : green")    #pak odstran az bude hotove
        winner = self.game(self.player_one_option, self.player_two_option)
        for x in winner:
            x.setStyleSheet("background-color : green")
        self.player_one_option.setStyleSheet("background-color : red")
        self.player_two_option.setStyleSheet("background-color : red")
        
    def player_vs_player(self):
        winner = self.game(self.player_one_option, self.player_two_option)
        for x in winner:
            x.setStyleSheet("background-color : green")
        self.player_one_option.setStyleSheet("background-color : red")
        self.player_two_option.setStyleSheet("background-color : red")

    def reset(self):
        self.player_one_option = None
        self.player_two_option = None
        self.left_button_pressed = False
        self.right_button_pressed = False
        for x in self.left_option + self.right_option:
            x.setStyleSheet("")

    def game(self, left, right):
        if left.text() == right.text():
            return self.right_option + self.left_option
        rules = \
            (
                ("stone", "scissor"),
                ("scissor", "paper"),
                ("paper", "stone"),
            )
        for winner, loser in rules:
            if winner == left.text() and loser == right.text():
                return self.left_option
        for loser, winner in rules:
            if winner == left.text() and loser == right.text():
                return self.right_option






class SettingWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon("ikony/setting.png"))
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())


        #creating buttons
        self.check_box_1 = qtw.QCheckBox("playing vs bot")

        #adding buttons to layout
        container.layout().addWidget(self.check_box_1)
        self.layout().addWidget(container)


app = qtw.QApplication(sys.argv)
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create("Fusion"))
sys.exit(app.exec_())
