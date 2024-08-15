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
            print(f"文件夹 '{dir_name}' 已成功创建于 {path}")
        else:
            print(f"文件夹 '{dir_name}' 已经存在于 {path}")
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


if __name__ == "__main__":
    pass
