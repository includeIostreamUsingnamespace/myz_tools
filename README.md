# myz_tools

[![PyPI version](https://img.shields.io/pypi/v/myz_tools.svg)](https://pypi.org/project/myz_tools/)
[![Python](https://img.shields.io/pypi/pyversions/myz_tools.svg)](https://pypi.org/project/myz_tools/)
[![License](https://img.shields.io/github/license/includeIostreamUsingnamespace/myz_tools.svg)](https://github.com/includeIostreamUsingnamespace/myz_tools)

A lightweight Python utility library focused on two things: **combinatorics & data-cleaning algorithms** and **automatic Markdown documentation generation from Python source code**.

## Installation

```bash
pip install myz_tools
```

## Highlights

### Source code → Markdown docs, in one line

```python
from myz_tools.source2md import dir2md

dir2md("./your_directory")
```

`dir2md` scans every Python file in a directory, parses function/class docstrings, and generates structured Markdown documentation — a much lighter alternative to Sphinx.

```python
dir2md(source_dir, output_dir="./MD/", single_file=True)
```

- `source_dir` — directory containing the Python files to process
- `output_dir` — where the generated docs are saved (default: `./MD/`)
- `single_file` — merge everything into one `.md` file (`True`), or output one file per module (`False`)

### IQR-based outlier removal

Column-wise outlier detection using the interquartile range method. Pass in raw data, get back clean data plus the valid row indices:

```python
from myz_tools.common_maths import remove_outliers_iqr

cleaned, valid_idx = remove_outliers_iqr(data)
```

### Lazy combinatorial generation

Generate all combinations across groups of 2D arrays on demand — memory-friendly even when the full combination space is huge:

```python
from myz_tools.common_maths import generate_2d_combinations_iter

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
for combo in generate_2d_combinations_iter(data):
    print(list(combo))
# [(1, 3), (1, 4), (2, 3), (2, 4)]
# [(5, 7), (5, 8), (6, 7), (6, 8)]
```

### Row permutations of a 2D array

```python
from myz_tools.common_maths import generate_row_permutations, calculate_total_permutations

data = [[1, 2], [3, 4]]
print(calculate_total_permutations(data))  # 4

for perm in generate_row_permutations(data):
    print(perm)
# [[1, 2], [3, 4]]
# [[1, 2], [4, 3]]
# [[2, 1], [3, 4]]
# [[2, 1], [4, 3]]
```

### List-to-target similarity scoring

Evaluate how close list elements are to a target value, with multiple metrics — smaller is better:

$$
\mathrm{MSE} = \frac{1}{m}\sum_{i=1}^{m}(d_i - n)^2
\qquad
\mathrm{MAE} = \frac{1}{m}\sum_{i=1}^{m}|d_i - n|
$$

```python
from myz_tools.common_maths import evaluate_list_similarity

score = evaluate_list_similarity([1, 3, 6, 10], n=2, method="MSE")
# method also supports "MAE" and "total_score"
```

## Changelog

### v0.2.0

Added 6 functions: `generate_2d_combinations_iter`, `generate_row_permutations`, `calculate_total_permutations`, `display_combinations`, `evaluate_list_similarity`, `check_unique`.

## Feedback & Contributing

Questions or algorithm requests? Feel free to open an [Issue](https://github.com/includeIostreamUsingnamespace/myz_tools/issues).
