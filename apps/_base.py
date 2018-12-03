# encoding:utf-8
# __author__:DeyLies,WangYu
from flask import Blueprint, Request, render_template, url_for, Flask


class WebAppMeta(type):
    """
    webapp元类
    """

    def __new__(cls, name, bases, attrs):
        print(attrs)
        # blueprint = attrs.get("__blueprint")
        attrs["__mapping__"] = [(url, func) for url, func in attrs.items() if url.startswith("url_")]
        # for url, func in attrs.items():
        #     if url.startswith("url_"):
        #         attrs[url] = blueprint.route("/login",methonds=["POST","GET"])(func)
        attrs["__mapping__"] = [(url, func) for url, func in attrs.items() if url.startswith("url_")]

        return type.__new__(cls, name, bases, attrs)


class WebApp(metaclass=WebAppMeta):
    """
    webapp父类
    ...
    """
    __slots__ = ('__appname', '__blueprint')
    __Request = Request
    __render_template = render_template
    __url_for = url_for

    def __init__(self, appname, importname):
        self.__appname = appname
        self.__blueprint = Blueprint(appname, importname)
        for url, func in self.__mapping__:
            self.__setattr__(url, self.__blueprint.route(url.replace('url_', ''), methods=["POST", "GET"])(func))

    @property
    def appname(self):
        return self.__appname

    @property
    def blueprint(self):
        return self.__blueprint

    @staticmethod
    def run(host="127.0.0.1", port=5000, debug=True):
        app = Flask(__name__)
        for sub_app_cls in WebApp.__subclasses__():
            sub_app = sub_app_cls()
            app.register_blueprint(sub_app.blueprint, url_prefix="/" + sub_app.appname)
        app.run(host, port, debug)

    def __str__(self):
        return "WebApp,named %s" % self.appname

    __repr__ = __str__


class TestSubApp(WebApp):
    """
    测试父类和元类的属性和方法
    >>> app2 = TestSubApp()
    """

    def __init__(self):
        super().__init__('test', __name__)

    def url_test(self, url):
        return 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
