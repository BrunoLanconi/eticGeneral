# Lab 34: Plotting

In this lab, you will learn how to plot data using the Pandas library.

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

**Note**: Use the `day_010/examples/simple_pandas/inputs/employees.csv`.

```csv
Name,Age,Gender,Department,Salary,Email,Phone,Address,City,State,Country,Postal Code
RIICE,25,Male,Marketing,38456,riice@company.com,7422226190,LH4C3OND9W,Paris,CA,USA,01917
TYPIU,21,Female,Finance,52064,typiu@company.com,8536498679,GP48VP6RY7,New York,FL,France,99421
YZHCD,54,Female,Finance,61916,yzhcd@company.com,3771788777,Q7M0ZD88I7,London,CA,USA,89675
...
```

3. Plot the `Salary` column using a histogram.

```python
df['Salary'].plot(kind='hist')
```

4. Plot the `Salary` column using a boxplot.

```python
df['Salary'].plot(kind='box')
```

5. Plot the `Salary` column using a bar chart.

```python
df['Salary'].plot(kind='bar')
```

6. Group the data by `Department` and plot the `Salary` column using a bar chart.

```python
df.groupby('Department')['Salary'].sum().plot(kind='bar')
```

7. Group the data by `Department` and plot the `Salary` column using a pie chart.

```python
df.groupby('Department')['Salary'].sum().plot(kind='pie')
```

8. Save the plots to a file.

```python
df['Salary'].plot(kind='hist').get_figure().savefig('histogram.png')
df['Salary'].plot(kind='box').get_figure().savefig('boxplot.png')
df['Salary'].plot(kind='bar').get_figure().savefig('bar_chart.png')

df.groupby('Department')['Salary'].sum().plot(kind='bar').get_figure().savefig('grouped_bar_chart.png')
df.groupby('Department')['Salary'].sum().plot(kind='pie').get_figure().savefig('grouped_pie_chart.png')
```

9. Create a heatmap using the `Salary` and `Age` columns.

```python
import seaborn as sns

sns.heatmap(df[['Salary', 'Age']].corr(), annot=True)
```

10. Save the heatmap to a file.

```python
sns.heatmap(df[['Salary', 'Age']].corr(), annot=True).get_figure().savefig('heatmap.png')
```
