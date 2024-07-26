from datetime import datetime, timedelta


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        days_left = today - given_date
        return days_left.days
    except Exception as e:
        return "wrong format date, must be 'YYYY-MM-DD'"
  
  
    
print(get_days_from_today("2024-07-20"))