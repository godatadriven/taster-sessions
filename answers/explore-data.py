
# 1

print('1. How many missing values are there in the data?',
      bikes.isnull().sum().sum(), sep='\n')


# 2

print('\n2. What is the earliest and latest date (min/max) in the data?', 
      f'Min: {bikes.index.min().date()}', f'Max"{bikes.index.max().date()}', sep='\n')


# 3

print('\n3. Which year was the most humid on average (mean)?', 
      (
          bikes
          .groupby(bikes.index.year)
          ['temp']
          .mean()
      ), sep='\n')

# 4

print('\n4. Plot the amount of bikes (cnt) (Extra: by month) - how does the amount of bikes being rented change between 2011 and 2012?',
      (
          bikes['cnt']
          .groupby([bikes.index.month, bikes.index.year])
          .sum()
          .unstack()
          .plot()
      ), sep='\n')