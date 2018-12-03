# encoding:utf-8
# __author__:DeyLies,WangYu
import unittest
from apps._base import WebApp

class TestApps(unittest.TestCase):
    def test_init(self):
        webapp = WebApp.run()

if __name__ == '__main__':
    unittest.main()