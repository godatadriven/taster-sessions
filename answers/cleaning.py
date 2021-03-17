penguins_cleaned = (
    penguins
    .assign(flipper_length_mm = penguins['flipper_length_cm']*10)
    .drop('flipper_length_cm', axis=1)
    .replace('F', 'Female')
    .dropna()
    .set_index('penguin_id')
)