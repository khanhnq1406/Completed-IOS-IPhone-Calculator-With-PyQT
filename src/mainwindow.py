# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(432, 768)
                MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.number1 = QtWidgets.QPushButton(self.centralwidget)
                self.number1.setGeometry(QtCore.QRect(30, 520, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number1.setFont(font)
                self.number1.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number1.setObjectName("number1")
                self.number2 = QtWidgets.QPushButton(self.centralwidget)
                self.number2.setGeometry(QtCore.QRect(130, 520, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number2.setFont(font)
                self.number2.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number2.setObjectName("number2")
                self.number3 = QtWidgets.QPushButton(self.centralwidget)
                self.number3.setGeometry(QtCore.QRect(230, 520, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number3.setFont(font)
                self.number3.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number3.setObjectName("number3")
                self.addition = QtWidgets.QPushButton(self.centralwidget)
                self.addition.setGeometry(QtCore.QRect(330, 520, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.addition.setFont(font)
                self.addition.setStyleSheet("QPushButton {background-color: #f1a43c;\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                         "QPushButton:pressed { background-color: rgb(255, 255, 255); color: #f1a43c}""")
                self.addition.setObjectName("addition")
                self.number0 = QtWidgets.QPushButton(self.centralwidget)
                self.number0.setGeometry(QtCore.QRect(30, 620, 181, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number0.setFont(font)
                self.number0.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number0.setObjectName("number0")
                self.number4 = QtWidgets.QPushButton(self.centralwidget)
                self.number4.setGeometry(QtCore.QRect(30, 420, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number4.setFont(font)
                self.number4.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number4.setObjectName("number4")
                self.number6 = QtWidgets.QPushButton(self.centralwidget)
                self.number6.setGeometry(QtCore.QRect(230, 420, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number6.setFont(font)
                self.number6.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number6.setObjectName("number6")
                self.number5 = QtWidgets.QPushButton(self.centralwidget)
                self.number5.setGeometry(QtCore.QRect(130, 420, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number5.setFont(font)
                self.number5.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number5.setObjectName("number5")
                self.number7 = QtWidgets.QPushButton(self.centralwidget)
                self.number7.setGeometry(QtCore.QRect(30, 320, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number7.setFont(font)
                self.number7.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number7.setObjectName("number7")
                self.number9 = QtWidgets.QPushButton(self.centralwidget)
                self.number9.setGeometry(QtCore.QRect(230, 320, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number9.setFont(font)
                self.number9.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number9.setObjectName("number9")
                self.number8 = QtWidgets.QPushButton(self.centralwidget)
                self.number8.setGeometry(QtCore.QRect(130, 320, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.number8.setFont(font)
                self.number8.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                "QPushButton:pressed { background-color: #737373}""")
                self.number8.setObjectName("number8")
                self.equal = QtWidgets.QPushButton(self.centralwidget)
                self.equal.setGeometry(QtCore.QRect(330, 620, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.equal.setFont(font)
                self.equal.setStyleSheet("QPushButton {background-color: #f1a43c;\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                         "QPushButton:pressed { background-color: rgb(255, 255, 255); color: #f1a43c}""")
                self.equal.setObjectName("equal")
                self.subtraction = QtWidgets.QPushButton(self.centralwidget)
                self.subtraction.setGeometry(QtCore.QRect(330, 420, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.subtraction.setFont(font)
                self.subtraction.setStyleSheet("QPushButton {background-color: #f1a43c;\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                               "QPushButton:pressed { background-color: rgb(255, 255, 255); color: #f1a43c}""")
                self.subtraction.setObjectName("subtraction")
                self.multiplication = QtWidgets.QPushButton(self.centralwidget)
                self.multiplication.setGeometry(QtCore.QRect(330, 320, 81, 81))

                self.comma = QtWidgets.QPushButton(self.centralwidget)
                self.comma.setGeometry(QtCore.QRect(230, 620, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.comma.setFont(font)
                self.comma.setStyleSheet("QPushButton {background-color: rgb(49, 49, 49);\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                         "QPushButton:pressed { background-color: #737373}""")
                self.comma.setObjectName("comma")

                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.multiplication.setFont(font)
                self.multiplication.setStyleSheet("QPushButton {background-color: #f1a43c;\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                                  "QPushButton:pressed { background-color: rgb(255, 255, 255); color: #f1a43c}""")
                self.multiplication.setObjectName("multiplication")
                self.division = QtWidgets.QPushButton(self.centralwidget)
                self.division.setGeometry(QtCore.QRect(330, 220, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.division.setFont(font)
                self.division.setStyleSheet("QPushButton {background-color: #f1a43c;\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(255, 255, 255)}"
                                            "QPushButton:pressed { background-color: rgb(255, 255, 255); color: #f1a43c}""")
                self.division.setObjectName("division")
                self.percent = QtWidgets.QPushButton(self.centralwidget)
                self.percent.setGeometry(QtCore.QRect(230, 220, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.percent.setFont(font)
                self.percent.setStyleSheet("QPushButton {background-color: #a5a5a5;\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(0, 0, 0)}"
                                           "QPushButton:pressed { background-color: #d9d9d9}""")
                self.percent.setObjectName("percent")
                self.negative = QtWidgets.QPushButton(self.centralwidget)
                self.negative.setGeometry(QtCore.QRect(130, 220, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.negative.setFont(font)
                self.negative.setStyleSheet("QPushButton {background-color: #a5a5a5;\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(0, 0, 0)}"
                                            "QPushButton:pressed { background-color: #d9d9d9}""")
                self.negative.setObjectName("negative")
                self.acButton = QtWidgets.QPushButton(self.centralwidget)
                self.acButton.setGeometry(QtCore.QRect(30, 220, 81, 81))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(16)
                self.acButton.setFont(font)
                self.acButton.setStyleSheet("QPushButton {background-color: #a5a5a5;\n" 
                                                        "border-radius : 40;\n"
                                                        "color: rgb(0, 0, 0)}"
                                            "QPushButton:pressed { background-color: #d9d9d9}""")
                self.acButton.setObjectName("acButton")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(30, 130, 371, 61))
                font = QtGui.QFont()
                font.setFamily("Noto Mono")
                font.setPointSize(48)
                self.label.setFont(font)
                self.label.setStyleSheet("color: #fff;")
                self.label.setText("")
                self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.label.setObjectName("label")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 20))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.number0.setText(_translate("MainWindow", "0"))
                self.number1.setText(_translate("MainWindow", "1"))
                self.number2.setText(_translate("MainWindow", "2"))
                self.number3.setText(_translate("MainWindow", "3"))
                self.number4.setText(_translate("MainWindow", "4"))
                self.number5.setText(_translate("MainWindow", "5"))
                self.number6.setText(_translate("MainWindow", "6"))
                self.number7.setText(_translate("MainWindow", "7"))
                self.number8.setText(_translate("MainWindow", "8"))
                self.number9.setText(_translate("MainWindow", "9"))
                self.addition.setText(_translate("MainWindow", "+"))
                self.subtraction.setText(_translate("MainWindow", "-"))
                self.multiplication.setText(_translate("MainWindow", "x"))
                self.division.setText(_translate("MainWindow", "÷"))
                self.equal.setText(_translate("MainWindow", "="))
                self.percent.setText(_translate("MainWindow", "%"))
                self.negative.setText(_translate("MainWindow", "+/-"))
                self.acButton.setText(_translate("MainWindow", "AC"))
                self.comma.setText(_translate("MainWindow", ","))        
        def buttonClick(self):
                self.number0.clicked.connect(self.number0Clicked)
                self.number1.clicked.connect(self.number1Clicked)
                self.number2.clicked.connect(self.number2Clicked)
                self.number3.clicked.connect(self.number3Clicked)
                self.number4.clicked.connect(self.number4Clicked)
                self.number5.clicked.connect(self.number5Clicked)
                self.number6.clicked.connect(self.number6Clicked)
                self.number7.clicked.connect(self.number7Clicked)
                self.number8.clicked.connect(self.number8Clicked)
                self.number9.clicked.connect(self.number9Clicked)
                self.acButton.clicked.connect(self.acButtonClicked)
                self.negative.clicked.connect(self.negativeClicked)
                self.equal.clicked.connect(self.equalClicked)
                self.addition.clicked.connect(self.additionClicked)
                self.subtraction.clicked.connect(self.subtractionClicked)
        def number0Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 0)*(not isNegative) + (numberInput*10 - 0)*isNegative
                if numberInput > 999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def number1Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 1)*(not isNegative) + (numberInput*10 - 1)*isNegative
                if numberInput > 999999999 or numberInput < -999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def number2Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 2)*(not isNegative) + (numberInput*10 - 2)*isNegative
                if numberInput > 999999999 or numberInput < -999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def number3Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 3)*(not isNegative) + (numberInput*10 - 3)*isNegative
                if numberInput > 999999999 or numberInput < -999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def number4Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 4)*(not isNegative) + (numberInput*10 - 4)*isNegative
                if numberInput > 999999999 or numberInput < -999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def number5Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 5)*(not isNegative) + (numberInput*10 - 5)*isNegative
                if numberInput > 999999999 or numberInput < -999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def number6Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 6)*(not isNegative) + (numberInput*10 - 6)*isNegative
                if numberInput > 999999999 or numberInput < -999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def number7Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 7)*(not isNegative) + (numberInput*10 - 7)*isNegative
                if numberInput > 999999999 or numberInput < -999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def number8Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 8)*(not isNegative) + (numberInput*10 - 8)*isNegative
                if numberInput > 999999999 or numberInput < -999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def number9Clicked(self):
                global numberInput
                numberInput = (numberInput*10 + 9)*(not isNegative) + (numberInput*10 - 9)*isNegative
                if numberInput > 999999999 or numberInput < -999999999:
                        numberInput = int(numberInput / 10)
                self.label.setText(str(numberInput))
                print (numberInput)
        def acButtonClicked(self):
                global numberInput, isNegative, result, calculation
                numberInput = int(numberInput/10)
                if numberInput == 0:
                        isNegative = False
                        result = 0
                        calculation = 0
                        self.addition.setStyleSheet("background-color: #f1a43c; color: #ffffff; border-radius : 40;")
                        self.subtraction.setStyleSheet("background-color: #f1a43c; color: #ffffff; border-radius : 40;")


                self.label.setText(str(numberInput))
                print (numberInput)
        def negativeClicked(self):
                global numberInput, isNegative
                isNegative = not isNegative
                numberInput = -numberInput
                self.label.setText(str(numberInput))
                print (numberInput)
        def equalClicked(self):
                global result, numberInput, calculation
                if calculation == 1:
                        result += numberInput
                        numberInput = 0
                        self.label.setText(str(result))
                        print(result)
                if calculation == 2:
                        result -= numberInput
                        numberInput = 0
                        self.label.setText(str(result))
                        print(result)
        def additionClicked(self):
                global result, numberInput, calculation
                calculation = 1
                result += numberInput
                numberInput = 0
                self.label.setText(str(result))
                print(result)
                self.addition.setStyleSheet("background-color: rgb(255, 255, 255); color: #f1a43c; border-radius : 40;")
                self.subtraction.setStyleSheet("background-color: #f1a43c; color: #ffffff; border-radius : 40;")
        def subtractionClicked(self):
                global result, numberInput, calculation
                calculation = 2
                if result == 0:
                        result = numberInput
                else:
                        result -= numberInput
                numberInput = 0
                self.label.setText(str(result))
                print(result)
                self.subtraction.setStyleSheet("background-color: rgb(255, 255, 255); color: #f1a43c; border-radius : 40;")
                self.addition.setStyleSheet("background-color: #f1a43c; color: #ffffff; border-radius : 40;")

global numberInput, result, isNegative, calculation
numberInput = 0
result = 0
isNegative = False
calculation = 0 #1: addition, 2: subtraction, 3: multiplication, 4: division
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.buttonClick()
    MainWindow.show()
    sys.exit(app.exec_())