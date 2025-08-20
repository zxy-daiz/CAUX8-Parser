class question_request_body:
    # display: none;
    assignmenttype: str = "onlinejudge"
    type: str = "onlinejudge"
    mform_showadvanced_last: int = 0
    conditiongraderepeats: int = 1
    conditionfieldrepeats: int = 1
    course: int = 141
    coursemodule: str = ""
    section: int = 7
    module: int = 1
    modulename: str = "assignment"
    instance: str = ""
    add: str = "assignment"
    update: int = 0
    return_: int = 0  # renamed to avoid conflict with Python's `return` keyword
    sr: int = 0
    sesskey: str = "pn2llXJdPQ"  # 登录时获取
    _qf__mod_assignment_mod_form: int = 1

    # 作业名称
    name: str = "test2"  # 验证:非空且最多255字符

    # 描述
    introeditor_text: str = "<p>test2</p>"
    # hidden
    introeditor_format: int = 1
    introeditor_itemid: int = 155595316  # 这个item_id要从上游请求里拿

    # 开放时间
    timeavailable_day: int = 13  # 1-31
    timeavailable_month: int = 8  # 1-12
    timeavailable_year: int = 2025  # 1970-2032
    timeavailable_hour: int = 18  # 00-23
    timeavailable_minute: int = 45  # 00-55 只能为5的倍数
    timeavailable_enabled: int = 1  # 是否启用

    # 截止时间
    timedue_day: int = 20
    timedue_month: int = 8
    timedue_year: int = 2025
    timedue_hour: int = 18
    timedue_minute: int = 45
    timedue_enabled: int = 1  # 是否启用

    # 在课程页面显示简介
    # showdescription: int = 0 # 这个字段在请求中没有被发送，原因未知

    # 禁止迟交
    preventlate: int = 0

    # 成绩
    grade: int = 100  # 0=没有成绩 -1=量表 1-100

    # 评分方式
    advancedgradingmethod_submission: str = ""  # "" = 直接打分,guide = 评分指南,rubric = 量规

    # 成绩类别
    gradecat: int = 168  # 168 = 未分类

    # 源文件最大长度
    maxbytes: int = 1048576
    """
    <option value="20971520">20MB</option>
    <option value="10485760">10MB</option>
    <option value="5242880">5MB</option>
    <option value="2097152">2MB</option>
    <option value="1048576" selected="selected">1MB</option>
    <option value="512000">500KB</option>
    <option value="102400">100KB</option>
    <option value="51200">50KB</option>
    <option value="10240">10KB</option>
    <option value="0">课程上传限制 (20MB)</option>
    """

    # 学生是否可删除作业
    resubmit: int = 1

    # 最多可传几个文件
    var1: int = 1  # 1-20

    # 是否允许备注
    var2: int = 0

    # 在可以提交作业前隐藏作业说明
    var3: int = 0

    # 用Email提醒教师
    emailteachers: int = 0

    # 编程语言
    language: str = "1111_ideone"
    """
    <select name="language" id="id_language">
        <option value="13_ideone">Assembler (masm, studybar.cau.edu.cn)</option>
        <option value="1_ideone">C and C++ (TDM-GCC4.8.1,xp32)</option>
        <option value="11_ideone">C and C++ (VC6, xp32)</option>
        <option value="1117_ideone">C and C++ (g++ -std=c++17  ubuntu 64bit)</option>
        <option value="1111_ideone" selected="selected">C and C++ (g++-5 -std=c++11 ubuntu 32)</option>
        <option value="12_ideone">C and C++ (vs2015, win7 32bit)</option>
        <option value="1113_ideone">C#  VS2015 (win7 32)</option>
        <option value="1112_ideone">C#  mono4.0 (ubuntu 32)</option>
        <option value="10_ideone">Java (JDK 1.7.0_25, xp32)</option>
        <option value="101_ideone">Java (open JDK 1.7.0_121, ubuntu32)</option>
        <option value="1011_ideone">Java (open JDK 1.7.0_121, ubuntu32, wallclock)</option>
        <option value="4_ideone">Python (python 2.7. win )</option>
        <option value="116_ideone">Python 3 (python-3.5, win)</option>
        <option value="1116_ideone">Python3 (python-3.10, ubuntu,64bit )</option>
        <option value="115_ideone">vPython (python-2.7, win32,64bit )</option>
        <option value="2000_ideone">web test (ubuntu 32)</option>
    </select>
    """

    # 格式错误得分比例
    ratiope: float = 1.0
    """
    <option value="0.0">无</option>
    <option value="1.0" selected="selected">100%</option>
    <option value="0.9">90%</option>
    <option value="0.8333333">83.33333%</option>
    <option value="0.8">80%</option>
    <option value="0.75">75%</option>
    <option value="0.7">70%</option>
    <option value="0.6666667">66.66667%</option>
    <option value="0.6">60%</option>
    <option value="0.5">50%</option>
    <option value="0.4">40%</option>
    <option value="0.3333333">33.33333%</option>
    <option value="0.3">30%</option>
    <option value="0.25">25%</option>
    <option value="0.2">20%</option>
    <option value="0.1666667">16.66667%</option>
    <option value="0.1428571">14.28571%</option>
    <option value="0.125">12.5%</option>
    <option value="0.1111111">11.11111%</option>
    <option value="0.1">10%</option>
    <option value="0.05">5%</option>
    """

    # CPU使用时间上限
    cpulimit: int = 9  # 1-10 单位:秒
    # 内存最多可用
    memlimit: int = 67108864
    """
    <option value="1048576">1MB</option>
    <option value="2097152">2MB</option>
    <option value="4194304">4MB</option>
    <option value="8388608">8MB</option>
    <option value="16777216">16MB</option>
    <option value="33554432">32MB</option>
    <option value="67108864" selected="selected">64MB</option>
    <option value="134217728">128MB</option>
    <option value="268435456">256MB</option>
    """

    # 只编译
    compileonly: int = 0

    # 前缀
    preamble: str = ""
    # 后缀
    postamble: str = ""

    # 学生代码中禁止出现的词，一行一个,分号结束，注意空格是有效的，比如"or" 和" or " 是不同的，后者是一个独立的词，前者是任何匹配的串，哪怕在for中，都不行
    forbiddenwords: str = ""

    # 小组模式
    groupmode: int = 0  # 0=无小组 1=分隔小组 2=可视小组

    # 可见
    visible: int = 1

    # ID号
    """
    ID号可以在成绩计算公式中唯一标识一个活动。 如果这个活动与任何成绩计算公式无关，那么它的ID号可以为空。
    ID号也可以在成绩薄中设定，不过只能在活动设置页面里编辑。
    """
    cmidnumber: str = ""

    # 可访问时间
    # 验证:until的时间要比from大
    availablefrom_day: int = 14
    availablefrom_month: int = 8
    availablefrom_year: int = 2025
    availablefrom_hour: int = 0
    availablefrom_minute: int = 0
    availablefrom_enabled: int = 1
    availableuntil_day: int = 14
    availableuntil_month: int = 8
    availableuntil_year: int = 2025
    availableuntil_hour: int = 7
    availableuntil_minute: int = 0
    availableuntil_enabled: int = 1

    # 成绩条件: itemid 至少要 min % 且少于 max %
    conditiongradegroup_0_conditiongradeitemid: int = 0
    conditiongradegroup_0_conditiongrademin: str = ""
    conditiongradegroup_0_conditiongrademax: str = ""

    # 用户条件 field-operator-value
    conditionfieldgroup_0_conditionfield: int = 0
    """
    <option value="0">（无）</option>
    <option value="aim">AIM号码</option>
    <option value="icq">ICQ号码</option>
    <option value="msn">MSN号码</option>
    <option value="skype">Skype号码</option>
    <option value="yahoo">Yahoo号码</option>
    <option value="firstname">名</option>
    <option value="country">国家或地区</option>
    <option value="address">地址</option>
    <option value="lastname">姓氏</option>
    <option value="idnumber">学号</option>
    <option value="city">市/县</option>
    <option value="phone2">手机</option>
    <option value="institution">机构</option>
    <option value="email">电子邮件地址</option>
    <option value="phone1">电话</option>
    <option value="department">系别</option>
    <option value="url">网页</option>
    """
    conditionfieldgroup_0_conditionfieldoperator: str = "contains"
    """
    <option value="contains">包含</option>
    <option value="doesnotcontain">不包含</option>
    <option value="isequalto">等于</option>
    <option value="startswith">以...开始</option>
    <option value="endswith">以...结束</option>
    <option value="isempty">为空</option>
    <option value="isnotempty">is not empty</option>
    """
    conditionfieldgroup_0_conditionfieldvalue: str = ""

    # 活动可用之前
    showavailability: int = 1  # 1 = 活动以暗色显示，并显示受限信息,0 = 完全隐藏活动

    # 不知道为什么会有这个
    submitbutton2: str = "保存并返回课程"


class testcases_request_body:
    # TODO:Code Here
    pass
