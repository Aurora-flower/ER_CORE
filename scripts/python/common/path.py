# !python
# -*- coding: utf-8 -*
import os
from pathlib import Path

sep = os.sep  # 文件分隔符

extsep = os.path.extsep  # 文件扩展分隔符


def get_path_ext(file_path):
    """
    获取文件路径的后缀
    :param file_path: 文件路径
    :return: ext
    """
    return Path(file_path).suffix


def get_path_parse(file_path):
    """
    用于获取路径的解析信息
    :param file_path: 文件路径
    :return: parser info
    """
    dirname = os.path.dirname(file_path)
    basename = os.path.basename(file_path)
    base, ext = os.path.splitext(file_path)
    return {
        "dir": dirname,
        "name": basename,
        "base": base,
        "ext": ext,
        "path": file_path,
    }


def replace_path_sep(file_path):
    """
    :param file_path: 文件路径
    :return: path

    @remarks
    windows 下直接拼接 config 中的路径，存在 xxx\\xxxx/xxx 形式的路径
    """
    file_path = file_path
    if sep == "\\":
        file_path = file_path.replace("/", sep)
    elif sep == "/":
        file_path = file_path.replace("//", "/")
    return file_path


def join_path(*paths):
    """
    拼接路径，并做替换路径拼接符的处理
    @remarks
    normpath -  规范化路径，去除多余的路径分隔符和解析相对路径
    """
    joined_path = os.path.join("", *paths)
    handling_path = os.path.normpath(joined_path)
    return replace_path_sep(handling_path)
