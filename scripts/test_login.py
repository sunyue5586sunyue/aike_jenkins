import os
import sys

from tool.get_data import get_list

sys.path.append(os.getcwd())

from page.page_login import PageLogin
import pytest


def get_data():
    list = []
    for i in get_list().values():
        list.append(tuple(i.values()))
    return list


class TestLogin(object):
    # 初始化
    def setup_class(self):
        # 实例化PageLogin
        self.login = PageLogin()

    # 结束
    def teardown_class(self):
        self.login.driver.quit()

    # 登录测试方法
    @pytest.mark.parametrize("phone,pwd", get_data())
    def test_login(self, phone, pwd):
        # 调用登录业务方法
        self.login.page_login(phone, pwd)
