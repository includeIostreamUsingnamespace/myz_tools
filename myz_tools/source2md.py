# 导入ast模块，用于解析Python源代码
import ast
# 导入inspect模块，用于获取源代码
import inspect
import json
import os


# TAG下，第三版，在第二版的基础上增加对文件里面所有的python文件处理，
# #################### 并且支持选择放到同一个md文件还是按照python文件的名称放到指定目录下的不同md文件
def dir2md(source_dir, output_dir="./MD/", single_file=True):
    """
    Args:
        source_dir: 待处理目录
        output_dir: 输出目录
        single_file: 是否将所有文件放到一个md文件中
    """
    if single_file:
        # 要放到一个md文件里面
        # 拿到source_dir的名称

        source_dir_name = os.path.basename(source_dir)
        output_path = output_dir + source_dir_name + ".md"
        mode = "w"

        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if file.endswith(".py"):
                    # 获取文件的绝对路径
                    file_path = os.path.join(root, file)
                    # 拿到文件信息
                    function_docs, class_info = extract_info(file_path)
                    all_save_markdown(
                        file_path, output_path, function_docs, class_info, mode
                    )
                    mode = "a"

        pass
    else:
        # 要放到指定目录下的不同md文件，文件名称为自己项目中的python文件名称
        # 遍历source_dir目录下的所有python文件
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if file.endswith(".py"):
                    # 获取文件的绝对路径
                    file_path = os.path.join(root, file)
                    # 拿到该文件的名称
                    file_name = os.path.basename(file_path)
                    # 后缀修改为md
                    md_file_name = os.path.splitext(file_name)[0] + ".md"
                    output_path = output_dir + md_file_name
                    all2md(file_path, output_path)

    pass


# TAG 下：第二版
# 解析、保存、调用
def extract_info(file_path):
    """
    功能：
        解析python文件，提取函数和类信息
    Args:
        file_path: 待处理文件路径
    Returns:
        function_docs: 函数信息
        class_info: 类信息
    """
    with open(file_path, "r", encoding="utf-8") as file:
        source = file.read()

    # 检测是否栈溢出
    try:
        # 将源代码解析为抽象语法树
        tree = ast.parse(source)
    except RecursionError as e:
        print(f"当前处理的{file_path}文件太大，栈溢出，请切割文件后重新调用: {e}")
        return None, None

    # 创建一个字典，用于存储函数的文档字符串
    function_docs = {}
    # 创建一个字典，用于存储类的信息
    class_info = {}
    # 一个字典，用于判断函数的时候跳过类函数，采用函数名 + 注释双重判定
    # HACK 不是很优雅，还可以继续优化这个逻辑
    skip_class_fun = {}

    for node in ast.walk(tree):
        # 类，以及类方法
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            class_docstring = ast.get_docstring(node)
            class_info[class_name] = {"docstring": class_docstring, "members": []}
            for member in node.body:
                if isinstance(member, ast.FunctionDef):
                    # 处理类中的方法
                    func_name = member.name
                    func_docstring = ast.get_docstring(member)
                    class_info[class_name]["members"].append(
                        {
                            "type": "method",
                            "name": func_name,
                            "docstring": func_docstring,
                        }
                    )
                    # 判定条件是：类方法名 + 注释
                    skip_class_fun[func_name] = func_docstring
                elif isinstance(member, ast.Assign):
                    # 处理类的属性
                    for target in member.targets:
                        if isinstance(target, ast.Name):
                            attr_name = target.id
                            class_info[class_name]["members"].append(
                                {"type": "attribute", "name": attr_name}
                            )
        # 普通函数
        elif isinstance(node, ast.FunctionDef):
            func_name = node.name
            func_docstring = ast.get_docstring(node)
            # HACK 不是很优雅，还可以继续优化这个逻辑
            # 根据方法名+注释信息判断是否为类方法，为类方法的话就直接跳过访问
            check_key_value = (func_name, func_docstring)
            if check_key_value in skip_class_fun.items():
                continue
            function_docs[func_name] = func_docstring
    return function_docs, class_info


def all_save_markdown(file_path, output_path, function_docs, class_info, mode="w"):
    """
    功能：
        将提取的函数和类信息保存为markdown文件
    Args:
        file_path: 待处理文件路径
        output_path: 保存路径
        function_docs: 函数信息
        class_info: 类信息
    Returns:
        无

    """
    with open(output_path, mode=mode, encoding="utf-8") as file:
        file.write("# 文件名称: " + os.path.basename(file_path) + "\n")
        file.write("***\n")
        if mode == "w":
            file.write("[TOC]\n")
        file.write("***\n")
        file.write("\n## 函数部分：\n")
        for func_name, docstring in function_docs.items():
            file.write(f"#### 函数{func_name}\n")
            if docstring:
                file.write(f"```\n{docstring}\n```\n")
            else:
                file.write("\n")
        file.write("***\n")

        file.write("\n## 类部分：\n")
        for class_name, class_info in class_info.items():
            file.write(f"### 类{class_name}\n")
            if class_info["docstring"]:
                file.write(f"```\n{class_info['docstring']}\n```\n")
            else:
                file.write("\n")
            for member in class_info["members"]:
                if member["type"] == "method":
                    file.write(f"#### 类方法{member['name']}\n")
                    if member["docstring"]:
                        file.write(f"```\n{member['docstring']}\n```\n")
                    else:
                        file.write("\n")
                elif member["type"] == "attribute":
                    file.write(f"#### attribute_name:{member['name']}\n")
        file.write("***\n")

        pass
    pass


def all2md(file_path, output_path):
    """
    功能：调用，将一个python文件中的函数和类信息提取出来，并保存为markdown文件
    Args:
        file_path: 字符串，python文件的路径
        output_path: 字符串，markdown文件的保存路径
    Returns:
        无
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    function_docs, class_info = extract_info(file_path)
    if function_docs or class_info:
        all_save_markdown(file_path, output_path, function_docs, class_info)
    else:
        print(f"文件{file_path}存在没有函数或类定义，或者是有但是文件本身太大，无法解析")
        # raise Exception("文件没有函数或类定义，或者是有但是文件本身太大，无法解析")
        pass
    pass


# TAG 下：第一版
def extract_function_docs_from_file(file_path):
    """
    从 Python 文件中提取函数的 docstring（注释部分）。

    参数:
        file_path: 字符串，Python 文件的路径。

    返回:
        字典，键为函数名，值为函数的 docstring。
    """

    with open(file_path, "r", encoding="utf-8") as file:
        source = file.read()

    # 解析源代码
    tree = ast.parse(source)

    function_docs = {}

    # 遍历 AST 节点，提取函数定义和 docstring
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            docstring = ast.get_docstring(node)
            function_docs[func_name] = docstring

    return function_docs


def save_docs_to_markdown(docs, output_path):
    """
    将函数的 docstring 保存到 Markdown 文件中。

    参数:
        docs: 字典，包含函数名和 docstring 的映射。
        output_path: 字符串，Markdown 文件的保存路径。
    """
    # if os.path.exists(output_path):
    #     mode = "a"
    # else:
    #     mode = "w"
    with open(output_path, mode="w", encoding="utf-8") as file:
        for func_name, docstring in docs.items():
            file.write(f"### {func_name}\n\n")
            if docstring:
                file.write(f"```\n{docstring}\n```\n")
            else:
                file.write("无 docstring\n")
            file.write("\n")


def pyFun2md(source_file, output_md):
    """
    将 Python 文件中提取 docstring 并保存为 Markdown 文件。

    参数:
        source_file: 字符串，源 Python 文件的路径。
        output_md: 字符串，输出 Markdown 文件的路径。
    """
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"文件 {source_file} 不存在")
    docs = extract_function_docs_from_file(source_file)
    save_docs_to_markdown(docs, output_md)


# TAG 简单测试位置
if __name__ == "__main__":
    # 第一版，只能对python里普通函数处理
    # source_file_path = "./myz_tools/common_maths.py"  # Python 文件路径
    # output_md_path = "./MD/common_maths_doc.md"  # 输出 Markdown 文件路径
    # pyFun2md(source_file_path, output_md_path)

    # # 第二版，可以对python里普通函数和类方法处理
    # source_file_path = "./myz_tools/common_maths.py"  # Python 文件路径
    # output_md_path = "./MD/common_maths_doc.md"  # 输出 Markdown 文件路径
    # all2md(source_file_path, output_md_path)

    # source_file_path = "./myz_tools/all_test.py"  # Python 文件路径
    # output_md_path = "./MD/all_test_doc.md"  # 输出 Markdown 文件路径
    # all2md(source_file_path, output_md_path)

    # 第三版，可以处理一个目录下的所有python文件，并且可以选择是否将所有文件放到一个md文件中
    # 分别放到单个文件测试
    source_dir = "./myz_tools"  # Python 项目目录
    output_dir = "./MD/"  # 输出目录
    dir2md(source_dir, output_dir, single_file=False)

    # 放到一个文件中测试
    source_dir = "./myz_tools"  # Python 项目目录
    output_dir = "./MD/"  # 输出目录
    dir2md(source_dir, output_dir, single_file=True)

    # 放到一个文件中测试，使用默认参数
    source_dir = "./myz_tools"  # Python 项目目录
    dir2md(source_dir)

    # 第三版简单测试通过
    # TODO 进行单元测试
    pass
