import xml.etree.ElementTree as ET
from glob import glob
from os.path import join

from export import export_to
from question import question, testcase
from util import testtype, tag, text


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

    time_lim_raw = problem_tag.find("time_limit")
    mem_lim_raw = problem_tag.find("memory_limit")

    # 转换单位并填入
    try:
        time_lim = unit_conversion(time_lim_raw.text, time_lim_raw.get("unit"))
        mem_lim = unit_conversion(mem_lim_raw.text, mem_lim_raw.get("unit"))
        q.extra["cputimelimitsecs"] = tag(str(time_lim))
        q.extra["memlimitmb"] = tag(str(mem_lim))
    except Exception as e:
        print(f"[INFO]解析内存或时间限制时出错,{e},跳过...")


    # 有些题目没有test_input,只有sample_input,对于这种情况,将sample_input作为测试用例
    test_input = problem_tag.findtext("test_input","")
    test_output = problem_tag.findtext("test_output","")

    t_sample = testcase()
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

def unit_conversion(value:str,unit:str) -> float:
    """
    将给定单位的值转换为question对象中规定的标准值(mb与s)
    :param value: 值
    :param unit: 单位
    :return: 以mb或s为单位的值
    """

    # 内存单位转换为MB所需的乘数因子
    mem_unit_factor = {
        "b": 1/1024/1024,
        "kb": 1/1024,
        "mb": 1,
        "gb": 1024,
        "tb": 1024*1024,
    }

    # 时间单位转换为s所需的乘数因子
    time_unit_factor = {
        "m": 60,
        "s": 1,
        "ms": 1/1000,
    }

    if unit in mem_unit_factor:
        return float(value) * mem_unit_factor[unit]
    elif unit in time_unit_factor:
        return float(value) * time_unit_factor[unit]
    else:
        raise Exception(f"未知单位{unit}")


if __name__ == '__main__':
    bootstrap("fps")