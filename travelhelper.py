# File Handling & Structure

import sys
import os
import re

# Check if the number of command-line arguments is valid (≥3)
def verify_argv():
    if len(sys.argv) < 3:
        print("Usage: python3 script.py <filename>")
        sys.exit(1)



#  获取文件名参数 argument_file，并使用 os.path.isfile() 和 os.access() 判断文件是否存在和可读

# Use os.path.isfile() and os.access() to verify the file exists and is readable

#  如果文件无效，输出错误并退出程序

# If file is invalid, print an error and exit the program using sys.exit()

# 📄 三、读取并解析数据文件
#  使用 with open(argument_file) 打开文件并读取所有行

# Use with open(argument_file) to read the file lines

#  对每一行调用 .strip().split(',') 提取起点、终点、距离

# Use .strip().split(',') on each line to get origin, destination, and distance

#  将每条记录存储成一个 list 或 dict，例如：

# python
# Copy
# Edit
# data = []  # 或者 dict，例如 defaultdict(list)
# data.append((origin, destination, int(distance)))
# Store each record as a tuple or in a dictionary for later access

# 🖨 四、调试 & 输出中间结果（临时测试用）
#  使用 print() 输出每行解析结果，确保数据读取无误

# Use print() to show parsed lines and verify correctness

#  添加注释：解释每一部分代码的功能

# Add comments to explain code sections




