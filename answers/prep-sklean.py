unwanted_cols = ['island','sex']

penguins = (
    penguins
    .dropna()
    .drop(unwanted_cols, axis=1)
)
