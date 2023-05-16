# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import math as m
import pickle

class Ui_MainWindow(object):
    def setupStartUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(30, 20, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.titlelabel.setFont(font)
        self.titlelabel.setObjectName("titlelabel")
        self.colorBox = QtWidgets.QComboBox(self.centralwidget)
        self.colorBox.setGeometry(QtCore.QRect(40, 90, 81, 31))
        self.colorBox.setObjectName("colorBox")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.colorBox.addItem("")
        self.sizeBox = QtWidgets.QComboBox(self.centralwidget)
        self.sizeBox.setGeometry(QtCore.QRect(230, 90, 81, 31))
        self.sizeBox.setObjectName("sizeBox")
        self.sizeBox.addItem("")
        self.sizeBox.addItem("")
        self.sizeBox.addItem("")
        self.sizeBox.addItem("")
        self.sizeBox.addItem("")
        self.sizeBox.addItem("")
        self.sizeBox.addItem("")
        self.sizeBox.addItem("")
        self.sizeBox.addItem("")
        self.colorlabel = QtWidgets.QLabel(self.centralwidget)
        self.colorlabel.setGeometry(QtCore.QRect(50, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.colorlabel.setFont(font)
        self.colorlabel.setObjectName("colorlabel")
        self.sizelabel = QtWidgets.QLabel(self.centralwidget)
        self.sizelabel.setGeometry(QtCore.QRect(250, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sizelabel.setFont(font)
        self.sizelabel.setObjectName("sizelabel")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(140, 130, 75, 23))
        self.createButton.setObjectName("createButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.menuFile.addAction(self.actionLoad)
        self.menubar.addAction(self.menuFile.menuAction())

        self.color = ""
        self.size = 0

        self.pencolor = "white"
        self.pensize = 1

        self.ishorizontal = False
        self.isvertical = False
        self.isfill = False

        self.loaded = False

        self.count = 1
        self.buttons = {}

        self.directory = ""

        self.retranslateStartUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateStartUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titlelabel.setText(_translate("MainWindow", "Pick the size of the image and the background color."))
        self.colorBox.setItemText(0, _translate("MainWindow", "White"))
        self.colorBox.setItemText(1, _translate("MainWindow", "Black"))
        self.colorBox.setItemText(2, _translate("MainWindow", "Gray"))
        self.colorBox.setItemText(3, _translate("MainWindow", "Lightgray"))
        self.colorBox.setItemText(4, _translate("MainWindow", "Maroon"))
        self.colorBox.setItemText(5, _translate("MainWindow", "Sienna"))
        self.colorBox.setItemText(6, _translate("MainWindow", "Red"))
        self.colorBox.setItemText(7, _translate("MainWindow", "Hotpink"))
        self.colorBox.setItemText(8, _translate("MainWindow", "Darkorange"))
        self.colorBox.setItemText(9, _translate("MainWindow", "Gold"))
        self.colorBox.setItemText(10, _translate("MainWindow", "Yellow"))
        self.colorBox.setItemText(11, _translate("MainWindow", "Oldlace"))
        self.colorBox.setItemText(12, _translate("MainWindow", "Seagreen"))
        self.colorBox.setItemText(13, _translate("MainWindow", "Springgreen"))
        self.colorBox.setItemText(14, _translate("MainWindow", "Dodgerblue"))
        self.colorBox.setItemText(15, _translate("MainWindow", "Skyblue"))
        self.colorBox.setItemText(16, _translate("MainWindow", "Mediumblue"))
        self.colorBox.setItemText(17, _translate("MainWindow", "Teal"))
        self.colorBox.setItemText(18, _translate("MainWindow", "Mediumpurple"))
        self.colorBox.setItemText(19, _translate("MainWindow", "Thistle"))
        self.sizeBox.setItemText(0, _translate("MainWindow", "8x8"))
        self.sizeBox.setItemText(1, _translate("MainWindow", "4x4"))
        self.sizeBox.setItemText(2, _translate("MainWindow", "6x6"))
        self.sizeBox.setItemText(3, _translate("MainWindow", "10x10"))
        self.sizeBox.setItemText(4, _translate("MainWindow", "12x12"))
        self.sizeBox.setItemText(5, _translate("MainWindow", "16x16"))
        self.sizeBox.setItemText(6, _translate("MainWindow", "20x20"))
        self.sizeBox.setItemText(7, _translate("MainWindow", "24x24"))
        self.sizeBox.setItemText(8, _translate("MainWindow", "25x25"))
        self.colorlabel.setText(_translate("MainWindow", "Color:"))
        self.sizelabel.setText(_translate("MainWindow", "Size:"))
        self.createButton.setText(_translate("MainWindow", "Create"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+L"))

        self.createButton.clicked.connect(self.createNewImage)
        self.actionLoad.triggered.connect(self.load)

    def setupMainUi(self, MainWindow):
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.colorGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.colorGroup.setGeometry(QtCore.QRect(10, 0, 91, 411))
        self.colorGroup.setObjectName("colorGroup")
        self.blackButton = QtWidgets.QPushButton(self.colorGroup)
        self.blackButton.setGeometry(QtCore.QRect(10, 20, 25, 25))
        self.blackButton.setStyleSheet("background-color: black;")
        self.blackButton.setText("")
        self.blackButton.setObjectName("blackButton")
        self.whiteButton = QtWidgets.QPushButton(self.colorGroup)
        self.whiteButton.setGeometry(QtCore.QRect(50, 20, 25, 25))
        self.whiteButton.setStyleSheet("background-color: white;")
        self.whiteButton.setText("")
        self.whiteButton.setObjectName("whiteButton")
        self.grayButton = QtWidgets.QPushButton(self.colorGroup)
        self.grayButton.setGeometry(QtCore.QRect(10, 60, 25, 25))
        self.grayButton.setStyleSheet("background-color: gray;")
        self.grayButton.setText("")
        self.grayButton.setObjectName("grayButton")
        self.lightgrayButton = QtWidgets.QPushButton(self.colorGroup)
        self.lightgrayButton.setGeometry(QtCore.QRect(50, 60, 25, 25))
        self.lightgrayButton.setStyleSheet("background-color: lightgray;")
        self.lightgrayButton.setText("")
        self.lightgrayButton.setObjectName("lightgrayButton")
        self.darkbrownButton = QtWidgets.QPushButton(self.colorGroup)
        self.darkbrownButton.setGeometry(QtCore.QRect(10, 100, 25, 25))
        self.darkbrownButton.setStyleSheet("background-color: maroon;")
        self.darkbrownButton.setText("")
        self.darkbrownButton.setObjectName("darkbrownButton")
        self.lightbrownButton = QtWidgets.QPushButton(self.colorGroup)
        self.lightbrownButton.setGeometry(QtCore.QRect(50, 100, 25, 25))
        self.lightbrownButton.setStyleSheet("background-color: sienna;")
        self.lightbrownButton.setText("")
        self.lightbrownButton.setObjectName("lightbrownButton")
        self.redButton = QtWidgets.QPushButton(self.colorGroup)
        self.redButton.setGeometry(QtCore.QRect(10, 140, 25, 25))
        self.redButton.setStyleSheet("background-color: red;")
        self.redButton.setText("")
        self.redButton.setObjectName("redButton")
        self.pinkButton = QtWidgets.QPushButton(self.colorGroup)
        self.pinkButton.setGeometry(QtCore.QRect(50, 140, 25, 25))
        self.pinkButton.setStyleSheet("background-color: hotpink;")
        self.pinkButton.setText("")
        self.pinkButton.setObjectName("pinkButton")
        self.orangeButton = QtWidgets.QPushButton(self.colorGroup)
        self.orangeButton.setGeometry(QtCore.QRect(10, 180, 25, 25))
        self.orangeButton.setStyleSheet("background-color: darkorange;")
        self.orangeButton.setText("")
        self.orangeButton.setObjectName("orangeButton")
        self.goldButton = QtWidgets.QPushButton(self.colorGroup)
        self.goldButton.setGeometry(QtCore.QRect(50, 180, 25, 25))
        self.goldButton.setStyleSheet("background-color: gold;")
        self.goldButton.setText("")
        self.goldButton.setObjectName("goldButton")
        self.yellowButton = QtWidgets.QPushButton(self.colorGroup)
        self.yellowButton.setGeometry(QtCore.QRect(10, 220, 25, 25))
        self.yellowButton.setStyleSheet("background-color: yellow;")
        self.yellowButton.setText("")
        self.yellowButton.setObjectName("yellowButton")
        self.beigeButton = QtWidgets.QPushButton(self.colorGroup)
        self.beigeButton.setGeometry(QtCore.QRect(50, 220, 25, 25))
        self.beigeButton.setStyleSheet("background-color: oldlace;")
        self.beigeButton.setText("")
        self.beigeButton.setObjectName("beigeButton")
        self.darkgreenButton = QtWidgets.QPushButton(self.colorGroup)
        self.darkgreenButton.setGeometry(QtCore.QRect(10, 260, 25, 25))
        self.darkgreenButton.setStyleSheet("background-color: seagreen;")
        self.darkgreenButton.setText("")
        self.darkgreenButton.setObjectName("darkgreenButton")
        self.limeButton = QtWidgets.QPushButton(self.colorGroup)
        self.limeButton.setGeometry(QtCore.QRect(50, 260, 25, 25))
        self.limeButton.setStyleSheet("background-color: springgreen;")
        self.limeButton.setText("")
        self.limeButton.setObjectName("limeButton")
        self.blueButton = QtWidgets.QPushButton(self.colorGroup)
        self.blueButton.setGeometry(QtCore.QRect(10, 300, 25, 25))
        self.blueButton.setStyleSheet("background-color: dodgerblue;")
        self.blueButton.setText("")
        self.blueButton.setObjectName("blueButton")
        self.lightblueButton = QtWidgets.QPushButton(self.colorGroup)
        self.lightblueButton.setGeometry(QtCore.QRect(50, 300, 25, 25))
        self.lightblueButton.setStyleSheet("background-color: skyblue;")
        self.lightblueButton.setText("")
        self.lightblueButton.setObjectName("lightblueButton")
        self.darkblueButton = QtWidgets.QPushButton(self.colorGroup)
        self.darkblueButton.setGeometry(QtCore.QRect(10, 340, 25, 25))
        self.darkblueButton.setStyleSheet("background-color: mediumblue;")
        self.darkblueButton.setText("")
        self.darkblueButton.setObjectName("darkblueButton")
        self.tealButton = QtWidgets.QPushButton(self.colorGroup)
        self.tealButton.setGeometry(QtCore.QRect(50, 340, 25, 25))
        self.tealButton.setStyleSheet("background-color: teal;")
        self.tealButton.setText("")
        self.tealButton.setObjectName("tealButton")
        self.purpleButton = QtWidgets.QPushButton(self.colorGroup)
        self.purpleButton.setGeometry(QtCore.QRect(10, 380, 25, 25))
        self.purpleButton.setStyleSheet("background-color: mediumpurple;")
        self.purpleButton.setText("")
        self.purpleButton.setObjectName("purpleButton")
        self.thistleButton = QtWidgets.QPushButton(self.colorGroup)
        self.thistleButton.setGeometry(QtCore.QRect(50, 380, 25, 25))
        self.thistleButton.setStyleSheet("background-color: thistle;")
        self.thistleButton.setText("")
        self.thistleButton.setObjectName("thistleButton")
        self.sizeGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.sizeGroup.setGeometry(QtCore.QRect(10, 420, 91, 121))
        self.sizeGroup.setObjectName("sizeGroup")
        self.penSize1Button = QtWidgets.QPushButton(self.sizeGroup)
        self.penSize1Button.setGeometry(QtCore.QRect(10, 20, 25, 25))
        self.penSize1Button.setObjectName("penSize1Button")
        self.penSize2Button = QtWidgets.QPushButton(self.sizeGroup)
        self.penSize2Button.setGeometry(QtCore.QRect(50, 20, 25, 25))
        self.penSize2Button.setObjectName("penSize2Button")
        self.penSize4Button = QtWidgets.QPushButton(self.sizeGroup)
        self.penSize4Button.setGeometry(QtCore.QRect(10, 50, 25, 25))
        self.penSize4Button.setObjectName("penSize4Button")
        self.penSize6Button = QtWidgets.QPushButton(self.sizeGroup)
        self.penSize6Button.setGeometry(QtCore.QRect(50, 50, 25, 25))
        self.penSize6Button.setObjectName("penSize6utton")
        self.penSize8Button = QtWidgets.QPushButton(self.sizeGroup)
        self.penSize8Button.setGeometry(QtCore.QRect(10, 80, 25, 25))
        self.penSize8Button.setObjectName("penSize8Button")
        self.penSize12Button = QtWidgets.QPushButton(self.sizeGroup)
        self.penSize12Button.setGeometry(QtCore.QRect(50, 80, 25, 25))
        self.penSize12Button.setObjectName("penSize12Button")
        self.toolGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.toolGroup.setGeometry(QtCore.QRect(710, 0, 81, 111))
        self.toolGroup.setStyleSheet("")
        self.toolGroup.setObjectName("toolGroup")
        self.rubberButton = QtWidgets.QPushButton(self.toolGroup)
        self.rubberButton.setGeometry(QtCore.QRect(10, 30, 25, 25))
        self.rubberButton.setStyleSheet("background-image: url(:/newPrefix/rubber.png);\n"
"background-repeat: no-repeat;")
        self.rubberButton.setText("")
        icon = QtGui.QIcon.fromTheme("Assets/rubber.png")
        self.rubberButton.setIcon(icon)
        self.rubberButton.setIconSize(QtCore.QSize(16, 16))
        self.rubberButton.setObjectName("rubberButton")
        self.fillButton = QtWidgets.QPushButton(self.toolGroup)
        self.fillButton.setGeometry(QtCore.QRect(50, 30, 25, 25))
        self.fillButton.setStyleSheet("background-image: url(:/newPrefix/bucket.png);\n"
"background-repeat: no-repeat;")
        self.fillButton.setText("")
        icon = QtGui.QIcon.fromTheme("Assets/rubber.png")
        self.fillButton.setIcon(icon)
        self.fillButton.setIconSize(QtCore.QSize(16, 16))
        self.fillButton.setObjectName("fillButton")
        self.horizontalButton = QtWidgets.QPushButton(self.toolGroup)
        self.horizontalButton.setGeometry(QtCore.QRect(10, 70, 25, 25))
        self.horizontalButton.setStyleSheet("background-image: url(:/newPrefix/horizontal.png);\n"
"background-repeat: no-repeat;")
        self.horizontalButton.setText("")
        icon = QtGui.QIcon.fromTheme("Assets/rubber.png")
        self.horizontalButton.setIcon(icon)
        self.horizontalButton.setIconSize(QtCore.QSize(16, 16))
        self.horizontalButton.setObjectName("horizontalButton")
        self.verticalButton = QtWidgets.QPushButton(self.toolGroup)
        self.verticalButton.setGeometry(QtCore.QRect(50, 70, 25, 25))
        self.verticalButton.setStyleSheet("background-image: url(:/newPrefix/vertical.png);\n"
"background-repeat: no-repeat;")
        self.verticalButton.setText("")
        icon = QtGui.QIcon.fromTheme("Assets/rubber.png")
        self.verticalButton.setIcon(icon)
        self.verticalButton.setIconSize(QtCore.QSize(16, 16))
        self.verticalButton.setObjectName("verticalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateMainUi(MainWindow)

    def retranslateMainUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Button Paint"))
        self.colorGroup.setStatusTip(_translate("MainWindow", "Change the color of the pen"))
        self.colorGroup.setTitle(_translate("MainWindow", "Colors"))
        self.sizeGroup.setStatusTip(_translate("MainWindow", "Change the pen size. Note that it also applies to rubber"))
        self.sizeGroup.setTitle(_translate("MainWindow", "PenSize"))
        self.penSize1Button.setText(_translate("MainWindow", "1"))
        self.penSize2Button.setText(_translate("MainWindow", "2"))
        self.penSize4Button.setText(_translate("MainWindow", "4"))
        self.penSize6Button.setText(_translate("MainWindow", "6"))
        self.penSize8Button.setText(_translate("MainWindow", "8"))
        self.penSize12Button.setText(_translate("MainWindow", "12"))
        self.toolGroup.setStatusTip(_translate("MainWindow", "Additional tools"))
        self.toolGroup.setTitle(_translate("MainWindow", "Tools"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Get some help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About the program"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))

        self.actionAbout.triggered.connect(lambda: self.showAbout(MainWindow))
        self.actionHelp.triggered.connect(lambda: self.showHelp(MainWindow))

        self.actionSave.triggered.connect(lambda: self.save(MainWindow))
        self.actionSave_As.triggered.connect(lambda: self.saveAs(MainWindow))

        self.whiteButton.clicked.connect(lambda: self.changePenColor(MainWindow, "white"))
        self.blackButton.clicked.connect(lambda: self.changePenColor(MainWindow, "black"))
        self.grayButton.clicked.connect(lambda: self.changePenColor(MainWindow, "gray"))
        self.lightgrayButton.clicked.connect(lambda: self.changePenColor(MainWindow, "lightgray"))
        self.darkbrownButton.clicked.connect(lambda: self.changePenColor(MainWindow, "maroon"))
        self.lightbrownButton.clicked.connect(lambda: self.changePenColor(MainWindow, "sienna"))
        self.redButton.clicked.connect(lambda: self.changePenColor(MainWindow, "red"))
        self.pinkButton.clicked.connect(lambda: self.changePenColor(MainWindow, "hotpink"))
        self.orangeButton.clicked.connect(lambda: self.changePenColor(MainWindow, "darkorange"))
        self.goldButton.clicked.connect(lambda: self.changePenColor(MainWindow, "gold"))
        self.yellowButton.clicked.connect(lambda: self.changePenColor(MainWindow, "yellow"))
        self.beigeButton.clicked.connect(lambda: self.changePenColor(MainWindow, "oldlace"))
        self.darkgreenButton.clicked.connect(lambda: self.changePenColor(MainWindow, "seagreen"))
        self.limeButton.clicked.connect(lambda: self.changePenColor(MainWindow, "springgreen"))
        self.blueButton.clicked.connect(lambda: self.changePenColor(MainWindow, "dodgerblue"))
        self.lightblueButton.clicked.connect(lambda: self.changePenColor(MainWindow, "skyblue"))
        self.darkblueButton.clicked.connect(lambda: self.changePenColor(MainWindow, "mediumblue"))
        self.tealButton.clicked.connect(lambda: self.changePenColor(MainWindow, "teal"))
        self.purpleButton.clicked.connect(lambda: self.changePenColor(MainWindow, "mediumpurple"))
        self.thistleButton.clicked.connect(lambda: self.changePenColor(MainWindow, "thistle"))

        self.penSize1Button.clicked.connect(lambda: self.changePenSize(MainWindow, "1"))
        self.penSize2Button.clicked.connect(lambda: self.changePenSize(MainWindow, "2"))
        self.penSize4Button.clicked.connect(lambda: self.changePenSize(MainWindow, "4"))
        self.penSize6Button.clicked.connect(lambda: self.changePenSize(MainWindow, "6"))
        self.penSize8Button.clicked.connect(lambda: self.changePenSize(MainWindow, "8"))
        self.penSize12Button.clicked.connect(lambda: self.changePenSize(MainWindow, "12"))

        self.rubberButton.clicked.connect(lambda: self.rubber(MainWindow))

        self.horizontalButton.clicked.connect(self.sethorizontal)
        self.verticalButton.clicked.connect(self.setvertical)
        self.fillButton.clicked.connect(self.setfill)

        self.drawButtons(MainWindow)

    def createNewImage(self):
        self.color = str(self.colorBox.currentText())
        s = str(self.sizeBox.currentText()).split("x")
        self.size = int(s[0])

        self.setupMainUi(MainWindow)

    def createLoadedImage(self):
        self.loaded = True

        s = str(self.size).split("x")

        self.size = int(s[0])
        self.setupMainUi(MainWindow)

    def drawButtons(self, MainWindow):
        self.buttons["Size"] = str(self.size) + "x" + str(self.size)
        self.count = 0
        button_pos = {"4": "385,225",
                      "6": "360,200",
                      "8": "335,175",
                      "10": "315,150",
                      "12": "275,135",
                      "16": "225,100",
                      "20": "175,65",
                      "24": "130,35",
                      "25": "117,22",}

        pos = str(button_pos[str(self.size)]).split(",")
        y = int(pos[1])

        if self.loaded == False:
            for _ in range(0,self.size):
                x = int(pos[0])

                for _ in range(0,self.size):
                    self.count += 1
                    self.buttons["Button"+str(self.count)] = [self.color,x,y]
                    self.b = QtWidgets.QPushButton(MainWindow)
                    self.b.setGeometry(QtCore.QRect(x, y, 25, 25))
                    self.b.setText("")
                    self.b.setStyleSheet("background-color: " + str(self.color) + ";")
                    self.b.clicked.connect(lambda x=self.size,index=self.count: self.changeColor(MainWindow,index))
                    self.b.setVisible(True)

                    x += 23

                y += 23
        else:
            for _ in range(0,self.size):
                x = int(pos[0])

                for _ in range(0,self.size):
                    self.count += 1
                    data = self.buttons["Button"+str(self.count)]

                    color = data[0]
                    x = data[1]
                    y = data[2]
                    self.buttons["Button"+str(self.count)] = [color,x,y]
                    self.b = QtWidgets.QPushButton(MainWindow)
                    self.b.setGeometry(QtCore.QRect(x, y, 25, 25))
                    self.b.setText("")
                    self.b.setStyleSheet("background-color: " + str(color) + ";")
                    self.b.clicked.connect(lambda x=self.size,index=self.count: self.changeColor(MainWindow,index))
                    self.b.setVisible(True)

                    x += 23

                y += 23

    def changeColor(self, MainWindow,index):
        if self.ishorizontal:
            self.paintHorizontal(MainWindow,index)
        elif self.isvertical:
            self.paintVertical(MainWindow,index)
        elif self.isfill:
            self.fill(MainWindow,index)
        else:

            for _ in range(0,int(self.pensize)):

                for _ in range(0,int(self.pensize)):
                    try:
                        pos = self.buttons["Button"+str(index)]
                        x = pos[1]
                        y = pos[2]
                        self.b = QtWidgets.QPushButton(MainWindow)
                        self.b.setGeometry(QtCore.QRect(x, y, 25, 25))
                        self.b.setText("")
                        self.b.setStyleSheet("background-color: " + str(self.pencolor) + ";")
                        self.b.clicked.connect(lambda x=pos,index=index: self.changeColor(MainWindow,index))
                        self.b.setVisible(True)
                        self.buttons["Button"+str(index)] = [str(self.pencolor),x,y]

                        index += 1
                    except:
                        pass

                index = index - int(self.pensize)
                index += self.size

    def paintHorizontal(self, MainWindow,index):
        if index % self.size == 0:
            row = index / self.size
        else:
            row = m.ceil(index / self.size)

        correctrow = ((row - 1) * self.size) + 1

        for x in range(0,self.size):
            index = correctrow

            pos = self.buttons["Button"+str(int(index))]
            x = pos[1]
            y = pos[2]

            self.b = QtWidgets.QPushButton(MainWindow)
            self.b.setGeometry(QtCore.QRect(x, y, 25, 25))
            self.b.setText("")
            self.b.setStyleSheet("background-color: " + str(self.pencolor) + ";")
            self.b.clicked.connect(lambda x=pos,index=index: self.changeColor(MainWindow,index))
            self.b.setVisible(True)
            self.buttons["Button"+str(index)] = [str(self.pencolor),x,y]

            correctrow += 1

    def paintVertical(self, MainWindow, index):
        if index % self.size == 0:
            row = index / self.size
        else:
            row = m.ceil(index / self.size)

        neededdown = int(self.size) - row

        x = index
        for _ in range(1,int(neededdown)+1):
            x += int(self.size)

        correctbutton = x

        for _ in range(0,self.size):
            index = correctbutton

            pos = self.buttons["Button"+str(int(index))]

            x = pos[1]
            y = pos[2]

            self.b = QtWidgets.QPushButton(MainWindow)
            self.b.setGeometry(QtCore.QRect(x, y, 25, 25))
            self.b.setText("")
            self.b.setStyleSheet("background-color: " + str(self.pencolor) + ";")
            self.b.clicked.connect(lambda x=pos,index=index: self.changeColor(MainWindow,index))
            self.b.setVisible(True)
            self.buttons["Button"+str(index)] = [str(self.pencolor),x,y]

            correctbutton -= self.size

    def fill(self,MainWindow,index):
        col = self.buttons["Button"+str(index)]
        color = col[0]

        for button in range(1,(self.size*self.size)+1):
            pos = self.buttons["Button"+str(int(button))]
            col = pos[0]

            x = pos[1]
            y = pos[2]

            if col == color:
                self.b = QtWidgets.QPushButton(MainWindow)
                self.b.setGeometry(QtCore.QRect(x, y, 25, 25))
                self.b.setText("")
                self.b.setStyleSheet("background-color: " + str(self.pencolor) + ";")
                self.b.clicked.connect(lambda x=pos,index=button: self.changeColor(MainWindow,index))
                self.b.setVisible(True)
                self.buttons["Button"+str(button)] = [str(self.pencolor),x,y]

    def sethorizontal(self):
        self.isvertical = False
        self.isfill = False
        self.ishorizontal = True

    def setvertical(self):
        self.ishorizontal = False
        self.isfill = False
        self.isvertical = True

    def setfill(self):
        self.ishorizontal = False
        self.isvertical = False
        self.isfill = True

    def changePenColor(self,MainWindow,color):
        self.pencolor = color

    def changePenSize(self,MainWindow,size):
        self.ishorizontal = False
        self.isvertical = False
        self.isfill = False

        self.pensize = size
        if int(self.pensize) > int(self.size):
            self.pensize = self.size

    def rubber(self,MainWindow):
        self.pencolor = "white"

    def showAbout(self,MainWindow):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("Button Paint v1.0 Coded by SP4R0W")
        msg.setIcon(QtWidgets.QMessageBox.Information)

        x = msg.exec_()

    def showHelp(self,MainWindow):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Help")
        msg.setText("If you want to switch back to regular pen, click on the pen size button.")
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        x = msg.exec_()

    def save(self,MainWindow):
        if self.directory == "":
            self.saveAs(MainWindow)
        else:
            savefile = open(self.directory,'wb')
            pickle.dump(self.buttons,savefile)
            savefile.close()

    def saveAs(self,MainWindow):
        saveDirectory = QtWidgets.QFileDialog.getSaveFileName(MainWindow,"Select directory to save",r"C:","Pickle files (*.pickle)")
        try:
            self.directory = saveDirectory[0]
            savefile = open(saveDirectory[0],'wb')
            pickle.dump(self.buttons,savefile)
            savefile.close()
        except:
            pass

    def load(self,MainWindow):
        try:
            loadLocation = QtWidgets.QFileDialog.getOpenFileName(caption="Open a file",directory=r"C:",filter="Pickle files (*.pickle)")
            self.directory = loadLocation[0]

            loadFile = open(loadLocation[0],'rb')
            self.buttons = pickle.load(loadFile)

            self.size = self.buttons["Size"]

            self.createLoadedImage()
        except:
            pass

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupStartUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())