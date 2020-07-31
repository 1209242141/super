import unittest
import os
from commen import HTMLTestRunner
import time
current_path = os.getcwd()

def all_case():
    # case_dir="E:\\learn\\script\\test\\case"
    case_dir = os.path.join(current_path, 'MT_case')
    discover=unittest.defaultTestLoader.discover(
        case_dir,pattern="test*.py")
    return discover
if __name__ == '__main__':
    # report_dir="E:\\learn\\script\\test\\commen\\report.html"
    # report_path = os.path.join(current_path, 'commen')
    report_dir = os.path.join(current_path, "report.html")
    fb=open(report_dir,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title="测试报告",
        description="用例执行情况"
    )
    runner.run(all_case())
    fb.close()