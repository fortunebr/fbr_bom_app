from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(877, 636)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icons/favicon.ico"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "QWidget{ background-color:rgb(202, 234, 255) }\n"
            "\n"
            "QMenuBar::item:selected{ background: rgb(235, 248, 255) }\n"
            "\n"
            "QMenu::item:selected {  background:rgb(65, 163, 255) }\n"
            "\n"
            "QLabel{background-color:transparent;border:0px}\n"
            "\n"
            ""
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "QPushButton::pressed {  background:rgb(144, 198, 255) }\n" ""
        )
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(3, 1, 871, 591))
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")
        self.main_left_frame = QtWidgets.QFrame(self.main_frame)
        self.main_left_frame.setGeometry(QtCore.QRect(8, 8, 310, 581))
        self.main_left_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_left_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_left_frame.setObjectName("main_left_frame")
        self.layoutWidget = QtWidgets.QWidget(self.main_left_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 27, 296, 535))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMaximumSize
        )
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(
            2,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(280, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.tableView = QtWidgets.QTableView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(280, 300))
        self.tableView.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            30,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem2)
        self.button_show_stats = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_show_stats.sizePolicy().hasHeightForWidth()
        )
        self.button_show_stats.setSizePolicy(sizePolicy)
        self.button_show_stats.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.button_show_stats.setFont(font)
        self.button_show_stats.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_show_stats.setObjectName("button_show_stats")
        self.horizontalLayout_2.addWidget(self.button_show_stats)
        spacerItem3 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(
            20,
            13,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_export_xl = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_export_xl.sizePolicy().hasHeightForWidth()
        )
        self.button_export_xl.setSizePolicy(sizePolicy)
        self.button_export_xl.setMinimumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.button_export_xl.setFont(font)
        self.button_export_xl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_export_xl.setObjectName("button_export_xl")
        self.horizontalLayout.addWidget(self.button_export_xl)
        spacerItem5 = QtWidgets.QSpacerItem(
            50,
            30,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem5)
        self.button_export_summary = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_export_summary.sizePolicy().hasHeightForWidth()
        )
        self.button_export_summary.setSizePolicy(sizePolicy)
        self.button_export_summary.setMinimumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.button_export_summary.setFont(font)
        self.button_export_summary.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight
        )
        self.button_export_summary.setObjectName("button_export_summary")
        self.horizontalLayout.addWidget(self.button_export_summary)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(
            2,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_credits = QtWidgets.QLabel(self.main_frame)
        self.label_credits.setGeometry(QtCore.QRect(580, 560, 281, 31))
        self.label_credits.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_credits.setObjectName("label_credits")
        self.widget_status = QtWidgets.QWidget(self.main_frame)
        self.widget_status.setGeometry(QtCore.QRect(320, 50, 541, 431))
        self.widget_status.setObjectName("widget_status")
        self.button_export_xl_sub = QtWidgets.QPushButton(self.widget_status)
        self.button_export_xl_sub.setGeometry(QtCore.QRect(490, 30, 41, 31))
        self.button_export_xl_sub.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("ui\\../icons/file-export-solid.svg"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.button_export_xl_sub.setIcon(icon1)
        self.button_export_xl_sub.setObjectName("button_export_xl_sub")
        self.label_article = QtWidgets.QLabel(self.widget_status)
        self.label_article.setGeometry(QtCore.QRect(110, 30, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_article.setFont(font)
        self.label_article.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_article.setObjectName("label_article")
        self.line = QtWidgets.QFrame(self.widget_status)
        self.line.setGeometry(QtCore.QRect(110, 60, 331, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget_status)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 90, 531, 301))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_2.setMaximumSize(QtCore.QSize(122, 63))
        self.widget_2.setStyleSheet(
            "background-color:rgb(255, 255, 255);\n"
            "border:1px solid black;\n"
            "border-radius:20px;"
        )
        self.widget_2.setObjectName("widget_2")
        self.label_stich = QtWidgets.QLabel(self.widget_2)
        self.label_stich.setEnabled(True)
        self.label_stich.setGeometry(QtCore.QRect(10, 10, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stich.sizePolicy().hasHeightForWidth())
        self.label_stich.setSizePolicy(sizePolicy)
        self.label_stich.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_stich.setFont(font)
        self.label_stich.setAutoFillBackground(False)
        self.label_stich.setStyleSheet("border:0px solid transperant;")
        self.label_stich.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_stich.setObjectName("label_stich")
        self.label_Vstitch = QtWidgets.QLabel(self.widget_2)
        self.label_Vstitch.setGeometry(QtCore.QRect(10, 30, 100, 29))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Vstitch.setFont(font)
        self.label_Vstitch.setStyleSheet("border:0px;")
        self.label_Vstitch.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_Vstitch.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Vstitch.setObjectName("label_Vstitch")
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_3.setMaximumSize(QtCore.QSize(122, 65))
        self.widget_3.setStyleSheet(
            "background-color:rgb(255, 255, 255);\n"
            "border:1px solid black;\n"
            "border-radius:20px;"
        )
        self.widget_3.setObjectName("widget_3")
        self.label_print = QtWidgets.QLabel(self.widget_3)
        self.label_print.setEnabled(True)
        self.label_print.setGeometry(QtCore.QRect(10, 10, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_print.sizePolicy().hasHeightForWidth())
        self.label_print.setSizePolicy(sizePolicy)
        self.label_print.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_print.setFont(font)
        self.label_print.setAutoFillBackground(False)
        self.label_print.setStyleSheet("border:0px;")
        self.label_print.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_print.setObjectName("label_print")
        self.label_Vprint = QtWidgets.QLabel(self.widget_3)
        self.label_Vprint.setGeometry(QtCore.QRect(10, 30, 100, 29))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Vprint.setFont(font)
        self.label_Vprint.setStyleSheet("border:0px;")
        self.label_Vprint.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_Vprint.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Vprint.setObjectName("label_Vprint")
        self.horizontalLayout_4.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_4.setMaximumSize(QtCore.QSize(122, 65))
        self.widget_4.setStyleSheet(
            "background-color:rgb(255, 255, 255);\n"
            "border:1px solid black;\n"
            "border-radius:20px;"
        )
        self.widget_4.setObjectName("widget_4")
        self.label_mc = QtWidgets.QLabel(self.widget_4)
        self.label_mc.setEnabled(True)
        self.label_mc.setGeometry(QtCore.QRect(10, 10, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mc.sizePolicy().hasHeightForWidth())
        self.label_mc.setSizePolicy(sizePolicy)
        self.label_mc.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_mc.setFont(font)
        self.label_mc.setAutoFillBackground(False)
        self.label_mc.setStyleSheet("border:0px;")
        self.label_mc.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_mc.setObjectName("label_mc")
        self.label_Vmc = QtWidgets.QLabel(self.widget_4)
        self.label_Vmc.setGeometry(QtCore.QRect(10, 30, 100, 29))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Vmc.setFont(font)
        self.label_Vmc.setStyleSheet("border:0px;")
        self.label_Vmc.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_Vmc.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Vmc.setObjectName("label_Vmc")
        self.horizontalLayout_4.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_5.setMaximumSize(QtCore.QSize(122, 65))
        self.widget_5.setStyleSheet(
            "background-color:rgb(255, 255, 255);\n"
            "border:1px solid black;\n"
            "border-radius:20px;"
        )
        self.widget_5.setObjectName("widget_5")
        self.label_cop = QtWidgets.QLabel(self.widget_5)
        self.label_cop.setEnabled(True)
        self.label_cop.setGeometry(QtCore.QRect(10, 10, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cop.sizePolicy().hasHeightForWidth())
        self.label_cop.setSizePolicy(sizePolicy)
        self.label_cop.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_cop.setFont(font)
        self.label_cop.setAutoFillBackground(False)
        self.label_cop.setStyleSheet("border:0px;")
        self.label_cop.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cop.setObjectName("label_cop")
        self.label_Vcop = QtWidgets.QLabel(self.widget_5)
        self.label_Vcop.setGeometry(QtCore.QRect(10, 30, 100, 29))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Vcop.setFont(font)
        self.label_Vcop.setStyleSheet("border:0px;")
        self.label_Vcop.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_Vcop.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Vcop.setObjectName("label_Vcop")
        self.horizontalLayout_4.addWidget(self.widget_5)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_6.setMinimumSize(QtCore.QSize(120, 0))
        self.widget_6.setMaximumSize(QtCore.QSize(122, 65))
        self.widget_6.setStyleSheet(
            "background-color:rgb(255, 255, 255);\n"
            "border:1px solid black;\n"
            "border-radius:20px;"
        )
        self.widget_6.setObjectName("widget_6")
        self.label_Vbasic = QtWidgets.QLabel(self.widget_6)
        self.label_Vbasic.setGeometry(QtCore.QRect(10, 30, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Vbasic.setFont(font)
        self.label_Vbasic.setStyleSheet("border:0px;")
        self.label_Vbasic.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_Vbasic.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Vbasic.setObjectName("label_Vbasic")
        self.label_basic = QtWidgets.QLabel(self.widget_6)
        self.label_basic.setEnabled(True)
        self.label_basic.setGeometry(QtCore.QRect(10, 10, 100, 15))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_basic.sizePolicy().hasHeightForWidth())
        self.label_basic.setSizePolicy(sizePolicy)
        self.label_basic.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_basic.setFont(font)
        self.label_basic.setAutoFillBackground(False)
        self.label_basic.setStyleSheet("border:0px;")
        self.label_basic.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_basic.setObjectName("label_basic")
        self.horizontalLayout_5.addWidget(self.widget_6)
        self.widget = QtWidgets.QWidget(self.layoutWidget1)
        self.widget.setMinimumSize(QtCore.QSize(120, 120))
        self.widget.setMaximumSize(QtCore.QSize(160, 140))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.widget.setFont(font)
        self.widget.setStyleSheet(
            "background-color:rgb(255, 255, 255);\n"
            "border:1px solid black;\n"
            "border-radius:60px;"
        )
        self.widget.setObjectName("widget")
        self.label_netm = QtWidgets.QLabel(self.widget)
        self.label_netm.setEnabled(True)
        self.label_netm.setGeometry(QtCore.QRect(30, 10, 100, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_netm.sizePolicy().hasHeightForWidth())
        self.label_netm.setSizePolicy(sizePolicy)
        self.label_netm.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_netm.setFont(font)
        self.label_netm.setAutoFillBackground(False)
        self.label_netm.setStyleSheet("border:0px;\n" "background-color:transparent;")
        self.label_netm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_netm.setObjectName("label_netm")
        self.label_Vnetm = QtWidgets.QLabel(self.widget)
        self.label_Vnetm.setGeometry(QtCore.QRect(10, 40, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_Vnetm.setFont(font)
        self.label_Vnetm.setStyleSheet("border:0px;\n" "background-color:transparent;")
        self.label_Vnetm.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_Vnetm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Vnetm.setObjectName("label_Vnetm")
        self.horizontalLayout_5.addWidget(self.widget)
        self.widget_7 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_7.setMaximumSize(QtCore.QSize(122, 65))
        self.widget_7.setStyleSheet(
            "background-color:rgb(255, 255, 255);\n"
            "border:1px solid black;\n"
            "border-radius:20px;"
        )
        self.widget_7.setObjectName("widget_7")
        self.label_mrp = QtWidgets.QLabel(self.widget_7)
        self.label_mrp.setEnabled(True)
        self.label_mrp.setGeometry(QtCore.QRect(10, 10, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mrp.sizePolicy().hasHeightForWidth())
        self.label_mrp.setSizePolicy(sizePolicy)
        self.label_mrp.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_mrp.setFont(font)
        self.label_mrp.setAutoFillBackground(False)
        self.label_mrp.setStyleSheet("border:0px;")
        self.label_mrp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_mrp.setObjectName("label_mrp")
        self.label_Vmrp = QtWidgets.QLabel(self.widget_7)
        self.label_Vmrp.setGeometry(QtCore.QRect(10, 30, 100, 29))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Vmrp.setFont(font)
        self.label_Vmrp.setStyleSheet("border:0px;")
        self.label_Vmrp.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_Vmrp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Vmrp.setObjectName("label_Vmrp")
        self.horizontalLayout_5.addWidget(self.widget_7)
        self.verticalLayout_12.addLayout(self.horizontalLayout_5)
        self.textBrowser = QtWidgets.QTextBrowser(self.main_frame)
        self.textBrowser.setGeometry(QtCore.QRect(430, 180, 321, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.raise_()
        self.widget_status.raise_()
        self.main_left_frame.raise_()
        self.label_credits.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("")
        self.menuFile.setObjectName("menuFile")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setStyleSheet("")
        self.menuDatabase.setObjectName("menuDatabase")
        self.menuBulkUpgrade = QtWidgets.QMenu(self.menuDatabase)
        self.menuBulkUpgrade.setObjectName("menuBulkUpgrade")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("")
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionUpgradeBom = QtGui.QAction(MainWindow)
        self.actionUpgradeBom.setObjectName("actionUpgradeBom")
        self.actionAdd_New_Charges = QtGui.QAction(MainWindow)
        self.actionAdd_New_Charges.setObjectName("actionAdd_New_Charges")
        self.actionUpdate_Existing_Charges = QtGui.QAction(MainWindow)
        self.actionUpdate_Existing_Charges.setObjectName(
            "actionUpdate_Existing_Charges"
        )
        self.actionUpdate_From_File_2 = QtGui.QAction(MainWindow)
        self.actionUpdate_From_File_2.setObjectName("actionUpdate_From_File_2")
        self.actionAdd_New_Price = QtGui.QAction(MainWindow)
        self.actionAdd_New_Price.setObjectName("actionAdd_New_Price")
        self.actionUpdate_Existing_Price = QtGui.QAction(MainWindow)
        self.actionUpdate_Existing_Price.setObjectName("actionUpdate_Existing_Price")
        self.actionUpdate_From_File_3 = QtGui.QAction(MainWindow)
        self.actionUpdate_From_File_3.setObjectName("actionUpdate_From_File_3")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdateOS_Charges = QtGui.QAction(MainWindow)
        self.actionUpdateOS_Charges.setObjectName("actionUpdateOS_Charges")
        self.actionUpdatePrice_Structure = QtGui.QAction(MainWindow)
        self.actionUpdatePrice_Structure.setObjectName("actionUpdatePrice_Structure")
        self.actionUpgradeOS_Charge = QtGui.QAction(MainWindow)
        self.actionUpgradeOS_Charge.setObjectName("actionUpgradeOS_Charge")
        self.actionUpgradePrice_Structure = QtGui.QAction(MainWindow)
        self.actionUpgradePrice_Structure.setObjectName("actionUpgradePrice_Structure")
        self.actionUpdateFixed_Charges = QtGui.QAction(MainWindow)
        self.actionUpdateFixed_Charges.setObjectName("actionUpdateFixed_Charges")
        self.menuFile.addAction(self.actionClose)
        self.menuBulkUpgrade.addAction(self.actionUpgradeBom)
        self.menuBulkUpgrade.addAction(self.actionUpgradeOS_Charge)
        self.menuBulkUpgrade.addAction(self.actionUpgradePrice_Structure)
        self.menuDatabase.addAction(self.menuBulkUpgrade.menuAction())
        self.menuDatabase.addAction(self.actionUpdateOS_Charges)
        self.menuDatabase.addAction(self.actionUpdatePrice_Structure)
        self.menuDatabase.addAction(self.actionUpdateFixed_Charges)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Fortune Br - Bill of Materials")
        )
        self.button_show_stats.setText(_translate("MainWindow", "Show Stats"))
        self.button_export_xl.setText(_translate("MainWindow", "Export"))
        self.button_export_summary.setText(_translate("MainWindow", "Report"))
        self.label_credits.setText(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-style:italic; background-color:#ffffff;"> Made with </span><span style=" font-family:\'apple color emoji,segoe ui emoji,noto color emoji,android emoji,emojisymbols,emojione mozilla,twemoji mozilla,segoe ui symbol\'; font-size:11pt; font-weight:600; color:#ff0000; background-color:#ffffff;">❤️ </span><span style=" font-family:\'apple color emoji,segoe ui emoji,noto color emoji,android emoji,emojisymbols,emojione mozilla,twemoji mozilla,segoe ui symbol\'; font-weight:600; color:#ff0000; background-color:#ffffff;"> </span><span style=" font-size:10pt; font-style:italic; background-color:#ffffff;">from </span><span style=" font-size:10pt; font-weight:600; font-style:italic; background-color:#ffffff;">OM</span><span style=" font-size:10pt; font-style:italic; background-color:#ffffff;"> Dept - Fortune Branch  </span></p></body></html>',
            )
        )
        self.label_article.setText(_translate("MainWindow", "0000 Black Gents"))
        self.label_stich.setText(_translate("MainWindow", "Stitching Charge"))
        self.label_Vstitch.setText(_translate("MainWindow", "00.00"))
        self.label_print.setText(_translate("MainWindow", "Printing Charge"))
        self.label_Vprint.setText(_translate("MainWindow", "00.00"))
        self.label_mc.setText(_translate("MainWindow", "Material Cost"))
        self.label_Vmc.setText(_translate("MainWindow", "00.00"))
        self.label_cop.setText(_translate("MainWindow", "Cost of Production"))
        self.label_Vcop.setText(_translate("MainWindow", "00.00"))
        self.label_Vbasic.setText(_translate("MainWindow", "00.00"))
        self.label_basic.setText(_translate("MainWindow", "BASIC"))
        self.label_netm.setText(_translate("MainWindow", "Net Margin"))
        self.label_Vnetm.setText(_translate("MainWindow", "-00.00%"))
        self.label_mrp.setText(_translate("MainWindow", "MRP"))
        self.label_Vmrp.setText(_translate("MainWindow", "00.00"))
        self.textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">This can\'t be 100% accurate, however it is easy to try me.</span></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p align="right" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600; color:#00aaff;">#TEAM_Fortune_Branch</span> </p></body></html>',
            )
        )
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.menuBulkUpgrade.setTitle(_translate("MainWindow", "Bulk Upgrade"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionUpgradeBom.setText(_translate("MainWindow", "Bom"))
        self.actionAdd_New_Charges.setText(_translate("MainWindow", "Add New Charges"))
        self.actionUpdate_Existing_Charges.setText(
            _translate("MainWindow", "Update Existing Charges")
        )
        self.actionUpdate_From_File_2.setText(
            _translate("MainWindow", "Update From File")
        )
        self.actionAdd_New_Price.setText(_translate("MainWindow", "Add New Price"))
        self.actionUpdate_Existing_Price.setText(
            _translate("MainWindow", "Update Existing Price")
        )
        self.actionUpdate_From_File_3.setText(
            _translate("MainWindow", "Update From File")
        )
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdateOS_Charges.setText(_translate("MainWindow", "OS Charges"))
        self.actionUpdatePrice_Structure.setText(
            _translate("MainWindow", "Price Structure")
        )
        self.actionUpgradeOS_Charge.setText(_translate("MainWindow", "OS Charges"))
        self.actionUpgradePrice_Structure.setText(
            _translate("MainWindow", "Price Structure")
        )
        self.actionUpdateFixed_Charges.setText(
            _translate("MainWindow", "Fixed Charges")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
