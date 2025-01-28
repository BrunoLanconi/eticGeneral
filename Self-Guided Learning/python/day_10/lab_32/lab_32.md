# Lab 22: Pandas Basics

In this lab, you will learn how to use the Pandas library to load CSV data into a DataFrame and perform basic operations on it.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

**Attention**: For a better experience, we recommend using the Google Colaboratory notebook or Jupyter notebook.

1. Create a new Jupyter notebook called `main.ipynb`.
2. Import the Pandas library and load the `data.csv` file into a DataFrame.

```python
import pandas as pd

df = pd.read_csv('data.csv')
df
```

**Note**: You may use the `day_10/examples/simple_pandas/inputs/employees.csv` or the CSV file you created in the lab 20 for the Optional Challenge.

3. Display the first five rows of the DataFrame.

```python
df.head()
```

4. Display the last five rows of the DataFrame.

```python
df.tail()
```

5. Display the shape of the DataFrame.

```python
df.shape
```

6. Display the columns of the DataFrame.

```python
df.columns
```

7. Display the data types of the columns in the DataFrame.

```python
df.dtypes
```

8. Display the summary statistics of the DataFrame.

```python
df.describe()
```

9. Display the unique values in the first column.

```python
df['column_name'].unique()
```

10. Display the number of unique values in the first column.

```python
df['column_name'].nunique()
```

11. Display the count of each unique value in the first column.

```python
df['column_name'].value_counts()
```

12. Display the sum of the values in the first column.

```python
df['column_name'].sum()
```

13. Display the mean of the values in the first column.

```python
df['column_name'].mean()
```

14. Display the median of the values in the first column.

```python
df['column_name'].median()
```

15. Display the maximum value in the first column.

```python
df['column_name'].max()
```