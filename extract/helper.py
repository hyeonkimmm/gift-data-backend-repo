from pytz import timezone
from datetime import datetime, timedelta
def get_date(date_type='date', day='yesterday'):
    yesterday = datetime.now(timezone('Asia/Seoul')) - timedelta(1)
    yesterday_date = datetime.strftime(yesterday, '%Y-%m-%d')

    # get today date
    today = datetime.now(timezone('Asia/Seoul'))
    today_date = datetime.strftime(today, '%Y-%m-%d')
    if date_type == 'date':
        if day == 'today':
            return today_date
        elif day == 'yesterday':
            return yesterday_date
    elif date_type == 'datetime':
        if day == 'today':
            return today
        elif day == 'yesterday':
            return yesterday
    else:
        return yesterday, yesterday_date, today, today_date
