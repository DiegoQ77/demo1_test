# def get_dates_in_interval(start_date, end_date):
#     result = []
#     if start_date is None or end_date is None:
#         return
#     if start_date == end_date:
#         return [start_date]

#     # TODO: Solve normal use case
#     return result

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


def create_array_dates(totaldays, start_date_parse):
    dates_array = []
    for day in range(totaldays):
        current_day = start_date_parse + timedelta(days=day)
        str_day = parse_date_to_str(current_day)
        dates_array.append(str_day)
    return dates_array


def parse_date_to_str(date, date_format=FORMAT_DATE):
    return date.strftime(date_format)


def get_dates_in_interval(start_date, end_date):

    if (is_date(start_date) is None):
        return

    if (start_date is None and end_date is None):
        return
    # Convert to datetime
    start_date_parse = datetime.strptime(start_date,  FORMAT_DATE).date()
    end_date_parse = datetime.strptime(end_date,  FORMAT_DATE).date()

    if (end_date_parse < start_date_parse):
        return
    # get the total days
    total_days = end_date_parse - start_date_parse
    total_days_current = total_days.days + 1
    totals = create_array_dates(total_days_current, start_date_parse)
    return totals
