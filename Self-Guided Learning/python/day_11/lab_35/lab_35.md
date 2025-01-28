# Lab 35: [Seaborn](https://seaborn.pydata.org/tutorial/introduction.html)

In this lab, you will learn how to enhance your plots using the Seaborn library.

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

**Note**: Use the `day_10/examples/simple_pandas/inputs/employees.csv`.

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

This is the usual way to plot a histogram using the Pandas library. Now, let's enhance this plot using the Seaborn library.

```python
import seaborn as sns

sns.histplot(df['Salary'])
```

4. Seaborn has a function called `displot` that combines the `histplot` and `kdeplot` functions. Use this function to plot the `Salary` column.

```python
sns.displot(df['Salary'])
```

5. Let's style the plot using Seaborn's built-in themes. Use the `set_theme` function to set the style to `darkgrid`.

```python
sns.set_theme(style='darkgrid')  # You may reset the style using sns.set_theme()

sns.displot(df['Salary'])
```

6. Seaborn has a function called `pairplot` that plots pairwise relationships in a dataset. Use this function to plot the pairwise relationships in the `df` DataFrame.

```python
sns.pairplot(df)
```

7. Seaborn has a function called `jointplot` that draws a plot of two variables with bivariate and univariate graphs. Use this function to plot the relationship between the `Salary` and `Age` columns.

```python
sns.jointplot(x='Salary', y='Age', data=df)
```

8. Let's style and add more information to the plot. Use the `kind` parameter to set the kind of plot to `hex`.

```python
sns.jointplot(x='Salary', y='Age', data=df, kind='hex')
```

9. Use the `marginal_kws` parameter to set the color of the marginal plots to `red`.

```python
sns.jointplot(x='Salary', y='Age', data=df, kind='hex', marginal_kws=dict(color='red'))
```

10. Save the plot to a file.

```python
sns.jointplot(x='Salary', y='Age', data=df, kind='hex', marginal_kws=dict(color='red')).savefig('jointplot.png')
```
