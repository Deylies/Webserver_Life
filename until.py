# encoding:utf-8
# __author__:DeyLies,WangYu
import os, json


class Conf(dict):
    """
        读取配置文件的基础功能封装，通过传入
        :param conf_name: 配置文件名称
        :return: 配置文件的json
        >>> conf_app = Conf("conf_program.json")
        >>> print(conf_app.keys)
        dict_keys(['init_dir'])
        >>> conf_app.desc()
        name:init_dir type:<class 'list'> size:6
    """

    def __init__(self, conf_name):
        super().__init__()
        self.name = conf_name
        with open(os.path.join('conf', conf_name), 'r') as f:
            self.__json = json.load(f)
        self.__keys = self.__json.keys()
        self.__desc = []
        for k, v in self.__json.items():
            self[k] = v
            self.__desc.append('name:%s type:%s size:%s' % (k, type(v), len(v)))
        self.__desc = '\n'.join(self.__desc)

    @property
    def keys(self):
        return self.__keys

    def desc(self):
        print(self.__desc)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
