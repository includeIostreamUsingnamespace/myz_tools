# myz_tools

[![PyPI version](https://img.shields.io/pypi/v/myz_tools.svg)](https://pypi.org/project/myz_tools/)
[![Python](https://img.shields.io/pypi/pyversions/myz_tools.svg)](https://pypi.org/project/myz_tools/)
[![License](https://img.shields.io/github/license/includeIostreamUsingnamespace/myz_tools.svg)](https://github.com/includeIostreamUsingnamespace/myz_tools)

A lightweight Python utility library: **commonly used algorithm helpers** + **automatic Markdown documentation generation from Python source code**.

It wraps algorithms you'd otherwise have to type out by hand (like IQR-based outlier removal) into ready-to-use functions — pass in your raw data, get clean results back.

## Installation

```bash
pip install myz_tools
```

## Quick Start

### Doc generation: turn source code into docs with one line

```python
from myz_tools.source2md import dir2md

dir2md("./your_directory")
```

`dir2md` automatically scans all Python files in the directory and generates documentation. Compared to Sphinx, it requires far less setup and gets you results faster.

Full signature:

```python
dir2md(source_dir, output_dir="./MD/", single_file=True)
```

- `source_dir` — directory containing the Python files to process
- `output_dir` — where the generated docs are saved (default: `./MD/`)
- `single_file` — merge everything into one `.md` file (`True`), or output one file per module (`False`)

### Algorithm helpers: call them directly

```python
from myz_tools.common_maths import remove_outliers_iqr

cleaned, valid_idx = remove_outliers_iqr(data)
```

## API Overview

### Algorithm module: `common_maths.py`

| Function                        | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| `create_dir`                    | Create a folder at the specified path                        |
| `get_max_diff`                  | Return the difference between max and min values per column of a 2D array |
| `remove_outliers_iqr`           | Remove outliers column-wise using the IQR method; returns cleaned data and valid row indices |
| `export_to_csv`                 | Save a 2D array to CSV; appends if the file already exists   |
| `generate_2d_combinations_iter` | Given a 3D array, lazily generate all element combinations of each 2D array |
| `generate_row_permutations`     | Generate all row permutations of a 2D array                  |
| `calculate_total_permutations`  | Calculate the total number of row-permutation combinations of a 2D array |
| `display_combinations`          | Print the first N combinations to verify generation results  |
| `evaluate_list_similarity`      | Evaluate how close list elements are to a target value (supports MSE / MAE / total_score) |
| `check_unique`                  | Check whether all elements in a 2D array are unique          |

### Doc generation module: `source2md.py`

| Function                          | Description                                                |
| --------------------------------- | ---------------------------------------------------------- |
| `dir2md`                          | Process an entire directory and generate docs in batch     |
| `extract_info`                    | Parse a Python file and extract function/class information |
| `all_save_markdown`               | Save extracted information as Markdown files               |
| `all2md`                          | Single-file version: extract info and save as Markdown     |
| `extract_function_docs_from_file` | Extract all function docstrings from a file                |
| `save_docs_to_markdown`           | Save a docstring dictionary to a Markdown file             |
| `pyFun2md`                        | Extract docstrings and save as Markdown in one step        |

> Full parameters, return values, and examples are available in each function's docstring — hover in your IDE to view them.

## Changelog

### v0.2.0

Added 6 new functions:

- `generate_2d_combinations_iter`
- `generate_row_permutations`
- `calculate_total_permutations`
- `display_combinations`
- `evaluate_list_similarity`
- `check_unique`

## Feedback & Contributing

Questions or algorithm requests? Feel free to open an [Issue](https://github.com/includeIostreamUsingnamespace/myz_tools/issues) — every one will be addressed.
