import os
# 关于文件路径os.path.dirname()
# 绝对路径,可以获取你当前的文件或者文件夹所在的目录的绝对路径
# 参数：__file__,文件夹的路径
# 以下我要写的代码：代表获取test.py所在的文件夹->tool
file_path = os.path.dirname(__file__)
print(file_path)
# 以下代码  获取tool所在的文件夹->lesson6_2->base_dir 工程目录
base_dir = os.path.dirname(file_path)
print(base_dir)