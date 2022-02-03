trends_cleaned = (
    trends               
    .assign(Month = pd.to_datetime(trends['Month'])) # convert Month to pd datetime
    .set_index('Month')   # set Month as the index col
    .replace('<5','5')    # replace exact values in the df
    .astype(int)          # change all columns to dtype int
    .rename(columns={'Visual Basic for Applications':'VBA'}) # rename columns (not values)
)