# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TicketInfo.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_TicketInfo(object):
    def setupUi(self, TicketInfo):
        if not TicketInfo.objectName():
            TicketInfo.setObjectName(u"TicketInfo")
        TicketInfo.resize(650, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TicketInfo.sizePolicy().hasHeightForWidth())
        TicketInfo.setSizePolicy(sizePolicy)
        TicketInfo.setMinimumSize(QSize(450, 390))
        TicketInfo.setMaximumSize(QSize(650, 750))
        TicketInfo.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        TicketInfo.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        TicketInfo.setStyleSheet(u"QWidget {\n"
"    background-color: #22272e; /* background1000 */\n"
"}\n"
"\n"
"QWidget#someWidget {\n"
"    background-color: #272e35; /* background500 */\n"
"}\n"
"\n"
"QWidget#anotherWidget {\n"
"    background-color: #6d7887; /* background250 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4895ef; /* background-dominant1 */\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: #22272e; /* background-dominant2 */\n"
"}\n"
"\n"
"QFont {\n"
"font: 600 14pt \"Noto Sans Mono Medium\";\n"
"}")
        self.Button_Exit = QPushButton(TicketInfo)
        self.Button_Exit.setObjectName(u"Button_Exit")
        self.Button_Exit.setGeometry(QRect(530, 710, 101, 31))
        font = QFont()
        font.setFamilies([u"Noto Sans Mono Black"])
        font.setPointSize(11)
        font.setWeight(QFont.Black)
        font.setItalic(False)
        self.Button_Exit.setFont(font)
        self.Button_Exit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Button_Exit.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Button_Exit.setStyleSheet(u"QPushButton {\n"
"	font: 900 11pt \"Noto Sans Mono Black\";\n"
"	color: rgb(255,255,255);\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,30);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,100);\n"
"}")
        self.Line_Where_From_On = QLineEdit(TicketInfo)
        self.Line_Where_From_On.setObjectName(u"Line_Where_From_On")
        self.Line_Where_From_On.setGeometry(QRect(30, 200, 91, 31))
        self.Line_Where_From_On.setMaximumSize(QSize(1920, 1080))
        self.Line_Where_From_On.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_Where_From_On.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_Where_From_On.setAcceptDrops(True)
        self.Line_Where_From_On.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_Where_From_On.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Line_Where_From_On.setDragEnabled(False)
        self.Line_Where_From_On.setReadOnly(True)
        self.Line_Where_From_On.setClearButtonEnabled(False)
        self.Line_When = QLineEdit(TicketInfo)
        self.Line_When.setObjectName(u"Line_When")
        self.Line_When.setGeometry(QRect(30, 240, 181, 31))
        self.Line_When.setMaximumSize(QSize(1920, 1080))
        self.Line_When.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_When.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_When.setAcceptDrops(True)
        self.Line_When.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_When.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Line_When.setDragEnabled(False)
        self.Line_When.setReadOnly(True)
        self.Line_When.setClearButtonEnabled(False)
        self.Line_What_Time = QLineEdit(TicketInfo)
        self.Line_What_Time.setObjectName(u"Line_What_Time")
        self.Line_What_Time.setGeometry(QRect(30, 280, 181, 31))
        self.Line_What_Time.setMaximumSize(QSize(1920, 1080))
        self.Line_What_Time.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_What_Time.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_What_Time.setAcceptDrops(True)
        self.Line_What_Time.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Line_What_Time.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_What_Time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Line_What_Time.setDragEnabled(False)
        self.Line_What_Time.setReadOnly(True)
        self.Line_What_Time.setClearButtonEnabled(False)
        self.Line_NameWinInfoByTicket = QLineEdit(TicketInfo)
        self.Line_NameWinInfoByTicket.setObjectName(u"Line_NameWinInfoByTicket")
        self.Line_NameWinInfoByTicket.setGeometry(QRect(20, 10, 611, 31))
        self.Line_NameWinInfoByTicket.setMaximumSize(QSize(1920, 1080))
        self.Line_NameWinInfoByTicket.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_NameWinInfoByTicket.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_NameWinInfoByTicket.setAcceptDrops(True)
        self.Line_NameWinInfoByTicket.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_NameWinInfoByTicket.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Line_NameWinInfoByTicket.setDragEnabled(False)
        self.Line_NameWinInfoByTicket.setReadOnly(True)
        self.Line_NameWinInfoByTicket.setClearButtonEnabled(False)
        self.Line_WhatNameAirCompany = QLineEdit(TicketInfo)
        self.Line_WhatNameAirCompany.setObjectName(u"Line_WhatNameAirCompany")
        self.Line_WhatNameAirCompany.setGeometry(QRect(30, 50, 171, 31))
        self.Line_WhatNameAirCompany.setMaximumSize(QSize(1920, 1080))
        self.Line_WhatNameAirCompany.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_WhatNameAirCompany.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_WhatNameAirCompany.setAcceptDrops(True)
        self.Line_WhatNameAirCompany.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_WhatNameAirCompany.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Line_WhatNameAirCompany.setDragEnabled(False)
        self.Line_WhatNameAirCompany.setReadOnly(True)
        self.Line_WhatNameAirCompany.setClearButtonEnabled(False)
        self.NoneLine1 = QLineEdit(TicketInfo)
        self.NoneLine1.setObjectName(u"NoneLine1")
        self.NoneLine1.setGeometry(QRect(10, 90, 631, 21))
        self.NoneLine1.setMaximumSize(QSize(1920, 1080))
        self.NoneLine1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.NoneLine1.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.NoneLine1.setAcceptDrops(True)
        self.NoneLine1.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.NoneLine1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NoneLine1.setDragEnabled(False)
        self.NoneLine1.setReadOnly(True)
        self.NoneLine1.setClearButtonEnabled(False)
        self.NoneLine2 = QLineEdit(TicketInfo)
        self.NoneLine2.setObjectName(u"NoneLine2")
        self.NoneLine2.setGeometry(QRect(10, 680, 631, 21))
        self.NoneLine2.setMaximumSize(QSize(1920, 1080))
        self.NoneLine2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.NoneLine2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.NoneLine2.setAcceptDrops(True)
        self.NoneLine2.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.NoneLine2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NoneLine2.setDragEnabled(False)
        self.NoneLine2.setReadOnly(True)
        self.NoneLine2.setClearButtonEnabled(False)
        self.Button_GoBuyTicket = QPushButton(TicketInfo)
        self.Button_GoBuyTicket.setObjectName(u"Button_GoBuyTicket")
        self.Button_GoBuyTicket.setGeometry(QRect(20, 710, 131, 31))
        self.Button_GoBuyTicket.setFont(font)
        self.Button_GoBuyTicket.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Button_GoBuyTicket.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Button_GoBuyTicket.setStyleSheet(u"QPushButton {\n"
"	font: 900 11pt \"Noto Sans Mono Black\";\n"
"	color: rgb(255,255,255);\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,30);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,100);\n"
"}")
        self.Line_Service = QLineEdit(TicketInfo)
        self.Line_Service.setObjectName(u"Line_Service")
        self.Line_Service.setGeometry(QRect(30, 120, 171, 31))
        self.Line_Service.setMaximumSize(QSize(1920, 1080))
        self.Line_Service.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_Service.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_Service.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Line_Service.setReadOnly(True)
        self.label = QLabel(TicketInfo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 120, 251, 31))
        self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.labelCompanyName = QLabel(TicketInfo)
        self.labelCompanyName.setObjectName(u"labelCompanyName")
        self.labelCompanyName.setGeometry(QRect(370, 50, 251, 31))
        self.labelCompanyName.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.labelCompanyName.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.labelWhere = QLabel(TicketInfo)
        self.labelWhere.setObjectName(u"labelWhere")
        self.labelWhere.setGeometry(QRect(280, 160, 341, 31))
        self.labelWhere.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.labelWhere.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.labelWhen = QLabel(TicketInfo)
        self.labelWhen.setObjectName(u"labelWhen")
        self.labelWhen.setGeometry(QRect(360, 240, 261, 31))
        self.labelWhen.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.labelWhen.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.label_5 = QLabel(TicketInfo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 280, 181, 31))
        self.label_5.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label_5.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_Where_From_On_2 = QLineEdit(TicketInfo)
        self.Line_Where_From_On_2.setObjectName(u"Line_Where_From_On_2")
        self.Line_Where_From_On_2.setGeometry(QRect(30, 160, 91, 31))
        self.Line_Where_From_On_2.setMaximumSize(QSize(1920, 1080))
        self.Line_Where_From_On_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_Where_From_On_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_Where_From_On_2.setAcceptDrops(True)
        self.Line_Where_From_On_2.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_Where_From_On_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Line_Where_From_On_2.setDragEnabled(False)
        self.Line_Where_From_On_2.setReadOnly(True)
        self.Line_Where_From_On_2.setClearButtonEnabled(False)
        self.labelWhere_2 = QLabel(TicketInfo)
        self.labelWhere_2.setObjectName(u"labelWhere_2")
        self.labelWhere_2.setGeometry(QRect(280, 200, 341, 31))
        self.labelWhere_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.labelWhere_2.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_What_Time_2 = QLineEdit(TicketInfo)
        self.Line_What_Time_2.setObjectName(u"Line_What_Time_2")
        self.Line_What_Time_2.setGeometry(QRect(30, 320, 181, 31))
        self.Line_What_Time_2.setMaximumSize(QSize(1920, 1080))
        self.Line_What_Time_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_What_Time_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_What_Time_2.setAcceptDrops(True)
        self.Line_What_Time_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Line_What_Time_2.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_What_Time_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Line_What_Time_2.setDragEnabled(False)
        self.Line_What_Time_2.setReadOnly(True)
        self.Line_What_Time_2.setClearButtonEnabled(False)
        self.label_6 = QLabel(TicketInfo)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(440, 320, 181, 31))
        self.label_6.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label_6.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.NoneLine1_2 = QLineEdit(TicketInfo)
        self.NoneLine1_2.setObjectName(u"NoneLine1_2")
        self.NoneLine1_2.setGeometry(QRect(240, 120, 16, 551))
        self.NoneLine1_2.setMaximumSize(QSize(1920, 1080))
        self.NoneLine1_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.NoneLine1_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.NoneLine1_2.setAcceptDrops(True)
        self.NoneLine1_2.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.NoneLine1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NoneLine1_2.setDragEnabled(False)
        self.NoneLine1_2.setReadOnly(True)
        self.NoneLine1_2.setClearButtonEnabled(False)
        self.Line_When_ON_10 = QLineEdit(TicketInfo)
        self.Line_When_ON_10.setObjectName(u"Line_When_ON_10")
        self.Line_When_ON_10.setGeometry(QRect(10, 360, 211, 31))
        self.Line_When_ON_10.setMaximumSize(QSize(1920, 1080))
        self.Line_When_ON_10.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_When_ON_10.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_When_ON_10.setAcceptDrops(True)
        self.Line_When_ON_10.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_When_ON_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Line_When_ON_10.setDragEnabled(False)
        self.Line_When_ON_10.setReadOnly(True)
        self.Line_When_ON_10.setClearButtonEnabled(False)
        self.NoneLine1_3 = QLineEdit(TicketInfo)
        self.NoneLine1_3.setObjectName(u"NoneLine1_3")
        self.NoneLine1_3.setGeometry(QRect(10, 400, 171, 21))
        self.NoneLine1_3.setMaximumSize(QSize(1920, 1080))
        self.NoneLine1_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.NoneLine1_3.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.NoneLine1_3.setAcceptDrops(True)
        self.NoneLine1_3.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.NoneLine1_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NoneLine1_3.setDragEnabled(False)
        self.NoneLine1_3.setReadOnly(True)
        self.NoneLine1_3.setClearButtonEnabled(False)
        self.label_7 = QLabel(TicketInfo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(440, 360, 181, 31))
        self.label_7.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label_7.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.NoneLine1_4 = QLineEdit(TicketInfo)
        self.NoneLine1_4.setObjectName(u"NoneLine1_4")
        self.NoneLine1_4.setGeometry(QRect(290, 400, 341, 21))
        self.NoneLine1_4.setMaximumSize(QSize(1920, 1080))
        self.NoneLine1_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.NoneLine1_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.NoneLine1_4.setAcceptDrops(True)
        self.NoneLine1_4.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.NoneLine1_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NoneLine1_4.setDragEnabled(False)
        self.NoneLine1_4.setReadOnly(True)
        self.NoneLine1_4.setClearButtonEnabled(False)
        self.Line_When_ON_11 = QLineEdit(TicketInfo)
        self.Line_When_ON_11.setObjectName(u"Line_When_ON_11")
        self.Line_When_ON_11.setGeometry(QRect(10, 430, 211, 31))
        self.Line_When_ON_11.setMaximumSize(QSize(1920, 1080))
        self.Line_When_ON_11.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_When_ON_11.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_When_ON_11.setAcceptDrops(True)
        self.Line_When_ON_11.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_When_ON_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Line_When_ON_11.setDragEnabled(False)
        self.Line_When_ON_11.setReadOnly(True)
        self.Line_When_ON_11.setClearButtonEnabled(False)
        self.lineEdit = QLineEdit(TicketInfo)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 430, 361, 31))
        self.lineEdit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.lineEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_When_ON_12 = QLineEdit(TicketInfo)
        self.Line_When_ON_12.setObjectName(u"Line_When_ON_12")
        self.Line_When_ON_12.setGeometry(QRect(10, 470, 211, 31))
        self.Line_When_ON_12.setMaximumSize(QSize(1920, 1080))
        self.Line_When_ON_12.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_When_ON_12.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_When_ON_12.setAcceptDrops(True)
        self.Line_When_ON_12.setStyleSheet(u"font: 700 12pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_When_ON_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Line_When_ON_12.setDragEnabled(False)
        self.Line_When_ON_12.setReadOnly(True)
        self.Line_When_ON_12.setClearButtonEnabled(False)
        self.lineEdit_2 = QLineEdit(TicketInfo)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(270, 470, 361, 31))
        self.lineEdit_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_2.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ButtonSelectService = QPushButton(TicketInfo)
        self.ButtonSelectService.setObjectName(u"ButtonSelectService")
        self.ButtonSelectService.setGeometry(QRect(310, 510, 291, 24))
        self.ButtonSelectService.setStyleSheet(u"QPushButton {\n"
"	font: 900 11pt \"Noto Sans Mono Black\";\n"
"	color: rgb(255,255,255);\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,30);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,100);\n"
"}")
        self.Line_When_ON_13 = QLineEdit(TicketInfo)
        self.Line_When_ON_13.setObjectName(u"Line_When_ON_13")
        self.Line_When_ON_13.setGeometry(QRect(10, 630, 211, 31))
        self.Line_When_ON_13.setMaximumSize(QSize(1920, 1080))
        self.Line_When_ON_13.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_When_ON_13.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_When_ON_13.setAcceptDrops(True)
        self.Line_When_ON_13.setStyleSheet(u"font: 700 12pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_When_ON_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Line_When_ON_13.setDragEnabled(False)
        self.Line_When_ON_13.setReadOnly(True)
        self.Line_When_ON_13.setClearButtonEnabled(False)
        self.lineEdit_3 = QLineEdit(TicketInfo)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(270, 630, 141, 31))
        self.lineEdit_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit_3.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_3.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_When_ON_14 = QLineEdit(TicketInfo)
        self.Line_When_ON_14.setObjectName(u"Line_When_ON_14")
        self.Line_When_ON_14.setGeometry(QRect(10, 550, 211, 31))
        self.Line_When_ON_14.setMaximumSize(QSize(1920, 1080))
        self.Line_When_ON_14.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_When_ON_14.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_When_ON_14.setAcceptDrops(True)
        self.Line_When_ON_14.setStyleSheet(u"font: 700 12pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_When_ON_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Line_When_ON_14.setDragEnabled(False)
        self.Line_When_ON_14.setReadOnly(True)
        self.Line_When_ON_14.setClearButtonEnabled(False)
        self.ButtonSelectService_2 = QPushButton(TicketInfo)
        self.ButtonSelectService_2.setObjectName(u"ButtonSelectService_2")
        self.ButtonSelectService_2.setGeometry(QRect(310, 590, 291, 24))
        self.ButtonSelectService_2.setStyleSheet(u"QPushButton {\n"
"	font: 900 11pt \"Noto Sans Mono Black\";\n"
"	color: rgb(255,255,255);\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,30);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,100);\n"
"}")
        self.lineEdit_4 = QLineEdit(TicketInfo)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(270, 550, 361, 31))
        self.lineEdit_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.lineEdit_4.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(TicketInfo)

        QMetaObject.connectSlotsByName(TicketInfo)
    # setupUi

    def retranslateUi(self, TicketInfo):
        TicketInfo.setWindowTitle(QCoreApplication.translate("TicketInfo", u"TicketInfo", None))
        self.Button_Exit.setText(QCoreApplication.translate("TicketInfo", u"\u0412\u044b\u0439\u0434\u0438", None))
        self.Line_Where_From_On.setText(QCoreApplication.translate("TicketInfo", u"\u041a\u0443\u0434\u0430: ", None))
        self.Line_Where_From_On.setPlaceholderText("")
        self.Line_When.setText(QCoreApplication.translate("TicketInfo", u"\u041a\u043e\u0433\u0434\u0430:", None))
        self.Line_When.setPlaceholderText("")
        self.Line_What_Time.setText(QCoreApplication.translate("TicketInfo", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043b\u0435\u0442\u0430:", None))
        self.Line_What_Time.setPlaceholderText("")
        self.Line_NameWinInfoByTicket.setText(QCoreApplication.translate("TicketInfo", u"-- \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0431\u0438\u043b\u0435\u0442\u0435 --", None))
        self.Line_NameWinInfoByTicket.setPlaceholderText("")
        self.Line_WhatNameAirCompany.setText(QCoreApplication.translate("TicketInfo", u"\u0410\u0432\u0438\u0430\u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f:", None))
        self.Line_WhatNameAirCompany.setPlaceholderText("")
        self.NoneLine1.setText("")
        self.NoneLine1.setPlaceholderText("")
        self.NoneLine2.setText("")
        self.NoneLine2.setPlaceholderText("")
        self.Button_GoBuyTicket.setText(QCoreApplication.translate("TicketInfo", u"\u041a\u0443\u043f\u0438\u0442\u044c \u0431\u0438\u043b\u0435\u0442", None))
        self.Line_Service.setText(QCoreApplication.translate("TicketInfo", u"\u041d\u043e\u043c\u0435\u0440 \u0440\u0435\u0439\u0441\u0430:", None))
        self.label.setText("")
        self.labelCompanyName.setText("")
        self.labelWhere.setText("")
        self.labelWhen.setText("")
        self.label_5.setText("")
        self.Line_Where_From_On_2.setText(QCoreApplication.translate("TicketInfo", u"\u041e\u0442\u043a\u0443\u0434\u0430:", None))
        self.Line_Where_From_On_2.setPlaceholderText("")
        self.labelWhere_2.setText("")
        self.Line_What_Time_2.setText(QCoreApplication.translate("TicketInfo", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0430\u0441\u0430\u0434\u043a\u0438:", None))
        self.Line_What_Time_2.setPlaceholderText("")
        self.label_6.setText("")
        self.NoneLine1_2.setText("")
        self.NoneLine1_2.setPlaceholderText("")
        self.Line_When_ON_10.setText(QCoreApplication.translate("TicketInfo", u"\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438 \u0431\u0438\u043b\u0435\u0442\u043e\u0432:", None))
        self.Line_When_ON_10.setPlaceholderText("")
        self.NoneLine1_3.setText("")
        self.NoneLine1_3.setPlaceholderText("")
        self.label_7.setText("")
        self.NoneLine1_4.setText("")
        self.NoneLine1_4.setPlaceholderText("")
        self.Line_When_ON_11.setText(QCoreApplication.translate("TicketInfo", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043e \u0431\u0438\u043b\u0435\u0442\u043e\u0432:", None))
        self.Line_When_ON_11.setPlaceholderText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("TicketInfo", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.Line_When_ON_12.setText(QCoreApplication.translate("TicketInfo", u"\u0421\u0435\u0440\u0432\u0438\u0441 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f:", None))
        self.Line_When_ON_12.setPlaceholderText("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("TicketInfo", u"\u0421\u0435\u0440\u0432\u0438\u0441 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.ButtonSelectService.setText(QCoreApplication.translate("TicketInfo", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u0447\u0442\u043e\u0431\u044b \u0432\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.Line_When_ON_13.setText(QCoreApplication.translate("TicketInfo", u"\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430:", None))
        self.Line_When_ON_13.setPlaceholderText("")
        self.lineEdit_3.setText(QCoreApplication.translate("TicketInfo", u"0", None))
        self.lineEdit_3.setPlaceholderText("")
        self.Line_When_ON_14.setText(QCoreApplication.translate("TicketInfo", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b:", None))
        self.Line_When_ON_14.setPlaceholderText("")
        self.ButtonSelectService_2.setText(QCoreApplication.translate("TicketInfo", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \u0447\u0442\u043e\u0431\u044b \u0432\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("TicketInfo", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u043f\u043e\u0441\u043e\u0431 \u043e\u043f\u043b\u0430\u0442\u044b", None))
    # retranslateUi

