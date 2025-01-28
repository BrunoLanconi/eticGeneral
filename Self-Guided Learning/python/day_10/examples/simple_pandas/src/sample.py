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
