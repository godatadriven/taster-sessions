# get X and y
X, y = get_Xy(bikes_inferred, onehotencoding = ['weekday', 'season'])

# train models
lm = train_model(X, y, linear_model)
rf = train_model(X, y, forest_model)
