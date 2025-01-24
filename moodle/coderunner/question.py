from typing import Optional
from moodle.question import question_graded_automatically


class qtype_coderunner_question(question_graded_automatically):
    def __init__(self):
        super().__init__()

        self.testcases:Optional[list] = None # Array of testcases.

        # @var string containing the language for coderunner type.
        self.coderunnertype:Optional[str] = None

        # @var int 0, 1 or 2 for not-a-prototype, built-in prototype and user-defined prototype
        self.prototypetype:Optional[int] = None

        # @var bool True for All-or-nothing grading
        self.allornothing:Optional[bool] = True

        # @var string The penalty regime of the question.
        self.penaltyregime:Optional[str] = None

        # @var int Precheck for the question.
        #  0 = 'disable': no pretest button available,
        #  1 = 'empty' for no actual tests,
        #  2 = 'examples' for all use-as-example tests,
        #  3 = 'selected' for specific selected tests,
        #  4 = 'all' for all tests.
        self.precheck:Optional[int] = None

        # @var int Hide check. Non-zero to hide the Check button.
        self.hidecheck:Optional[int] = None

        # @var bool Show source. If true, the Twigged template output is displayed for each run.
        self.showsource:Optional[int] = None

        # @var int|string The number of lines for the answer box.
        self.answerboxlines:Optional[int] = None

        # @var string The string that is preloaded into the answer box.
        self.answerpreload:Optional[str] = None

        # @var string Extra data for use by template authors, global to all tests.
        self.globalextra:Optional[str] = None

        # @var bool True if template uses ace.
        self.useace:Optional[bool] = None

        # @var string JSON-encoded list of column specifiers.
        self.resultcolumns:Optional[str] = None

        # @var string The question template.
        self.template:Optional[str] = None

        # @var ?bool True if a combinator template is being used.
        self.iscombinatortemplate:Optional[bool] = None

        # @var bool True if multiple tests are allowed.
        self.allowmultiplestdins:Optional[bool] = None

        # @var string The answer of the question.
        self.answer:Optional[str] = None

        # @var int True to validate the question on save.
        self.validateonsave:Optional[int] = None

        # @var string The regular expression to split output from the combinator run into the basic tests again.
        self.testsplitterre:Optional[str] = None

        # @var string The language of the question.
        self.language:Optional[str] = None

        # @var string The language for the Ace editor
        self.acelang:Optional[str] = None

        # @var mixed The question sandbox.
        self.sandbox:Optional[str] = None

        # @var string The grader instance.
        self.grader:Optional[str] = None

        # @var ?double The allowed CPU time (null unless explicitly set).
        self.cputimelimitsecs:Optional[float] = None

        # @var ?int The allowed memory in MB (null unless explicitly set).
        self.memlimitmb:Optional[int] = None

        # @var string The JSON string used to specify the sandbox parameters.
        self.sandboxparams:Optional[str] = None

        # @var string The template parameters.
        self.templateparams:Optional[str] = None

        # @var bool The hoisted template parameters.
        self.hoisttemplateparams:Optional[bool] = None

        # @var bool True if the response is json from which the actual code attribute should be extracted
        self.extractcodefromjson:Optional[bool] = None

        # @var ?string The template parameters language.
        self.templateparamslang:Optional[str] = None

        # @var bool The template parameters eval per try.
        self.templateparamsevalpertry:Optional[bool] = None

        # @var string The evaluated template parameters (JSON).
        self.templateparamsevald:Optional[str] = None

        # @var ?int True if all question fields need Twig expansion.
        self.twigall:Optional[int] = None

        # @var ?string The UI plugin in use.
        self.uiplugin:Optional[str] = None

        # @var ?string The parameters to pass to the UI plugin
        self.uiparameters:Optional[str] = None

        # @var ?string The attachments of the question.
        self.attachments:Optional[str] = None

        # @var ?int The number of attachments required.
        self.attachmentsrequired:Optional[int] = None

        # @var ?int Max allowed file size (bytes)
        self.maxfilesize:Optional[int] = None

        # @var ?string Allowed file names (regular expression)
        self.filenamesregex:Optional[str] = None

        # @var ?string Description of file name.
        self.filenamesexplain:Optional[str] = None

        # @var ?int Set to 0 or 1, feedback (result table) is shown.
        # Not if display feedback is set to 2.
        self.displayfeedback:Optional[int] = None

        # @var int True if Stop button is to be displayed.
        self.giveupallowed:Optional[int] = None

        # @var ?string Extra data for use by prototype or customised code.
        self.prototypeextra:Optional[str] = None

        # @var ?array The answers of the question (unused - for superclass compatibility only)
        self.answers:Optional[list] = None

        # @var bool Whether the question is customised or not.
        self.customise:Optional[bool] = None

        # @var \qtype_coderunner_student Holds student details.
        self.student:Optional[object] = None

        # @var ?\qtype_coderunner_question The question prototype.
        self.prototype:Optional[object] = None

        # @var ?string The initialisation error message.
        self.initialisationerrormessage:Optional[str] = None

        # @var ?array Cache in this to avoid multiple evaluations during question editing and validation.
        self.cachedfuncparams:Optional[list] = None

        # @var ?string Cache for evaluated template parameters field
        self.cachedevaldtemplateparams:Optional[str] = None

        # @var ?string merged UI parameters
        self.mergeduiparameters:Optional[str] = None

        # @var string The json string of template params.
        self.templateparamsjson:Optional[str] = None

        # @var ?array PHP associative array containing Twig environment variables plus UI plugin parameters
        self.parameters:Optional[list] = None

        # @var stdClass Object containing step information of the response.
        self.stepinfo:Optional[object] = None

        # @var question_display_options the question options that control display of the question.
        self.options:Optional[object] = None

        # @var bool
        self.isnew:Optional[bool] = None

        # @var int question context id.
        self.context:Optional[int] = None

        # @var int questionid.
        self.questionid:Optional[int] = None

        # 不知道为什么有这个字段,在源码中找不到,但是导出xml时出现了,所以放在这占个位
        self.answerboxcolumns:Optional[int] = None