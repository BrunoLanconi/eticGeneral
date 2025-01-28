import pandas as pd  # type: ignore

df = pd.DataFrame(
    {
        "Name": ["RIICE", "TYPIU", "YZHCD"],
        "Age": [25, 21, 54],
        "Gender": ["Male", "Female", "Female"],
        "Department": ["Marketing", "Finance", "Finance"],
        "Salary": [38456, 52064, 61916],
        "Email": ["riice@company.com", "typiu@company.com", "yzhcd@company.com"],
        "Phone": [7422226190, 8536498679, 3771788777],
        "Address": ["LH4C3OND9W", "GP48VP6RY7", "Q7M0ZD88I7"],
        "City": ["Paris", "New York", "London"],
        "State": ["CA", "FL", "CA"],
        "Country": ["USA", "France", "USA"],
        "Postal Code": ["01917", "99421", "89675"],
    }
)


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


def calculate_bonus(salary: float) -> float:
    """
    Calculate the bonus based on the given salary.

    Parameters:
    salary (float): The salary of the employee.

    Returns:
    float: The calculated bonus.
    """
    return salary * 0.1


filtered_df = filter_data(df)
selected_df = select_columns(df)
selected_df["Bonus"] = selected_df["Salary"].apply(calculate_bonus)

print(selected_df)
# Output:
#     Name  Age  Salary Country   Bonus
# 0  RIICE   25   38456     USA  3845.6
# 1  TYPIU   21   52064  France  5206.4
# 2  YZHCD   54   61916     USA  6191.6

selected_df["Country"] = selected_df["Country"].map(
    {"USA": "United States", "France": "France"}
)

print(selected_df)
# Output:
#     Name  Age  Salary        Country   Bonus
# 0  RIICE   25   38456  United States  3845.6
# 1  TYPIU   21   52064         France  5206.4
# 2  YZHCD   54   61916  United States  6191.6
