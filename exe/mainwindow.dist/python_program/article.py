from dataclasses import dataclass, asdict
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
import re
from html2text import HTML2Text
from python_gui.dialog_art import SetArt
import json
from pathlib2 import Path


# 保存回答内容的网页元素数据类
@dataclass
class ArtHtml:
    background: WebElement | None = None
    title: WebElement = None
    tag_list: WebElement = None
    article: WebElement = None
    author_name: WebElement = None
    author_avatar: WebElement = None
    author_word: WebElement = None
    time: WebElement = None
    like: WebElement = None
    comment: WebElement = None


# 对ArtHTML类中元素信息解析后存储的数据类
@dataclass
class DataHtmlArt:
    background: str = None
    title: str = None
    tag_list: tuple = None
    article: str = None
    author_name: str = None
    author_space: str = None
    author_avatar: str = None
    author_word: str = None
    time: tuple = None
    like: str = None
    comment: str = None


# 预览需求的数据类
@dataclass
class DataPreviewArt:
    background: str = None
    title: str = None
    author: str = None
    article: str = None
    time: str = None
    tag_list: str = None
    like: str = None
    comment: str = None
    error: str = None
    url: str = None


# 获取网页对应元素的函数
def get_html_art(driver: Chrome, xpath_dict: dict = None) -> ArtHtml:
    # sourcery skip: remove-redundant-if, use-contextlib-suppress
    """获取网页内容"""
    _dict = {}
    if xpath_dict is None:
        _xpath_data = {
            'background': '//div[@class="css-78p1r9"]/div/div/img',
            'title': '//h1[@class="Post-Title"]',
            'tag_list': '//div[@class="TopicList Post-Topics"]',
            'article': '//div[@class="RichText ztext Post-RichText css-4em6pe"]',
            'author_name': '//a[@class="UserLink-link" and @data-za-detail-view-element_name="User"]',
            'author_avatar': '//img[@class="Avatar AuthorInfo-avatar css-1y9jkzv"]',
            'author_word': '//div[@class="AuthorInfo-badge"]',
            'time': '//div[@class="ContentItem-time"]',
            'like': '//button[@class="Button VoteButton VoteButton--up"]',
            'comment': '//button[@class="Button BottomActions-CommentBtn Button'
                       '--plain Button--withIcon Button--withLabel"]'
        }
    else:
        _xpath_data = xpath_dict
    for _name, _xpath in _xpath_data.items():
        try:
            _element = driver.find_element(By.XPATH, _xpath)
            _dict[_name] = _element
        # 报错处理
        except Exception as _error:
            if _name != 'background':  # 部分文章没有背景图，没找到就直接无视
                match _name:
                    case 'title':
                        raise ValueError(f'文章标题获取出错，当前XPath使用:\n{_xpath}\n请检查网页元素是否对应正确。')
                    case 'tag_list':
                        raise ValueError(f'tag列表获取出错，当前XPath使用:\n{_xpath}\n请检查网页元素是否对应正确。')
                    case 'answer':
                        raise ValueError(f'回答正文获取出错，当前XPath使用:\n{_xpath}\n请检查网页元素是否对应正确。')
                    case 'author_name':
                        raise ValueError(f'作者ID获取出错，当前XPath使用:\n{_xpath}\n请检查网页元素是否对应正确。')
                    case 'author_avatar':
                        raise ValueError(f'作者头像获取出错，当前XPath使用:\n{_xpath}\n请检查网页元素是否对应正确。')
                    case 'author_word':
                        raise ValueError(f'作者签名获取出错，当前XPath使用:\n{_xpath}\n请检查网页元素是否对应正确。')
                    case 'time':
                        raise ValueError(f'时间信息获取出错，当前XPath使用:\n{_xpath}\n请检查网页元素是否对应正确。')
                    case 'like':
                        raise ValueError(f'点赞数获取出错，当前XPath使用:\n{_xpath}\n请检查网页元素是否对应正确。')
                    case 'comment':
                        raise ValueError(f'评论数获取出错，当前XPath使用:\n{_xpath}\n请检查网页元素是否对应正确。')

    return ArtHtml(**_dict)


# 处理数据的函数
def message_art(arthtml: ArtHtml) -> DataHtmlArt:
    # sourcery skip: use-getitem-for-re-match-groups
    _handle = HTML2Text()
    # 不知道为什么网页元素不能直接提取文本，所以用正则处理标题
    _dict = {'title': re.sub(r'\<h.*?\>(.*?)\</.*?\>', r'\1', arthtml.title.get_attribute('outerHTML'))}
    # 对空的问题描述单独处理
    if arthtml.background is not None:
        _dict['background'] = process_html_art(arthtml.background)
    else:
        _dict['background'] = ''
    # tag列表创建
    _list = []
    for _tag in arthtml.tag_list.find_elements(By.XPATH, '//a[@class="TopicLink"]'):
        _url = _tag.get_attribute('href')
        _elment = _tag.find_element(By.XPATH, './div[@class="css-1gomreu"]')
        _name = _elment.text
        _tag_tuple = (_name, _url)
        _list.append(_tag_tuple)
    # 转成元组
    _tuple = tuple(_list)
    _dict['tag_list'] = _tuple
    _dict['article'] = process_html_art(arthtml.article)
    # 作者信息
    _dict['author_name'] = arthtml.author_avatar.get_attribute('alt')
    _dict['author_space'] = arthtml.author_name.get_attribute('href')
    _dict['author_avatar'] = arthtml.author_avatar.get_attribute('src')
    _word = _handle.handle(arthtml.author_word.get_attribute('outerHTML'))
    _dict['author_word'] = re.sub(r'\n', '', _word)
    # 时间信息的获取
    _time = arthtml.time.text
    _match_1 = re.match(r'.*?(\d{4})-(\d{1,2})-(\d{1,2}) (\d{1,2}:\d{1,2})', _time)
    _t = (_match_1.group(1), _match_1.group(2), _match_1.group(3), _match_1.group(4))
    _dict['time'] = _t
    _like = arthtml.like.get_attribute('aria-label')
    _dict['like'] = re.match(r'赞同 (\d+?)', _like).group(1)
    _comment = arthtml.comment.text
    _comment_num = re.match(r'(\d+?) 条评论', _comment)
    if _comment_num is None:
        _dict['comment'] = '0'
    else:
        _dict['comment'] = _comment_num.group(1)
    return DataHtmlArt(**_dict)


# 获取最终正文数据的函数
def preview_art(datahtml: DataHtmlArt, setans: SetArt) -> DataPreviewArt:
    # 文本
    _article = datahtml.article
    _background = datahtml.background
    # 自定义修正的载入
    _error_sub_data = ''
    for _i in range(len(setans.sub_data)):
        _type = setans.sub_data[_i][0]
        _old = setans.sub_data[_i][1]
        _new = setans.sub_data[_i][2]
        if _type == 'str':
            _article = _article.replace(_old, _new)
            _background = _background.replace(_old, _new)
        else:
            try:
                _pattern = re.compile(_old)
                _article = _pattern.sub(_new, _article)
                _background = _pattern.sub(_new, _background)
            except Exception as _error:
                _error_sub_data += f'第{_i + 1}行出现错误:{_error}\n'

    # 数学公式的处理
    # 插入指定的前缀
    if setans.math_type != '':
        _article = re.sub(r'\$([\s\S]+?)\$', f'$\\{setans.math_type} \\1$', _article)
        _background = re.sub(r'\$([\s\S]+?)\$', f'$\\{setans.math_type} \\1$', _background)
    # 对自成一行的公式换行
    if setans.math_auto:
        _article = re.sub(r'(?P<head>\n\n|^)\$(?P<text>((?!\n\n)[^$])*?)\$(?P<end>\n\n|$)',
                          '\\g<head>$$\n\n\\g<text>\n\n$$\\g<end>', _article)
        _background = re.sub(r'(?P<head>\n\n|^)\$(?P<text>((?!\n\n)[^$])*?)\$(?P<end>\n\n|$)',
                             '\\g<head>$$\n\n\\g<text>\n\n$$\\g<end>', _background)

    # tag的处理
    _pattern_tag = re.compile(r'(?<!/)/n')
    _tag_list = ''
    for _i in range(len(datahtml.tag_list)):
        if _i != 0:
            _tag_list += setans.tag_interval
        _tag_name = _pattern_tag.sub(datahtml.tag_list[_i][0], setans.tag_name)
        _tag_name.replace('//n', '/n')
        _tag_list += f'[{_tag_name}]({datahtml.tag_list[_i][1]})'

    # 作者信息的处理
    _author = setans.author
    # 先保护//n的东西
    # 替换/n
    _pattern_author = re.compile(r'(?<!/)/[ntau]')
    # 替换函数

    def repl_author(_match) -> str:
        _s = _match.group()
        match _s:
            case '/a':
                if setans.avatar_with_size:
                    return f'<img src="{datahtml.author_avatar}" width=44px height=38px>'
                else:
                    return f'![]({datahtml.author_avatar})'
            case '/n':
                return datahtml.author_name
            case '/u':
                return datahtml.author_space
            case '/t':
                return datahtml.author_word
    _author = _pattern_author.sub(repl_author, _author)

    # 时间信息的处理
    _time = setans.time
    # 替换/n
    _pattern_time = re.compile(r'(?<!/)/[ymdt]')

    # 替换函数

    def repl_time(_match) -> str:
        _inf = datahtml.time
        _s = _match.group()
        match _s:
            case '/y':
                return _inf[0]
            case '/m':
                return _inf[1]
            case '/d':
                return _inf[2]
            case '/t':
                return _inf[3]

    _time = _pattern_time.sub(repl_time, _time)

    # 返回结果
    _result = DataPreviewArt(title=datahtml.title,
                             background=_background,
                             author=_author,
                             article=_article,
                             tag_list=_tag_list,
                             time=_time,
                             like=datahtml.like,
                             comment=datahtml.comment,
                             error=_error_sub_data)
    return _result


# 对问题细节与回答内容处理的函数
def process_html_art(element: WebElement) -> str:
    _handle = HTML2Text()
    # 初始参数的各种设置
    # 读取html并处理
    _html = element.get_attribute('outerHTML')
    # 获取tex并转为文本的形式
    for _el in element.find_elements(By.XPATH, '//span[@class="ztext-math"]'):
        _tex = _el.get_attribute('data-tex')
        _el_html = _el.get_attribute('outerHTML')
        _html = _html.replace(_el_html, f'${_tex}$')
    # 对提到的跳转链接的处理(保留链接与标题，以超链接的形式留存在文本中)
    for _el in element.find_elements(By.XPATH, '//div[@class ="RichText-LinkCardContainer"]/a'):
        _url = _el.get_attribute('href')
        _title = _el.get_attribute('data-text')
        _html = _html.replace(_el.get_attribute('outerHTML'), f'<p>[{_title}]({_url})</p>')
    # 转化html为markdown, 然后做基本修正
    _text = _handle.handle(_html)
    # 转换后markdown遇到公式就会换行，使用这个正则表达式替换
    _text = re.sub(r'(\$)\n([^\n])|([^\n])\n(\$)', r'\1\2\3\4', _text)
    return _text


if __name__ == '__main__':
    _option = ChromeOptions()
    # _option.add_argument('--headless')
    _option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')
    _service = Service(str(Path.cwd().parent.joinpath('driver', 'chromedriver.exe')))
    d = Chrome(service=_service, options=_option)

    _dir = Path.cwd().parent.joinpath('file', 'stealth.min.js')
    _js = Path(_dir).read_text()
    d.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": _js})
    d.get('https://zhuanlan.zhihu.com/p/452415452')
    d.implicitly_wait(10)
    _b = d.find_element(By.XPATH, '//button[@aria-label="关闭"]')
    _b.click()
    # _b = d.find_element(By.XPATH, '//button[@class="Button QuestionRichText-more Button--plain"]')
    # _b.click()
    with open(r'E:\pythonProject\ZhiHu\config\ans_set.json', 'r', encoding='utf-8') as _f:
        _dict = json.load(_f)
    _set = SetAns(**_dict)
    _html = get_html_art(d)
    _data = message_art(_html)
    _preview = preview_art(_data, _set)
    for i, j in asdict(_preview).items():
        print(f'{i}:\n{j}\n')

