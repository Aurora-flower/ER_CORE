# !python
# -*- coding: utf-8 -*
import os
import re
import sys
import time
import shutil
import platform

import opencc


# env = os.getenv('HOME')


def get_platform_by_arch() -> str:
    """
    通过 获取操作系统名称、机器类型进行细分系统平台类型
    :return: Platform
    """
    current_platform = platform.system().lower()
    architecture = platform.machine()
    if current_platform == "darwin":
        if architecture == "arm64":
            return "Mac_OS_ARM"
        else:  # 通常是 'x86_64' 或其他
            return "Mac_OS_X64"
    elif current_platform == "windows":
        return "Windows"
    elif current_platform == "linux":
        return "Linux"
    else:
        return ""


# def get_platform_by_osname() -> str:
#     """
#     通过 os 的 name 获取指示操作系统的类型。
#     'posix': 代表类 UNIX 系统，包括 Linux、macOS 等。
#     'nt': 代表 Windows 系统。
#     'java': 代表在 Java 平台上运行的环境，例如 Jython。
#
#     缺点：不够精确
#
#     :return: Platform
#     """
#     os_name = os.name
#     if os_name == "nt":
#         return "Windows"
#     elif os_name == "posix":
#         return "Mac_Or_Linux"
#     elif os_name == "java":
#         return "Jython"


# def get_platform() -> str:
#     if sys.platform == "darwin":
#         return "Mac_Os_X64"
#     elif sys.platform == "win32":
#         return "Windows"
#     elif sys.platform == "linux":
#         return "Linux"


def find_occurrences(text, pattern):
    """
    获取字符在文本中出现的下标位置
    """
    start = 0
    positions = []
    while True:
        start = text.find(pattern, start)
        if start == -1:
            break
        positions.append(start)
        start += 1
    return positions


def find_occurrences_regex(text, pattern):
    """
    获取字符串在文本中出现的位置
    re.escape() 转义特殊字符
    """
    regex = re.compile(re.escape(pattern))
    return [match.start() for match in regex.finditer(text)]


def exists(file_path):
    """
    判断文件是否存在
    """
    return os.path.exists(file_path)


def exists_create_dir(dirs):
    """
    判断文件夹是否存在，不存在则创建
    """
    dirs_list = [dirs] if isinstance(dirs, str) else dirs
    for folder in dirs_list:
        if not os.path.exists(folder):
            os.makedirs(folder)


class SwitchCase:
    key = "default"  # 默认值
    params = ()

    # 初始化
    def __init__(self, *args):
        self.params = args[1:]
        self.key = args[0] or "default"
        # for i, arg in enumerate(args, start=1):
        #     setattr(self, f"arg{i}", arg)

    def default(self):
        print("default:", self.params)


def case(*arg, key=""):
    switcher = SwitchCase(key, *arg)
    method = getattr(switcher, key, lambda: "Uncaught key")
    return method()


def get_locale_time():
    now = int(time.time())
    time_array = time.localtime(now)
    time_string = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return time_string


def clean_backup(backup_dir, max_files=5):
    files_in_dir = [
        f for f in os.listdir(backup_dir) if os.path.isfile(os.path.join(backup_dir, f))
    ]
    # 如果文件数超过最大值，清空目录
    if len(files_in_dir) > max_files:
        shutil.rmtree(backup_dir)
        os.makedirs(backup_dir)  # 重新创建目录


def remove_comments(content):
    # 匹配单行注释和多行注释
    pass


def remove_array_elements(target: list, elements):
    """
    删除列表中的指定元素
    :param target: 需要移除元素的对象
    :param elements: 元素（单个或多个）
    :return: 处理后的列表
    """
    if isinstance(elements, tuple):
        for element in elements:
            target.remove(element)
    elif isinstance(elements, str):
        target.remove(elements)
    return target


def rest_elements_to_array(target: list, elements):
    """
    相当于 js 中的 [...[x1, x2...]]，扩展运算符添加至列表的操作
    :param target: 列表对象
    :param elements: 元素列表
    :return: 处理后的列表
    """
    for element in elements:
        target.append(element)
    return target


def decode_html_entity(html: str) -> str:
    def replace_entity(match):
        code = int(match.group(1))
        return chr(code)

    return re.sub(r"&#(\d+);", replace_entity, html)


def convert_string(string: str, flag="Simplified") -> str:
    if flag == "Simplified":
        file = "t2s.json"  # 繁体转简体
    elif flag == "Traditional":
        file = "s2t.json"  # 简体转繁体
    else:
        raise ValueError("Invalid flag value, expected 'Simplified' or 'Traditional'.")
    converter = opencc.OpenCC(file)
    return converter.convert(string)
