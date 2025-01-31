import xml.etree.ElementTree as ET
from glob import glob
from os.path import join

from export import export_to
from question import question, testcase
from util import testtype, feedback, tag, text, coderunnertype


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
        except Exception as e:
            print(f"[WARN]解析{xml}时出错,{e}")
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
    q.header["name"] = tag(text(problem_tag.findtext("title")))
    questiontext = (problem_tag.findtext("description","")
                    + problem_tag.findtext("input","")
                    + problem_tag.findtext("output",""))
    q.header["questiontext"] = tag(text(questiontext), {"format": "html"})
    q.header["penalty"] = "0"
    q.header["coderunnertype"] = coderunnertype.c_program  # 需要手动设定
    q.extra["displayfeedback"] = feedback.SHOW

    # 有些题目没有test_input,只有sample_input,对于这种情况,将sample_input作为测试用例
    test_input = problem_tag.findtext("test_input","")
    test_output = problem_tag.findtext("test_output","")

    t_sample = testcase()
    t_sample.attr["mark"] = "0" if test_input else "1" # 如果不存在test_input,则sample测试用例计分
    t_sample.attr["testtype"] = testtype.NORMAL
    t_sample.attr["useasexample"] = "1"
    t_sample.stdin = tag(text(problem_tag.findtext("sample_input")))
    t_sample.expected = tag(text(problem_tag.findtext("sample_output")))

    t = testcase()
    t.attr["testtype"] = testtype.NORMAL
    t.stdin = tag(text(test_input if test_input else ""))
    t.expected = tag(text(test_output if test_output else ""))

    q.testcases = {"0":t_sample, "1":t}

    return q

if __name__ == '__main__':
    bootstrap("fps")