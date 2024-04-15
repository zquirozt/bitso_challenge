import pandas as pd


# Identify on a given day which users have made more than 5 deposits historically
def users_with_more_than_5_deposits(date, deposit_sample_data):
    date = pd.to_datetime(date)
    deposit_count = (
        deposit_sample_data.loc[deposit_sample_data["event_timestamp"] < date]
        .groupby("user_id")
        .size()
    )
    users_more_than_5_deposits = deposit_count[deposit_count > 5].index.tolist()
    if users_more_than_5_deposits:
        return users_more_than_5_deposits[0]
    else:
        return None
