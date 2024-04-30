# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SkyFly.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDateTimeEdit,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 600)
        MainWindow.setMinimumSize(QSize(960, 600))
        MainWindow.setMaximumSize(QSize(960, 600))
        font = QFont()
        font.setHintingPreference(QFont.PreferFullHinting)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #22272e; /* background1000 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4895ef; /* background-dominant1 */\n"
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
"QLabel {\n"
"    background-color: #cbd0df; /* background-dominant2 */\n"
"}\n"
"\n"
"QFont {\n"
"font: 600 14pt \"Noto Sans Mono Medium\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Line_Where_ON = QLineEdit(self.centralwidget)
        self.Line_Where_ON.setObjectName(u"Line_Where_ON")
        self.Line_Where_ON.setGeometry(QRect(20, 100, 241, 32))
        self.Line_Where_ON.setMaximumSize(QSize(1920, 1080))
        self.Line_Where_ON.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Line_Where_ON.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_Where_ON.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_Where_ON.setDragEnabled(False)
        self.Line_Where_ON.setClearButtonEnabled(True)
        self.Line_Where_OFF = QLineEdit(self.centralwidget)
        self.Line_Where_OFF.setObjectName(u"Line_Where_OFF")
        self.Line_Where_OFF.setGeometry(QRect(270, 100, 251, 32))
        self.Line_Where_OFF.setMaximumSize(QSize(1920, 1080))
        self.Line_Where_OFF.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Line_Where_OFF.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_Where_OFF.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_Where_OFF.setClearButtonEnabled(True)
        self.WhenBackDate = QDateEdit(self.centralwidget)
        self.WhenBackDate.setObjectName(u"WhenBackDate")
        self.WhenBackDate.setGeometry(QRect(380, 140, 141, 30))
        self.WhenBackDate.setMaximumSize(QSize(141, 30))
        self.WhenBackDate.setMouseTracking(False)
        self.WhenBackDate.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.WhenBackDate.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.WhenBackDate.setAutoFillBackground(False)
        self.WhenBackDate.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b QDateEdit */\n"
"QDateEdit {\n"
"    /* \u0421\u0442\u0438\u043b\u0438 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font: 700 14pt \"Noto Sans Mono\";\n"
"    /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    color: rgb(255, 255, 255);\n"
"    /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"    border-radius: 5px;\n"
"    /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    background-color: rgb(34, 39, 46);\n"
"    /* \u0426\u0432\u0435\u0442 \u0440\u0430\u043c\u043a\u0438 */\n"
"    border: 2px solid white;\n"
"    /* \u041f\u043b\u0430\u0432\u043d\u044b\u0435 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0434\u043b\u044f \u0430\u043d\u0438\u043c\u0430\u0446\u0438\u0438 */\n"
"    transition: background-color 0.3s, color 0.3s;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b"
                        "\u044f \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f */\n"
"QDateEdit::drop-down {\n"
"    /* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043a\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f */\n"
"    /* \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0438\u043b\u0438 \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 */\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f */\n"
"QCalendarWidget {\n"
"    /* \u0414\u043e"
                        "\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f */\n"
"    /* \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    background-color: rgb(34, 39, 46);\n"
"    /* \u041f\u043b\u0430\u0432\u043d\u044b\u0435 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0434\u043b\u044f \u0430\u043d\u0438\u043c\u0430\u0446\u0438\u0438 */\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0434\u043d\u0435\u0439 \u043c\u0435\u0441\u044f\u0446\u0430 */\n"
"QCalendarWidget QAbstractItemView {\n"
"    /* \u0421\u0442\u0438\u043b\u0438 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font: 700 12pt \"Noto Sans Mono\";\n"
"    /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    background-color: rg"
                        "b(50, 50, 50);\n"
"    /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    color: rgb(255, 255, 255);\n"
"    /* \u0421\u0433\u043b\u0430\u0436\u0435\u043d\u043d\u044b\u0435 \u043a\u0440\u0430\u044f */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f */\n"
"QCalendarWidget QAbstractItemView:selected {\n"
"    /* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f */\n"
"    /* \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0432\u0435\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f */\n"
"    background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b"
                        "\u044f \u0434\u043d\u0435\u0439, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u044e\u0442 \u0434\u0440\u0443\u0433\u0438\u0435 \u043c\u0435\u0441\u044f\u0446\u044b */\n"
"QCalendarWidget QAbstractItemView:alternate {\n"
"    /* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0434\u043d\u0435\u0439 \u0434\u0440\u0443\u0433\u0438\u0445 \u043c\u0435\u0441\u044f\u0446\u0435\u0432 */\n"
"    /* \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0438\u043b\u0438 \u0444\u043e\u043d\u0430 */\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 \u043c\u0435\u0441\u044f\u0446\u0430 \u0438 \u0433\u043e\u0434\u0430 */\n"
"QDateEdit QCalendarWidget QWi"
                        "dget {\n"
"    /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043c\u0435\u0441\u044f\u0446\u0430 \u0438 \u0433\u043e\u0434\u0430 */\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u0410\u043d\u0438\u043c\u0430\u0446\u0438\u044f \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QDateEdit:hover,\n"
"QDateEdit::drop-down:hover,\n"
"QCalendarWidget:hover {\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"")
        self.WhenBackDate.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.WhenBackDate.setWrapping(False)
        self.WhenBackDate.setFrame(True)
        self.WhenBackDate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.WhenBackDate.setReadOnly(False)
        self.WhenBackDate.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.WhenBackDate.setAccelerated(False)
        self.WhenBackDate.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.WhenBackDate.setKeyboardTracking(False)
        self.WhenBackDate.setProperty("showGroupSeparator", False)
        self.WhenBackDate.setDateTime(QDateTime(QDate(2024, 4, 27), QTime(23, 45, 0)))
        self.WhenBackDate.setTime(QTime(23, 45, 0))
        self.WhenBackDate.setMinimumDate(QDate(2024, 4, 27))
        self.WhenBackDate.setMaximumTime(QTime(3, 59, 59))
        self.WhenBackDate.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.WhenBackDate.setCalendarPopup(True)
        self.WhenBackDate.setTimeSpec(Qt.TimeSpec.UTC)
        self.WhenDate = QDateEdit(self.centralwidget)
        self.WhenDate.setObjectName(u"WhenDate")
        self.WhenDate.setGeometry(QRect(120, 140, 141, 30))
        self.WhenDate.setMaximumSize(QSize(141, 30))
        self.WhenDate.setMouseTracking(False)
        self.WhenDate.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.WhenDate.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.WhenDate.setAutoFillBackground(False)
        self.WhenDate.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b QDateEdit */\n"
"QDateEdit {\n"
"    /* \u0421\u0442\u0438\u043b\u0438 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font: 700 14pt \"Noto Sans Mono\";\n"
"    /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    color: rgb(255, 255, 255);\n"
"    /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"    border-radius: 5px;\n"
"    /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    background-color: rgb(34, 39, 46);\n"
"    /* \u0426\u0432\u0435\u0442 \u0440\u0430\u043c\u043a\u0438 */\n"
"    border: 2px solid white;\n"
"    /* \u041f\u043b\u0430\u0432\u043d\u044b\u0435 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0434\u043b\u044f \u0430\u043d\u0438\u043c\u0430\u0446\u0438\u0438 */\n"
"    transition: background-color 0.3s, color 0.3s;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b"
                        "\u044f \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f */\n"
"QDateEdit::drop-down {\n"
"    /* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043a\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f */\n"
"    /* \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0438\u043b\u0438 \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 */\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f */\n"
"QCalendarWidget {\n"
"    /* \u0414\u043e"
                        "\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f */\n"
"    /* \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    background-color: rgb(34, 39, 46);\n"
"    /* \u041f\u043b\u0430\u0432\u043d\u044b\u0435 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u044b \u0434\u043b\u044f \u0430\u043d\u0438\u043c\u0430\u0446\u0438\u0438 */\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0434\u043d\u0435\u0439 \u043c\u0435\u0441\u044f\u0446\u0430 */\n"
"QCalendarWidget QAbstractItemView {\n"
"    /* \u0421\u0442\u0438\u043b\u0438 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font: 700 12pt \"Noto Sans Mono\";\n"
"    /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    background-color: rg"
                        "b(50, 50, 50);\n"
"    /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    color: rgb(255, 255, 255);\n"
"    /* \u0421\u0433\u043b\u0430\u0436\u0435\u043d\u043d\u044b\u0435 \u043a\u0440\u0430\u044f */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f */\n"
"QCalendarWidget QAbstractItemView:selected {\n"
"    /* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f */\n"
"    /* \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0432\u0435\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f */\n"
"    background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b"
                        "\u044f \u0434\u043d\u0435\u0439, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u044e\u0442 \u0434\u0440\u0443\u0433\u0438\u0435 \u043c\u0435\u0441\u044f\u0446\u044b */\n"
"QCalendarWidget QAbstractItemView:alternate {\n"
"    /* \u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0434\u043d\u0435\u0439 \u0434\u0440\u0443\u0433\u0438\u0445 \u043c\u0435\u0441\u044f\u0446\u0435\u0432 */\n"
"    /* \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043c\u043e\u0436\u043d\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0438\u043b\u0438 \u0444\u043e\u043d\u0430 */\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 \u043c\u0435\u0441\u044f\u0446\u0430 \u0438 \u0433\u043e\u0434\u0430 */\n"
"QDateEdit QCalendarWidget QWi"
                        "dget {\n"
"    /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043c\u0435\u0441\u044f\u0446\u0430 \u0438 \u0433\u043e\u0434\u0430 */\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u0410\u043d\u0438\u043c\u0430\u0446\u0438\u044f \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QDateEdit:hover,\n"
"QDateEdit::drop-down:hover,\n"
"QCalendarWidget:hover {\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"")
        self.WhenDate.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.WhenDate.setWrapping(False)
        self.WhenDate.setFrame(True)
        self.WhenDate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.WhenDate.setReadOnly(False)
        self.WhenDate.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.WhenDate.setKeyboardTracking(False)
        self.WhenDate.setProperty("showGroupSeparator", False)
        self.WhenDate.setDateTime(QDateTime(QDate(2024, 4, 27), QTime(19, 45, 0)))
        self.WhenDate.setTime(QTime(19, 45, 0))
        self.WhenDate.setMinimumDate(QDate(2024, 4, 27))
        self.WhenDate.setMaximumTime(QTime(23, 59, 59))
        self.WhenDate.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.WhenDate.setCalendarPopup(True)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 209, 281, 151))
        self.groupBox.setMaximumSize(QSize(1920, 1080))
        self.groupBox.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.groupBox.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);")
        self.Line_AdultPassangers = QLineEdit(self.groupBox)
        self.Line_AdultPassangers.setObjectName(u"Line_AdultPassangers")
        self.Line_AdultPassangers.setGeometry(QRect(10, 30, 131, 31))
        self.Line_AdultPassangers.setMaximumSize(QSize(1920, 1080))
        self.Line_AdultPassangers.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Line_AdultPassangers.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_AdultPassangers.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_AdultPassangers.setReadOnly(True)
        self.Line_ChildrenPassangers = QLineEdit(self.groupBox)
        self.Line_ChildrenPassangers.setObjectName(u"Line_ChildrenPassangers")
        self.Line_ChildrenPassangers.setGeometry(QRect(10, 70, 111, 31))
        self.Line_ChildrenPassangers.setMaximumSize(QSize(1920, 1080))
        self.Line_ChildrenPassangers.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Line_ChildrenPassangers.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_ChildrenPassangers.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_ChildrenPassangers.setReadOnly(True)
        self.Line_BabyPassangers = QLineEdit(self.groupBox)
        self.Line_BabyPassangers.setObjectName(u"Line_BabyPassangers")
        self.Line_BabyPassangers.setGeometry(QRect(10, 110, 121, 31))
        self.Line_BabyPassangers.setMaximumSize(QSize(1920, 1080))
        self.Line_BabyPassangers.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Line_BabyPassangers.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_BabyPassangers.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_BabyPassangers.setReadOnly(True)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(160, 30, 111, 32))
        self.layoutWidget.setMaximumSize(QSize(1920, 1080))
        self.layoutWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.AdultPassangers = QHBoxLayout(self.layoutWidget)
        self.AdultPassangers.setObjectName(u"AdultPassangers")
        self.AdultPassangers.setContentsMargins(0, 0, 0, 0)
        self.AdultPMinus = QPushButton(self.layoutWidget)
        self.AdultPMinus.setObjectName(u"AdultPMinus")
        self.AdultPMinus.setMinimumSize(QSize(5, 5))
        self.AdultPMinus.setMaximumSize(QSize(1920, 1080))
        self.AdultPMinus.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.AdultPMinus.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.AdultPMinus.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,255);\n"
"}")
        self.AdultPMinus.setAutoRepeat(False)

        self.AdultPassangers.addWidget(self.AdultPMinus)

        self.AdultPCounter = QSpinBox(self.layoutWidget)
        self.AdultPCounter.setObjectName(u"AdultPCounter")
        self.AdultPCounter.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AdultPCounter.sizePolicy().hasHeightForWidth())
        self.AdultPCounter.setSizePolicy(sizePolicy)
        self.AdultPCounter.setMaximumSize(QSize(1920, 1080))
        self.AdultPCounter.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.AdultPCounter.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.AdultPCounter.setAutoFillBackground(False)
        self.AdultPCounter.setStyleSheet(u"QSpinBox::up-button {\n"
"    width: 0;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    width: 0;\n"
"}\n"
"QSpinBox {\n"
"    text-align: center;\n"
"}")
        self.AdultPCounter.setWrapping(False)
        self.AdultPCounter.setFrame(True)
        self.AdultPCounter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.AdultPCounter.setReadOnly(True)
        self.AdultPCounter.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.AdultPCounter.setAccelerated(False)
        self.AdultPCounter.setKeyboardTracking(False)
        self.AdultPCounter.setProperty("showGroupSeparator", False)
        self.AdultPCounter.setMaximum(15)
        self.AdultPCounter.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.AdultPassangers.addWidget(self.AdultPCounter)

        self.AdultPPlus = QPushButton(self.layoutWidget)
        self.AdultPPlus.setObjectName(u"AdultPPlus")
        self.AdultPPlus.setMinimumSize(QSize(5, 5))
        self.AdultPPlus.setMaximumSize(QSize(1920, 1080))
        self.AdultPPlus.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.AdultPPlus.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.AdultPPlus.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,255);\n"
"}")
        self.AdultPPlus.setAutoRepeat(False)

        self.AdultPassangers.addWidget(self.AdultPPlus)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(160, 70, 111, 32))
        self.layoutWidget1.setMaximumSize(QSize(1920, 1080))
        self.layoutWidget1.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ChildrenPassangers = QHBoxLayout(self.layoutWidget1)
        self.ChildrenPassangers.setObjectName(u"ChildrenPassangers")
        self.ChildrenPassangers.setContentsMargins(0, 0, 0, 0)
        self.ChildrenPMinus = QPushButton(self.layoutWidget1)
        self.ChildrenPMinus.setObjectName(u"ChildrenPMinus")
        self.ChildrenPMinus.setMinimumSize(QSize(5, 5))
        self.ChildrenPMinus.setMaximumSize(QSize(1920, 1080))
        self.ChildrenPMinus.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.ChildrenPMinus.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ChildrenPMinus.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,255);\n"
"}")
        self.ChildrenPMinus.setAutoRepeat(False)

        self.ChildrenPassangers.addWidget(self.ChildrenPMinus)

        self.ChildrenPCounters = QSpinBox(self.layoutWidget1)
        self.ChildrenPCounters.setObjectName(u"ChildrenPCounters")
        self.ChildrenPCounters.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ChildrenPCounters.sizePolicy().hasHeightForWidth())
        self.ChildrenPCounters.setSizePolicy(sizePolicy)
        self.ChildrenPCounters.setMaximumSize(QSize(1920, 1080))
        self.ChildrenPCounters.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ChildrenPCounters.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ChildrenPCounters.setAutoFillBackground(False)
        self.ChildrenPCounters.setStyleSheet(u"QSpinBox::up-button {\n"
"    width: 0;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    width: 0;\n"
"}\n"
"QSpinBox {\n"
"    text-align: center;\n"
"}")
        self.ChildrenPCounters.setWrapping(False)
        self.ChildrenPCounters.setFrame(True)
        self.ChildrenPCounters.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ChildrenPCounters.setReadOnly(True)
        self.ChildrenPCounters.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.ChildrenPCounters.setAccelerated(False)
        self.ChildrenPCounters.setKeyboardTracking(False)
        self.ChildrenPCounters.setProperty("showGroupSeparator", False)
        self.ChildrenPCounters.setMaximum(15)
        self.ChildrenPCounters.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.ChildrenPassangers.addWidget(self.ChildrenPCounters)

        self.ChildrenPPlus = QPushButton(self.layoutWidget1)
        self.ChildrenPPlus.setObjectName(u"ChildrenPPlus")
        self.ChildrenPPlus.setMinimumSize(QSize(5, 5))
        self.ChildrenPPlus.setMaximumSize(QSize(1920, 1080))
        self.ChildrenPPlus.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.ChildrenPPlus.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ChildrenPPlus.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,255);\n"
"}")
        self.ChildrenPPlus.setAutoRepeat(False)

        self.ChildrenPassangers.addWidget(self.ChildrenPPlus)

        self.layoutWidget_2 = QWidget(self.groupBox)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(160, 110, 111, 32))
        self.layoutWidget_2.setMaximumSize(QSize(1920, 1080))
        self.layoutWidget_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.BabyPassangers = QHBoxLayout(self.layoutWidget_2)
        self.BabyPassangers.setObjectName(u"BabyPassangers")
        self.BabyPassangers.setContentsMargins(0, 0, 0, 0)
        self.BabyPMinus = QPushButton(self.layoutWidget_2)
        self.BabyPMinus.setObjectName(u"BabyPMinus")
        self.BabyPMinus.setMinimumSize(QSize(5, 5))
        self.BabyPMinus.setMaximumSize(QSize(1920, 1080))
        self.BabyPMinus.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.BabyPMinus.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.BabyPMinus.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,255);\n"
"}")
        self.BabyPMinus.setAutoRepeat(False)

        self.BabyPassangers.addWidget(self.BabyPMinus)

        self.BabyPCounter = QSpinBox(self.layoutWidget_2)
        self.BabyPCounter.setObjectName(u"BabyPCounter")
        self.BabyPCounter.setEnabled(True)
        sizePolicy.setHeightForWidth(self.BabyPCounter.sizePolicy().hasHeightForWidth())
        self.BabyPCounter.setSizePolicy(sizePolicy)
        self.BabyPCounter.setMaximumSize(QSize(1920, 1080))
        self.BabyPCounter.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.BabyPCounter.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.BabyPCounter.setAutoFillBackground(False)
        self.BabyPCounter.setStyleSheet(u"QSpinBox::up-button {\n"
"    width: 0;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    width: 0;\n"
"}\n"
"QSpinBox {\n"
"    text-align: center;\n"
"}")
        self.BabyPCounter.setWrapping(False)
        self.BabyPCounter.setFrame(True)
        self.BabyPCounter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BabyPCounter.setReadOnly(True)
        self.BabyPCounter.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.BabyPCounter.setAccelerated(False)
        self.BabyPCounter.setKeyboardTracking(False)
        self.BabyPCounter.setProperty("showGroupSeparator", False)
        self.BabyPCounter.setMaximum(15)
        self.BabyPCounter.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.BabyPassangers.addWidget(self.BabyPCounter)

        self.BabyPPlus = QPushButton(self.layoutWidget_2)
        self.BabyPPlus.setObjectName(u"BabyPPlus")
        self.BabyPPlus.setMinimumSize(QSize(5, 5))
        self.BabyPPlus.setMaximumSize(QSize(1920, 1080))
        self.BabyPPlus.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.BabyPPlus.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.BabyPPlus.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,255);\n"
"}")
        self.BabyPPlus.setAutoRepeat(False)

        self.BabyPassangers.addWidget(self.BabyPPlus)

        self.ServiceGroup = QGroupBox(self.centralwidget)
        self.ServiceGroup.setObjectName(u"ServiceGroup")
        self.ServiceGroup.setGeometry(QRect(40, 380, 281, 191))
        self.ServiceGroup.setMaximumSize(QSize(1920, 1080))
        self.ServiceGroup.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ServiceGroup.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Line_Economy = QLineEdit(self.ServiceGroup)
        self.Line_Economy.setObjectName(u"Line_Economy")
        self.Line_Economy.setGeometry(QRect(10, 30, 181, 31))
        self.Line_Economy.setMaximumSize(QSize(1920, 1080))
        self.Line_Economy.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_Economy.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_Economy.setReadOnly(True)
        self.Line_Comfort = QLineEdit(self.ServiceGroup)
        self.Line_Comfort.setObjectName(u"Line_Comfort")
        self.Line_Comfort.setGeometry(QRect(10, 70, 191, 31))
        self.Line_Comfort.setMaximumSize(QSize(1920, 1080))
        self.Line_Comfort.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_Comfort.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_Comfort.setReadOnly(True)
        self.Line_FirstClass = QLineEdit(self.ServiceGroup)
        self.Line_FirstClass.setObjectName(u"Line_FirstClass")
        self.Line_FirstClass.setGeometry(QRect(10, 150, 181, 31))
        self.Line_FirstClass.setMaximumSize(QSize(1920, 1080))
        self.Line_FirstClass.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_FirstClass.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_FirstClass.setReadOnly(True)
        self.Line_Business = QLineEdit(self.ServiceGroup)
        self.Line_Business.setObjectName(u"Line_Business")
        self.Line_Business.setGeometry(QRect(10, 110, 171, 31))
        self.Line_Business.setMaximumSize(QSize(1920, 1080))
        self.Line_Business.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_Business.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_Business.setReadOnly(True)
        self.RadButt_Economy = QRadioButton(self.ServiceGroup)
        self.RadButt_Economy.setObjectName(u"RadButt_Economy")
        self.RadButt_Economy.setGeometry(QRect(240, 35, 16, 20))
        self.RadButt_Economy.setMaximumSize(QSize(1920, 1080))
        self.RadButt_Economy.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.RadButt_Economy.setText(u"")
        self.RadButt_Economy.setCheckable(True)
        self.RadButt_Economy.setChecked(True)
        self.RadButt_Comfort = QRadioButton(self.ServiceGroup)
        self.RadButt_Comfort.setObjectName(u"RadButt_Comfort")
        self.RadButt_Comfort.setGeometry(QRect(240, 75, 16, 20))
        self.RadButt_Comfort.setMaximumSize(QSize(1920, 1080))
        self.RadButt_Comfort.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.RadButt_Comfort.setText(u"")
        self.RadButt_Comfort.setCheckable(True)
        self.RadButt_Comfort.setChecked(False)
        self.RadButt_Business = QRadioButton(self.ServiceGroup)
        self.RadButt_Business.setObjectName(u"RadButt_Business")
        self.RadButt_Business.setGeometry(QRect(240, 115, 16, 20))
        self.RadButt_Business.setMaximumSize(QSize(1920, 1080))
        self.RadButt_Business.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.RadButt_Business.setText(u"")
        self.RadButt_Business.setCheckable(True)
        self.RadButt_Business.setChecked(False)
        self.RadButt_FirstClass = QRadioButton(self.ServiceGroup)
        self.RadButt_FirstClass.setObjectName(u"RadButt_FirstClass")
        self.RadButt_FirstClass.setGeometry(QRect(240, 156, 16, 20))
        self.RadButt_FirstClass.setMaximumSize(QSize(1920, 1080))
        self.RadButt_FirstClass.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.RadButt_FirstClass.setText(u"")
        self.RadButt_FirstClass.setCheckable(True)
        self.RadButt_FirstClass.setChecked(False)
        self.Line_NumOfPassangers = QLineEdit(self.centralwidget)
        self.Line_NumOfPassangers.setObjectName(u"Line_NumOfPassangers")
        self.Line_NumOfPassangers.setGeometry(QRect(30, 200, 301, 32))
        self.Line_NumOfPassangers.setMaximumSize(QSize(1920, 1080))
        self.Line_NumOfPassangers.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_NumOfPassangers.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_NumOfPassangers.setReadOnly(True)
        self.Line_Service = QLineEdit(self.centralwidget)
        self.Line_Service.setObjectName(u"Line_Service")
        self.Line_Service.setGeometry(QRect(30, 370, 301, 32))
        self.Line_Service.setMaximumSize(QSize(1920, 1080))
        self.Line_Service.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_Service.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_Service.setReadOnly(True)
        self.Line_SearcherName = QLineEdit(self.centralwidget)
        self.Line_SearcherName.setObjectName(u"Line_SearcherName")
        self.Line_SearcherName.setGeometry(QRect(30, 20, 621, 61))
        self.Line_SearcherName.setMaximumSize(QSize(1920, 1080))
        self.Line_SearcherName.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_SearcherName.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_SearcherName.setStyleSheet(u"font: 700 26pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.Line_SearcherName.setEchoMode(QLineEdit.EchoMode.Normal)
        self.Line_SearcherName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Line_SearcherName.setReadOnly(True)
        self.Line_When_ON = QLineEdit(self.centralwidget)
        self.Line_When_ON.setObjectName(u"Line_When_ON")
        self.Line_When_ON.setGeometry(QRect(20, 140, 91, 31))
        self.Line_When_ON.setMaximumSize(QSize(1920, 1080))
        self.Line_When_ON.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_When_ON.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_When_ON.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_When_ON.setDragEnabled(False)
        self.Line_When_ON.setReadOnly(True)
        self.Line_When_ON.setClearButtonEnabled(False)
        self.Line_When_OFF = QLineEdit(self.centralwidget)
        self.Line_When_OFF.setObjectName(u"Line_When_OFF")
        self.Line_When_OFF.setGeometry(QRect(270, 140, 101, 31))
        self.Line_When_OFF.setMaximumSize(QSize(1920, 1080))
        self.Line_When_OFF.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_When_OFF.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_When_OFF.setStyleSheet(u"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.Line_When_OFF.setDragEnabled(False)
        self.Line_When_OFF.setReadOnly(True)
        self.Line_When_OFF.setClearButtonEnabled(False)
        self.ButtonSeacherTickets = QPushButton(self.centralwidget)
        self.ButtonSeacherTickets.setObjectName(u"ButtonSeacherTickets")
        self.ButtonSeacherTickets.setGeometry(QRect(530, 110, 121, 51))
        self.ButtonSeacherTickets.setMaximumSize(QSize(1920, 1080))
        self.ButtonSeacherTickets.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.ButtonSeacherTickets.setStyleSheet(u"QPushButton {\n"
"	font: 700 14pt \"Noto Sans Mono\" solid;    \n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid #ffffff; \n"
"	background-color: rgb(222, 148, 0);\n"
"    border-radius: 5px; \n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(222, 148, 0, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,150);\n"
"}")
        self.List_FoundTickets = QListWidget(self.centralwidget)
        font1 = QFont()
        font1.setFamilies([u"Noto Sans Mono ExtraBold"])
        font1.setPointSize(12)
        __qlistwidgetitem = QListWidgetItem(self.List_FoundTickets)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setFont(font1);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDropEnabled);
        self.List_FoundTickets.setObjectName(u"List_FoundTickets")
        self.List_FoundTickets.setGeometry(QRect(350, 230, 581, 311))
        self.List_FoundTickets.setMaximumSize(QSize(1920, 1080))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans Mono Black"])
        font2.setPointSize(11)
        font2.setWeight(QFont.Black)
        font2.setItalic(False)
        self.List_FoundTickets.setFont(font2)
        self.List_FoundTickets.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.List_FoundTickets.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.List_FoundTickets.setStyleSheet(u"font: 900 11pt \"Noto Sans Mono Black\";\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 2px solid white;\n"
"")
        self.List_FoundTickets.setFrameShadow(QFrame.Shadow.Sunken)
        self.Line_FoundTickets = QLineEdit(self.centralwidget)
        self.Line_FoundTickets.setObjectName(u"Line_FoundTickets")
        self.Line_FoundTickets.setGeometry(QRect(350, 200, 581, 31))
        self.Line_FoundTickets.setMaximumSize(QSize(1920, 1080))
        self.Line_FoundTickets.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Line_FoundTickets.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.Line_FoundTickets.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid white;\n"
"font: 700 14pt \"Noto Sans Mono\";\n"
"color: rgb(255, 255, 255);")
        self.Line_FoundTickets.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LogoSkyFly = QLabel(self.centralwidget)
        self.LogoSkyFly.setObjectName(u"LogoSkyFly")
        self.LogoSkyFly.setGeometry(QRect(660, 20, 271, 161))
        self.LogoSkyFly.setMaximumSize(QSize(1920, 1080))
        self.LogoSkyFly.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.LogoSkyFly.setStyleSheet(u"background-color: rgb(34, 39, 46);\n"
"border-radius: 5px;\n"
"border: 2px solid white;")
        self.LogoSkyFly.setTextFormat(Qt.TextFormat.AutoText)
        self.LogoSkyFly.setPixmap(QPixmap(u":/Img/Default_Logo_minimalistic_type_modern_disign_2d_no_backgrounts_3.jpg"))
        self.LogoSkyFly.setScaledContents(False)
        self.LogoSkyFly.setWordWrap(False)
        self.LogoSkyFly.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.ButtonMoreInfo = QPushButton(self.centralwidget)
        self.ButtonMoreInfo.setObjectName(u"ButtonMoreInfo")
        self.ButtonMoreInfo.setGeometry(QRect(800, 540, 131, 31))
        self.ButtonMoreInfo.setStyleSheet(u"QPushButton {\n"
"	font: 900 11pt \"Noto Sans Mono Black\";\n"
"	color: rgb(255,255,255);\n"
"    border: 2px solid #ffffff; \n"
"	background-color: rgb(34, 39, 46);\n"
"    border-radius: 5px; \n"
"	width: 24px;\n"
"    height: 30px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(165,165,165,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165,165,165,255);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SkyFly", None))
        self.Line_Where_ON.setText("")
        self.Line_Where_ON.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0443\u0434\u0430", None))
        self.Line_Where_OFF.setText("")
        self.Line_Where_OFF.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0434\u0430", None))
        self.groupBox.setTitle("")
        self.Line_AdultPassangers.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0437\u0440\u043e\u0441\u043b\u044b\u0435", None))
        self.Line_ChildrenPassangers.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0442\u0438", None))
        self.Line_BabyPassangers.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043b\u0430\u0434\u0435\u043d\u0446\u044b", None))
        self.AdultPMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.AdultPCounter.setSpecialValueText("")
        self.AdultPPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.ChildrenPMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.ChildrenPCounters.setSpecialValueText("")
        self.ChildrenPPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.BabyPMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.BabyPCounter.setSpecialValueText("")
        self.BabyPPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.ServiceGroup.setTitle("")
        self.Line_Economy.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u043e\u043d\u043e\u043c", None))
        self.Line_Comfort.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0444\u043e\u0440\u0442", None))
        self.Line_FirstClass.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u044b\u0439 \u043a\u043b\u0430\u0441\u0441", None))
        self.Line_Business.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0438\u0437\u043d\u0435\u0441", None))
        self.Line_NumOfPassangers.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043e\u0432:", None))
        self.Line_Service.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f:", None))
        self.Line_SearcherName.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0431\u0438\u043b\u0435\u0442\u043e\u0432", None))
        self.Line_When_ON.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0433\u0434\u0430:", None))
        self.Line_When_ON.setPlaceholderText("")
        self.Line_When_OFF.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0442\u043d\u043e:", None))
        self.Line_When_OFF.setPlaceholderText("")
        self.ButtonSeacherTickets.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \n"
"\u0431\u0438\u043b\u0435\u0442\u043e\u0432", None))

        __sortingEnabled = self.List_FoundTickets.isSortingEnabled()
        self.List_FoundTickets.setSortingEnabled(False)
        ___qlistwidgetitem = self.List_FoundTickets.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u043e\u0447\u043a\u0438 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u0431\u0438\u043b\u0435\u0442\u043e\u0432", None));
        self.List_FoundTickets.setSortingEnabled(__sortingEnabled)

        self.Line_FoundTickets.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u0431\u0438\u043b\u0435\u0442\u044b", None))
        self.LogoSkyFly.setText("")
        self.ButtonMoreInfo.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
    # retranslateUi

