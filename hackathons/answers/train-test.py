# Perform the train test split on the data to create X_train, X_test, y_train, y_test

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=111)


# Check the shape of X_train, X_test, y_train and y_test

print('Shape of X_train and y_train', X_train.shape, y_train.shape)
print('Shape of x_test and y_test', X_test.shape, y_test.shape)


# Use series.value_counts(normalize=True) on both y_train and y_test 
# to check that the proportion of bads remained the same for each sample.

y_train.value_counts(normalize=True)
print('Percentage of bads in the train data:', y_train.value_counts(normalize=True).round(5)[1])
print('Percentage of bads in the test data:', y_test.value_counts(normalize=True).round(5)[1])