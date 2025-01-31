import xml.etree.ElementTree as ET
from glob import glob
from os.path import join

from export import export_to
from question import question, testcase
from util import testtype, feedback


def bootstrap(folder_path:str) -> None:
    """
    给定含fps格式的题目的文件夹,导出其中所有的.xml文件至同目录下的EXPORT.xml
    :param folder_path: 含题目的文件夹
    """
    all_xml = glob(join(folder_path, "*.xml"))
    questions = []
    for xml in all_xml:
        try:
            questions.append(parse(xml))
        except:
            print(f"[WARN]解析{xml}时出错,跳过")
    export_to(join(folder_path, "EXPORT.xml"), questions)


def parse(xml_path:str) -> question:
    """
    解析一个fps格式的xml文件
    :param xml_path: 文件路径
    :return: 解析出的question对象
    """
    etree = ET.parse(xml_path)
    problem_tag = etree.find("item")

    q = question()
    q.header["name"] = problem_tag.find("title").text
    q.header["questiontext"] = (problem_tag.find("description").text
                                + problem_tag.find("input").text
                                + problem_tag.find("output").text)
    q.header["penalty"] = "0"
    q.extra["displayfeedback"] = feedback.SHOW

    t_sample = testcase()
    t_sample.attr["mark"] = "0"
    t_sample.attr["testtype"] = testtype.NORMAL
    t_sample.attr["useasexample"] = "1"
    t_sample.stdin = problem_tag.find("sample_input").text
    t_sample.expected = problem_tag.find("sample_output").text

    t = testcase()
    t.attr["testtype"] = testtype.NORMAL
    t.stdin = problem_tag.find("test_input").text
    t.expected = problem_tag.find("test_output").text

    q.testcases = {"0":t_sample, "1":t}

    return q

if __name__ == '__main__':
    bootstrap("fps")