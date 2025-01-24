import html
from typing import Optional

# tag表示单个xml节点
class tag:
    def __init__(self, value=None, attr=None):
        self.attr: dict = {} if not attr else attr
        self.name = value

    def export(self):
        pass
        # TODO: 未完成


# text表示要解析为<text><text/>的内容
class text:
    def __init__(self, string: Optional[str] = None):
        self.original: Optional[str] = string

    # 该函数翻译自php代码
    # Take a string, and wrap it in a CDATA secion,
    # if that is required to make the output XML valid.
    def __xml_escape(self):
        if self.original and html.escape(self.original) == self.original:
            # If the string contains something that looks like the end
            # of a CDATA section, then we need to avoid errors by splitting
            # the string between two CDATA sections.
            temp = str.replace(self.original, ']]>', ']]]]><![CDATA[>')
            return "<![CDATA[" + temp + "]]>"
        else:
            return self.original

    # 该函数翻译自php代码
    # Generates <text></text> tags, processing raw text therein
    def exporttext(self, indent=0, short=True):
        indent = "  " * indent
        raw = self.__xml_escape()

        if short:
            xml = f"{indent}<text>{raw}</text>\n"
        else:
            xml = f"{indent}<text>\n{raw}\n{indent}</text>\n"

        return xml