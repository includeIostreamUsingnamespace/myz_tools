# 导入setuptools模块，用于打包和分发Python项目
# 导入re模块，用于正则表达式操作
import re

# 导入requests模块，用于发送HTTP请求
import requests
import setuptools
# 导入BeautifulSoup模块，用于解析HTML文档
from bs4 import BeautifulSoup

package_name = "myz_tools"


def curr_version():
    """
    参数：无
    返回值：当前官网上最新的版本号，格式为x.y.z
    原理是从PyPi网站上面获取最新的版本号
    """

    # 从官网获取版本号
    # 定义URL，使用f-string格式化字符串，将package_name插入URL中
    url = f"https://pypi.org/project/{package_name}/"
    # url = f"https://test.pypi.org/project/{package_name}/"
    # 发送GET请求，获取响应
    response = requests.get(url)

    # 检查是否响应成功
    if response.status_code == 200:
        # print(f"成功获取官网的{package_name}的响应")
        pass
    else:
        # raise Exception(f"获取{package_name}的响应失败，状态码：{response.status_code}")
        # 通过文件的存储版本号
        # 打开文件
        print(f"test.pypi获取{package_name}的响应失败，状态码：{response.status_code}，尝试从文件中获取版本号")
        with open("version.txt", "r", encoding="utf-8") as f:
            # 读取所有行
            lines = f.readlines()
        # 获取最后一行
        latest_version = lines[-1]
        return str(latest_version)
        # 打印最新版本号
        # print(latest_version)
        pass

    # 使用BeautifulSoup解析响应内容
    soup = BeautifulSoup(response.content, "html.parser")

    # 使用CSS选择器，选择.release__version类下的第一个元素，获取其文本内容，并去除首尾空格
    latest_version = soup.select_one(".release__version").text.strip()
    # print(f"当前PyPi上面的最新的版本号是：{latest_version}")
    # 返回最新版本号
    return str(latest_version)


def get_version():
    """
    参数：无
    返回值：由官网上的最新的版本好计算出当前最新的版本号，格式为x.y.z
    """

    # # 从版本号字符串中提取三个数字并将它们转换为整数类型
    # # 使用正则表达式匹配当前版本号
    # match = re.search(r"(\d+)\.(\d+)\.(\d+)", curr_version())
    # # 将匹配到的第一个数字转换为整数，作为主版本号
    # major = int(match.group(1))
    # # 将匹配到的第二个数字转换为整数，作为次版本号
    # minor = int(match.group(2))
    # # 将匹配到的第三个数字转换为整数，作为补丁号
    # patch = int(match.group(3))

    # # 对三个数字进行加一操作
    # patch += 1
    # # 如果patch大于9，则将patch置为0，并将minor加一
    # if patch > 9:
    #     patch = 0
    #     minor += 1
    #     # 如果minor大于9，则将minor置为0，并将major加一
    #     if minor > 9:
    #         minor = 0
    #         major += 1
    # # 将major、minor、patch拼接成新的版本号字符串
    # new_version_str = f"{major}.{minor}.{patch}"
    # # 返回新的版本号字符串

    # 手动指定版本号
    new_version_str = "0.2.0"

    return new_version_str


def upload():
    # 打开README.md文件，以只读模式读取文件内容
    with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
        long_description = fh.read()
    # 打开requirements.txt文件，读取文件内容，并按行分割
    with open("requirements.txt", encoding="utf-8", errors="ignore") as f:
        required = f.read().splitlines()

    setuptools.setup(
        name=package_name,
        # 此处可以手动指定版本号
        version=get_version(),
        author="宇千思",  # 作者名称
        author_email="",  # 作者邮箱
        description="Python helper tools",  # 库描述
        long_description=long_description,  # 设置长描述
        long_description_content_type="text/markdown",  # 设置长描述的内容类型为Markdown
        url="https://pypi.org/project/myz_tools/",  # 库的官方地址
        # 查找项目中的所有包
        packages=setuptools.find_packages(include=["myz_tools", "myz_tools.*"]),
        data_files=["requirements.txt"],  # myz_tools库依赖的其他库
        classifiers=[
            "License :: OSI Approved :: Apache Software License",  # 授权协议
        ],
        # 指定Python版本要求，这里要求Python版本大于等于
        python_requires=">=3.6",
        # 指定安装依赖，这里使用required变量，该变量应该是一个包含所有依赖的列表
        install_requires=required,
    )


# 定义一个函数，用于写入当前版本号
def write_now_version():
    # 打开名为VERSION的文件，以写入模式
    with open("version.txt", "a", encoding="utf-8", errors="ignore") as version_f:
        # 将当前版本号写入文件
        version_f.write(get_version())
        # 写完后换行
        version_f.write("\n")
        pass


def main():
    try:
        # 尝试执行上传操作
        upload()
        write_now_version()
        # 打印上传成功信息，并显示当前版本号
        print("已经成功准备好包，可以进行打包操作, 更新后的最新版本号将是:", get_version())
    except Exception as e:
        # 如果上传过程中出现异常，则抛出异常，并显示异常信息
        raise Exception("上传出现异常", e)


if __name__ == "__main__":
    main()
    pass
