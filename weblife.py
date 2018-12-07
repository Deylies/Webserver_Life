# encoding:utf-8
# __author__:DeyLies,WangYu
import os
from until import Conf

def init():
    PROG_CONF = Conf("conf_program.json")
    print(PROG_CONF)
    for fd in PROG_CONF['init_dir']:
        if not os.path.exists(fd):
            os.mkdir(fd)


if __name__ == '__main__':
    init()