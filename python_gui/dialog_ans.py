from uic.dialog_answerset import Ui_Dialog  # 这里要改掉为自己的文件

# Pyside6的导入
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHeaderView,
    QComboBox,
    QTextEdit
)
from PySide6.QtCore import (
    QCoreApplication, Qt,
    Signal, Slot, QSize
)

# 其它模块的导入
from dataclasses import dataclass, asdict
from pathlib2 import Path
from sys import exit
from copy import deepcopy
import json


# 如果出现找不到部件的提示，可以加入下面这四行代码解决问题
# import PySide6
# _dir_name = path.dirname(PySide6.__file__)
# plugin_path = path.join(_dir_name, 'plugins', 'platforms')
# environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


# 数据类
@dataclass
class SetAns:
    math_type: str = None
    math_auto: bool = None
    tag_interval: str = None
    tag_name: str = None
    avatar_with_size: bool = None
    author: str = None
    time_type: int = None
    time: str = None
    sub_data: tuple = None


class DialogAns(QDialog):
    """
    注释
    """

    # 信号区
    data_submit = Signal(dict)

    def __init__(self, data_dict: dict = None):
        """
        注释
        """
        # UI加载
        super(DialogAns, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 列表控件头部修改
        self.ui.tableWidget_subdata.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 加载数据
        self.load(data_dict)

        # UI槽函数加载
        self.ui.pushButton_addline.clicked.connect(self.table_addline)
        self.ui.pushButton_delline.clicked.connect(self.table_delline)
        self.ui.pushButton_accept.clicked.connect(self.data_admit)
        self.ui.pushButton_quit.clicked.connect(self.close)

    """
    槽函数
    """
    # 在列表底部插入行
    @Slot()
    def table_addline(self):
        _num = self.ui.tableWidget_subdata.rowCount()
        self.ui.tableWidget_subdata.insertRow(_num)
        _combobox = QComboBox()
        _combobox.addItem('直接替换')
        _combobox.addItem('正则')
        self.ui.tableWidget_subdata.setCellWidget(_num, 0, _combobox)
        _text_edit1 = QTextEdit()
        _text_edit2 = QTextEdit()
        self.ui.tableWidget_subdata.setCellWidget(_num, 1, _text_edit1)
        self.ui.tableWidget_subdata.setCellWidget(_num, 2, _text_edit2)

    # 在列表底部删去行
    @Slot()
    def table_delline(self):
        _num = self.ui.tableWidget_subdata.rowCount()
        self.ui.tableWidget_subdata.removeRow(_num - 1)

    @Slot()
    def data_admit(self):
        _config = self.get_data()
        self.data_submit.emit(_config)
        self.close()

    """
    自定义函数
    """
    def load(self, data: dict = None):  # sourcery skip: use-contextlib-suppress
        # 参考数据
        _default = {
            'math_type': r'\displaystyle',
            'math_auto': True,
            'tag_interval': ' ',
            'tag_name': '__/n__',
            'avatar_with_size': True,
            'author': '作者：知乎用户/a[/n](/u) 签名：/t',
            'time_type': 0,
            'time': '发布时间：/y-/m-/d /t',
            'sub_data': [[r'\\{', r'\{'], [r'\\}', r'\}'], [r'\\\&', r'\\\ &']],
        }
        # 读取数据
        if data is None:
            _path = Path.cwd().parent.joinpath('config', 'ans_set.json')
            try:
                _dict = json.loads(Path(_path).read_text(encoding='utf-8'))
            except FileNotFoundError:
                _dict = _default
        else:
            _dict = deepcopy(data)
        # 载入数据
        _data = SetAns(**_dict)
        # 数学公式部分
        if _data.math_type != '':
            _index = self.ui.comboBox_mathtype.findText(_data.math_type)
            if _index != -1:
                self.ui.comboBox_mathtype.setCurrentIndex(_index)
        else:
            self.ui.comboBox_mathtype.setCurrentIndex(0)
        self.ui.checkBox_mathauto.setChecked(_data.math_auto)
        # tag设置的部分
        self.ui.lineEdit_interval.setText(_data.tag_interval)
        self.ui.lineEdit_tagname.setText(_data.tag_name)
        # 作者信息部分
        self.ui.checkBox_avatarwithsize.setChecked(_data.avatar_with_size)
        self.ui.textEdit_author.setPlainText(_data.author)
        # 时间信息
        self.ui.comboBox_timetype.setCurrentIndex(_data.time_type)
        self.ui.textEdit_time.setPlainText(_data.time)
        # 删去多余行
        self.table_delline()
        # 自定义修正
        for _i in range(len(_data.sub_data)):
            _old = _data.sub_data[_i][1]
            _new = _data.sub_data[_i][2]
            self.table_addline()
            if _data.sub_data[_i][0] == 're':
                self.ui.tableWidget_subdata.cellWidget(_i, 0).setCurrentIndex(1)
            self.ui.tableWidget_subdata.cellWidget(_i, 1).setPlainText(_old)
            self.ui.tableWidget_subdata.cellWidget(_i, 2).setPlainText(_new)

    # 获取当前设置的数据类
    def get_data(self) -> dict:  # sourcery skip: merge-dict-assign, move-assign
        _dict = {}
        # 数学公式的部分
        _mathtype = self.ui.comboBox_mathtype.currentText()
        _dict['math_type'] = _mathtype if _mathtype != '保持原公式' else ''
        _dict['math_auto'] = self.ui.checkBox_mathauto.isChecked()
        # tag设置的部分
        _dict['tag_interval'] = self.ui.lineEdit_interval.text()
        _dict['tag_name'] = self.ui.lineEdit_tagname.text()
        # 作者信息部分
        _dict['avatar_with_size'] = self.ui.checkBox_avatarwithsize.isChecked()
        _dict['author'] = self.ui.textEdit_author.toPlainText()
        # 时间信息
        _dict['time_type'] = self.ui.comboBox_timetype.currentIndex()
        _dict['time'] = self.ui.textEdit_time.toPlainText()
        # 自定义修正
        _num = self.ui.tableWidget_subdata.rowCount()
        _list = []
        for _i in range(_num):
            _sig = self.ui.tableWidget_subdata.cellWidget(_i, 0).currentText()
            _type = 're' if _sig == '正则' else 'str'
            _old = self.ui.tableWidget_subdata.cellWidget(_i, 1).toPlainText()
            _new = self.ui.tableWidget_subdata.cellWidget(_i, 2).toPlainText()
            _list.append((_type, _old, _new))
        _dict['sub_data'] = tuple(_list)
        return _dict


@Slot(dict)
def test(con):
    _path = Path.cwd().parent.joinpath('config', 'ans_set.json')
    Path(_path).write_text(json.dumps(con), encoding='utf-8')


# 运行
def main():
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication()
    # 更改界面样式，windows的我个人不喜欢
    app.setStyle('fusion')
    window = DialogAns()
    window.data_submit.connect(test)

    # 选择是否加载qss
    # qss_file = Path.joinpath(Path.cwd(), 'qss', 'style.qss')
    # style_sheet = qss_file.read_text(encoding='utf-8')
    # window.setStyleSheet(style_sheet)

    window.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
