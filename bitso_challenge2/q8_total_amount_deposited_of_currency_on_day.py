# Total amount deposited of a given currency on a given day
def total_amount_deposited_of_currency_on_day(currency, date, deposit_sample_data):
    total_amount = deposit_sample_data.loc[
        (deposit_sample_data["event_timestamp"].dt.date == date)
        & (deposit_sample_data["currency"] == currency),
        "amount",
    ].sum()
    return total_amount
