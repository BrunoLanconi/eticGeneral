# Challenge 05: Transforming

Use the `pandas` library to transform the data from the Cafe Rewards Offers dataset.

## Materials

- [Cafe Rewards Offers Data](https://maven-datasets.s3.amazonaws.com/Cafe+Rewards+Offers/Cafe+Rewards+Offers.zip)

**Note**: Use the `offers.csv` file.

## Challenge

- Load the file into a DataFrame.
- Filter the DataFrame to show only the `bogo` offers.
- Create a new column called `total_reward` that multiplies the `reward` by the `difficulty`.
- Create a new column called `reward_per_day` that divides the `total_reward` by the `duration`.
- Save the transformed DataFrame to a new CSV file.
- Plot.

### Godlike Mode

- Create a Makefile to automate the process of loading, transforming, and saving the data.
- Create an API and a `/offers` endpoint to return the transformed data.
