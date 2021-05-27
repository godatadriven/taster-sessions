# 1. How many missing values are there in the data?

bikes.isnull().sum()


# 2. What is the earliest and latest date (min/max) in the data?

bikes.index.min(), bikes.index.max()


# 3. Which year was the most humid on average (mean)?

(
    bikes
    .groupby(bikes.index.year)
    ['temp']
    .mean()
)

# 4. Plot the amount of bikes (cnt) (Extra: by month) - how does the amount of bikes being rented change between 2011 and 2012?

(
    bikes['cnt']
    .groupby([bikes.index.month, bikes.index.year])
    .sum()
    .unstack()
    .plot()
)