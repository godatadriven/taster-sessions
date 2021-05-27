import pandas as pd

from pandas.tseries.holiday import USFederalHolidayCalendar

bikes = pd.read_csv('data/bike-rental.csv', parse_dates = ['datetime'], index_col='datetime')
bikes.head()

HOLIDAYS = (
    USFederalHolidayCalendar()
    .holidays(start=bikes.index.min(), end=bikes.index.max())
)
HOLIDAYS