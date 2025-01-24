from copy import copy

from moodle.coderunner.question import qtype_coderunner_question
from moodle.qformat_xml import qformat_xml
from moodle.questiontype import question_type


class qtype_coderunner(question_type):
    def __init__(self):
        super().__init__()

    #假设 question.option 返回一个字典
    def export_to_xml(self,question:qtype_coderunner_question,fmt:qformat_xml) -> str:
        global course

        question_to_export = copy(question)

        qtype = question.coderunner_type
        course_context = None
        row = qtype_coderunner.get_prototype(qtype,course_context)

        if row and question_to_export.prototype_type == 0:
            non_inherited_fields = self.non_inherited_fields()
            extra_fields = self.extra_question_fields()
            for field,value in row.items():
                if (field in extra_fields
                        and field not in non_inherited_fields
                        and getattr(question,field) == value):
                    delattr(question,field)

        exp_out = [super().export_to_xml(question, fmt)]
        exp_out.append("    <testcases>\n")
        for testcase in question.options["testcases"]:
            use_as_example = testcase

    @staticmethod
    def get_prototype(coderunnertype:str,prototype:context) -> dict:
        pass

    @staticmethod
    def non_inherited_fields() -> list[str]:
        return [
            'coderunnertype',
            'prototypetype',
            'allornothing',
            'penaltyregime',
            'precheck',
            'hidecheck',
            'showsource',
            'answerboxlines',
            'answerboxcolumns',
            'answerpreload',
            'globalextra',
            'answer',
            'validateonsave',
            'templateparams',
            'hoisttemplateparams',
            'extractcodefromjson',
            'templateparamslang',
            'templateparamsevalpertry',
            'templateparamsevald',
            'twigall',
            'uiparameters',
            'attachments',
            'attachmentsrequired',
            'maxfilesize',
            'filenamesregex',
            'filenamesexplain',
            'displayfeedback',
            'giveupallowed',
        ]

    @staticmethod
    def extra_question_fields() -> list[str]:
        return [
            'question_coderunner_options',
            'coderunnertype',
            'prototypetype',
            'allornothing',
            'penaltyregime',
            'precheck',
            'hidecheck',
            'showsource',
            'answerboxlines',
            'answerboxcolumns', # Defunct.
            'answerpreload',
            'globalextra',
            'useace',
            'resultcolumns',
            'template',
            'iscombinatortemplate',
            'allowmultiplestdins',
            'answer',
            'validateonsave',
            'testsplitterre',
            'language',
            'acelang',
            'sandbox',
            'grader',
            'cputimelimitsecs',
            'memlimitmb',
            'sandboxparams',
            'templateparams',
            'hoisttemplateparams',
            'extractcodefromjson',
            'templateparamslang',
            'templateparamsevalpertry',
            'templateparamsevald',
            'twigall',
            'uiplugin',
            'uiparameters',
            'attachments',
            'attachmentsrequired',
            'maxfilesize',
            'filenamesregex',
            'filenamesexplain',
            'displayfeedback',
            'giveupallowed',
            'prototypeextra',
            ]