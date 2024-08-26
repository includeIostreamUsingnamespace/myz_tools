import itertools
import math
import os

import numpy as np
import pandas as pd


# 单元测试通过
def create_dir(dir_name, path="."):
    """
    在指定路径下创建名称为{dir_name}的文件夹
    Args:
        dir_name: 文件夹名称
        path: 要创建文件夹的路径，默认为当前路径

    Returns:
        无
    """
    full_path = os.path.join(path, dir_name)
    try:
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            # print(f"文件夹 '{dir_name}' 已成功创建于 {path}")
        else:
            # print(f"文件夹 '{dir_name}' 已经存在于 {path}")
            pass
    except OSError as e:
        print(f"创建文件夹 '{dir_name}' 失败: {e}")


# 单元测试通过
def get_max_diff(two_dimensional_array):
    """
    参数：
        two_dimensional_array: 二维数组
    返回值：
        每一列里面最大值和最小值的差值，类型是一个一维数组
    功能：
        传入一个二维数组，函数返回每一列里面最大值和最小值的差值。
    """
    # 将输入转换为 NumPy 数组，并确保其为二维数组
    data = np.asarray(two_dimensional_array)

    if data.ndim != 2:
        raise ValueError("输入必须是一个二维数组或可以转换为二维数组的结构")

    # 使用 NumPy 的 ptp 函数直接计算每列的最大值和最小值差值
    diff = np.ptp(data, axis=0)

    return diff


# 单元测试通过
def remove_outliers_iqr(data):
    """
    参数：
        data: 二维数组
    返回值：
        去除异常值后的二维数组和有效的行索引，类型是一个元组
    功能：
        四分位距法去除传入的二维数组中的异常值，注意是对于每一列来说的自己的异常值
    """
    data = np.asarray(data)

    # 记录哪些行满足条件
    valid_rows = np.ones(data.shape[0], dtype=bool)

    for col in range(data.shape[1]):
        # 计算Q1和Q3
        Q1 = np.percentile(data[:, col], 25)
        Q3 = np.percentile(data[:, col], 75)
        IQR = Q3 - Q1

        # 计算上下边界
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # 更新valid_rows数组，保留不包含异常值的行
        valid_rows &= (data[:, col] >= lower_bound) & (data[:, col] <= upper_bound)

    # 筛选出有效的行
    cleaned_data = data[valid_rows]

    # 返回去除异常值后的数组和行索引
    valid_indices = np.where(valid_rows)[0]

    return cleaned_data, valid_indices


# 单元测试通过
def export_to_csv(array_data, file_name, output_directory="."):
    """
    参数：
        array_data: 二维数组，要保存的数据
        file_name: 字符串，CSV文件的名称（不包含扩展名）
        output_directory: 字符串，保存文件的目录路径，默认为当前目录
    返回：
        None
    功能：
        将给定的二维数组保存到指定目录中的CSV文件。如果文件已存在，则追加数据，并在每次写入时添加空行作为分隔符。
    """
    try:
        array_data = np.asarray(array_data)
        # 确保输入的是二维数组
        if array_data.ndim != 2:
            raise ValueError("输入必须是一个二维数组或可以转换为二维数组的结构")
        # 确保输出目录存在
        os.makedirs(output_directory, exist_ok=True)

        # 构建完整的文件路径
        full_file_path = os.path.join(output_directory, file_name + ".csv")

        # 判断文件是否存在并设置写入模式
        write_mode = "a" if os.path.exists(full_file_path) else "w"

        # 将二维数组转换为DataFrame并保存为CSV文件
        df = pd.DataFrame(array_data)
        df.to_csv(full_file_path, mode=write_mode, index=False, header=False)

        # 在文件末尾添加空行以分隔数据块
        with open(full_file_path, "a", encoding="utf-8") as file:
            file.write("\n")

    except Exception as error:
        raise IOError(f"保存数据到CSV文件失败: {str(error)}")


# TAG 0.2.0 更新


# 单元测试通过
def generate_2d_combinations_iter(data_3d, test_first_group=False):
    """
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
    """
    # 检查输入是否为三维列表
    if not all(isinstance(item, list) for sublist in data_3d for item in sublist):
        raise ValueError("输入的数据必须是一个三维列表")
    if not data_3d or not any(data_3d):
        raise ValueError("输入的三维列表不能为空")

    # 根据 test_first_group 参数决定处理方式
    data_to_process = [data_3d[0]] if test_first_group else data_3d

    for data_2d in data_to_process:
        # 使用 itertools.product 生成所有组合，返回迭代器
        yield itertools.product(*data_2d)


# 单元测试通过
def generate_row_permutations(data_2d):
    """
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
    """
    if not data_2d or not all(data_2d):
        raise ValueError("输入的二维数组不能为空，且每一行都应包含至少一个元素。")

    row_permutations = [itertools.permutations(row) for row in data_2d]
    # 一次 row:[1,2]  -> row_permutations: [(1, 2), (2, 1)]

    for combination in itertools.product(*row_permutations):
        yield [list(row) for row in combination]


# 单元测试通过
def calculate_total_permutations(data_2d):
    """
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
    """
    if not data_2d or not all(data_2d):
        raise ValueError("输入的二维数组不能为空，且每一行都应包含至少一个元素。")

    num_permutations = math.factorial(len(data_2d[0]))
    # 一维列表长度为n,则排列组合数为n!，得到的一维组合列表的长度是n!
    # n!*n!*n!...n!总共是行数个，所以下面乘以行数
    total = num_permutations ** len(data_2d)
    # print(f"总排列组合数: {total}")
    return total


# 不测试
def display_combinations(data_2d, N=5):
    """
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
    """
    if not data_2d or not all(data_2d):
        raise ValueError("输入的二维数组不能为空，且每一行都应包含至少一个元素。")

    combinations = generate_row_permutations(data_2d)

    for i, combination in enumerate(combinations):
        if i < N:
            for row in combination:
                print(row)
            print()
        else:
            break


# 单元测试通过
def evaluate_list_similarity(lst, n, method="MSE"):
    """
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

    """
    # 验证输入的有效性
    if not isinstance(lst, list) or not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("输入的列表 `lst` 必须是包含整数或浮点数的列表。")
    if not isinstance(n, (int, float)):
        raise TypeError("参数 `n` 必须是整数或浮点数。")
    if method not in ["MSE", "MAE", "total_score"]:
        raise ValueError(f"不支持的评分方法 '{method}'。请选择 'MSE'、'MAE' 或 'total_score'。")

    # 对列表进行排序
    sorted_lst = sorted(lst)

    # 计算相邻元素之间的差值
    differences = [
        abs(sorted_lst[i + 1] - sorted_lst[i]) for i in range(len(sorted_lst) - 1)
    ]

    if not differences:
        return 0

    if method == "MSE":
        # 计算均方误差 (MSE)
        squared_errors = [(diff - n) ** 2 for diff in differences]
        score = np.mean(squared_errors)

    elif method == "MAE":
        # 计算平均绝对误差 (MAE)
        absolute_errors = [abs(diff - n) for diff in differences]
        score = np.mean(absolute_errors)

    elif method == "total_score":
        # 计算总分
        total_score = sum(abs(diff - n) for diff in differences)
        score = total_score

    return score


# 单元测试通过
def check_unique(data):
    """
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
    """
    # 验证输入是否为二维列表
    if not isinstance(data, list) or not all(
        isinstance(sublist, list) for sublist in data
    ):
        raise TypeError("输入必须是一个二维列表。")

    # 将二维数组展平为一维数组
    flattened_data = [item for sublist in data for item in sublist]

    # 检查是否所有元素都是唯一的
    return len(flattened_data) == len(set(flattened_data))


if __name__ == "__main__":
    pass
