class TestCaseUploadRequest:
    """
    测试用例上传请求体的Python类表示
    基于抓取到的表单数据结构设计
    """
    def __init__(self, problem_id, sesskey):
        # 基础配置
        self.boundary_repeats = 5
        self.id = problem_id  # 题目ID
        self.sesskey = sesskey  # 会话密钥
        self._qf__testcase_form = 1
        self.submitbutton = "保存更改"
        
        # 初始化5个测试用例位置
        self.test_cases = [
            {"caseid": -1, "subgrade": 0.0, "input": "", "output": "", "feedback": ""},
            {"caseid": -1, "subgrade": 0.0, "input": "", "output": "", "feedback": ""},
            {"caseid": -1, "subgrade": 0.0, "input": "", "output": "", "feedback": ""},
            {"caseid": -1, "subgrade": 0.0, "input": "", "output": "", "feedback": ""},
            {"caseid": -1, "subgrade": 0.0, "input": "", "output": "", "feedback": ""}
        ]
    
    def set_test_case(self, index, input_data, output_data, subgrade=1.0, feedback="", caseid=-1):
        """
        设置指定索引的测试用例
        
        参数:
            index: 测试用例索引(0-4)
            input_data: 输入数据
            output_data: 输出数据
            subgrade: 该测试用例的分值权重
            feedback: 反馈信息
            caseid: 测试用例ID，默认为-1表示新用例
        """
        if 0 <= index < 5:
            self.test_cases[index] = {
                "caseid": caseid,
                "subgrade": subgrade,
                "input": input_data,
                "output": output_data,
                "feedback": feedback
            }
        else:
            raise ValueError("索引必须在0-4之间")
    
    def to_form_data(self):
        """
        将类转换为表单数据格式，用于发送POST请求
        
        返回:
            字典形式的表单数据
        """
        form_data = {
            "boundary_repeats": self.boundary_repeats,
            "id": self.id,
            "sesskey": self.sesskey,
            "_qf__testcase_form": self._qf__testcase_form,
            "submitbutton": self.submitbutton
        }
        
        # 添加测试用例相关字段
        for i in range(5):
            form_data[f"caseid[{i}]"] = self.test_cases[i]["caseid"]
            form_data[f"subgrade[{i}]"] = self.test_cases[i]["subgrade"]
            form_data[f"input[{i}]"] = self.test_cases[i]["input"]
            form_data[f"output[{i}]"] = self.test_cases[i]["output"]
            form_data[f"feedback[{i}]"] = self.test_cases[i]["feedback"]
        
        return form_data


# 使用示例
if __name__ == "__main__":
    # 创建请求实例，传入题目ID和会话密钥
    upload_request = TestCaseUploadRequest(problem_id=38222, sesskey="dKBfkNkji1")
    
    # 设置第一个测试用例
    upload_request.set_test_case(
        index=0,
        input_data="1 2",
        output_data="3",
        subgrade=1.0
    )
    
    # 可以继续设置其他测试用例
    # upload_request.set_test_case(index=1, input_data="...", output_data="...")
    
    # 转换为表单数据
    form_data = upload_request.to_form_data()
    
    # 打印结果查看
    for key, value in form_data.items():
        print(f"{key}: {value}")
