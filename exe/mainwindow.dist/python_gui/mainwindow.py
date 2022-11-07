from uic.mainwindow_ZhiHu import Ui_MainWindow  # 这里要改掉为自己的文件

# Pyside6的导入
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QMessageBox, QFileDialog,
    QHeaderView, QLineEdit
)
from PySide6.QtCore import (
    QCoreApplication, Qt,
    Slot, Signal,
    QTimer
)

# 其它模块的导入
from pathlib2 import Path
from sys import exit
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import re
import threading
from os import startfile
from python_gui.dialog_ans import SetAns, DialogAns
from python_gui.dialog_art import SetArt, DialogArt
from python_program.answer import get_html_ans, message_ans, preview_ans
from python_program.article import get_html_art, message_art, preview_art
import json


# 如果出现找不到部件的提示，可以加入下面这四行代码解决问题
# import PySide6
# _dir_name = path.dirname(PySide6.__file__)
# plugin_path = path.join(_dir_name, 'plugins', 'platforms')
# environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class MainWindow(QMainWindow):
    """
    注释
    """

    # 信号区
    sig_ans = Signal(str)
    sig_art = Signal(str)

    def __init__(self):
        """
        注释
        """
        # UI加载
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 浏览器驱动
        _option = ChromeOptions()
        _option.add_argument('--headless')
        _option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')
        # 驱动路径设置
        try:
            _service = Service(str(Path.cwd().parent.joinpath('driver', 'chromedriver.exe')))
            self.driver = Chrome(service=_service, options=_option)
            _dir = Path.cwd().parent.joinpath('file', 'stealth.min.js')
            _js = Path(_dir).read_text()
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": _js})
        except Exception as _error:
            QMessageBox.warning(self, '打开错误报告', f'错误报告：\n{_error}')
            self.close()
        # 子窗口的变量
        self.sub_window_ans = None
        self.sub_window_art = None
        # 读取内容的变量
        self.data_ans = None
        self.preview_ans = None
        self.preview_allow_ans = False
        _path = Path.cwd().parent.joinpath('config', 'ans_set.json')
        self.set_ans = json.loads(Path(_path).read_text(encoding='utf-8'))
        self.data_art = None
        self.preview_art = None
        self.preview_allow_art = False
        _path = Path.cwd().parent.joinpath('config', 'art_set.json')
        self.set_art = json.loads(Path(_path).read_text(encoding='utf-8'))
        # 检测的计时器
        self.timer_sig_ans = QTimer()
        self.timer_sig_art = QTimer()
        # 列表的表头与内容设置
        self.ui.tableWidget_sub_ans.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_sub_art.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for _i in range(self.ui.tableWidget_sub_ans.rowCount()):
            _lineedit = QLineEdit()
            _lineedit.setPlaceholderText('不可留空，不可使用除英文与数字以外的符号')
            self.ui.tableWidget_sub_ans.setCellWidget(_i, 0, _lineedit)
        for _i in range(self.ui.tableWidget_sub_art.rowCount()):
            _lineedit = QLineEdit()
            _lineedit.setPlaceholderText('不可留空，不可使用除英文与数字以外的符号')
            self.ui.tableWidget_sub_art.setCellWidget(_i, 0, _lineedit)
        # UI槽函数加载
        # 回答部分
        self.ui.pushButton_get_ans.clicked.connect(self.m_get_ans)
        self.ui.pushButton_setmodel_ans.clicked.connect(self.subwindow_set_ans)
        self.ui.textEdit_model_ans.textChanged.connect(self.preview_text_ans)
        self.ui.pushButton_setdir_ans.clicked.connect(self.change_save_dir_ans)
        self.ui.pushButton_savefile_ans.clicked.connect(self.save_ans)
        self.ui.commandLinkButton_filedir_ans.clicked.connect(self.open_dir_ans)
        self.ui.comboBox_filetype_ans.currentIndexChanged.connect(self.preview_text_ans)
        self.ui.pushButton_importmodel_ans.clicked.connect(self.import_model_ans)
        self.ui.pushButton_exportmodel_ans.clicked.connect(self.export_model_ans)
        self.timer_sig_ans.timeout.connect(self.change_sig_ans)
        self.sig_ans.connect(self.start_sig_ans)
        # 文章部分
        self.ui.pushButton_get_art.clicked.connect(self.m_get_art)
        self.ui.pushButton_setmodel_art.clicked.connect(self.subwindow_set_art)
        self.ui.textEdit_model_art.textChanged.connect(self.preview_text_art)
        self.ui.pushButton_setdir_art.clicked.connect(self.change_save_dir_art)
        self.ui.pushButton_savefile_art.clicked.connect(self.save_art)
        self.ui.commandLinkButton_filedir_art.clicked.connect(self.open_dir_art)
        self.ui.comboBox_filetype_art.currentIndexChanged.connect(self.preview_text_art)
        self.ui.pushButton_importmodel_art.clicked.connect(self.import_model_art)
        self.ui.pushButton_exportmodel_art.clicked.connect(self.export_model_art)
        self.timer_sig_art.timeout.connect(self.change_sig_art)
        self.sig_art.connect(self.start_sig_art)

    """
    槽函数
    """
    # 获取回答网页并读取网页内容
    @Slot()
    def m_get_ans(self):
        """创建子线程调用回答爬虫函数"""
        _pattern = re.compile(r'^https://www\.zhihu\.com/question/\d*?/answer/\d*?$')
        if _pattern.match(self.ui.lineEdit_url_ans.text()) is None:
            self.ui.label_sig_ans.setText('url格式错误')
        else:
            # 禁止其它发送请求的操作
            self.ui.pushButton_get_ans.setDisabled(True)
            self.ui.pushButton_get_art.setDisabled(True)
            # 创建子进程尝试连接
            _t_get_ans = threading.Thread(target=self.get_ans)
            _t_get_ans.start()

    # 开始回答读取信号
    @Slot(str)
    def start_sig_ans(self, text):
        """根据给定的文本，开启指示标签计时器"""
        if text != '':
            self.ui.label_sig_ans.setText(f'{text}中.')
            self.timer_sig_ans.start(500)
        else:
            self.timer_sig_ans.stop()

    # 呼出子窗口
    @Slot()
    def subwindow_set_ans(self):
        """呼出回答爬虫属性设置子窗口"""
        del self.sub_window_ans
        self.sub_window_ans = DialogAns(self.set_ans)
        self.sub_window_ans.show()

        def submit(data: dict):
            self.preview_allow_ans = False
            sub_t = threading.Thread(target=sub_thread, args=(data,))
            sub_t.start()
            sub_t.join()
            # 重新加载预览
            if self.preview_ans is not None:
                self.preview_text_ans()

        def sub_thread(data: dict):
            # 更新set_ans里的数据
            self.set_ans = data
            # 如果已经载入了数据，那么同时更新预览的数据preview_ans
            if self.data_ans is not None:
                _url = self.preview_ans.url
                self.preview_ans = preview_ans(self.data_ans, SetAns(**self.set_ans))
                self.preview_ans.url = _url
                self.preview_allow_ans = True

        self.sub_window_ans.data_submit.connect(submit)

    @Slot()
    def preview_text_ans(self):
        """回答爬虫预览文本刷新"""
        # 检测是否有空项
        _permission = True
        for _i in range(8):
            _p = self.ui.tableWidget_sub_ans.cellWidget(_i, 0).text()
            if re.match('^[a-zA-Z0-9]+?$', _p) is None:
                _permission = False
                QMessageBox.warning(self, '模板错误', '存在不合规的替代')
                break
        # 当允许编辑时才加载预览
        if self.preview_allow_ans and _permission:
            _text = self.process_ans()
            # 根据给定类型设置预览样式
            _type = self.ui.comboBox_filetype_ans.currentText()
            if _type == '.md':
                self.ui.textEdit_preview_ans.setMarkdown(_text)
            else:
                self.ui.textEdit_preview_ans.setPlainText(_text)

    @Slot()
    def change_save_dir_ans(self):
        """改变回答存储目录，同时变更快捷打开回答保存目录按钮的文本"""
        _dir_start = self.ui.commandLinkButton_filedir_ans.text()
        if Path(_dir_start).is_dir():
            _dir = QFileDialog.getExistingDirectory(self, '保存位置设置', _dir_start)
        else:
            _dir = QFileDialog.getExistingDirectory(self, '保存位置设置', str(Path.cwd()))
        if _dir != '':
            self.ui.commandLinkButton_filedir_ans.setText(_dir)

    @Slot()
    def open_dir_ans(self):
        """打开回答快捷保存目录"""
        _dir = self.ui.commandLinkButton_filedir_ans.text()
        if Path(_dir).is_dir():
            startfile(_dir)
        else:
            QMessageBox.warning(self, '打开目录异常', '目标目录不存在或无法打开')

    @Slot()
    def save_ans(self):
        """保存当前数据与模板所确定的回答到指定文件"""
        _dir = self.ui.commandLinkButton_filedir_ans.text()
        if Path(_dir).is_dir():
            _type = self.ui.comboBox_filetype_ans.currentText()
            _name = self.ui.lineEdit_filename_ans.text()
            if _name == '':
                QMessageBox.critical(self, '保存文件错误', '请输入文件名')
            else:
                try:
                    _text = self.process_ans()
                    _path = Path(Path(_dir).joinpath(_name + _type))
                    _path.write_text(_text, encoding='utf-8')
                except Exception as _error:
                    QMessageBox.critical(self, '保存文件错误', f'错误报告：\n{_error}')
        else:
            QMessageBox.warning(self, '保存目录异常', '目标目录不存在或无法打开')

    @Slot()
    def import_model_ans(self):
        """加载外部json文件模板，包括设置与代称"""
        _file_path = QFileDialog.getOpenFileName(self, '导入模板', str(Path.cwd()), 'json文件(*.json)')
        if _file_path[0] != '':
            _file = Path(_file_path[0])
            try:
                _json = _file.read_text(encoding='utf-8')
                _dict = json.loads(_json)
                # 检查导入的文件是否是模板
                if _dict['model_type'] != 'answer':
                    raise ValueError()
                if type(_dict['set_ans']) != dict:
                    raise ValueError()
                self.set_ans = _dict['set_ans']
                if len(_dict['model_name']) != 9:
                    raise ValueError()
                for _i in range(9):
                    self.ui.tableWidget_sub_ans.cellWidget(_i, 0).setText(_dict['model_name'][_i])
                if type(_dict['model']) != str:
                    raise ValueError()
                self.ui.textEdit_model_ans.setPlainText(_dict['model'])
            except Exception:
                QMessageBox.warning(self, '导入模板失败', '导入了不合规模板。')

    @Slot()
    def export_model_ans(self):
        """根据当前社渚数据与代称保存模板为json文件"""
        # 检测模板所需信息是否齐全
        _permission = True
        _model_name = []
        for _i in range(9):
            _p = self.ui.tableWidget_sub_ans.cellWidget(_i, 0).text()
            if re.match('^[a-zA-Z0-9]+?$', _p) is None:
                _permission = False
                QMessageBox.warning(self, '模板错误', '存在不合规的替代')
                break
            else:
                _model_name.append(_p)
        if _permission:
            _save_path = QFileDialog.getSaveFileName(self, '保存模板', str(Path.cwd()), 'json文件(*.json)')
            if _save_path[0] != '':
                _file = Path(_save_path[0])
                _dict = {
                    'model_type': 'answer',
                    'set_ans': self.set_ans,
                    'model': self.ui.textEdit_model_ans.toPlainText(),
                    'model_name': _model_name
                }
                _json = json.dumps(_dict)
                _file.write_text(_json, encoding='utf-8')

    # 获取文章网页并读取网页内容
    @Slot()
    def m_get_art(self):
        """创建子线程调用文章爬虫函数"""
        _pattern = re.compile(r'^https://zhuanlan\.zhihu\.com/p/\d+?$')
        if _pattern.match(self.ui.lineEdit_url_art.text()) is None:
            self.ui.label_sig_art.setText('url格式错误')
        else:
            # 禁止其它发送请求的操作
            self.ui.pushButton_get_ans.setDisabled(True)
            self.ui.pushButton_get_art.setDisabled(True)
            # 创建子进程尝试连接
            _t_get_art = threading.Thread(target=self.get_art)
            _t_get_art.start()

    # 开始文章读取信号
    @Slot(str)
    def start_sig_art(self, text):
        """根据给定的文本，开启指示标签计时器"""
        if text != '':
            self.ui.label_sig_art.setText(f'{text}中.')
            self.timer_sig_art.start(500)
        else:
            self.timer_sig_art.stop()

    # 呼出子窗口
    @Slot()
    def subwindow_set_art(self):
        """呼出回答爬虫属性设置子窗口"""
        del self.sub_window_art
        self.sub_window_art = DialogArt(self.set_art)
        self.sub_window_art.show()

        def submit(data: dict):
            self.preview_allow_art = False
            sub_t = threading.Thread(target=sub_thread, args=(data,))
            sub_t.start()
            sub_t.join()
            # 重新加载预览
            if self.preview_art is not None:
                self.preview_text_art()

        def sub_thread(data: dict):
            # 更新set_art里的数据
            self.set_art = data
            # 如果已经载入了数据，那么同时更新预览的数据preview_ans
            if self.data_art is not None:
                _url = self.preview_art.url
                self.preview_art = preview_art(self.data_art, SetArt(**self.set_art))
                self.preview_art.url = _url
                self.preview_allow_art = True

        self.sub_window_art.data_submit.connect(submit)

    @Slot()
    def preview_text_art(self):
        """回答爬虫预览文本刷新"""
        # 检测是否有空项
        _permission = True
        for _i in range(8):
            _p = self.ui.tableWidget_sub_art.cellWidget(_i, 0).text()
            if re.match('^[a-zA-Z0-9]+?$', _p) is None:
                _permission = False
                QMessageBox.warning(self, '模板错误', '存在不合规的替代')
                break
        # 当允许编辑时才加载预览
        if self.preview_allow_art and _permission:
            _text = self.process_art()
            # 根据给定类型设置预览样式
            _type = self.ui.comboBox_filetype_art.currentText()
            if _type == '.md':
                self.ui.textEdit_preview_art.setMarkdown(_text)
            else:
                self.ui.textEdit_preview_art.setPlainText(_text)

    @Slot()
    def change_save_dir_art(self):
        """改变回答存储目录，同时变更快捷打开回答保存目录按钮的文本"""
        _dir_start = self.ui.commandLinkButton_filedir_art.text()
        if Path(_dir_start).is_dir():
            _dir = QFileDialog.getExistingDirectory(self, '保存位置设置', _dir_start)
        else:
            _dir = QFileDialog.getExistingDirectory(self, '保存位置设置', str(Path.cwd()))
        if _dir != '':
            self.ui.commandLinkButton_filedir_art.setText(_dir)

    @Slot()
    def open_dir_art(self):
        """打开回答快捷保存目录"""
        _dir = self.ui.commandLinkButton_filedir_art.text()
        if Path(_dir).is_dir():
            startfile(_dir)
        else:
            QMessageBox.warning(self, '打开目录异常', '目标目录不存在或无法打开')

    @Slot()
    def save_art(self):
        """保存当前数据与模板所确定的回答到指定文件"""
        _dir = self.ui.commandLinkButton_filedir_art.text()
        if Path(_dir).is_dir():
            _type = self.ui.comboBox_filetype_art.currentText()
            _name = self.ui.lineEdit_filename_art.text()
            if _name == '':
                QMessageBox.critical(self, '保存文件错误', '请输入文件名')
            else:
                try:
                    _text = self.process_art()
                    _path = Path(Path(_dir).joinpath(_name + _type))
                    _path.write_text(_text, encoding='utf-8')
                except Exception as _error:
                    QMessageBox.critical(self, '保存文件错误', f'错误报告：\n{_error}')
        else:
            QMessageBox.warning(self, '保存目录异常', '目标目录不存在或无法打开')

    @Slot()
    def import_model_art(self):
        """加载外部json文件模板，包括设置与代称"""
        _file_path = QFileDialog.getOpenFileName(self, '导入模板', str(Path.cwd()), 'json文件(*.json)')
        if _file_path[0] != '':
            _file = Path(_file_path[0])
            try:
                _json = _file.read_text(encoding='utf-8')
                _dict = json.loads(_json)
                # 检查导入的文件是否是模板
                if _dict['model_type'] != 'article':
                    raise ValueError()
                if type(_dict['set_art']) != dict:
                    raise ValueError()
                self.set_art = _dict['set_art']
                if len(_dict['model_name']) != 9:
                    raise ValueError()
                for _i in range(9):
                    self.ui.tableWidget_sub_art.cellWidget(_i, 0).setText(_dict['model_name'][_i])
                if type(_dict['model']) != str:
                    raise ValueError()
                self.ui.textEdit_model_art.setPlainText(_dict['model'])
            except Exception:
                QMessageBox.warning(self, '导入模板失败', '导入了不合规模板。')

    @Slot()
    def export_model_art(self):
        """根据当前社渚数据与代称保存模板为json文件"""
        # 检测模板所需信息是否齐全
        _permission = True
        _model_name = []
        for _i in range(9):
            _p = self.ui.tableWidget_sub_art.cellWidget(_i, 0).text()
            if re.match('^[a-zA-Z0-9]+?$', _p) is None:
                _permission = False
                QMessageBox.warning(self, '模板错误', '存在不合规的替代')
                break
            else:
                _model_name.append(_p)
        if _permission:
            _save_path = QFileDialog.getSaveFileName(self, '保存模板', str(Path.cwd()), 'json文件(*.json)')
            if _save_path[0] != '':
                _file = Path(_save_path[0])
                _dict = {
                    'model_type': 'article',
                    'set_art': self.set_art,
                    'model': self.ui.textEdit_model_art.toPlainText(),
                    'model_name': _model_name
                }
                _json = json.dumps(_dict)
                _file.write_text(_json, encoding='utf-8')

    """
    自定义函数
    """
    # 获取url对应回答网页
    def get_ans(self):  # sourcery skip: use-contextlib-suppress
        self.preview_allow_ans = False
        self.sig_ans.emit('连接')
        _url = self.ui.lineEdit_url_ans.text()
        self.driver.get(_url)
        # 浏览器驱动转到知乎网页会弹出登录窗口，若转到错误页面则没有该窗口，以该窗口关闭按钮为成功判断标准
        try:
            self.driver.implicitly_wait(4)
            _button = self.driver.find_element(By.XPATH, '//button[@aria-label="关闭"]')
            _button.click()
        except Exception:
            self.sig_ans.emit('')
            self.ui.label_sig_ans.setText('连接失败，已放弃')
        else:
            self.sig_ans.emit('')
            self.ui.label_sig_ans.setText('连接成功')
            sleep(0.4)
            self.sig_ans.emit('读取')
            # 尝试点击展开按钮，没有就不管
            try:
                _button = self.driver.find_element(By.XPATH,
                                                   '//button[@class="Button QuestionRichText-more Button--plain"]')
                _button.click()
            except Exception:
                pass
            # 读取数据，存储到相应变量
            try:
                _html_ans = get_html_ans(self.driver)
                self.data_ans = message_ans(_html_ans)
                self.preview_ans = preview_ans(self.data_ans, SetAns(**self.set_ans))
                self.preview_ans.url = _url
                self.preview_allow_ans = True
                # 停止信号
                self.sig_ans.emit('')
                self.ui.label_sig_ans.setText('读取完毕，可以开始进一步的编辑')
            except Exception as _error:
                self.preview_allow_ans = False
                self.sig_ans.emit('')
                self.ui.label_sig_ans.setText('读取失败，已放弃')
                QMessageBox.warning(self, '读取错误报告', f'错误报告：\n{_error}')
            finally:
                # 解放发送请求的按钮
                self.ui.pushButton_get_ans.setDisabled(False)
                self.ui.pushButton_get_art.setDisabled(False)

    def process_ans(self) -> str:
        # 生成正则的替换模式
        _tuple = tuple(self.ui.tableWidget_sub_ans.cellWidget(_i, 0).text() for _i in range(9))
        _pattern = '|'.join(_tuple)

        # 正则替换的函数
        def repl(match):
            _s = match.group()
            if _s == _tuple[0]:
                return self.preview_ans.question
            elif _s == _tuple[1]:
                return self.preview_ans.detail
            elif _s == _tuple[2]:
                return self.preview_ans.author
            elif _s == _tuple[3]:
                return self.preview_ans.answer
            elif _s == _tuple[4]:
                return self.preview_ans.time
            elif _s == _tuple[5]:
                return self.preview_ans.tag_list
            elif _s == _tuple[6]:
                return self.preview_ans.like
            elif _s == _tuple[7]:
                return self.preview_ans.comment
            elif _s == _tuple[8]:
                return self.preview_ans.url

        _model = self.ui.textEdit_model_ans.toPlainText()
        _text = re.sub(_pattern, repl, _model)
        return _text

    # 变更信号标签
    def change_sig_ans(self):
        _text = self.ui.label_sig_ans.text()
        if len(_text) < 6:
            self.ui.label_sig_ans.setText(f'{_text}.')
        else:
            self.ui.label_sig_ans.setText(f'{_text[:2]}中.')

    # 获取url对应文章
    def get_art(self):  # sourcery skip: use-contextlib-suppress
        self.preview_allow_art = False
        self.sig_art.emit('连接')
        _url = self.ui.lineEdit_url_art.text()
        self.driver.get(_url)
        # 浏览器驱动转到知乎网页会弹出登录窗口，若转到错误页面则没有该窗口，以该窗口关闭按钮为成功判断标准
        try:
            self.driver.implicitly_wait(4)
            _button = self.driver.find_element(By.XPATH, '//button[@aria-label="关闭"]')
            _button.click()
        except Exception:
            self.sig_art.emit('')
            self.ui.label_sig_art.setText('连接失败，已放弃')
        else:
            self.sig_art.emit('')
            self.ui.label_sig_art.setText('连接成功')
            sleep(0.4)
            self.sig_art.emit('读取')
            # 读取数据，存储到相应变量
            try:
                _html_art = get_html_art(self.driver)
                self.data_art = message_art(_html_art)
                self.preview_art = preview_art(self.data_art, SetArt(**self.set_art))
                self.preview_art.url = _url
                self.preview_allow_art = True
                # 停止信号
                self.sig_art.emit('')
                self.ui.label_sig_art.setText('读取完毕，可以开始进一步的编辑')
            except Exception as _error:
                self.preview_allow_art = False
                self.sig_art.emit('')
                self.ui.label_sig_art.setText('读取失败，已放弃')
                QMessageBox.warning(self, '读取错误报告', f'错误报告：\n{_error}')
            finally:
                # 解放发送请求的按钮
                self.ui.pushButton_get_ans.setDisabled(False)
                self.ui.pushButton_get_art.setDisabled(False)

    def process_art(self) -> str:
        # 生成正则的替换模式
        _tuple = tuple(self.ui.tableWidget_sub_art.cellWidget(_i, 0).text() for _i in range(9))
        _pattern = '|'.join(_tuple)

        # 正则替换的函数
        def repl(match):
            _s = match.group()
            if _s == _tuple[0]:
                return self.preview_art.background
            elif _s == _tuple[1]:
                return self.preview_art.title
            elif _s == _tuple[2]:
                return self.preview_art.author
            elif _s == _tuple[3]:
                return self.preview_art.article
            elif _s == _tuple[4]:
                return self.preview_art.time
            elif _s == _tuple[5]:
                return self.preview_art.tag_list
            elif _s == _tuple[6]:
                return self.preview_art.like
            elif _s == _tuple[7]:
                return self.preview_art.comment
            elif _s == _tuple[8]:
                return self.preview_art.url

        _model = self.ui.textEdit_model_art.toPlainText()
        _text = re.sub(_pattern, repl, _model)
        return _text

    # 变更信号标签
    def change_sig_art(self):
        _text = self.ui.label_sig_art.text()
        if len(_text) < 6:
            self.ui.label_sig_art.setText(f'{_text}.')
        else:
            self.ui.label_sig_art.setText(f'{_text[:2]}中.')


# 运行
def main():
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication()
    # 更改界面样式，windows的我个人不喜欢
    app.setStyle('fusion')
    window = MainWindow()

    # 选择是否加载qss
    # qss_file = Path.joinpath(Path.cwd().parent, 'qss', 'style.qss')
    # style_sheet = qss_file.read_text(encoding='utf-8')
    # window.setStyleSheet(style_sheet)

    window.show()

    exit(app.exec())
    window.driver.quit()


if __name__ == '__main__':
    main()
