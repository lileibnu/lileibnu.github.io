# coding: utf-8

# ## Import necessary libraries
# 我们将使用 os 库来处理文件路径

# In[1]:

import os

# ## 读取指定目录中的所有 Markdown 文件
# 指定存放 Markdown 文件的目录
markdown_directory = "_publications"

# 检查目录是否存在
if not os.path.exists(markdown_directory):
    print(f"目录 {markdown_directory} 不存在，请检查路径。")
else:
    # 遍历目录中的所有文件
    for filename in os.listdir(markdown_directory):
        # 检查文件扩展名
        if filename.endswith(".md"):
            markdown_file_path = os.path.join(markdown_directory, filename)
            try:
                # 读取并显示每个 Markdown 文件的内容
                with open(markdown_file_path, 'r', encoding='utf-8') as f:
                    markdown_content = f.read()
                    print(f"内容来自文件: {filename}\n")
                    print(markdown_content)
                    print("\n" + ("-" * 40) + "\n")  # 分隔符
            except Exception as e:
                print(f"读取文件 {filename} 时发生错误: {e}")
