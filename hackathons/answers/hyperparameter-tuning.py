
# Use GridSearchCV() to search across the different model parameters

pipeline_dt.get_params()
from sklearn.model_selection import GridSearchCV

model_parameters = { 
    'model__max_depth': [4, 7, 10, 12],
    'model__max_features': [None, "auto", "sqrt", "log2"],
    'model__min_samples_leaf': [1, 2],
    'model__min_samples_split': [2, 3, 4],
}

grid = GridSearchCV(pipeline_dt, model_parameters)

grid.fit(X_train, y_train)

print(grid.best_params_, grid.best_score_)

# Use grid.score(X, y) to find the accuracy score on your train and test data.

print(grid.score(X_train, y_train), grid.score(X_test, y_test))


# Make a dataframe from the cv_results_ from your grid and sort_values() by rank_test_score to see the best models and their parameters.

cv_results = pd.DataFrame(grid.cv_results_)
cv_results.sort_values('rank_test_score').head(6)