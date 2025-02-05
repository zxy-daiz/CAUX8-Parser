from parser.util import text, tag, coderunnertype, feedback

# 含有"⚠️"注释的字段建议填写

class question:
    def __init__(self):
        self.attr:dict = {
            "type":"coderunner"
        }

        self.header: dict[str,str|tag|None] = {
            # @var string question name.
            # 问题名称
            # ⚠️ 重要:该选项必填！
            "name":tag(text()), #⚠️

            # @var string question text.
            # 问题文本
            "questiontext":tag(text(),{"format":"html"}), #⚠️

            # @var string question general feedback.
            # 问题的一般反馈
            "generalfeedback":tag(text(),{"format":"html"}),

            # @var string question idnumber.
            # 问题编号
            "idnumber":None,

            # @var float what this question is marked out of, by default.
            # 默认分数
            # fix:虽然在php源码中该字段为defaultmark,但导入时似乎由于兼容性原因识别的是defaultgrade
            # 该选项代表该问题的总分。
            "defaultgrade":"100", #⚠️

            # @var number penalty factor of this question.
            # 惩罚因子
            # 编者改为0
            "penalty":"0",
        }

        self.extra: dict[str,str|tag|None] = {
            # @var bool True for All-or-nothing grading
            # 全或无评分
            # 编者改:默认值为1,编者改为0。一般不开,要用时手动开。
            'allornothing': "0",

            # @var int Precheck for the question.
            #  0 = 'disable': no pretest button available,
            #  1 = 'empty' for no actual tests,
            #  2 = 'examples' for all use-as-example tests,
            #  3 = 'selected' for specific selected tests,
            #  4 = 'all' for all tests.
            # 预检查
            # 可选的值定义与枚举类中
            'precheck': "0",

            # @var int The number of lines for the answer box.
            # 答案框行数
            'answerboxlines': "15",

            # 不知道为什么有这个字段,在源码中找不到,但是导出xml时出现了,所以放在这占个位
            'answerboxcolumns': "90",

            # @var int True to validate the question on save.
            # 保存时验证问题
            'validateonsave': "1",

            # @var string The string that is preloaded into the answer box.
            # 预加载到答案框的字符串
            'answerpreload': "",

            # @var string Extra data for use by template authors, global to all tests.
            # 模板作者使用的额外数据, 全局适用于所有测试
            'globalextra': "",

            # @var bool True if template uses ace.
            # 模板是否使用ace
            'useace': "1",

            # @var ?bool True if a combinator template is being used.
            # 是否使用组合模板
            'iscombinatortemplate': "0",

            # @var string The question template.
            # 问题模板
            'template': "", #该项如果不为空字符串,则会导致“定制”选项被勾选，导致一系列评分问题

            # @var ?string The template parameters language.
            # 模板参数语言
            'templateparamslang': "twig",

            # @var bool The template parameters eval per try.
            # 每次尝试评估模板参数
            'templateparamsevalpertry': "0",

            # @var string The evaluated template parameters (JSON).
            # 评估的模板参数 (JSON)
            'templateparamsevald': "",

            # @var ?string The parameters to pass to the UI plugin
            # 传递给UI插件的参数
            'uiparameters': "",

            # @var int Hide check. Non-zero to hide the Check button.
            # 隐藏检查按钮
            'hidecheck': "0",

            # @var ?string The attachments of the question.
            # 问题的附件
            'attachments': "0",

            # @var bool True if the response is json from which the actual code attribute should be extracted
            # 响应是否为json, 从中提取实际代码属性
            'extractcodefromjson': "1",

            # @var int True if Stop button is to be displayed.
            # 是否显示停止按钮
            # 可选的值定义与枚举类中
            'giveupallowed': "0",

            # @var string The coderunner type.
            # coderunner类型
            # 可选的类型位于枚举类中,默认为多语言
            'coderunnertype': coderunnertype.multilanguage, #⚠️

            # @var string The prototype type.
            # 原型类型
            'prototypetype': None,

            # @var string The penalty regime of the question.
            # 惩罚机制
            'penaltyregime': None,

            # @var bool Show source. If true, the Twigged template output is displayed for each run.
            # 显示源代码
            'showsource': None,

            # @var string JSON-encoded list of column specifiers.
            # JSON编码的列说明列表
            'resultcolumns': None,

            # @var bool True if multiple tests are allowed.
            # 是否允许多个测试
            'allowmultiplestdins': None,

            # @var string The answer of the question.
            # 问题的答案
            'answer': None,

            # @var string The regular expression to split output from the combinator run into the basic tests again.
            # 正则表达式, 用于将组合运行的输出拆分为基本测试
            'testsplitterre': None,

            # @var string The language of the question.
            # 问题的语言
            'language': None,

            # @var string The language for the Ace editor
            # Ace编辑器的语言
            'acelang': None,

            # @var mixed The question sandbox.
            # 问题沙箱
            'sandbox': None,

            # @var string The grader instance.
            # 评分器实例
            'grader': None,

            # @var ?double The allowed CPU time (null unless explicitly set).
            # 允许的CPU时间 (除非明确设置, 否则为null)
            'cputimelimitsecs': None, #⚠️

            # @var ?int The allowed memory in MB (null unless explicitly set).
            # 允许的内存 (MB) (除非明确设置, 否则为null)
            'memlimitmb': None, #⚠️

            # @var string The JSON string used to specify the sandbox parameters.
            # 用于指定沙箱参数的JSON字符串
            'sandboxparams': None,

            # @var string The template parameters.
            # 模板参数
            'templateparams': None,

            # @var bool The hoisted template parameters.
            # 提升的模板参数
            'hoisttemplateparams': None, #似乎需要设为0

            # @var ?int True if all question fields need Twig expansion.
            # 是否需要Twig扩展所有问题字段
            'twigall': None,

            # @var ?string The UI plugin in use.
            # 使用的UI插件
            'uiplugin': None,

            # @var ?int The number of attachments required.
            # 需要的附件数量
            'attachmentsrequired': None,

            # @var ?int Max allowed file size (bytes)
            # 最大允许文件大小 (字节)
            # 编者设为1M
            'maxfilesize': "1024000",

            # @var ?string Allowed file names (regular expression)
            # 允许的文件名 (正则表达式)
            'filenamesregex': None,

            # @var ?string Description of file name.
            # 文件名说明
            'filenamesexplain': None,

            # @var ?int Set to 0 or 1, feedback (result table) is shown.
            # Not if display feedback is set to 2.
            # 设置为0或1, 显示反馈 (结果表). 如果显示反馈设置为2, 则不显示
            # 可选的值定义与枚举类中
            'displayfeedback': None,

            # @var ?string Extra data for use by prototype or customised code.
            # 原型或自定义代码使用的额外数据
            'prototypeextra': None
        }

        # 使用字典类型是为了使导出函数能够不要判断类型，这个字典只要求每个不同测试用例的key不同
        self.testcases:dict[str,testcase] = {} #⚠️

class testcase:
    def __init__(self):
        self.attr: dict = {
            # @var float The mark for this test case.
            # 该测试用例的分数
            # 经测试，该字段表示该测试用例占所有分数的权重
            # 如果有多个测试用例，则通过该测试用例的分数=该测试用例mark值/所有测试用例mark值的总和
            "mark": "1.0", #⚠️

            # @var int Whether to hide the rest of the tests if this one fails (0 or 1).
            # 如果此测试失败，是否隐藏其余测试 (0 或 1)
            "hiderestiffail": "0",

            # @var int The type of the test.
            # 测试类型
            # 可选的值位于枚举类中
            "testtype": "0",

            # @var int Whether to use this test case as an example (0 or 1).
            # 是否将此测试用例用作示例 (0 或 1)
            "useasexample": "0" #⚠️
        }

        # @var string The code to be tested.
        # 要测试的代码
        self.testcode = tag(text())

        # @var string The standard input for the test.
        # 测试的标准输入
        self.stdin = tag(text()) #⚠️

        # @var string The expected output of the test.
        # 预期输出
        self.expected = tag(text()) #⚠️

        # @var string Extra data for the test.
        # 测试的额外数据
        self.extra = tag(text())

        # @var string Whether to display the test case ("SHOW" or "HIDE").
        # 是否显示测试用例 ("SHOW" 或 "HIDE")
        self.display = tag(text("SHOW"))
