import os
import unittest

from caux8_moodle_parser import parse_fps

class TestExport(unittest.TestCase):
    def test_sample_question(self):
        path = os.path.join(os.getcwd(),"tests","sample","fps")
        export_path = os.path.join(path,"EXPORT.xml")

        parse_fps(path)

        # 判断文件是否存在
        self.assertTrue(os.path.isfile(export_path), "导出文件不存在")
        # 判断文件是否为空
        self.assertGreater(os.path.getsize(export_path), 0, "导出文件为空")

        # 删除文件
        os.remove(export_path)

if __name__ == '__main__':
    unittest.main()
