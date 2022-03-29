from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline

model_dt = DecisionTreeClassifier(max_depth=10, random_state=111)
pipeline_dt = Pipeline(steps = [
    ('imputer', column_imputer),
    ('model', model_dt)
])


# Fit the pipeline to X_train and y_train

pipeline_dt.fit(X_train, y_train)