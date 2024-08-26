# 0.2.0

正式版，增加了 5 个函数

# 文件名称: all_test.py

---

[TOC]

---

## 函数部分：

#### 函数 test_invalid_input

```
测试函数在非二维数组输入中的行为
```

#### 函数 test_empty_input

```
测试传入空的三维数组。
```

#### 函数 test_valid_input

```
测试正常输入的排列组合生成。
```

#### 函数 test_empty_list

```
测试传入空列表的情况。
```

---

## 类部分：

### 类 TestCreateDir

```
TestCreateDir
```

#### 类方法 setUp

```
在每个测试之前运行的代码，用于设置测试环境
```

#### 类方法 tearDown

```
在每个测试之后运行的代码，用于清理测试环境
```

#### 类方法 test_create_new_directory

```
测试函数在不存在的路径中创建目录
```

#### 类方法 test_directory_already_exists

```
测试函数在目录已经存在的情况下处理
```

### 类 TestGetMaxDiff

#### 类方法 test_standard_case

```
测试函数在正常二维数组中的行为
```

#### 类方法 test_single_column_array

```
测试函数在只有一列的二维数组中的行为
```

#### 类方法 test_invalid_input

```
测试函数在非二维数组输入中的行为
```

#### 类方法 test_non_numeric_data

```
测试函数在包含非数字数据的二维数组中的行为
```

### 类 TestRemoveOutliersIQR

#### 类方法 test_remove_outliers_basic

```
测试简单的二维数组，确保函数能正确去除异常值。
```

#### 类方法 test_all_inliers

```
测试当没有异常值时，所有数据都应该保留。
```

#### 类方法 test_single_column

```
测试只有一列数据的情况。
```

### 类 TestExportToCsv

#### 类方法 setUp

```
在每个测试之前运行的代码，用于设置测试环境
```

#### 类方法 tearDown

```
在每个测试之后运行的代码，用于清理测试环境
```

#### 类方法 test_file_creation

```
测试函数是否能够创建CSV文件
```

#### 类方法 test_data_written_correctly

```
测试函数是否正确写入数据到CSV文件
```

#### 类方法 test_append_data

```
测试函数在文件存在时是否能够正确追加数据
```

### 类 TestGenerate2DCombinationsIter

#### 类方法 test_generate_all_combinations

```
测试正常情况下，生成所有二维数组组合的迭代器。
```

#### 类方法 test_generate_first_group_combinations

```
测试只生成第一个二维数组组合的迭代器。
```

#### 类方法 test_empty_input

```
测试传入空的三维数组。
```

#### 类方法 test_invalid_input

```
测试传入非三维数组，应该抛出 ValueError。
```

#### 类方法 test_single_element_input

```
测试仅包含一个元素的三维数组。
```

#### 类方法 test_single_layer_array

```
测试包含一个二维数组的三维数组。
```

### 类 TestGenerateRowPermutations

#### 类方法 test_valid_input

```
测试正常输入的排列组合生成。
```

#### 类方法 test_single_row

```
测试只有一行的二维数组。
```

#### 类方法 test_empty_rows

```
测试包含空行的二维数组。
```

#### 类方法 test_empty_input

```
测试空的二维数组。
```

#### 类方法 test_empty_element_in_rows

```
测试包含空元素的二维数组。
```

### 类 TestCalculateTotalPermutations

#### 类方法 test_valid_input

```
测试正常输入的排列组合总数。
```

#### 类方法 test_single_row

```
测试只有一行的二维数组。
```

#### 类方法 test_multiple_rows

```
测试多行，每行元素数量不同的情况。
```

#### 类方法 test_empty_input

```
测试空的二维数组。
```

#### 类方法 test_empty_row

```
测试包含空行的二维数组。
```

#### 类方法 test_non_integer_elements

```
测试包含非整数元素的二维数组。
```

### 类 TestEvaluateListSimilarity

#### 类方法 test_mse

```
测试均方误差 (MSE) 评分方法。
```

#### 类方法 test_mae

```
测试平均绝对误差 (MAE) 评分方法。
```

#### 类方法 test_total_score

```
测试总分评分方法。
```

#### 类方法 test_empty_list

```
测试传入空列表的情况。
```

#### 类方法 test_invalid_list_type

```
测试传入无效的列表类型。
```

#### 类方法 test_invalid_element_type

```
测试列表中含有无效元素类型。
```

#### 类方法 test_invalid_n_type

```
测试传入无效的 n 类型。
```

#### 类方法 test_invalid_method

```
测试传入无效评分方法的情况。
```

### 类 TestCheckUnique

#### 类方法 test_unique_elements

```
测试所有元素唯一的情况。
```

#### 类方法 test_non_unique_elements

```
测试存在重复元素的情况。
```

#### 类方法 test_empty_list

```
测试空二维列表的情况。
```

#### 类方法 test_empty_sublist

```
测试包含空子列表的情况。
```

#### 类方法 test_empty_and_non_empty_sublists

```
测试包含空子列表和非空子列表的情况。
```

#### 类方法 test_invalid_input_type

```
测试传入非法输入类型的情况。
```

---

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

#### 函数 generate_2d_combinations_iter

```
功能：
    传入一个三维数组，返回每个二维数组的所有元素组合的迭代器。如果设置了 `test_first_group` 参数True,
    则仅返回第一个二维数组的组合。

参数：
    data_3d (list): 一个三维列表，每个元素都是一个二维列表，表示多个二维数组。
    test_first_group (bool): 是否只生成第一个二维数组的组合。默认为 False。

返回值：
    generator: 一个生成器对象，按需生成每个二维数组的所有元素组合。

异常：
    ValueError: 如果输入的数据不是三维列表，则抛出异常。

示例：
    >>> data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    >>> result_iter = generate_2d_combinations_iter(data)
    >>> for combinations in result_iter:
            # 每次拿到是一个二维列表的组合
    ...     print(list(combinations)) # [(1, 3), (1, 4), (2, 3), (2, 4)]
    下一次
    [(5, 7), (5, 8), (6, 7), (6, 8)]


    >>> result_iter = generate_2d_combinations_iter(data, test_first_group=True)
    >>> print(list(next(result_iter)))
    [(1, 3), (1, 4), (2, 3), (2, 4)]
```

#### 函数 generate_row_permutations

```
功能：
    传入一个二维数组，返回该二维数组中每一行元素所有可能的排列组合。


参数：
    data_2d (list): 一个二维列表，表示多个行数据。

返回值：
    generator: 生成器对象，按需生成每一行的所有排列组合并组合成二维数组。

异常：
    ValueError: 如果输入的二维数组为空或某行为空，则抛出异常。

示例：
    >>> data = [[1, 2], [3, 4]]
    >>> permutations = generate_row_permutations(data)
    >>> for perm in permutations:
    ...     print(perm)
    [[1, 2], [3, 4]]
    [[1, 2], [4, 3]]
    [[2, 1], [3, 4]]
    [[2, 1], [4, 3]]
```

#### 函数 calculate_total_permutations

```
功能：
    计算并返回二维数组中所有行的排列组合总数。

参数：
    data_2d (list): 一个二维列表，表示多个行数据。

返回值：
    int: 所有行排列组合的总数。

异常：
    ValueError: 如果输入的二维数组为空或某行为空，则抛出异常。

示例：
    >>> data = [[1, 2], [3, 4]]
    >>> total = calculate_total_permutations(data)
    >>> print(total)
    4
```

#### 函数 display_combinations

```
功能：
    打印二维数组中前 N 个排列组合，以检测组合生成的正确性。

参数：
    data_2d (list): 一个二维列表，表示多个行数据。
    N (int): 要打印的组合数量，默认为 5。

返回值：
    None

异常：
    ValueError: 如果输入的二维数组为空或某行为空，则抛出异常。

示例：
    >>> data = [[1, 2], [3, 4]]
    >>> display_combinations(data, N=2)
    [1, 2]
    [3, 4]

    [1, 2]
    [4, 3]
```

#### 函数 evaluate_list_similarity

```
功能：
    评估列表中元素间的差异与给定值 `n` 的接近程度。支持不同的评分方法，例如均方误差 (MSE)、绝对误差等。
    三种方式都是得分越小表示列表元素与目标值的接近程度越高
参数：
    lst (list of int/float): 需要评估的数字列表。
    n (int/float): 用于比较的参考值，计算差异的目标值。
    method (str): 选择的评分方法。支持 'MSE'（均方误差）、'MAE'（平均绝对误差）、'total_score'（总分）等。

返回值：
    float: 计算得出的评分值。

异常：
    ValueError: 如果输入的 `lst` 不是列表或 `n` 不是整数或浮点数，则抛出异常。
    TypeError: 如果 `lst` 中的元素不是整数或浮点数，则抛出异常。
    ValueError: 如果选择的评分方法不被支持，则抛出异常。

示例：
    >>> lst = [1, 3, 6, 10]
    >>> n = 2
    >>> score = evaluate_list_similarity(lst, n, method='MSE')
    >>> print(score)

    >>> score = evaluate_list_similarity(lst, n, method='MAE')
    >>> print(score)
```

#### 函数 check_unique

```
功能：
    检查传入的二维数组中的每个元素是否都是唯一的。如果所有元素唯一，返回 True；否则，返回 False。

参数：
    data (list of list): 一个二维列表，其中包含需要检查的元素。

返回值：
    bool: 如果所有元素都唯一，返回 True；否则，返回 False。

异常：
    TypeError: 如果输入的 `data` 不是一个二维列表，或包含非列表的元素，则抛出异常。

示例：
    >>> data = [[1, 2, 3], [4, 5, 6]]
    >>> check_unique(data)
    True

    >>> data = [[1, 2, 3], [3, 4, 5]]
    >>> check_unique(data)
    False
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

# 文件名称: **init**.py

---

---

## 函数部分：

---

## 类部分：

---

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
