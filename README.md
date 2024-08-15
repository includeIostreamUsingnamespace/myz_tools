# 0.1.9

测试通过，发布正式版

# 0.1.8

更新内容如下

# 文件名称: common_maths.py

---

---

## 函数部分：

#### 函数 create_dir

```
在指定路径下创建名称为{dir_name}的文件夹
Args:
    dir_name: 文件夹名称
    path: 要创建文件夹的路径，默认为当前路径

Returns:
    无
```

#### 函数 get_max_diff

```
参数：
    two_dimensional_array: 二维数组
返回值：
    每一列里面最大值和最小值的差值，类型是一个一维数组
功能：
    传入一个二维数组，函数返回每一列里面最大值和最小值的差值。
```

#### 函数 remove_outliers_iqr

```
参数：
    data: 二维数组
返回值：
    去除异常值后的二维数组和有效的行索引，类型是一个元组
功能：
    四分位距法去除传入的二维数组中的异常值，注意是对于每一列来说的自己的异常值
```

#### 函数 export_to_csv

```
参数：
    array_data: 二维数组，要保存的数据
    file_name: 字符串，CSV文件的名称（不包含扩展名）
    output_directory: 字符串，保存文件的目录路径，默认为当前目录
返回：
    None
功能：
    将给定的二维数组保存到指定目录中的CSV文件。如果文件已存在，则追加数据，并在每次写入时添加空行作为分隔符。
```

---

## 类部分：

---

# 文件名称: source2md.py

---

---

## 函数部分：

#### 函数 dir2md

```
Args:
    source_dir: 待处理目录
    output_dir: 输出目录
    single_file: 是否将所有文件放到一个md文件中
```

#### 函数 extract_info

```
功能：
    解析python文件，提取函数和类信息
Args:
    file_path: 待处理文件路径
Returns:
    function_docs: 函数信息
    class_info: 类信息
```

#### 函数 all_save_markdown

```
功能：
    将提取的函数和类信息保存为markdown文件
Args:
    file_path: 待处理文件路径
    output_path: 保存路径
    function_docs: 函数信息
    class_info: 类信息
Returns:
    无
```

#### 函数 all2md

```
功能：调用，将一个python文件中的函数和类信息提取出来，并保存为markdown文件
Args:
    file_path: 字符串，python文件的路径
    output_path: 字符串，markdown文件的保存路径
Returns:
    无
```

#### 函数 extract_function_docs_from_file

```
从 Python 文件中提取函数的 docstring（注释部分）。

参数:
    file_path: 字符串，Python 文件的路径。

返回:
    字典，键为函数名，值为函数的 docstring。
```

#### 函数 save_docs_to_markdown

```
将函数的 docstring 保存到 Markdown 文件中。

参数:
    docs: 字典，包含函数名和 docstring 的映射。
    output_path: 字符串，Markdown 文件的保存路径。
```

#### 函数 pyFun2md

```
将 Python 文件中提取 docstring 并保存为 Markdown 文件。

参数:
    source_file: 字符串，源 Python 文件的路径。
    output_md: 字符串，输出 Markdown 文件的路径。
```

---

## 类部分：

---

# 0.1.7

与 0.1.8 相同

# 0.1.6

发布至正式版

# 0.1.5

更新以下内容

注：所有的函数调用方式都是
`myz_tools.文件名称.函数名称(必要的参数)`

各项函数均已通过单元测试

## py2md.py 文件内容

```
主函数，用于从 Python 文件中提取 docstring 并保存为 Markdown 文件。

参数:
    source_file: 字符串，源 Python 文件的路径。
    output_md: 字符串，输出 Markdown 文件的路径。
```

## common_maths.py 文件内容

### create_dir

```
参数：
    dir_name: 文件夹名称
    path: 要创建文件夹的路径，默认为当前路径
返回值：
    无
功能：
    在指定路径下创建名称为{dir_name}的文件夹
```

### get_max_diff

```
参数：
    two_dimensional_array: 二维数组
返回值：
    每一列里面最大值和最小值的差值，类型是一个一维数组
功能：
    传入一个二维数组，函数返回每一列里面最大值和最小值的差值。
```

### remove_outliers_iqr

```
参数：
    data: 二维数组
返回值：
    去除异常值后的二维数组和有效的行索引，类型是一个元组
功能：
    四分位距法去除传入的二维数组中的异常值，注意是对于每一列来说的自己的异常值
```

### export_to_csv

```
参数：
    array_data: 二维数组，要保存的数据
    file_name: 字符串，CSV文件的名称（不包含扩展名）
    output_directory: 字符串，保存文件的目录路径，默认为当前目录
返回：
    None
功能：
    将给定的二维数组保存到指定目录中的CSV文件。如果文件已存在，则追加数据，并在每次写入时添加空行作为分隔符。
```

# 0.1.4

from .mytest import \*

测试结果
调用 myz_tools.my_test1()结果为
AttributeError: module 'myz_tools' has no attribute 'my_test1'

# 0.1.3

from . import \*

测试成功，可以通过 myz_tools.mytest.my_test2()调用

# 0.1.2

测试内容：
md 格式原因，下划线下划线换为--表示
--init--.py 为空

测试结果
ModuleNotFoundError: No module named 'mytest'
