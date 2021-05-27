HOLIDAYS = (
    USFederalHolidayCalendar()
    .holidays(start=bikes.index.min(), end=bikes.index.max())
)
print(f'There were {len(HOLIDAYS)} US Bank Holidays from {bikes.index.min().date()} to {bikes.index.max().date()}')