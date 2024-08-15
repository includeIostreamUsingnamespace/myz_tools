import os
import shutil
import unittest

import numpy as np
import pandas as pd
from common_maths import *


#################################################################################
class TestCreateDir(unittest.TestCase):
    """TestCreateDir"""

    def setUp(self):
        """在每个测试之前运行的代码，用于设置测试环境"""
        self.test_dir = "test_create_dir"
        self.sub_dir = "subfolder"
        self.test_path = os.path.join(self.test_dir, self.sub_dir)

        # 确保测试目录是干净的
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)

    def tearDown(self):
        """在每个测试之后运行的代码，用于清理测试环境"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_create_new_directory(self):
        """测试函数在不存在的路径中创建目录"""
        new_dir_name = "new_folder"
        create_dir(new_dir_name, self.test_dir)
        full_path = os.path.join(self.test_dir, new_dir_name)
        self.assertTrue(os.path.exists(full_path), "目录未创建成功")

    def test_directory_already_exists(self):
        """测试函数在目录已经存在的情况下处理"""
        existing_dir_name = "existing_folder"
        os.makedirs(os.path.join(self.test_dir, existing_dir_name))
        create_dir(existing_dir_name, self.test_dir)
        # 验证目录是否仍然存在，且没有抛出异常
        full_path = os.path.join(self.test_dir, existing_dir_name)
        self.assertTrue(os.path.exists(full_path), "目录应该已经存在")


#######################################################################


class TestGetMaxDiff(unittest.TestCase):
    def test_standard_case(self):
        """测试函数在正常二维数组中的行为"""
        array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = np.array([6, 6, 6])  # 每列的最大值与最小值的差
        result = get_max_diff(array)
        np.testing.assert_array_equal(result, expected)

    # def test_empty_array(self):
    #     """测试函数在空二维数组中的行为"""
    #     array = []
    #     expected = np.array([])
    #     result = get_max_diff(array)
    #     np.testing.assert_array_equal(result, expected)

    def test_single_column_array(self):
        """测试函数在只有一列的二维数组中的行为"""
        array = [[1], [3], [5]]
        expected = np.array([4])  # 只有一列，最大值与最小值的差
        result = get_max_diff(array)
        np.testing.assert_array_equal(result, expected)

    def test_invalid_input(self):
        """测试函数在非二维数组输入中的行为"""
        with self.assertRaises(ValueError):
            get_max_diff([1, 2, 3])  # 一维数组

        with self.assertRaises(ValueError):
            get_max_diff([[1, 2], [3, 4], [5]])  # 不规则的二维数组

    def test_non_numeric_data(self):
        """测试函数在包含非数字数据的二维数组中的行为"""
        array = [[1, 2, "a"], [3, 4, "b"]]
        with self.assertRaises(TypeError):
            get_max_diff(array)


###########################################################################################
class TestRemoveOutliersIQR(unittest.TestCase):
    def test_remove_outliers_basic(self):
        """
        测试简单的二维数组，确保函数能正确去除异常值。
        """
        data = np.array(
            [
                [1, 2, 3, 4],
                [5, 5, 5, 5],
                [100, 200, 300, 1000],  # 明显的异常值
                [2, 3, 4, 5],
                [6, 7, 8, 9],
                [0, 0, 0, 0],
            ]
        )

        cleaned_data, valid_indices = remove_outliers_iqr(data)
        expected_data = np.array(
            [[1, 2, 3, 4], [5, 5, 5, 5], [2, 3, 4, 5], [6, 7, 8, 9], [0, 0, 0, 0]]
        )

        expected_indices = [0, 1, 3, 4, 5]

        np.testing.assert_array_equal(cleaned_data, expected_data)
        np.testing.assert_array_equal(valid_indices, expected_indices)

    def test_all_inliers(self):
        """
        测试当没有异常值时，所有数据都应该保留。
        """
        data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [2, 3, 4, 5], [6, 7, 8, 9]])

        cleaned_data, valid_indices = remove_outliers_iqr(data)

        np.testing.assert_array_equal(cleaned_data, data)
        np.testing.assert_array_equal(valid_indices, [0, 1, 2, 3])

    def test_single_column(self):
        """
        测试只有一列数据的情况。
        """
        data = np.array([[1], [2], [100], [3], [4]])  # 异常值

        cleaned_data, valid_indices = remove_outliers_iqr(data)
        expected_data = np.array([[1], [2], [3], [4]])

        expected_indices = [0, 1, 3, 4]

        np.testing.assert_array_equal(cleaned_data, expected_data)
        np.testing.assert_array_equal(valid_indices, expected_indices)


##################################################################
class TestExportToCsv(unittest.TestCase):
    def setUp(self):
        """在每个测试之前运行的代码，用于设置测试环境"""
        self.test_dir = "test_output"
        self.test_file = "test_data"
        self.test_data = [[1, 2, 3], [4, 5, 6]]

        # 确保测试目录是干净的
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)

    def tearDown(self):
        """在每个测试之后运行的代码，用于清理测试环境"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_file_creation(self):
        """测试函数是否能够创建CSV文件"""
        export_to_csv(self.test_data, self.test_file, self.test_dir)
        file_path = os.path.join(self.test_dir, self.test_file + ".csv")
        self.assertTrue(os.path.exists(file_path), "CSV文件未创建成功")

    def test_data_written_correctly(self):
        """测试函数是否正确写入数据到CSV文件"""
        export_to_csv(self.test_data, self.test_file, self.test_dir)

        file_path = os.path.join(self.test_dir, self.test_file + ".csv")
        # 检查CSV内容是否正确
        df = pd.read_csv(file_path, header=None, index_col=False)
        self.assertTrue(df.equals(pd.DataFrame(self.test_data)), "CSV文件内容不匹配")

    def test_append_data(self):
        """测试函数在文件存在时是否能够正确追加数据"""
        export_to_csv(self.test_data, self.test_file, self.test_dir)
        additional_data = [[7, 8, 9]]
        export_to_csv(additional_data, self.test_file, self.test_dir)

        file_path = os.path.join(self.test_dir, self.test_file + ".csv")

        # 检查CSV内容是否包含追加的数据
        df = pd.read_csv(file_path, header=None, index_col=False)
        expected_data = self.test_data + additional_data
        self.assertTrue(df.equals(pd.DataFrame(expected_data)), "数据追加失败")

    # def test_empty_data(self):
    #     """测试函数在传入空数据时的处理"""
    #     try:
    #         export_to_csv([], self.test_file, self.test_dir)
    #     except Exception as e:
    #         self.fail(f"函数在处理空数据时抛出异常: {e}")

    #     file_path = os.path.join(self.test_dir, self.test_file + ".csv")

    #     self.assertTrue(os.path.exists(file_path), "CSV文件未创建")

    #     # 检查CSV文件内容
    #     df = pd.read_csv(file_path)
    #     self.assertTrue(df.empty, "CSV文件不应包含数据")


if __name__ == "__main__":
    unittest.main()
