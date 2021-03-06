# -*- coding: utf-8 -*-
import os
import sys

# 设置系统编码为 utf8
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


# 加入根目录
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
# 加入第三方类库搜索路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))


if __name__ == "__main__":
    import server
    server.init()