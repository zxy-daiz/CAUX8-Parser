from typing import Optional

# tag表示单个xml节点
class tag:
    def __init__(self,value=None,attr=None):
        self.attr:dict = {} if not attr else attr
        self.name = value

# text表示要解析为<text><text/>的内容
class text:
    def __init__(self, string:Optional[str] = None):
        self.original:Optional[str] = string
        self.decorated:Optional[str] = "<text>" + string + "</text>" if string else None