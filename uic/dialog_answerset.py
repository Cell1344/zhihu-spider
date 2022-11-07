# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_answerset.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(562, 640)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea /*.QWidget*/{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -365, 505, 933))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_math = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_math.setObjectName(u"groupBox_math")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_math)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_mathtype = QLabel(self.groupBox_math)
        self.label_mathtype.setObjectName(u"label_mathtype")

        self.horizontalLayout_2.addWidget(self.label_mathtype)

        self.comboBox_mathtype = QComboBox(self.groupBox_math)
        self.comboBox_mathtype.addItem("")
        self.comboBox_mathtype.addItem("")
        self.comboBox_mathtype.addItem("")
        self.comboBox_mathtype.addItem("")
        self.comboBox_mathtype.addItem("")
        self.comboBox_mathtype.setObjectName(u"comboBox_mathtype")

        self.horizontalLayout_2.addWidget(self.comboBox_mathtype)

        self.horizontalSpacer_2 = QSpacerItem(16, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.checkBox_mathauto = QCheckBox(self.groupBox_math)
        self.checkBox_mathauto.setObjectName(u"checkBox_mathauto")

        self.horizontalLayout_2.addWidget(self.checkBox_mathauto)


        self.verticalLayout_6.addWidget(self.groupBox_math)

        self.groupBox_tag = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_tag.setObjectName(u"groupBox_tag")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_tag)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_interval = QLabel(self.groupBox_tag)
        self.label_interval.setObjectName(u"label_interval")

        self.horizontalLayout_5.addWidget(self.label_interval)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.lineEdit_interval = QLineEdit(self.groupBox_tag)
        self.lineEdit_interval.setObjectName(u"lineEdit_interval")
        self.lineEdit_interval.setMinimumSize(QSize(180, 0))
        self.lineEdit_interval.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_interval)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_tagname = QLabel(self.groupBox_tag)
        self.label_tagname.setObjectName(u"label_tagname")

        self.horizontalLayout_6.addWidget(self.label_tagname)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.lineEdit_tagname = QLineEdit(self.groupBox_tag)
        self.lineEdit_tagname.setObjectName(u"lineEdit_tagname")
        self.lineEdit_tagname.setMinimumSize(QSize(180, 0))
        self.lineEdit_tagname.setMaximumSize(QSize(180, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit_tagname)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addWidget(self.groupBox_tag)

        self.groupBox_author = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_author.setObjectName(u"groupBox_author")
        self.groupBox_author.setMinimumSize(QSize(0, 200))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_author)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_avatarwithsize = QCheckBox(self.groupBox_author)
        self.checkBox_avatarwithsize.setObjectName(u"checkBox_avatarwithsize")

        self.horizontalLayout_3.addWidget(self.checkBox_avatarwithsize)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_author = QLabel(self.groupBox_author)
        self.label_author.setObjectName(u"label_author")

        self.horizontalLayout_4.addWidget(self.label_author)

        self.textEdit_author = QTextEdit(self.groupBox_author)
        self.textEdit_author.setObjectName(u"textEdit_author")

        self.horizontalLayout_4.addWidget(self.textEdit_author)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addWidget(self.groupBox_author)

        self.groupBox_time = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_time.setObjectName(u"groupBox_time")
        self.groupBox_time.setMinimumSize(QSize(0, 150))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_time)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_timetype = QLabel(self.groupBox_time)
        self.label_timetype.setObjectName(u"label_timetype")

        self.horizontalLayout_7.addWidget(self.label_timetype)

        self.comboBox_timetype = QComboBox(self.groupBox_time)
        self.comboBox_timetype.addItem("")
        self.comboBox_timetype.addItem("")
        self.comboBox_timetype.setObjectName(u"comboBox_timetype")

        self.horizontalLayout_7.addWidget(self.comboBox_timetype)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_time = QLabel(self.groupBox_time)
        self.label_time.setObjectName(u"label_time")

        self.horizontalLayout_8.addWidget(self.label_time)

        self.textEdit_time = QTextEdit(self.groupBox_time)
        self.textEdit_time.setObjectName(u"textEdit_time")
        self.textEdit_time.setMaximumSize(QSize(16777215, 150))

        self.horizontalLayout_8.addWidget(self.textEdit_time)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addWidget(self.groupBox_time)

        self.groupBox_subdata = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_subdata.setObjectName(u"groupBox_subdata")
        self.groupBox_subdata.setMinimumSize(QSize(0, 400))
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_subdata)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.pushButton_addline = QPushButton(self.groupBox_subdata)
        self.pushButton_addline.setObjectName(u"pushButton_addline")
        self.pushButton_addline.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.pushButton_addline)

        self.pushButton_delline = QPushButton(self.groupBox_subdata)
        self.pushButton_delline.setObjectName(u"pushButton_delline")
        self.pushButton_delline.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.pushButton_delline)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.tableWidget_subdata = QTableWidget(self.groupBox_subdata)
        if (self.tableWidget_subdata.columnCount() < 3):
            self.tableWidget_subdata.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_subdata.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_subdata.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_subdata.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_subdata.rowCount() < 1):
            self.tableWidget_subdata.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_subdata.setVerticalHeaderItem(0, __qtablewidgetitem3)
        self.tableWidget_subdata.setObjectName(u"tableWidget_subdata")
        self.tableWidget_subdata.setSortingEnabled(True)
        self.tableWidget_subdata.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_subdata.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_subdata.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_subdata.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_subdata.verticalHeader().setVisible(False)
        self.tableWidget_subdata.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget_subdata.verticalHeader().setDefaultSectionSize(60)
        self.tableWidget_subdata.verticalHeader().setHighlightSections(True)
        self.tableWidget_subdata.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_subdata.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_7.addWidget(self.tableWidget_subdata)


        self.verticalLayout_6.addWidget(self.groupBox_subdata)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_accept = QPushButton(self.frame)
        self.pushButton_accept.setObjectName(u"pushButton_accept")

        self.horizontalLayout.addWidget(self.pushButton_accept)

        self.pushButton_quit = QPushButton(self.frame)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.horizontalLayout.addWidget(self.pushButton_quit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u56de\u7b54\u5c5e\u6027\u8bbe\u7f6e", None))
        self.groupBox_math.setTitle(QCoreApplication.translate("Dialog", u"\u6570\u5b66\u516c\u5f0f(\u95ee\u9898\u63cf\u8ff0\u4e0e\u56de\u7b54\u5185\u5bb9)", None))
        self.label_mathtype.setText(QCoreApplication.translate("Dialog", u"\u524d\u7f00\u4f7f\u7528\uff1a", None))
        self.comboBox_mathtype.setItemText(0, QCoreApplication.translate("Dialog", u"\u4fdd\u6301\u539f\u516c\u5f0f", None))
        self.comboBox_mathtype.setItemText(1, QCoreApplication.translate("Dialog", u"\\displaystyle", None))
        self.comboBox_mathtype.setItemText(2, QCoreApplication.translate("Dialog", u"\\textstyle", None))
        self.comboBox_mathtype.setItemText(3, QCoreApplication.translate("Dialog", u"\\scriptstyle", None))
        self.comboBox_mathtype.setItemText(4, QCoreApplication.translate("Dialog", u"\\scriptscriptstyle", None))

        self.checkBox_mathauto.setText(QCoreApplication.translate("Dialog", u"\u5bf9\u5355\u72ec\u6210\u6bb5\u7684\u516c\u5f0f\u4f7f\u7528\u884c\u95f4\u516c\u5f0f", None))
        self.groupBox_tag.setTitle(QCoreApplication.translate("Dialog", u"tag\u5217\u8868", None))
        self.label_interval.setText(QCoreApplication.translate("Dialog", u"tag\u95f4\u95f4\u9694\u586b\u5145\uff1a", None))
        self.lineEdit_interval.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u586b\u5145\uff0c\u4e0d\u8bbe\u7f6e\u5219\u89c6\u4e3a\u65e0\u95f4\u9694", None))
        self.label_tagname.setText(QCoreApplication.translate("Dialog", u"tag\u6587\u672c\uff1a", None))
        self.lineEdit_tagname.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u7528/n\u66ff\u4ee3tag\u7684\u540d\u5b57", None))
        self.groupBox_author.setTitle(QCoreApplication.translate("Dialog", u"\u4f5c\u8005\u4fe1\u606f", None))
        self.checkBox_avatarwithsize.setText(QCoreApplication.translate("Dialog", u"\u5934\u50cf\u4f7f\u7528\u7f51\u9875\u4e2d\u5c3a\u5bf8", None))
        self.label_author.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u7f16\u8f91\u4f5c\u8005\u4fe1\u606f\uff1a</p></body></html>", None))
        self.textEdit_author.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u5bf9\u5e94\u89c4\u5219\uff1a/n\uff1a\u4f5c\u8005\u59d3\u540d\uff1b/a\uff1a\u4f5c\u8005\u5934\u50cf\uff1b/t\uff1a\u4f5c\u8005\u7b7e\u540d\uff1b/u\uff1a\u4f5c\u8005\u4e3b\u9875url\u3002\u8981\u6253\u51fa/t\u53ef\u4ee5\u7528//t\u66ff\u4ee3\uff0c\u5176\u5b83\u540c\u7406\u3002", None))
        self.groupBox_time.setTitle(QCoreApplication.translate("Dialog", u"\u65f6\u95f4\u4fe1\u606f", None))
        self.label_timetype.setText(QCoreApplication.translate("Dialog", u"\u4f7f\u7528\uff1a", None))
        self.comboBox_timetype.setItemText(0, QCoreApplication.translate("Dialog", u"\u53d1\u5e03\u65f6\u95f4", None))
        self.comboBox_timetype.setItemText(1, QCoreApplication.translate("Dialog", u"\u6700\u540e\u7f16\u8f91\u65f6\u95f4", None))

        self.label_time.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u7f16\u8f91\u65f6\u95f4\u4fe1\u606f\uff1a</p></body></html>", None))
        self.textEdit_time.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u5bf9\u5e94\u89c4\u5219\uff1a/y\uff1a\u5e74\u4efd\uff1b/m\uff1a\u6708\u4efd\uff1b/d\uff1a\u65e5\u671f\uff1b/t\uff1a\u65f6\u95f4\u3002\u8981\u6253\u51fa/t\u53ef\u4ee5\u7528//t\u66ff\u4ee3\uff0c\u5176\u5b83\u540c\u7406\u3002", None))
        self.groupBox_subdata.setTitle(QCoreApplication.translate("Dialog", u"\u81ea\u5b9a\u4e49\u4fee\u6b63(\u652f\u6301python\u7684\u6b63\u5219\uff0c\u5bf9\u95ee\u9898\u63cf\u8ff0\u4e0e\u56de\u7b54\u5185\u5bb9\u6709\u6548)", None))
        self.pushButton_addline.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.pushButton_delline.setText(QCoreApplication.translate("Dialog", u"-", None))
        ___qtablewidgetitem = self.tableWidget_subdata.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u7c7b\u578b", None));
        ___qtablewidgetitem1 = self.tableWidget_subdata.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u539f\u6587\u5185\u5bb9", None));
        ___qtablewidgetitem2 = self.tableWidget_subdata.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u66ff\u6362\u5185\u5bb9", None));
        ___qtablewidgetitem3 = self.tableWidget_subdata.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa\u884c", None));
        self.pushButton_accept.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

