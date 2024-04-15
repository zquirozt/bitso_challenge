# Number of unique currencies deposited on a given day


def unique_currencies_deposited_on_day(date, deposit_sample_data):
    unique_currencies = deposit_sample_data.loc[
        deposit_sample_data["event_timestamp"].dt.date == date, "currency"
    ].nunique()
    return unique_currencies
