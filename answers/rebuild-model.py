# get X and y
X, y = get_Xy(bikes_date_features, dummy_cols = ['weekday', 'season'])

# train models
lm = train_model(X, y, linear_model)
rf = train_model(X, y, forest_model)