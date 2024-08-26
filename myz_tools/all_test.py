import itertools
import math
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


# TAG 20240818 更新


class TestGenerate2DCombinationsIter(unittest.TestCase):
    def test_generate_all_combinations(self):
        """
        测试正常情况下，生成所有二维数组组合的迭代器。
        """
        data_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        expected_output = [
            [(1, 3), (1, 4), (2, 3), (2, 4)],
            [(5, 7), (5, 8), (6, 7), (6, 8)],
        ]
        result_iter = generate_2d_combinations_iter(data_3d)

        for expected, result in zip(expected_output, result_iter):
            self.assertEqual(list(result), expected)

    def test_generate_first_group_combinations(self):
        """
        测试只生成第一个二维数组组合的迭代器。
        """
        data_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        expected_output = [(1, 3), (1, 4), (2, 3), (2, 4)]

        result_iter = generate_2d_combinations_iter(data_3d, test_first_group=True)
        self.assertEqual(list(next(result_iter)), expected_output)

    def test_empty_input(self):
        """
        测试传入空的三维数组。
        """
        data_3d = []
        with self.assertRaises(ValueError):
            # 生成器内部有异常的话只有在真正调用的时候才会捕获
            list(generate_2d_combinations_iter(data_3d))

    def test_invalid_input(self):
        """
        测试传入非三维数组，应该抛出 ValueError。
        """
        invalid_data = [[[1, 2], 3], [4, 5]]  # 第二层不是一个列表
        with self.assertRaises(ValueError):
            list(generate_2d_combinations_iter(invalid_data))

    def test_single_element_input(self):
        """
        测试仅包含一个元素的三维数组。
        """
        data_3d = [[[1], [2]]]
        expected_output = [(1, 2)]

        result_iter = generate_2d_combinations_iter(data_3d)
        self.assertEqual(list(next(result_iter)), expected_output)

    def test_single_layer_array(self):
        """
        测试包含一个二维数组的三维数组。
        """
        data_3d = [[[1, 2], [3, 4]]]
        expected_output = [(1, 3), (1, 4), (2, 3), (2, 4)]

        result_iter = generate_2d_combinations_iter(data_3d)
        self.assertEqual(list(next(result_iter)), expected_output)


class TestGenerateRowPermutations(unittest.TestCase):
    def test_valid_input(self):
        """
        测试正常输入的排列组合生成。
        """
        data = [[1, 2], [3, 4]]
        expected_output = [
            [[1, 2], [3, 4]],
            [[1, 2], [4, 3]],
            [[2, 1], [3, 4]],
            [[2, 1], [4, 3]],
        ]
        result = list(generate_row_permutations(data))
        self.assertEqual(result, expected_output)

    def test_single_row(self):
        """
        测试只有一行的二维数组。
        """
        data = [[1, 2, 3]]
        expected_output = [[list(p)] for p in itertools.permutations(data[0])]
        result = list(generate_row_permutations(data))
        self.assertEqual(result, expected_output)

    def test_empty_rows(self):
        """
        测试包含空行的二维数组。
        """
        with self.assertRaises(ValueError):
            list(generate_row_permutations([[], [1, 2]]))

    def test_empty_input(self):
        """
        测试空的二维数组。
        """
        with self.assertRaises(ValueError):
            list(generate_row_permutations([]))

    def test_empty_element_in_rows(self):
        """
        测试包含空元素的二维数组。
        """
        with self.assertRaises(ValueError):
            list(generate_row_permutations([[1, 2], []]))


class TestCalculateTotalPermutations(unittest.TestCase):
    def test_valid_input(self):
        """
        测试正常输入的排列组合总数。
        """
        data = [[1, 2], [3, 4]]
        expected_total = 4  # 2! * 2! = 4
        self.assertEqual(calculate_total_permutations(data), expected_total)

    def test_single_row(self):
        """
        测试只有一行的二维数组。
        """
        data = [[1, 2, 3]]
        expected_total = 6  # 3! = 6
        self.assertEqual(calculate_total_permutations(data), expected_total)

    def test_multiple_rows(self):
        """
        测试多行，每行元素数量不同的情况。
        """
        data = [[1, 2], [3, 4], [5, 6]]
        # 每行有2个元素，所以排列组合总数是 2! * 2! * 2! = 8
        expected_total = 8
        self.assertEqual(calculate_total_permutations(data), expected_total)

    def test_empty_input(self):
        """
        测试空的二维数组。
        """
        with self.assertRaises(ValueError):
            calculate_total_permutations([])

    def test_empty_row(self):
        """
        测试包含空行的二维数组。
        """
        with self.assertRaises(ValueError):
            calculate_total_permutations([[], [1, 2]])

    def test_non_integer_elements(self):
        """
        测试包含非整数元素的二维数组。
        """
        data = [["a", "b"], ["c", "d"]]
        expected_total = 4  # 2! * 2! = 4
        self.assertEqual(calculate_total_permutations(data), expected_total)


class TestEvaluateListSimilarity(unittest.TestCase):
    def test_mse(self):
        """
        测试均方误差 (MSE) 评分方法。
        """
        lst = [1, 3, 6, 10]
        n = 2
        expected_score = 1.6666666666666667
        score = evaluate_list_similarity(lst, n, method="MSE")
        self.assertAlmostEqual(score, expected_score, places=7)

    def test_mae(self):
        """
        测试平均绝对误差 (MAE) 评分方法。
        """
        lst = [1, 3, 6, 10]
        n = 2
        expected_score = 1
        score = evaluate_list_similarity(lst, n, method="MAE")
        self.assertAlmostEqual(score, expected_score, places=7)

    def test_total_score(self):
        """
        测试总分评分方法。
        """
        lst = [1, 3, 6, 10]
        n = 2
        expected_score = 3
        score = evaluate_list_similarity(lst, n, method="total_score")
        self.assertAlmostEqual(score, expected_score, places=7)

    def test_empty_list(self):
        """
        测试传入空列表的情况。
        """
        lst = []
        n = 2
        expected_score = 0
        score = evaluate_list_similarity(lst, n, method="MSE")
        self.assertEqual(score, expected_score)

    def test_invalid_list_type(self):
        """
        测试传入无效的列表类型。
        """
        with self.assertRaises(TypeError):
            evaluate_list_similarity(None, 2, method="MSE")
        with self.assertRaises(TypeError):
            evaluate_list_similarity("string", 2, method="MSE")

    def test_invalid_element_type(self):
        """
        测试列表中含有无效元素类型。
        """
        with self.assertRaises(TypeError):
            evaluate_list_similarity([1, 2, "a"], 2, method="MSE")

    def test_invalid_n_type(self):
        """
        测试传入无效的 n 类型。
        """
        with self.assertRaises(TypeError):
            evaluate_list_similarity([1, 2, 3], "string", method="MSE")

    def test_invalid_method(self):
        """
        测试传入无效评分方法的情况。
        """
        with self.assertRaises(ValueError):
            evaluate_list_similarity([1, 2, 3], 2, method="INVALID_METHOD")


class TestCheckUnique(unittest.TestCase):
    def test_unique_elements(self):
        """
        测试所有元素唯一的情况。
        """
        data = [[1, 2, 3], [4, 5, 6]]
        self.assertTrue(check_unique(data))

    def test_non_unique_elements(self):
        """
        测试存在重复元素的情况。
        """
        data = [[1, 2, 3], [3, 4, 5]]
        self.assertFalse(check_unique(data))

    def test_empty_list(self):
        """
        测试空二维列表的情况。
        """
        data = []
        self.assertTrue(check_unique(data))  # 空列表视为唯一

    def test_empty_sublist(self):
        """
        测试包含空子列表的情况。
        """
        data = [[], [1, 2, 3]]
        self.assertTrue(check_unique(data))  # 仅有非空子列表，所以视为唯一

    def test_empty_and_non_empty_sublists(self):
        """
        测试包含空子列表和非空子列表的情况。
        """
        data = [[], [1, 1, 2]]
        self.assertFalse(check_unique(data))  # 含有重复元素

    def test_invalid_input_type(self):
        """
        测试传入非法输入类型的情况。
        """
        with self.assertRaises(TypeError):
            check_unique(123)  # 不是列表
        with self.assertRaises(TypeError):
            check_unique([[1, 2], 3])  # 第二个元素不是列表
        with self.assertRaises(TypeError):
            check_unique([[1, 2], [3, [4]]])  # 内部元素不是整数或浮点数


if __name__ == "__main__":
    unittest.main()
