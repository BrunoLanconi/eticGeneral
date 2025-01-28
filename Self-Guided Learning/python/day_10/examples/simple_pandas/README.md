# Simple Pandas

This directory contains a simple example of using Pandas to read a CSV file and display the data.

## Commands

```bash
generate-csv                   Generate CSV file
help                           Show help
jupyter                        Run Jupyter notebook
sample                         Run sample
transform                      Run transform
```

**Note**: For Pandas samples refer to the `src.notebooks.pandas.ipynb` notebook.

---

## [Pandas](https://pandas.pydata.org/docs/)

Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and data manipulation library built on top of the Python programming language.

---

## [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.

### Example
```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

print(df)
```

---

## [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)

A Series is a one-dimensional labeled array capable of holding data of any type.

### Example
```python
import pandas as pd

data = [1, 2, 3, 4, 5]
s = pd.Series(data)

print(s)
```
