import matplotlib.pyplot as plt # for the bonuses

# 1. What are the data types of each column?

credit.dtypes


# 2. Use .value_counts() to find out how many customers have no dependents.

credit['num_deps'].value_counts()


# 3. Use groupby to find the mean value for all the features when split (groupby) the bad_flag

credit.groupby('bad_flag').mean()


# 4. What is the bad rate (mean bad_flag) when grouped by age? 

fig, ax_bad = plt.subplots()

credit.groupby('age')['bad_flag'].mean().sort_index().plot(color='orange', ax=ax_bad)


# 5. What is the average income by age? 

fig, ax_income = plt.subplots()

credit.groupby('age')['income'].mean().sort_index().plot(ax=ax_income)