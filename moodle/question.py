from typing import Optional

class question_definition:
    def __init__(self):
        # @var string question name.
        self.name:Optional[str] = None

        # @var string question text.
        self.questiontext:Optional[str] = None

        # 对应PHP源代码中defaultmark,历史遗留问题导致defaultmark和defaultgrade指的是同一个字段
        # @var float what this quetsion is marked out of, by default.
        self.defaultgrade:Optional[float] = None

        # @var string question general feedback.
        self.generalfeedback:Optional[str] = None

        # @var number penalty factor of this question.
        self.penalty:Optional[float] = None

        # 对应status字段,question\format\xml\format.php中提及了导出该字段时的格式化方法
        # @var boolean question status hidden/ready/draft in the question bank.
        self.hidden:Optional[bool] = None

        # @var string question idnumber.
        self.idnumber:Optional[str] = None

    @staticmethod
    def default():
        q = question_definition()



class question_graded_automatically(question_definition):
    def __init__(self):
        super().__init__()
        self.show_num_correct:Optional[bool] = None