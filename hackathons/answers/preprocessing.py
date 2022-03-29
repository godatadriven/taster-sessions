# Check to see if there are any categorical features or missing values in the data.

X.dtypes


# Now check to see if there is any missing data.

X.isnull().sum()


# Let's do a little analysis on both these columns (mean and size used in .agg() to show the count also)
print(credit['num_deps'].mean())

(
    credit
    .groupby('num_deps', dropna=False)['bad_flag']
    .agg(['mean','size'])
    .sort_index()
)



# Now let's look into the income column (fillna used to move NaN values to top of value_counts)
print(credit['income'].mean())

(
    credit
    .assign(income_round = lambda df: df['income'].round(-3).fillna(-1))
    .groupby('income_round', dropna=False)['bad_flag']
    .agg(['mean','size'])
    .sort_index()
    .head(15)
)