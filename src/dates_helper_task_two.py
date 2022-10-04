from datetime import datetime, timedelta
from dateutil.parser import parse


def is_date(string, fuzzy=False):
    if string is None:
        return
    try:
        parse(string, fuzzy=fuzzy)
        return string
    except ValueError:
        return


FORMAT_DATE = "%m/%d/%Y"


def parse_date_to_str(date):
    return date.strftime("%m/%d/%Y")


def generate_day(number_day, start_date_parse):
    return parse_date_to_str(start_date_parse + timedelta(days=number_day))


def generate_range_dates(start_date, end_date, default_value):
    dates_array = []

    if (is_date(start_date) is None):
        return []

    if (start_date is None or end_date is None):
        return []
    start_date_parse = datetime.strptime(start_date, FORMAT_DATE).date()
    end_date_parse = datetime.strptime(end_date,  FORMAT_DATE).date()
    total_days = end_date_parse - start_date_parse
    dates_array = [
        {
            'date': generate_day(current_day, start_date_parse),
            'participants': default_value
        }
        for current_day in range(total_days.days + 1)
    ]
    return dates_array
