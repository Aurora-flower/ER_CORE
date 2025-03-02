# !python
# -*- coding: utf-8 -*


def get_dict_value(d, key, default=None):
    """
    用来防止读取 dict 的键时，不存在时的报错。
    :param d: dict 对象
    :param key: 属性的键
    :param default: 获取不到值时，提供的默认值
    :return:
    """
    try:
        return d[key]
    except (KeyError, TypeError):
        return default
