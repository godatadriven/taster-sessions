# Using the pipeline, access the model and then select the feature importances using

importances = pipeline_dt['model'].feature_importances_


# Convert this to a pandas series and then plot the data in a bar plot using

pd.Series(importances, index=features).sort_values().plot(kind='barh')


# Re-build the model using fewer features. Does this impact performance at all?

new_features = ['num_realestate', 'debt_ratio', 'income', 'num_credit', 'num_deps']
X = credit.loc[:, new_features]
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y, stratify=y, random_state=111)

column_imputer = ColumnTransformer([
        ('imp_deps', SimpleImputer(strategy='most_frequent'), ['num_deps']),
        ('imp_inc', SimpleImputer(strategy='mean'), ['income'])
    ],
    remainder='passthrough'
)

pipeline_fewer_features = Pipeline(steps = [
    ('imputer', column_imputer),
    ('model', DecisionTreeClassifier(max_depth=4))
])


pipeline_fewer_features.fit(X_train_r, y_train_r)
pipeline_fewer_features.score(X_train_r, y_train_r), pipeline_fewer_features.score(X_test_r, y_test_r)