# !python
# -*- coding: utf-8 -*
import os
import json
import shutil
from path import join_path, get_path_ext


def is_json(file_path):
    # 可以考虑自动判断区分 JSON 格式文件与其他文本（ .js | .txt 等) ，而无需传入 command 参数
    json_extensions = (".json", ".fire", ".prefab")
    # text_extensions = (".js", ".ts", ".vue", ".react", ".py", ".txt")
    file_ext = get_path_ext(file_path)
    return file_ext in json_extensions


def load_file(file_path: str, encoding="utf-8"):
    """
    用于加载文件的内容。
    :param file_path: 文件路径
    :param encoding: 编码
    :return: File Content
    """
    try:
        with open(file_path, "r", encoding=encoding) as file:
            if is_json(file_path):
                return json.load(file)
            else:
                return file.read()
    except FileNotFoundError:
        return None


def write_file(content, dest_file: str, encoding="utf-8"):
    """
    写入内容至指定文件。
    :param content: 写入的内容
    :param dest_file: 目标路径
    :param encoding: 编码
    :return: void
    """
    with open(dest_file, "w", encoding=encoding) as file:
        if is_json(dest_file):
            json.dump(content, file, indent=2, ensure_ascii=False)
        else:
            file.write(content)
    # with open 语句可以自动管理文件的打开和关闭。
    # file: TextIO = open(dest_file, "w", encoding=encoding)
    # try:
    # finally:
    #     file.close() #  open 的打开需要手动关闭


def remove_files_with_extension(dir_path, extensions):
    pass


def copy_files_with_extension(
    dir_path, dest_path, extensions, is_same_structure=True, is_force=False
):
    """
    复制某一目录下，具有指定扩展名的文件到目标目录，同时可选是否保持原有的目录结构。
    :param dir_path: 源目录路径
    :param dest_path: 目标路径
    :param extensions: 扩展名列表
    :param is_same_structure: 是否保持目录结构一致，否-则统一在目录结构下
    :param is_force: 是否强制覆盖，当存在同名的文件会进行覆盖
    :return: void
    """
    if len(extensions) <= 0:
        return

    shutil.rmtree(dest_path)  # 决定是否先进行清除
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    for folder, dirs, files in os.walk(dir_path):
        destination = dest_path
        if is_same_structure:
            relative_path = os.path.relpath(folder, dir_path)
            if relative_path != ".":
                destination = join_path(dest_path, relative_path)

        for file in files:
            if not file.endswith(tuple(extensions)):
                continue
            if not os.path.exists(destination):
                os.makedirs(destination)
            source_file_path = join_path(folder, file)
            dest_file_path = join_path(destination, file)
            if os.path.exists(dest_file_path):
                if is_force:
                    os.remove(dest_file_path)
                else:
                    continue
            shutil.copy2(source_file_path, dest_file_path)

if __name__ == "__main__":
    write_file([{}, {}], 'debug.json')
