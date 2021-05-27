# 1. A new boolean column called is_weekday where True is a weekday (Mon-Fri) and False a weekend day (Sat-Sun)

def check_is_weekday(df):
    """Create a new column that is True if it is a 
    weekday and False if weekend"""
    
    df = df.assign(**{'is_weekday': df.index.weekday < 5})
    print(f"There are {(~df['is_weekday']).sum()} weekend days in the data.")
    return df

# 2. A new boolean column called is_weekday where True is a WORK day (Mon-Fri but NOT a bank holiday) and False a weekend day or Bank Holiday (Sat-Sun and other Bank Holiday days)


def check_is_workday(df):
    """Create a new column that is True if it is a 
    workday (weekday and not bank holiday) and False 
    if weekend or bank holiday"""
    
    df = df.assign(**{'is_workday': (df.index.weekday < 5) & (~df.index.isin(HOLIDAYS))})
    print(f"There are {df['is_workday'].sum()} work days in the data.")
    return df


# Answers:
# How many weekend days are there?
# How many work days are there in total?

(
    bikes_processed
    .pipe(check_is_weekday)
    .pipe(check_is_workday)
)