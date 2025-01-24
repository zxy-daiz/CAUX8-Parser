class coderunnertype:
    c_function = "c_function"
    c_program = "c_program"
    cpp_function = "cpp_function"
    java_program = "java_program"
    multilanguage = "multilanguage"
    octave_function = "octave_function"
    pascal_function = "pascal_function"
    pascal_program = "pascal_program"
    php = "php"
    python2 = "python2"
    python3 = "python3"
    sql = "sql"
    undirected_graph = "undirected_graph"
    nodejs = "nodejs"
    python3_w_input = "python3_w_input"

class precheck:
    # @var int Precheck for the question.
    #  0 = 'disable': no pretest button available,
    #  1 = 'empty' for no actual tests,
    #  2 = 'examples' for all use-as-example tests,
    #  3 = 'selected' for specific selected tests,
    #  4 = 'all' for all tests.
    DISABLED = 0
    EMPTY = 1
    EXAMPLES = 2
    SELECTED = 3
    ALL = 4

class testtype:
    NORMAL = 0
    PRECHECK = 1
    BOTH = 2

class feedback:
    USE_QUIZ = 0
    SHOW = 1
    HIDE = 2

class giveup:
    NEVER = 0
    AFTER_MAX_MARKS = 1
    ALWAYS = 2