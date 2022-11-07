# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_ZhiHu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(740, 638)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tabWidgetPage_ans = QWidget()
        self.tabWidgetPage_ans.setObjectName(u"tabWidgetPage_ans")
        self.horizontalLayout_2 = QHBoxLayout(self.tabWidgetPage_ans)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolBox_answer = QToolBox(self.tabWidgetPage_ans)
        self.toolBox_answer.setObjectName(u"toolBox_answer")
        self.toolBox_answer.setMaximumSize(QSize(400, 16777215))
        self.toolBox_answer.setStyleSheet(u"")
        self.toolBox_answer.setFrameShape(QFrame.NoFrame)
        self.page_target_ans = QWidget()
        self.page_target_ans.setObjectName(u"page_target_ans")
        self.page_target_ans.setGeometry(QRect(0, 0, 346, 442))
        self.verticalLayout_3 = QVBoxLayout(self.page_target_ans)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_url_ans = QLabel(self.page_target_ans)
        self.label_url_ans.setObjectName(u"label_url_ans")

        self.horizontalLayout_4.addWidget(self.label_url_ans)

        self.lineEdit_url_ans = QLineEdit(self.page_target_ans)
        self.lineEdit_url_ans.setObjectName(u"lineEdit_url_ans")

        self.horizontalLayout_4.addWidget(self.lineEdit_url_ans)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 304, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_sig_ans = QLabel(self.page_target_ans)
        self.label_sig_ans.setObjectName(u"label_sig_ans")
        self.label_sig_ans.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_sig_ans)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pushButton_get_ans = QPushButton(self.page_target_ans)
        self.pushButton_get_ans.setObjectName(u"pushButton_get_ans")

        self.verticalLayout_3.addWidget(self.pushButton_get_ans)

        self.toolBox_answer.addItem(self.page_target_ans, u"\u76ee\u6807\u8bbe\u7f6e")
        self.page_edit_ans = QWidget()
        self.page_edit_ans.setObjectName(u"page_edit_ans")
        self.page_edit_ans.setGeometry(QRect(0, 0, 346, 442))
        self.verticalLayout_2 = QVBoxLayout(self.page_edit_ans)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit_model_ans = QTextEdit(self.page_edit_ans)
        self.textEdit_model_ans.setObjectName(u"textEdit_model_ans")

        self.verticalLayout_2.addWidget(self.textEdit_model_ans)

        self.pushButton_importmodel_ans = QPushButton(self.page_edit_ans)
        self.pushButton_importmodel_ans.setObjectName(u"pushButton_importmodel_ans")

        self.verticalLayout_2.addWidget(self.pushButton_importmodel_ans)

        self.pushButton_exportmodel_ans = QPushButton(self.page_edit_ans)
        self.pushButton_exportmodel_ans.setObjectName(u"pushButton_exportmodel_ans")

        self.verticalLayout_2.addWidget(self.pushButton_exportmodel_ans)

        self.toolBox_answer.addItem(self.page_edit_ans, u"\u6587\u672c\u7f16\u8f91")
        self.page_set_ans = QWidget()
        self.page_set_ans.setObjectName(u"page_set_ans")
        self.page_set_ans.setGeometry(QRect(0, 0, 346, 442))
        self.verticalLayout_4 = QVBoxLayout(self.page_set_ans)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_set_ans = QGroupBox(self.page_set_ans)
        self.groupBox_set_ans.setObjectName(u"groupBox_set_ans")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_set_ans)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tableWidget_sub_ans = QTableWidget(self.groupBox_set_ans)
        if (self.tableWidget_sub_ans.columnCount() < 1):
            self.tableWidget_sub_ans.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_sub_ans.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget_sub_ans.rowCount() < 9):
            self.tableWidget_sub_ans.setRowCount(9)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_sub_ans.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_sub_ans.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_sub_ans.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_sub_ans.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_sub_ans.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_sub_ans.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_sub_ans.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_sub_ans.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_sub_ans.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_sub_ans.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_sub_ans.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_sub_ans.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_sub_ans.setItem(3, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_sub_ans.setItem(4, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_sub_ans.setItem(5, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_sub_ans.setItem(6, 0, __qtablewidgetitem16)
        self.tableWidget_sub_ans.setObjectName(u"tableWidget_sub_ans")
        self.tableWidget_sub_ans.setAutoScrollMargin(16)
        self.tableWidget_sub_ans.horizontalHeader().setVisible(True)
        self.tableWidget_sub_ans.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_sub_ans.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_sub_ans.horizontalHeader().setHighlightSections(True)
        self.tableWidget_sub_ans.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_sub_ans.verticalHeader().setVisible(True)
        self.tableWidget_sub_ans.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_6.addWidget(self.tableWidget_sub_ans)

        self.pushButton_setmodel_ans = QPushButton(self.groupBox_set_ans)
        self.pushButton_setmodel_ans.setObjectName(u"pushButton_setmodel_ans")

        self.verticalLayout_6.addWidget(self.pushButton_setmodel_ans)


        self.verticalLayout_4.addWidget(self.groupBox_set_ans)

        self.line_ans = QFrame(self.page_set_ans)
        self.line_ans.setObjectName(u"line_ans")
        self.line_ans.setFrameShape(QFrame.HLine)
        self.line_ans.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_ans)

        self.groupBox_file_ans = QGroupBox(self.page_set_ans)
        self.groupBox_file_ans.setObjectName(u"groupBox_file_ans")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_file_ans)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_filename_ans = QLineEdit(self.groupBox_file_ans)
        self.lineEdit_filename_ans.setObjectName(u"lineEdit_filename_ans")

        self.horizontalLayout_3.addWidget(self.lineEdit_filename_ans)

        self.comboBox_filetype_ans = QComboBox(self.groupBox_file_ans)
        self.comboBox_filetype_ans.addItem("")
        self.comboBox_filetype_ans.addItem("")
        self.comboBox_filetype_ans.setObjectName(u"comboBox_filetype_ans")

        self.horizontalLayout_3.addWidget(self.comboBox_filetype_ans)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.commandLinkButton_filedir_ans = QCommandLinkButton(self.groupBox_file_ans)
        self.commandLinkButton_filedir_ans.setObjectName(u"commandLinkButton_filedir_ans")
        self.commandLinkButton_filedir_ans.setStyleSheet(u"QCommandLinkButton {\n"
"	font: 9pt;\n"
"}")
        self.commandLinkButton_filedir_ans.setIconSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.commandLinkButton_filedir_ans)

        self.pushButton_setdir_ans = QPushButton(self.groupBox_file_ans)
        self.pushButton_setdir_ans.setObjectName(u"pushButton_setdir_ans")
        self.pushButton_setdir_ans.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_setdir_ans)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox_file_ans)

        self.toolBox_answer.addItem(self.page_set_ans, u"\u8bbe\u7f6e")

        self.horizontalLayout_2.addWidget(self.toolBox_answer)

        self.frame_preview_ans = QFrame(self.tabWidgetPage_ans)
        self.frame_preview_ans.setObjectName(u"frame_preview_ans")
        self.frame_preview_ans.setStyleSheet(u"")
        self.frame_preview_ans.setFrameShape(QFrame.StyledPanel)
        self.frame_preview_ans.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_preview_ans)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_preview_ans = QLabel(self.frame_preview_ans)
        self.label_preview_ans.setObjectName(u"label_preview_ans")
        self.label_preview_ans.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_preview_ans)

        self.textEdit_preview_ans = QTextEdit(self.frame_preview_ans)
        self.textEdit_preview_ans.setObjectName(u"textEdit_preview_ans")
        self.textEdit_preview_ans.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_preview_ans)

        self.pushButton_savefile_ans = QPushButton(self.frame_preview_ans)
        self.pushButton_savefile_ans.setObjectName(u"pushButton_savefile_ans")

        self.verticalLayout.addWidget(self.pushButton_savefile_ans)


        self.horizontalLayout_2.addWidget(self.frame_preview_ans)

        self.tabWidget.addTab(self.tabWidgetPage_ans, "")
        self.tabWidgetPage_art = QWidget()
        self.tabWidgetPage_art.setObjectName(u"tabWidgetPage_art")
        self.horizontalLayout_9 = QHBoxLayout(self.tabWidgetPage_art)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.toolBox_article = QToolBox(self.tabWidgetPage_art)
        self.toolBox_article.setObjectName(u"toolBox_article")
        self.toolBox_article.setMaximumSize(QSize(400, 16777215))
        self.toolBox_article.setStyleSheet(u"")
        self.toolBox_article.setFrameShape(QFrame.NoFrame)
        self.page_target_art = QWidget()
        self.page_target_art.setObjectName(u"page_target_art")
        self.page_target_art.setGeometry(QRect(0, 0, 346, 442))
        self.verticalLayout_8 = QVBoxLayout(self.page_target_art)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_url_art = QLabel(self.page_target_art)
        self.label_url_art.setObjectName(u"label_url_art")

        self.horizontalLayout_6.addWidget(self.label_url_art)

        self.lineEdit_url_art = QLineEdit(self.page_target_art)
        self.lineEdit_url_art.setObjectName(u"lineEdit_url_art")

        self.horizontalLayout_6.addWidget(self.lineEdit_url_art)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 304, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.label_sig_art = QLabel(self.page_target_art)
        self.label_sig_art.setObjectName(u"label_sig_art")
        self.label_sig_art.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_sig_art)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.pushButton_get_art = QPushButton(self.page_target_art)
        self.pushButton_get_art.setObjectName(u"pushButton_get_art")

        self.verticalLayout_8.addWidget(self.pushButton_get_art)

        self.toolBox_article.addItem(self.page_target_art, u"\u76ee\u6807\u8bbe\u7f6e")
        self.page_edit_art = QWidget()
        self.page_edit_art.setObjectName(u"page_edit_art")
        self.page_edit_art.setGeometry(QRect(0, 0, 98, 149))
        self.verticalLayout_9 = QVBoxLayout(self.page_edit_art)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textEdit_model_art = QTextEdit(self.page_edit_art)
        self.textEdit_model_art.setObjectName(u"textEdit_model_art")

        self.verticalLayout_9.addWidget(self.textEdit_model_art)

        self.pushButton_importmodel_art = QPushButton(self.page_edit_art)
        self.pushButton_importmodel_art.setObjectName(u"pushButton_importmodel_art")

        self.verticalLayout_9.addWidget(self.pushButton_importmodel_art)

        self.pushButton_exportmodel_art = QPushButton(self.page_edit_art)
        self.pushButton_exportmodel_art.setObjectName(u"pushButton_exportmodel_art")

        self.verticalLayout_9.addWidget(self.pushButton_exportmodel_art)

        self.toolBox_article.addItem(self.page_edit_art, u"\u6587\u672c\u7f16\u8f91")
        self.page_set_art = QWidget()
        self.page_set_art.setObjectName(u"page_set_art")
        self.page_set_art.setGeometry(QRect(0, 0, 273, 392))
        self.verticalLayout_10 = QVBoxLayout(self.page_set_art)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_set_art = QGroupBox(self.page_set_art)
        self.groupBox_set_art.setObjectName(u"groupBox_set_art")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_set_art)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tableWidget_sub_art = QTableWidget(self.groupBox_set_art)
        if (self.tableWidget_sub_art.columnCount() < 1):
            self.tableWidget_sub_art.setColumnCount(1)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_sub_art.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        if (self.tableWidget_sub_art.rowCount() < 9):
            self.tableWidget_sub_art.setRowCount(9)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_sub_art.setVerticalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_sub_art.setVerticalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_sub_art.setVerticalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_sub_art.setVerticalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_sub_art.setVerticalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_sub_art.setVerticalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_sub_art.setVerticalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_sub_art.setVerticalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_sub_art.setVerticalHeaderItem(8, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_sub_art.setItem(0, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_sub_art.setItem(1, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_sub_art.setItem(2, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_sub_art.setItem(3, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_sub_art.setItem(4, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_sub_art.setItem(5, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_sub_art.setItem(6, 0, __qtablewidgetitem33)
        self.tableWidget_sub_art.setObjectName(u"tableWidget_sub_art")
        self.tableWidget_sub_art.setAutoScrollMargin(16)
        self.tableWidget_sub_art.horizontalHeader().setVisible(True)
        self.tableWidget_sub_art.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_sub_art.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_sub_art.horizontalHeader().setHighlightSections(True)
        self.tableWidget_sub_art.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_sub_art.verticalHeader().setVisible(True)
        self.tableWidget_sub_art.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_11.addWidget(self.tableWidget_sub_art)

        self.pushButton_setmodel_art = QPushButton(self.groupBox_set_art)
        self.pushButton_setmodel_art.setObjectName(u"pushButton_setmodel_art")

        self.verticalLayout_11.addWidget(self.pushButton_setmodel_art)


        self.verticalLayout_10.addWidget(self.groupBox_set_art)

        self.line_art = QFrame(self.page_set_art)
        self.line_art.setObjectName(u"line_art")
        self.line_art.setFrameShape(QFrame.HLine)
        self.line_art.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_art)

        self.groupBox_file_art = QGroupBox(self.page_set_art)
        self.groupBox_file_art.setObjectName(u"groupBox_file_art")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_file_art)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_filename_art = QLineEdit(self.groupBox_file_art)
        self.lineEdit_filename_art.setObjectName(u"lineEdit_filename_art")

        self.horizontalLayout_7.addWidget(self.lineEdit_filename_art)

        self.comboBox_filetype_art = QComboBox(self.groupBox_file_art)
        self.comboBox_filetype_art.addItem("")
        self.comboBox_filetype_art.addItem("")
        self.comboBox_filetype_art.setObjectName(u"comboBox_filetype_art")

        self.horizontalLayout_7.addWidget(self.comboBox_filetype_art)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.commandLinkButton_filedir_art = QCommandLinkButton(self.groupBox_file_art)
        self.commandLinkButton_filedir_art.setObjectName(u"commandLinkButton_filedir_art")
        self.commandLinkButton_filedir_art.setStyleSheet(u"QCommandLinkButton {\n"
"	font: 9pt;\n"
"}")
        self.commandLinkButton_filedir_art.setIconSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.commandLinkButton_filedir_art)

        self.pushButton_setdir_art = QPushButton(self.groupBox_file_art)
        self.pushButton_setdir_art.setObjectName(u"pushButton_setdir_art")
        self.pushButton_setdir_art.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_8.addWidget(self.pushButton_setdir_art)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)


        self.verticalLayout_10.addWidget(self.groupBox_file_art)

        self.toolBox_article.addItem(self.page_set_art, u"\u8bbe\u7f6e")

        self.horizontalLayout_9.addWidget(self.toolBox_article)

        self.frame_preview_ans_2 = QFrame(self.tabWidgetPage_art)
        self.frame_preview_ans_2.setObjectName(u"frame_preview_ans_2")
        self.frame_preview_ans_2.setStyleSheet(u"")
        self.frame_preview_ans_2.setFrameShape(QFrame.StyledPanel)
        self.frame_preview_ans_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_preview_ans_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_preview_art = QLabel(self.frame_preview_ans_2)
        self.label_preview_art.setObjectName(u"label_preview_art")
        self.label_preview_art.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_preview_art)

        self.textEdit_preview_art = QTextEdit(self.frame_preview_ans_2)
        self.textEdit_preview_art.setObjectName(u"textEdit_preview_art")
        self.textEdit_preview_art.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.textEdit_preview_art)

        self.pushButton_savefile_art = QPushButton(self.frame_preview_ans_2)
        self.pushButton_savefile_art.setObjectName(u"pushButton_savefile_art")

        self.verticalLayout_7.addWidget(self.pushButton_savefile_art)


        self.horizontalLayout_9.addWidget(self.frame_preview_ans_2)

        self.tabWidget.addTab(self.tabWidgetPage_art, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 740, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox_answer.setCurrentIndex(0)
        self.toolBox_article.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u77e5\u4e4e\u722c\u866b", None))
        self.label_url_ans.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740\uff1a", None))
        self.lineEdit_url_ans.setPlaceholderText(QCoreApplication.translate("MainWindow", u"url", None))
        self.label_sig_ans.setText(QCoreApplication.translate("MainWindow", u"\u672a\u6267\u884c", None))
        self.pushButton_get_ans.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u7f51\u9875", None))
        self.toolBox_answer.setItemText(self.toolBox_answer.indexOf(self.page_target_ans), QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8bbe\u7f6e", None))
        self.textEdit_model_ans.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u6a21\u677f", None))
        self.pushButton_importmodel_ans.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u5df2\u6709\u6a21\u677f", None))
        self.pushButton_exportmodel_ans.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u4e3a\u6a21\u677f", None))
        self.toolBox_answer.setItemText(self.toolBox_answer.indexOf(self.page_edit_ans), QCoreApplication.translate("MainWindow", u"\u6587\u672c\u7f16\u8f91", None))
        self.groupBox_set_ans.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u677f\u8bbe\u7f6e", None))
        ___qtablewidgetitem = self.tableWidget_sub_ans.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u5e94\u5185\u5bb9", None));
        ___qtablewidgetitem1 = self.tableWidget_sub_ans.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u95ee\u9898\u6807\u9898", None));
        ___qtablewidgetitem2 = self.tableWidget_sub_ans.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u95ee\u9898\u53d9\u8ff0", None));
        ___qtablewidgetitem3 = self.tableWidget_sub_ans.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005\u4fe1\u606f", None));
        ___qtablewidgetitem4 = self.tableWidget_sub_ans.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u56de\u7b54\u6b63\u6587", None));
        ___qtablewidgetitem5 = self.tableWidget_sub_ans.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u56de\u7b54\u65f6\u95f4", None));
        ___qtablewidgetitem6 = self.tableWidget_sub_ans.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"tag\u5217\u8868", None));
        ___qtablewidgetitem7 = self.tableWidget_sub_ans.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u8d5e\u6570", None));
        ___qtablewidgetitem8 = self.tableWidget_sub_ans.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u8bba\u6570", None));
        ___qtablewidgetitem9 = self.tableWidget_sub_ans.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"url", None));

        __sortingEnabled = self.tableWidget_sub_ans.isSortingEnabled()
        self.tableWidget_sub_ans.setSortingEnabled(False)
        self.tableWidget_sub_ans.setSortingEnabled(__sortingEnabled)

        self.pushButton_setmodel_ans.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6a21\u677f", None))
        self.groupBox_file_ans.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6587\u4ef6", None))
        self.lineEdit_filename_ans.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None))
        self.comboBox_filetype_ans.setItemText(0, QCoreApplication.translate("MainWindow", u".md", None))
        self.comboBox_filetype_ans.setItemText(1, QCoreApplication.translate("MainWindow", u".txt", None))

        self.commandLinkButton_filedir_ans.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.pushButton_setdir_ans.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u6587\u4ef6\u5939", None))
        self.toolBox_answer.setItemText(self.toolBox_answer.indexOf(self.page_set_ans), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_preview_ans.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.textEdit_preview_ans.setMarkdown("")
        self.textEdit_preview_ans.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.pushButton_savefile_ans.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage_ans), QCoreApplication.translate("MainWindow", u"\u56de\u7b54\u722c\u53d6", None))
        self.label_url_art.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740\uff1a", None))
        self.lineEdit_url_art.setPlaceholderText(QCoreApplication.translate("MainWindow", u"url", None))
        self.label_sig_art.setText(QCoreApplication.translate("MainWindow", u"\u672a\u6267\u884c", None))
        self.pushButton_get_art.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u7f51\u9875", None))
        self.toolBox_article.setItemText(self.toolBox_article.indexOf(self.page_target_art), QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8bbe\u7f6e", None))
        self.textEdit_model_art.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u6a21\u677f", None))
        self.pushButton_importmodel_art.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u5df2\u6709\u6a21\u677f", None))
        self.pushButton_exportmodel_art.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u4e3a\u6a21\u677f", None))
        self.toolBox_article.setItemText(self.toolBox_article.indexOf(self.page_edit_art), QCoreApplication.translate("MainWindow", u"\u6587\u672c\u7f16\u8f91", None))
        self.groupBox_set_art.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u677f\u8bbe\u7f6e", None))
        ___qtablewidgetitem10 = self.tableWidget_sub_art.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u5e94\u5185\u5bb9", None));
        ___qtablewidgetitem11 = self.tableWidget_sub_art.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u80cc\u666f\u56fe", None));
        ___qtablewidgetitem12 = self.tableWidget_sub_art.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u6807\u9898", None));
        ___qtablewidgetitem13 = self.tableWidget_sub_art.verticalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005\u4fe1\u606f", None));
        ___qtablewidgetitem14 = self.tableWidget_sub_art.verticalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u6b63\u6587", None));
        ___qtablewidgetitem15 = self.tableWidget_sub_art.verticalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u4fe1\u606f", None));
        ___qtablewidgetitem16 = self.tableWidget_sub_art.verticalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"tag\u5217\u8868", None));
        ___qtablewidgetitem17 = self.tableWidget_sub_art.verticalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u8d5e\u6570", None));
        ___qtablewidgetitem18 = self.tableWidget_sub_art.verticalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u8bba\u6570", None));
        ___qtablewidgetitem19 = self.tableWidget_sub_art.verticalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"url", None));

        __sortingEnabled1 = self.tableWidget_sub_art.isSortingEnabled()
        self.tableWidget_sub_art.setSortingEnabled(False)
        self.tableWidget_sub_art.setSortingEnabled(__sortingEnabled1)

        self.pushButton_setmodel_art.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6a21\u677f", None))
        self.groupBox_file_art.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6587\u4ef6", None))
        self.lineEdit_filename_art.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None))
        self.comboBox_filetype_art.setItemText(0, QCoreApplication.translate("MainWindow", u".md", None))
        self.comboBox_filetype_art.setItemText(1, QCoreApplication.translate("MainWindow", u".txt", None))

        self.commandLinkButton_filedir_art.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.pushButton_setdir_art.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u6587\u4ef6\u5939", None))
        self.toolBox_article.setItemText(self.toolBox_article.indexOf(self.page_set_art), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_preview_art.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.textEdit_preview_art.setMarkdown("")
        self.textEdit_preview_art.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.pushButton_savefile_art.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage_art), QCoreApplication.translate("MainWindow", u"\u6587\u7ae0\u722c\u53d6", None))
    # retranslateUi

