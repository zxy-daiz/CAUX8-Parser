import json
import os

from export import export_to
from question import question, testcase
from util import tag, text, testtype


def bootstrap(folder_path: str) -> None:
    """
    给定含一本通格式的题目的文件夹,导出其中所有的.xml文件至同目录下的EXPORT.xml
    :param folder_path: 含题目的文件夹
    """
    files = os.listdir(folder_path)

    # 创建一个空列表，用于存储所有的 question 对象
    questions = []

    # 遍历文件列表
    for filename in files:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    q = parse_to(data)
                    questions.append(q)
                except Exception as e:
                    print(f"[WARN]解析{filename}时出错,{e}")

    export_to(os.path.join(folder_path, "EXPORT.xml"), questions)

def parse_to(d) -> question:
    """
    将一本通的json数据解析到新question对象中
    :param d:json.load()得到的file-like object
    :return:对应question对象
    """
    q = question()

    q.header["name"] = tag(text(d['localizedContentsOfLocale']['title']))

    str_buf = ""
    # 将多个contentSection合并到questiontext中
    for sec in d['localizedContentsOfLocale']['contentSections']:
        sec_str = f"{sec['sectionTitle']}:{sec['text']}\n"
        str_buf += sec_str
    q.header["questiontext"] = tag(text(str_buf),{"format": "html"})

    # TODO:cpu时间限制,内存限制

    # 构造作为sample的用例
    for sample in d['samples']:
        t = testcase()
        t.attr["mark"] = "0.0"
        t.attr["testtype"] = testtype.NORMAL
        t.attr["useasexample"] = "1"
        t.stdin = tag(text(sample["inputData"]))
        t.expected = tag(text(sample["outputData"]))
        q.testcases[sample["inputData"]] = t

    # 构造作为测试的用例
    for st in d['judgeInfo']['subtasks']:
        for test in st['testcases']:
            t = testcase()
            t.attr["testtype"] = testtype.NORMAL
            t.attr["useasexample"] = "0"
            in_file = find_file(os.getcwd(),test["inputFile"])
            out_file = find_file(os.getcwd(),test["outputFile"])
            # 读取对应输入输出文件
            try:
                with open(in_file, 'r', encoding='utf-8') as f:
                    t.stdin = tag(text(f.read()))
                    f.close()
                with open(out_file, 'r', encoding='utf-8') as f:
                    t.expected = tag(text(f.read()))
                    f.close()
            except Exception as e:
                print(f"[WARN]读取测试用例{in_file}或{out_file}时出错,{e}")
                continue
            q.testcases[test["inputFile"]] = t

    return q

def find_file(root_folder, target_filename) -> str|None:
    """
    在给定目录下递归地寻找指定名称的文件
    :param root_folder: 给定目录
    :param target_filename: 要查找的文件名
    :return: 文件路径或 None
    """
    for root, dirs, files in os.walk(root_folder):
        if target_filename in files:
            return str(os.path.join(root, target_filename))  # 找到就返回路径
    return None  # 未找到返回 None

if __name__ == '__main__':
    bootstrap("ybt")