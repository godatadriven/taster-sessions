penguins_cleaned = (
    penguins
    .assign(flipper_length_cm = penguins['flipper_length_cm']*10)
    .rename(columns = {'flipper_length_cm':'flipper_length_mm'})
    .replace('F', 'Female')
    .dropna()
    .set_index('penguin_id')
)