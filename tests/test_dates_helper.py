from src.dates_helper import get_dates_in_interval


def test_get_dates_in_interval_returns_none():
    start_date = None
    end_date = None

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is None


def test_get_dates_in_interval_returns_single_element_list():
    start_date = '9/12/2022'
    end_date = '9/12/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is not None, 'Expected non null list'
    assert '09/12/2022' in dates, f'Expected {start_date} in list'


def test_get_dates_in_interval_returns_list():
    start_date = '9/12/2022'
    end_date = '9/15/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is not None, 'Expected non null list'
    assert '09/12/2022' in dates, f'Expected {start_date} in list'
    assert '09/13/2022' in dates, f'Expected {start_date} in list'
    assert '09/14/2022' in dates, f'Expected {start_date} in list'
    assert '09/15/2022' in dates, f'Expected {start_date} in list'


def test_get_dates_in_interval_returns_none_on_not_date_format():
    start_date = '9/12asd/2022'
    end_date = '9/12/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is None, f'Expected {start_date} in list'
