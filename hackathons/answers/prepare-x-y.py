# Split the data into X and y where X is the feature matrix and y is the target (bad_flag)

features = ['rev_unsecured', 'days_past_due_30', 'debt_ratio', 'income',
       'num_credit', 'num_days_late', 'num_realestate', 'days_past_due_60',
       'num_deps']
X = credit.loc[:, features]
y = credit.loc[:, 'bad_flag']


# Check the shape of X and y. You should see (150000, 5) and (150000,)

X.shape, y.shape


# Perform a value_counts() on y to see how many bad_flags of 1 there are. Use normalize=True to see this as a percentage.

y.value_counts(normalize=True)