# !python
# -*- coding: utf-8 -*
import re


def contains_korean(text):
    # 匹配韩文字符的正则表达式
    pattern = "[\uAC00-\uD7AF\u3130-\u318F\uA960-\uA97F\uD7B0-\uD7FF]"
    return bool(re.search(pattern, text))


# ZH | KO
def is_contains_language_char(char, lang="ZH"):
    if lang == "ZH":
        # 检查是否为中文字符
        return "\u4e00" <= char <= "\u9fa5"
    if lang == "TW":
        if "\u4e00" <= char <= "\u9fa5":
            return False  # 排除简体字
        # 检查是否为繁体字
        return (
            "\u3400" <= char <= "\u4DBF"  # CJK 扩展 A 区
            or "\u20000" <= char <= "\u2A6DF"  # CJK 扩展 B 区
            or "\u2A700" <= char <= "\u2B73F"  # CJK 扩展 C 区
        )  # （一些常见的繁体字区间）
    elif lang == "KO":
        # 检查是否为韩文字符
        return "\uAC00" <= char <= "\uD7A3"
        # (
        #     "\uAC00" <= char <= "\uD7AF"
        #     or "\u3130" <= char <= "\u318F"
        #     or "\uA960" <= char <= "\uA97F"
        #     or "\uD7B0" <= char <= "\uD7FF"
        # )
    else:
        return False


def is_contains_language_string(string, lang="ZH"):
    # 这样写判断不准确
    # if force:
    #     return all([is_contains_language_char(char, lang) for char in string])
    # else:
    for char in string:
        if is_contains_language_char(char, lang):
            return True
    return False


def is_number(data):
    """
    检查变量是否为数字（整数、浮点数或复数类型）
    :param data: 数据对象
    :return: Bool
    """
    # assert isinstance(data, (int, float, complex)), "target_id is not number"
    return isinstance(data, (int, float, complex))


def contains_chinese(text):
    """
    检查文本中是否包含中文字符。
    """
    chinese_char_pattern = re.compile(r"[\u4e00-\u9fff]+")
    return bool(chinese_char_pattern.search(text))
