 

 

 

 

# [myz_tools] Python Library myz_tools: Automatic Algorithm and Documentation Generation for Python - Version 0.2.0 updated



[toc]

 

 

 

The # 0.2.0 update follows

 

6 functions added

 

The updates are as follows

 

\#### Function generate_2d_combinations_iter

 

\```

Functions:

Pass in a three-dimensional array and return an iterator of all combinations of elements of each two-dimensional array. If the 'test_first_group' parameter is set to True,

Returns only the combination of the first two-dimensional array.

 

Parameters:

data_3d (list): A three-dimensional list where each element is a two-dimensional list representing multiple two-dimensional arrays.

test_first_group (bool): Whether to generate a combination of only the first 2D array. Defaults to False.

 

Return value:

generator: A generator object that generates all combinations of elements of each two - dimensional array on demand.

 

Exception:

ValueError: This throws an exception if the input data is not a 3D list.

 

Examples:

\>>> data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

\>>> result_iter = generate_2d_combinations_iter(data) >>> for combinations in result_iter:

\# Each fetch is a combination of two dimensional lists

... print(list(combinations)) # [(1, 3), (1, 4), (2, 3), (2, 4)] Next time

[(5, 7), (5, 8), (6, 7), (6, 8)]



 

 

 

 

\>>> result_iter = generate_2d_combinations_iter(data,test_first_group=True) >>> print(list(next(result_iter)))

[(1, 3), (1, 4), (2, 3), (2, 4)] ```

\#### function generate_row_permutations

 

\```

Functions:

Pass in a two-dimensional array and return all possible permutations of the elements in each row of the two-dimensional array.

 

 

Parameters:

data_2d (list): A two-dimensional list representing multiple rows of data.

 

Return value:

generator: A generator object that generates all permutations of each row on demand and combines them into a two-dimensional array.

 

Exception:

ValueError: This throws an exception if the input 2-D array is empty or if a row is empty.

 

Example:

\>>> data = [[1, 2], [3, 4]]

\>>> permutations = generate_row_permutations(data) >>> for perm in permutations:

... print(perm) [[1, 2], [3, 4]] [[1, 2], [4, 3]] [[2, 1], [3, 4]]

[[2, 1], [4, 3]] ```

\#### function calculate_total_permutations

 

\```

Functions:

Calculate and return the total number of permutations and combinations of all rows in a two-dimensional array.

 

Parameters:

data_2d (list): A two-dimensional list representing multiple rows of data.



 

 

 

 

Return value:

int: The total number of all combinations of row permutations.

 

Exception:

ValueError: This throws an exception if the input 2-D array is empty or if a row is empty.

 

Example:

\>>> data = [[1, 2], [3, 4]]

\>>> total = calculate_total_permutations(data) >>> print(total)

4 ```

\#### function display_combinations

 

\```

Functions:

Print the first N permutations in a two-dimensional array to check the correctness of the combination generation.

 

Parameters:

data_2d (list): A two-dimensional list representing multiple rows of data. N (int): The number of combinations to print, which defaults to 5.

 

Return value: None

 

Anomaly:

ValueError: This throws an exception if the input 2-D array is empty or if a row is empty.

 

Example:

\>>> data = [[1, 2], [3, 4]]

\>>> display_combinations(data, N=2) [1, 2]

[3, 4]

 

[1, 2]

[4, 3] ```

\#### function evaluate_list_similarity

 

The various scoring methods of the 'evaluate_list_similarity' function can be interpreted as a form of "smaller is better".



 

 

 

 

 

\1. ** Mean Squared Error (MSE)** :

\- * * * * formula: $$\ text = {MSE} \ frac {1} {m} \ sum_ {I = 1} ^ {m} (d_i - n) ^ 2 $$

\- ** Explanation **: Calculate the average of the squared differences of all differences and the target value 'n'. The mean squared error penalizes larger differences more severely, with

smaller scores indicating that the list element is closer to the target value.

 

\2. ** Mean Absolute Error ** :

\- * * * * formula: $$\ text MAE {} = \ frac {1} {m} \ sum_ {I = 1} ^ {m} | d_i -n | $$

\- ** Explanation **: Calculate the average of the absolute differences between all differences and the target value 'n'. Compared to the mean squared error, the mean absolute error penalizes all differences equally. A smaller score indicates that the list element is closer

to the target value.

 

\3. ** Total Score ** :

\- * * * * formula: $$\ text {Total Score} = \ sum_ {I = 1} ^ {m} | d_i -n | $$

\- ** Explanation **: Calculate the sum of absolute differences between all differences and the target value 'n'. The total score directly reflects the cumulative degree of all the differences.

A smaller score indicates that the list element is closer to the target value.

 

 

 

\```

Features:

Evaluate how close the difference between items in the list is to a given value 'n'. Different scoring methods are supported, such as mean squared error (MSE), absolute error, etc.

In all three cases, a smaller score indicates that the list element is closer to the target value

Parameters:

lst (list of int/float): A list of numbers to evaluate.

n (int/float): A reference value for comparison, a target value for calculating differences.

method (str): The scoring method selected. Support 'MSE' (mean squared error), 'MAE' (Mean absolute error), 'total_score' (total score), etc.

 

Return value:

float: The calculated rating value.

 

Anomaly:

ValueError: Throws an exception if the input 'lst' is not a list or 'n' is not an integer or float.

TypeError: Throws an exception if the element in 'lst' is not an integer or float.

ValueError: Throws an exception if the selected scoring method is not supported.

 

Example:



 

 

 

 

\>>> lst = [1, 3, 6, 10] >>> n = 2

\>>> score = evaluate_list_similarity(lst, n, method='MSE') >>> print(score)

 

\>>> score = evaluate_list_similarity(lst, n, method='MAE') >>> print(score)

\```

\#### function check_unique

 

\```

Functions:

Checks whether each element of the passed two-dimensional array is unique. If all elements are unique, return True; Otherwise, False is returned.

 

Parameters:

data (list of list): A two-dimensional list containing the elements to check.

 

Return value:

bool: This returns True if all elements are unique Otherwise, False.

 

Exception:

TypeError: An exception is thrown if the input 'data' is not a two-dimensional list, or contains elements that are not a list.

 

Example:

\>>> data = [[1, 2, 3], [4, 5, 6]] >>> check_unique(data)

True

 

\>>> data = [[1, 2, 3], [3, 4, 5]] >>> check_unique(data)

False

\``` *** ##

 

 

****************************



 

 

 

 

\# Write in front

 

Originally, I just wanted to sort out the various algorithms I used frequently, and some helper functions, so that I could quickly develop them in a short time. Later, I found that it was more convenient to organize into a library, so I simply made it into a library, which can be installed and used directly through pip install

 

\# About Libraries

 

Most of the various algorithms you usually see still need to be typed manually, such as the interquartile range method, and you have to change the code after knowing the principle, simply make it directly into a function, directly pass the original data, and return the cleaned data. Internal code has also been open source, but also done a few rounds of testing, so do not worry about what strange bugs will appear, of course, if there are, please put forward

 

\# Using the library  Installation methods

\```

pip install myz_tools ```

Once installed, it works

 

At present, there are two main parts, an algorithm, and a function for converting python files into documents, which is also very convenient to use. It supports custom directories and specifying output to an md or different md files that are transformed respectively. Although Sphinx can be used, I still look forward to finding a more concise way to solve the problem quickly

 

The usage is as follows.

 

\```

from myz_tools.source2md import dir2md

 

dir2md("./ directory to be processed ") ```

 

 

 

dir2md will automatically check all the python files in this directory and generate documentation. The full parameters can be mouseover to view



 

 

 

 

!                   [image-20240815105239302](https://gitee.com/include_ios/picture - collection/raw/master/images/image-20240815105239302.png )

 

 

 

************

\# Directory of all functions in the library

 

 

 

\# File name: common_maths.py

 

*** ***

\## Functions section:

 

\#### Function create_dir

 

\```

Create a folder with the name {dir_name} in the specified path Args:

dir_name: folder name

path: The path to create the folder, defaults to the current path

 

Returns:

There is no

\```

\#### function get_max_diff

 

\```

Parameters:

two_dimensional_array: A two-dimensional array Return value:

The difference between the maximum and minimum values in each column, as a one -

dimensional array Features:

Passed a two-dimensional  array, the function returns the difference between the maximum and minimum values in each column.

\```



 

 

 

 

\#### Function remove_outliers_iqr

 

\```

Parameters:

data: Two-dimensional array Return value:

Two-dimensional array with outliers removed and valid row index, and type is a tuple Features:

The interquartile range method removes outliers from the passed two-dimensional array, noting that it is its own outlier for each column

\```

\#### function export_to_csv

 

\```

Parameters:

array_data: A two-dimensional array of the data to hold

file_name: String, the name of the CSV file (without extension)

output_directory: String, the directory path to save the file, defaults to the current directory

Return:

None Features:

Saves the given two-dimensional array to a CSV file in the specified directory. If the file already exists, append the data and add a blank line as a separator on each write.

\```

\#### Function generate_2d_combinations_iter

 

\```

Functions:

Pass in a three-dimensional array and return an iterator of all combinations of the elements of each two-dimensional array. If the 'test_first_group' parameter is set to True,

Returns only the combination of the first two-dimensional array.

 

Parameters:

data_3d (list): A three-dimensional list where each element is a two-dimensional list representing multiple two-dimensional arrays.

test_first_group (bool): Whether to generate a combination of only the first 2D array. Defaults to False.

 

Return value:

generator: A generator object that generates all combinations of elements of each two - dimensional array on demand.



 

 

 

 

 

Exception:

ValueError: This throws an exception if the input data is not a 3D list.

 

Example:

\>>> data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

\>>> result_iter = generate_2d_combinations_iter(data) >>> for combinations in result_iter:

\# Each fetch is a combination of two dimensional lists ... print(list(combinations)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

Next time

[(5, 7), (5, 8), (6, 7), (6, 8)]

 

 

\>>> result_iter = generate_2d_combinations_iter(data,test_first_group=True) >>> print(list(next(result_iter)))

[(1, 3), (1, 4), (2, 3), (2, 4)] ```

\#### function generate_row_permutations

 

\```

Functions:

Pass in a two-dimensional array and return all possible permutations of the elements in each row of the two-dimensional array.

 

 

Parameters:

data_2d (list): A two-dimensional list representing multiple rows of data.

 

Return value:

generator: A generator object that generates all permutations of each row on demand and combines them into a two-dimensional array.

 

Exception:

ValueError: This throws an exception if the input 2-D array is empty or if a row is empty.

 

Example:

\>>> data = [[1, 2], [3, 4]]

\>>> permutations = generate_row_permutations(data) >>> for perm in permutations:

... print(perm) [[1, 2], [3, 4]] [[1, 2], [4, 3]]



 

 

 

 

[[2, 1], [3, 4]]

[[2, 1], [4, 3]] ```

\#### function calculate_total_permutations

 

\```

Functions:

Calculate and return the total number of permutations and combinations of all rows in a two-dimensional array.

 

Parameters:

data_2d (list): A two-dimensional list representing multiple rows of data.

 

Return value:

int: The total number of all combinations of row permutations.

 

Exception:

ValueError: This throws an exception if the input 2-D array is empty or if a row is empty.

 

Example:

\>>> data = [[1, 2], [3, 4]]

\>>> total = calculate_total_permutations(data) >>> print(total)

4 ```

\#### function display_combinations

 

\```

Functions:

Print the first N permutations in a two-dimensional array to check the correctness of the combination generation.

 

Parameters:

data_2d (list): A two-dimensional list representing multiple rows of data. N (int): The number of combinations to print, which defaults to 5.

 

Return value: None

 

Anomaly:

ValueError: This throws an exception if the input 2-D array is empty or if a row is empty.



 

 

 

 

Example:

\>>> data = [[1, 2], [3, 4]]

\>>> display_combinations(data, N=2) [1, 2]

[3, 4]

 

[1, 2]

[4, 3] ```

\#### function evaluate_list_similarity

 

\```

Functions:

Evaluate how close the difference between items in the list is to a given value 'n'. Different scoring methods are supported, such as mean squared error (MSE), absolute error, etc.

In all three cases, a smaller score indicates that the list element is closer to the target value

Parameters:

lst (list of int/float): A list of numbers to evaluate.

n (int/float): A reference value for comparison, a target value for calculating differences.

method (str): The scoring method selected. Support 'MSE' (mean squared error), 'MAE' (Mean absolute error), 'total_score' (total score), etc.

 

Return value:

float: The calculated rating value.

 

Anomaly:

ValueError: Throws an exception if the input 'lst' is not a list or 'n' is not an integer or float.

TypeError: Throws an exception if the element in 'lst' is not an integer or float.

ValueError: Throws an exception if the selected scoring method is not supported.

 

Example:

\>>> lst = [1, 3, 6, 10] >>> n = 2

\>>> score = evaluate_list_similarity(lst, n, method='MSE') >>> print(score)

 

\>>> score = evaluate_list_similarity(lst, n, method='MAE') >>> print(score)

\```

\#### function check_unique



 

 

 

 

 

\```

Functions:

Checks whether each element of the passed two-dimensional array is unique. If all elements are unique, return True; Otherwise, False is returned.

 

Parameters:

data (list of list): A two-dimensional list containing the elements to check.

 

Return value:

bool: True if all elements are unique; Otherwise, False.

 

Exception:

TypeError: An exception is thrown if the input 'data' is not a two-dimensional list, or contains elements that are not a list.

 

Example:

\>>> data = [[1, 2, 3], [4, 5, 6]] >>> check_unique(data)

True

 

\>>> data = [[1, 2, 3], [3, 4, 5]] >>> check_unique(data)

False

\``` ***

\## Class part: ***

\# Filename: source2md.py ***

***

\## Functions section:  #### Function dir2md

\```

Args:



 

 

 

 

source_dir: The directory to be processed output_dir: The output directory

single_file: Whether to put all files into a single md file ```

\#### function extract_info

 

\```

Functions:

Parse python files to extract function and class information Args:

file_path: The path of the file to be processed Returns:

function_docs: Function information

class_info: Class information ```

\#### function all_save_markdown

 

\```

Functions:

Save the extracted function and class information as markdown files Args:

file_path: The path of the file to be processed output_path: The save path

function_docs: function information

class_info: Class information Returns:

There is no ```

\#### function all2md

 

\```

Function: Call to extract function and class information from a python file and save it as a

markdown file Args:

file_path: String, the path to the python file

output_path: String, the path to save the markdown file Returns:

There is no ```

\#### function extract_function_docs_from_file



 

 

 

 

 

\```

Extract the docstring (comment section) of the function from the Python file.

 

Parameters:

file_path: String, the path to the Python file.

 

Returns:

Dictionary with the function name as key and the function docstring as value. ```

\#### function save_docs_to_markdown

 

\```

Save the function's docstring to a Markdown file.

 

Parameters:

docs: dictionary that contains a mapping of function names and docstrings. output_path: String, the path to save the Markdown file.

\```

\#### function pyFun2md

 

\```

Extract docstring from Python file and save as Markdown file.

 

Parameters:

source_file: String, the path to the source Python file.

output_md: String, the path to the output Markdown file.

\``` *** ## ***

\# The link to the repository

 

If you have any questions or need any other algorithms, feel free to mention the Issues and I will go through them one by one

 

\# END



 

 

 

 

***
