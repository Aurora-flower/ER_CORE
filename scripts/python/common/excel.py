# !python
# -*- coding: utf-8 -*
import os
import sys
import numpy
import pandas
from file import load_file
from path import join_path

cwd = os.getcwd()


def json_to_excel(json_content: dict, file_path, columns, index=False):
    if isinstance(json_content, dict):
        # sorted(pairs, key=lambda x: int(x[0]), reverse=False)
        json_content = [value for k, value in json_content.items()]
    # debug
    # if columns is None:
    #     columns = json_content[0].keys() if json_content else []
    excel_df = pandas.DataFrame(json_content, columns=columns)
    excel_df.to_excel(file_path, index=index)


def load_excel(file_path, skip_lines=None, header_line=0):
    df = pandas.read_excel(io=f"{file_path}", skiprows=skip_lines, header=header_line)
    # df.columns = df.columns.str.strip()  # 去除列名的空格
    return df


def get_excel_columns(excel_path):
    excel_content = load_excel(excel_path)
    excel_data_frame = pandas.DataFrame(excel_content)
    return excel_data_frame.columns.tolist()


def get_excel_data(excel_path, key=None, skips=None):
    """
    获取表格数据，转为 dict
    :param excel_path: 表格路径
    :param key: dict 的指定键
    :param skips:
    :return: pandas.DataFrame.to_dict | None
    """
    excel_content = load_excel(excel_path, skip_lines=skips)  # [1, 2]
    excel_data_frame = pandas.DataFrame(excel_content)
    if excel_data_frame.empty:
        return dict()

    # excel_frame = None
    # 若要多语言转换，就不能指定索引键
    if key is not None:
        columns = tuple(excel_data_frame.columns)
        if key not in columns:
            print("Not Found key", file=sys.stderr)
            return None
        # 检查索引键的唯一性
        if excel_data_frame[key].duplicated().any():
            print(f"键 '{key}' 包含重复值。", file=sys.stderr)
            return None
        excel_frame = excel_data_frame.set_index(key, inplace=False).replace(
            numpy.nan, None
        )
    else:
        excel_frame = excel_data_frame.replace(numpy.nan, None)
    excel_json_data = excel_frame.to_dict(orient="index")
    return excel_json_data  # df.to_json
    # json_content = {str(i): {"a": i, "b": i * 2} for i in range(10)}
    # json_content = {int(k): v for k, v in json_content.items()}


if __name__ == "__main__":
    map_file_path = join_path(cwd, "script/files/map_config.json")
    # temp_svn_folder = "/Users/HuaYing/Desktop/resources/Work/.hidden_resource/qntestls"
    # locale_dir = join_path(temp_svn_folder, "locale")
    locale_dir = join_path(cwd, "script/files")
    is_exists_folder = os.path.exists(locale_dir)
    language_map_excel_path = join_path(
        locale_dir,
        "language_map.xlsx",  # f"{map_filename}_{current_lang}" 以某一语言为主体进行分类
    )
    # language_map_excel_path = join_path(cwd, "../files/language_map_excel.xlsx")
    language_map_data = load_file(map_file_path)
    process_zh_files = []
    json_to_excel(language_map_data, language_map_excel_path, ["ZH", "KO", "TW"])
