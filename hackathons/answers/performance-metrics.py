print(f'Train set accuracy:', pipeline_dt.score(X_train, y_train))
print(f'Test set accuracy:', pipeline_dt.score(X_test, y_test))