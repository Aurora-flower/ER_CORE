# !python
# -*- coding: utf-8 -*
import re

demo_pattern = {
    "space": r"[\s\t\r\n]+",  # 空格
    "comment": r"//.*?$|/\*(?:.|\n)*?\*/",  # 注释
    "zh": r"[\u4e00-\u9fa5]+",  # 中文
    "string": r"\"(.*?)\"|\'(.*?)\'|`(.*?)`",  # 字符串(字面量)
    "en": r"[a-zA-Z]+",  # 英文
    "num": r"[0-9]+",  # 数字
    "symbol": r"[!@#$%^&*()_+{}:\"<>?/|\\]",  # 特殊符号
    "email": r"",  # 邮箱
    "url": r"",  # url
    "ip": r"",  # ip 地址
}


# verbose 示例
verbose_pattern = r"""
\d+ # 一个或多个数字
\s* # 零个或多个空格
[a-z]+ # 一个多个小写字母
"""

mode = {
    "default": 0,  # 普通的单行模式。^ 只匹配整个字符串的开头，$ 只匹配整个字符串的结尾，. 不会匹配换行符。
    "ignore": re.IGNORECASE,  # re.I 不区分大小写
    "multiline": re.MULTILINE,  # re.M 使用 ^ 和 $ 匹配每一行的开始和结束，而不仅仅是整个字符串的开始和结束
    "verbose": re.VERBOSE,  # 允许使用更易读的格式书写正则表达式，可以在表达式中添加空格和注释
    "ascii": re.ASCII,  # 在匹配时仅考虑 ASCII 字符，而不是 Unicode 字符
    "dotall": re.DOTALL,  # 使 . 匹配所有的字符，包括换行符
    "between": re.DOTALL | re.MULTILINE,
}


def match_pattern(pattern, string, flag="default"):
    """
    从字符串的起始位置匹配正则表达式。
    如果起始位置匹配成功，返回一个匹配对象，否则返回 None。
    :param pattern: 匹配模式
    :param string: 字符串
    :param flag: 指定标志
    :return: 匹配元素
    """
    ms = re.match(pattern, string, mode[flag])
    return ms.group() if ms else None


def search_pattern(pattern, string, flag="default"):
    """
    搜索整个字符串，返回第一个匹配的结果。如果没有匹配，返回 None
    :param pattern: 匹配模式
    :param string: 字符串
    :param flag: 指定标志
    :return: 匹配元素
    """
    ms = re.search(pattern, string, mode[flag])
    return ms.group() if ms else None


def find_pattern(pattern, string, flag="default"):
    """
    返回字符串中所有匹配的结果，以列表形式返回。
    :param pattern: 匹配模式
    :param string: 字符串
    :param flag: 指定标志
    :return: 匹配列表
    """
    ms = re.findall(pattern, string, mode[flag])
    return ms  # if ms else None


def substring_pattern(pattern, replacement, string, count=0, flag="default"):
    """
    替换匹配的字符串
    :param pattern: 匹配模式
    :param string: 字符串
    :param replacement: 替换内容
    :param count: 指定要替换的最大次数。默认情况下，count 的值为 0，这意味着会替换所有匹配的实例
    :param flag: 指定标志
    :return: 处理后的文本
    """
    handled_string = re.sub(pattern, replacement, string, count, mode[flag])
    return handled_string


def split_pattern(pattern, string, flag="default"):
    """
    根据匹配的模式分割字符串，返回列表
    :param pattern: 匹配模式
    :param string: 字符串
    :param flag: 指定标志
    :return: 切割列表
    """
    ms = re.split(pattern, string, mode[flag])
    return ms


def compile_pattern(pattern, flag="default"):
    """
    性能提升 - 编译一次后可以重复使用，避免每次调用都重新解析字符串。
    可读性 -  使用编译的正则表达式对象，可以让代码更清晰。
    复用标志 -  在编译时指定标志，比如 re.DOTALL 等，简化调用时的参数。
    方法访问 - 编译后的正则表达式对象可以直接调用方法（如 match()、search()、findall() 等）。
    :param pattern: 匹配模式
    :param flag: 指定标志
    :return: 正则表达式对象
    """
    return re.compile(pattern, mode[flag])


def finditer_pattern(pattern, string):
    """

    :param pattern:
    :param string:
    :return:
    """
    return re.finditer(pattern, string)
