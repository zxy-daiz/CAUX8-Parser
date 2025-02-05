import unittest

from parser.export import export_single_question_to
from parser.question import question, testcase
from parser.util import text, tag, coderunnertype, testtype, feedback, giveup


class TestExport(unittest.TestCase):
    def test_something(self):
        q = question()
        q.header = {
            "name": tag(text("Hello World")),
            "questiontext": tag(text("""编写一个能够输出 Hello,World! 的程序。

        提示：
        - 使用英文标点符号；
        - Hello,World! 逗号后面没有空格。
        - H 和 W 为大写字母。
        <p>输入格式:<p><p>输出格式:<p>"""), {"format": "html"}),
            "generalfeedback": tag(text(""), {"format": "html"}),
            "defaultmark": "1.0000000",
            "penalty": "0.0000000",

        }
        q.extra = {
            "answerboxlines": "18",
            "answerboxcolumns": "100",
            "coderunnertype": coderunnertype.c_program,
            "prototypetype": "0",
            "penaltyregime": "0",
            "showsource": "0",
            "hoisttemplateparams": "1",
            "twigall": "0",
            "attachmentrequired": "0",
            "maxfilesize": "10240",
            "displayfeedback": feedback.SHOW,
            "giveupallowed": giveup.NEVER
        }

        t1 = testcase()

        t1.attr = {
            "testtype": testtype.NORMAL,
            "useasexample": "1",
            "hiderestiffail": "0",
            "mark": "1.0000000",
        }
        t1.testcode = tag(text(""))
        t1.stdin = tag(text(""))
        t1.expected = tag(text("Hello,World!"))
        t1.extra = tag(text(""))
        t1.display = tag(text("SHOW"))

        q.testcases = {"0":t1}

        export_single_question_to("hello_world.xml", q)


if __name__ == '__main__':
    unittest.main()
