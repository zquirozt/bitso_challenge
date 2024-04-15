# Number of unique currencies withdrew on a given day
def unique_currencies_withdrew_on_day(date, withdrawals_sample_data):
    unique_currencies = withdrawals_sample_data.loc[
        withdrawals_sample_data["event_timestamp"].dt.date == date, "currency"
    ].nunique()
    return unique_currencies
