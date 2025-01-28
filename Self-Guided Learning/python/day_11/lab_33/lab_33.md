# Lab 33: Pandas

In this lab, you will learn how to transform data using the Pandas library. You will read a CSV file into a DataFrame and perform various operations on the data.

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

3. Create a function called `filter_data` that filters the rows where the `Salary` column is greater than 50000.

```python
def filter_data(df: pd.DataFrame) -> pd.Series:
    """
    Filter the given DataFrame based on the condition that the "Salary" column is greater than 50000.

    Parameters:
        df (pandas.DataFrame): The input DataFrame to be filtered.

    Returns:
        pandas.Series: The filtered DataFrame.
    """
    df_slice = df[df["Salary"] > 50000]
    new_df = (
        df_slice.copy()
    )  # This is important to avoid modifying the original DataFrame

    return new_df

filtered_df = filter_data(df)
filtered_df
```

4. Create a function called `select_columns` that selects the `Name`, `Age`, and `Salary` columns.

```python
def select_columns(df: pd.DataFrame) -> pd.Series:
    """
    Selects specific ["Name", "Age", "Salary", "Country"] columns from a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.Series: A new DataFrame containing only the selected columns.
    """
    df_slice = df[["Name", "Age", "Salary", "Country"]]
    new_df = df_slice.copy()

    return new_df

selected_df = select_columns(df)
selected_df
```

5. Let's create a function to use with the `apply()` function. Create a function called `calculate_bonus` that calculates a bonus of 10% for each employee.

```python
def calculate_bonus(salary: float) -> float:
    """
    Calculate the bonus based on the given salary.

    Parameters:
    salary (float): The salary of the employee.

    Returns:
    float: The calculated bonus.
    """
    return salary * 0.1

selected_df['Bonus'] = selected_df['Salary'].apply(calculate_bonus)
selected_df
```

You should see a new column called `Bonus` with the calculated bonus for each employee.

```text
        Name  Age  Salary Country    Bonus
1      RIICE   25   38456     USA   3845.6
2      TYPIU   21   52064  France   5206.4
3      YZHCD   54   61916     USA   6191.6
```

6. Let's substitute the `Country` column with the full country name. Create a function called `get_country_name` that receives the country code and returns the full country name.

```python
def get_country_name(country_code: str) -> str:
    """
    Returns the name of a country based on its country code.

    Args:
        country_code (str): The country code.

    Returns:
        str: The name of the country corresponding to the country code. If the country code is not found, 'Unknown' is returned.
    """
    countries = {
        'USA': 'United States',
        'France': 'France'
    }
    return countries.get(country_code, 'Unknown')

selected_df['Country'] = selected_df['Country'].apply(get_country_name)
selected_df
```

We may use the `map()` function to achieve the same result.

```python
selected_df['Country'] = selected_df['Country'].map({
    'USA': 'United States',
    'France': 'France'
})
selected_df
```

7. Finally, let's save the DataFrame to a new CSV file called `new_output.csv`.

```python
selected_df.to_csv('new_output.csv', index=True)
```