from src.dates_helper_task_two import generate_range_dates


def test_generate_one_date():
    start_date = '9/12/2022'
    end_date = '9/12/2022'
    default_value = -99999
    dates = generate_range_dates(start_date, end_date, default_value)
    assert {'date': '09/12/2022', 'participants': -99999} in dates


def test_generate_more_than_one_dates():
    start_date = '9/12/2022'
    end_date = '9/15/2022'
    default_value = -99999
    dates = generate_range_dates(start_date, end_date, default_value)
    assert {'date': '09/12/2022', 'participants': -99999} in dates
    assert {'date': '09/13/2022', 'participants': -99999} in dates
    assert {'date': '09/14/2022', 'participants': -99999} in dates
    assert {'date': '09/15/2022', 'participants': -99999} in dates


def test_that_the_end_date_is_less_than_start():
    start_date = '9/15/2022'
    end_date = '9/10/2022'
    default_value = -99999

    dates = generate_range_dates(start_date, end_date, default_value)
    assert len(dates) == 0


def test_thatn_start_and_end_date_are_none():
    start_date = None
    end_date = None
    default_value = -99999

    dates = generate_range_dates(start_date, end_date, default_value)

    assert len(dates) == 0


def test_that_have_range_and_default_value_is_string():
    start_date = '9/12/2022'
    end_date = '9/15/2022'
    default_value = "0h 0m"

    dates = generate_range_dates(start_date, end_date, default_value)

    assert {'date': '09/12/2022', 'participants': '0h 0m'} in dates
    assert {'date': '09/13/2022', 'participants': '0h 0m'} in dates
    assert {'date': '09/14/2022', 'participants': '0h 0m'} in dates
    assert {'date': '09/15/2022', 'participants': '0h 0m'} in dates


def test_return_array_len_zero_if_dates_are_not_dates():
    start_date = '9/12asd/2022'
    end_date = '9/12asdsad/2022'
    default_value = -99999
    dates = generate_range_dates(start_date, end_date, default_value)
    assert len(dates) == 0
