# 为了避免对这套框架进行大的改动，比如支持一堆表格，或者字符串拼接来识别不同令牌

# 我们决定，干脆一套代码放八遍，然后批处理执行八次

import os

os.system("python main_basic.py")
os.system("python main_editor.py")
os.system("python main_tool.py")
os.system("python main_derivative.py")