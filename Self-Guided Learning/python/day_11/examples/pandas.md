# [Pandas](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)

In Python, we can work with data using the `pandas` library. `pandas` is a powerful data manipulation library that provides data structures and functions to work with structured data. It is built on top of `NumPy` and provides easy-to-use data structures like `Series` and `DataFrame` to work with tabular data.

---

## Reading Data

To read data from a file, we can use the `read_csv()` function of the `pandas` library. This function reads a CSV file and returns a `DataFrame` object.

### Example
```python
import pandas as pd

df = pd.read_csv('data.csv')
```

The `read_csv()` function takes the file path as an argument and returns a `DataFrame` object containing the data from the CSV file.

### Example
```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df)
```

You can also read data from other file formats like Excel, JSON, SQL, etc., using the corresponding functions provided by `pandas`, as `read_excel()`, `read_json()`, `read_sql()`, etc. Then, you can use the `head()`, `tail()`, `shape`, `columns`, `size`, and `len()` functions to get information about the `DataFrame`.

- `df.head()`: Returns the first 5 rows of the `DataFrame`.
- `df.tail()`: Returns the last 5 rows of the `DataFrame`.
- `df.shape`: Returns the shape of the `DataFrame` (number of rows and columns).
- `df.columns`: Returns the column names of the `DataFrame`.
- `df.size`: Returns the number of elements in the `DataFrame`.
- `len(df)`: Returns the number of rows in the `DataFrame`.

Once we have read the data, we can transform it using various functions provided by `pandas`. We can filter rows, select columns, group data, sort data, and perform various other operations on the `DataFrame`.

### Example
```csv
# data.csv

A,B,C
1,2,3
4,5,6
7,8,9
10,11,12
```

### Example
```python
import pandas as pd

df = pd.read_csv('data.csv')

# Filter rows where column 'A' is greater than 10
filtered_df = df[df['A'] > 10]

# Select columns 'A' and 'B'
selected_df = df[['A', 'B']]
```

In the example above, we read data from a CSV file, filtered rows where column 'A' is greater than 10, and selected columns 'A' and 'B' from the `DataFrame`. Reading/selecting data this way returns a new `DataFrame` with the filtered/selected data.

---

## Writing Data

To write data to a file, we can use the `to_csv()` function of the `pandas` library. This function writes a `DataFrame` object to a CSV file.

### Example
```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df.to_csv('output.csv', index=False)
```

The `to_csv()` function takes the file path as an argument and writes the `DataFrame` object to the specified file. The `index=False` argument specifies that we do not want to write the row index to the file.

### Example
```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

df.to_csv('output.csv', index=False)

print('Data written to output.csv')
```

You can also write data to other file formats like Excel, JSON, SQL, etc., using the corresponding functions provided by `pandas`, as `to_excel()`, `to_json()`, `to_sql()`, etc.

---

## Using Functions to Transform Data

`pandas` provides a wide range of functions to transform data in a `DataFrame`. We can use functions like `apply()`, `map()`, `groupby()`, `sort_values()`, `merge()`, etc., to transform and manipulate data in a `DataFrame`.

### Example
```python
import pandas as pd  # type: ignore

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})

# Apply a function to each element in column 'A'
df["A"] = df["A"].apply(lambda x: x * 2)

print(df)
# Output:
#    A  B  C
# 0  2  4  7
# 1  4  5  8
# 2  6  6  9

# Map values in column 'B' to new values
df["B"] = df["B"].map({4: "four", 5: "five", 6: "six"})

print(df)
# Output:
#    A     B  C
# 0  2  four  7
# 1  4  five  8
# 2  6   six  9

# Group data by column 'C' and calculate the sum of column 'A'
grouped_df = df.groupby("C")["A"].sum()

print(grouped_df)
# Output:
# C
# 7    2
# 8    4
# 9    6
# Name: A, dtype: int64

# Sort data by column 'B' in descending order
sorted_df = df.sort_values("B", ascending=False)

print(sorted_df)
# Output:
#    A     B  C
# 2  6   six  9
# 1  4  five  8
# 0  2  four  7

df_1 = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [7, 8, 9],
    }
)
df_2 = pd.DataFrame(
    {
        "A": [1, 2, 3],  # Same values as df_1
        "B": [7, 8, 9],
        "C": [10, 11, 12],
    }
)

# Merge two DataFrames into new DataFrame
merged_df = pd.merge(df_1, df_2, left_on=["A"], right_on=["A"])

print(merged_df)
# Output:
#    A  B_x  C_x  B_y  C_y
# 0  1    4    7    7   10
# 1  2    5    8    8   11
# 2  3    6    9    9   12

# Change column names
merged_df.columns = ["A", "B_1", "C_1", "B_2", "C_2"]

print(merged_df)
# Output:
#    A  B_1  C_1  B_2  C_2
# 0  1    4    7    7   10
# 1  2    5    8    8   11
# 2  3    6    9    9   12
```

In the example above, we applied a function to each element in column 'A', mapped values in column 'B' to new values, grouped data by column 'C' and calculated the sum of column 'A', and sorted data by column 'B' in descending order. These functions return a new `DataFrame` with the transformed data.

- `apply()`: Applies a function to each element in a column or row.
- `map()`: Maps values in a column to new values.
- `groupby()`: Groups data by a column and performs an operation on the grouped data.
- `sort_values()`: Sorts data by the values in a column.
- `merge()`: Merges two `DataFrame` objects based on a common column.

---

## [Plotting Data](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)

`pandas` provides functions to plot data in a `DataFrame`. We can use functions like `plot()`, `hist()`, `box()`, `bar()`, `pie()`, etc., to create different types of plots from the data in a `DataFrame`.

### Example
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Plot the 'Salary' column using a histogram
df['Salary'].plot(kind='hist')
plt.show()
```

In the example above, we read data from a CSV file, plotted the 'Salary' column using a histogram, and displayed the plot using `plt.show()`. `kind` specifies the type of plot to create and can be 'hist' for a histogram, 'box' for a boxplot, 'bar' for a bar chart, 'pie' for a pie chart, etc.

---

## Customizing Plots

We can customize the plots by setting various parameters like `title`, `xlabel`, `ylabel`, `color`, `legend`, etc., to make the plots more informative and visually appealing.

### Example
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Plot the 'Salary' column using a histogram
df['Salary'].plot(kind='hist', title='Salary Distribution', xlabel='Salary', ylabel='Frequency', color='blue')
plt.show()
```

- `title`: Sets the title of the plot.
- `xlabel`: Sets the label for the x-axis.
- `ylabel`: Sets the label for the y-axis.
- `color`: Sets the color of the plot.
- `legend`: Displays a legend for the plot.
- `grid`: Displays grid lines on the plot.
- `figsize`: Sets the size of the plot.
- `fontsize`: Sets the font size of the plot.

---

## Saving Plots

We can save the plots to a file using the `savefig()` function of the `matplotlib.pyplot` module. This function saves the current figure to a file in the specified format.

### Example
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Plot the 'Salary' column using a histogram
df['Salary'].plot(kind='hist')
plt.savefig('histogram.png')
```