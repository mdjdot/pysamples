#!/usr/bin/env python3

"""
pytest
https://docs.pytest.org/en/latest/
https://docs.pytest.org/en/latest/contents.html#toc
https://www.jianshu.com/p/a754e3d47671
https://www.jianshu.com/p/932a4d9f78f8

安装 pytest
pip3 install pytest
指定模块运行
pytest test_sample.py
python -m pytest test_sample.py
运行模块中的指定方法
pytest test_sample.py::test_answerCorrect::test_answer
指定目录运行
pytest testing/
当前目录及子目录运行
pytest # 在当前目录及子目录运行 test_xx.py 和 xx_test.py文件

pytest -q 静默执行
pytest 只执行 test_xx 函数

装饰器
@pytest.mark.slow
pytest -m "slow"
pytest -m "not slow"

from pytest import ExitCode
退出代码 0：所有测试都收集并成功通过
退出代码 1：测试已收集和运行，但某些测试失败
退出代码 2：测试执行被用户中断
退出代码 3：执行测试时发生内部错误
退出代码 4：pytest 命令行使用错误
退出代码 5：未收集任何测试

"""

import pytest


def inc(x):
    return x+1

# 每个方法都执行
@pytest.fixture(scope='function')
def setUp():
    print("start")

@pytest.mark.slow
def test_answer():
    assert inc(3) == 5

@pytest.mark.bvt
def test_answerCorrect():
    assert inc(3) == 4


def pytest_configure(config):
    config.addinivalue_line(
        "bvt", "env(name): mark test to run only on named environment"
    )