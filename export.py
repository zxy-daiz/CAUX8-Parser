import os.path
from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, tostring

from question import question, testcase
from util import text, tag

def export_single_question_to(filename:str,q:question):
    """
    将一个问题导出到给定文件中
    """
    export_to(filename,[q])

def export_to(filename:str,questions:list[question]) -> None:
    """
    将所有问题导出到给定文件中
    """

    # 转换所有节点,添加到根quiz节点中
    elems = [__export_question_to_xml(q) for q in questions]
    root = Element("quiz")
    for elem in elems:
        root.append(elem)

    # 使用 minidom 格式化,增加换行和缩进
    xml_string = tostring(root, encoding="utf-8")
    pretty_xml = parseString(xml_string).toprettyxml(indent="    ",encoding="utf-8")

    if os.path.exists(filename):
        print("[WARN]文件已存在,将被覆盖")
    try:
        with open(filename,"wb") as f:
            f.write(pretty_xml)
            f.close()
    except:
        print("[ERROR]写入文件失败")


def __export_question_to_xml(q: question) -> Element:
    """
    将一个question对象导出为xml element
    """

    # 将question对象转换为xml节点
    original_xml = __export_dict_to_xml("question", vars(q))
    trimmed_xml = Element(original_xml.tag, original_xml.attrib)

    # 修剪掉moodle xml格式中不存在的header节点等,将其子节点移动到根节点中
    for elem in original_xml.findall("*"):  # findall("*")选择所有子元素(只有一层)
        if elem.tag not in ["testcases"]:
            for sub_elem in elem.findall("*"):
                trimmed_xml.append(sub_elem)
        else:
            trimmed_xml.append(elem)

    return trimmed_xml

def __export_dict_to_xml(key: str, d: dict) -> Element:
    """
    递归地将一个字典转换成xml节点
    :param key: 返回节点的tag值
    :param d: 给定字典
    :return: 一个Element对象,
    """
    root = Element(key)
    for k, v in d.items():
        if isinstance(v, dict):
            # 处理递归字典
            root.append(__export_dict_to_xml(k, v))
        else:
            elem = __build_node(k, v)
            if elem is not None:
                root.append(elem)

    # 清除attr子节点,转换为element的属性
    attr_elem = root.find("attr")
    if attr_elem is not None:
        root.remove(attr_elem)
        root.attrib = d["attr"]

    return root

def __build_node(key: str, value) -> Element | None:
    """
    将一个键值对转换为xml节点
    :param key: 键
    :param value: 值
    :return: Element对象,如果值的类型不被支持,返回None.
    """
    if isinstance(value, str):
        e = Element(key)
        e.text = value
    elif isinstance(value, tag):
        e = Element(key)
        e.attrib = value.attr
        if isinstance(value.text, text):
            e.append(value.text.exporttext())
        elif isinstance(value.text, str):
            e.text = value.text
        else:
            e = None
    elif isinstance(value, testcase):
        e = __export_dict_to_xml("testcase", vars(value))
    else:
        e = None
        if value is not None:
            print(f"[WARN]无法识别的键值对类型:({key},{value})")
    return e
