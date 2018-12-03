# encoding:utf-8
# __author__:DeyLies,WangYu
from apps._base import WebApp


class HealthApp(WebApp):
    def __init__(self):
        super().__init__('health',__name__)