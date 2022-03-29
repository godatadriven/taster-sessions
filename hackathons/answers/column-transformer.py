from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

column_imputer = ColumnTransformer(
    [
        ('imp_inc', SimpleImputer(strategy='mean'), ['income']),
        ('imp_deps', SimpleImputer(strategy='most_frequent'), ['num_deps'])
    ]
    , remainder='passthrough'
)

pd.DataFrame(column_imputer.fit_transform(X_train), columns=features)